"""
Team Fraicheur IDFM - Streamlit Application
Identify priority bus stops/lines for cooling in Île-de-France
"""

import sys
from pathlib import Path

# Add modules to path
sys.path.append(str(Path(__file__).parent))

import streamlit as st
import pandas as pd
import geopandas as gpd
from streamlit_folium import folium_static

from modules.climate_loader import ClimateDataLoader
from modules.idfm_loader import IDFMDataLoader
from modules.spatial_analysis import SpatialAnalyzer
from modules.scoring import PriorityScorer
from modules.visualization import MapVisualizer


# Page configuration
st.set_page_config(
    page_title="Team Fraicheur IDFM",
    page_icon="🌡️",
    layout="wide",
    initial_sidebar_state="expanded"
)


def main():
    """Main application function."""
    
    # Title and description
    st.title("🌡️ Team Fraicheur IDFM")
    st.markdown("""
    ### Priority Bus Stops/Lines for Cooling in Île-de-France
    
    This application identifies priority bus stops and lines that need cooling interventions
    based on climate projections, passenger volume, and existing amenities.
    """)
    
    # Sidebar controls
    st.sidebar.header("Configuration")
    
    # Year selection
    year = st.sidebar.selectbox(
        "Select Year",
        options=[2025, 2030, 2035, 2040, 2045, 2050],
        index=1  # Default to 2030
    )
    
    # Climate variable selection
    climate_var = st.sidebar.selectbox(
        "Climate Variable",
        options=['tas', 'tasmin', 'tasmax'],
        format_func=lambda x: {
            'tas': 'Average Temperature (tas)',
            'tasmin': 'Minimum Temperature (tasmin)',
            'tasmax': 'Maximum Temperature (tasmax)'
        }[x]
    )
    
    # Temperature threshold
    temp_threshold = st.sidebar.slider(
        "Temperature Threshold (°C)",
        min_value=25.0,
        max_value=40.0,
        value=30.0,
        step=0.5,
        help="Filter stops in areas exceeding this temperature"
    )
    
    # Number of top results
    top_stops = st.sidebar.slider(
        "Top Priority Stops to Display",
        min_value=10,
        max_value=100,
        value=50,
        step=10
    )
    
    top_lines = st.sidebar.slider(
        "Top Priority Lines to Display",
        min_value=5,
        max_value=50,
        value=20,
        step=5
    )
    
    # Run analysis button
    if st.sidebar.button("🔍 Run Analysis", type="primary"):
        run_analysis(year, climate_var, temp_threshold, top_stops, top_lines)


@st.cache_data
def load_data(year: int, climate_var: str):
    """
    Load and cache all necessary data.
    
    Args:
        year: Year for climate projection
        climate_var: Climate variable to load
        
    Returns:
        Tuple of (climate_gdf, stops_gdf, lines_df)
    """
    # Get data directories
    base_dir = Path(__file__).parent.parent
    climate_dir = base_dir / 'data' / 'climate'
    idfm_dir = base_dir / 'data' / 'idfm'
    
    # Load data
    climate_loader = ClimateDataLoader(climate_dir)
    idfm_loader = IDFMDataLoader(idfm_dir)
    
    climate_gdf = climate_loader.load_climate_tiles(year, climate_var)
    stops_gdf = idfm_loader.load_stops()
    lines_df = idfm_loader.load_lines()
    
    return climate_gdf, stops_gdf, lines_df


def run_analysis(year: int, climate_var: str, temp_threshold: float, 
                 top_stops: int, top_lines: int):
    """
    Run the complete analysis pipeline.
    
    Args:
        year: Selected year
        climate_var: Selected climate variable
        temp_threshold: Temperature threshold
        top_stops: Number of top stops to display
        top_lines: Number of top lines to display
    """
    with st.spinner("Loading data..."):
        climate_gdf, stops_gdf, lines_df = load_data(year, climate_var)
    
    st.success(f"Loaded {len(climate_gdf)} climate tiles and {len(stops_gdf)} bus stops")
    
    # Display basic statistics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Climate Tiles", f"{len(climate_gdf):,}")
    
    with col2:
        st.metric("Bus Stops", f"{len(stops_gdf):,}")
    
    with col3:
        st.metric("Bus Lines", f"{len(lines_df):,}")
    
    with col4:
        temp_stats = climate_gdf['temperature'].describe()
        st.metric("Avg Temperature", f"{temp_stats['mean']:.1f}°C")
    
    # Spatial analysis
    with st.spinner("Performing spatial analysis..."):
        analyzer = SpatialAnalyzer()
        joined_stops = analyzer.join_stops_with_climate(stops_gdf, climate_gdf)
        joined_stops = analyzer.calculate_stop_heat_exposure(joined_stops)
        
        # Filter by temperature threshold
        hot_stops = analyzer.find_stops_in_hot_areas(joined_stops, temp_threshold)
        
        # Aggregate by line
        line_stats = analyzer.aggregate_by_line(joined_stops)
    
    st.info(f"Found {len(hot_stops)} stops exceeding {temp_threshold}°C")
    
    # Calculate priority scores
    with st.spinner("Calculating priority scores..."):
        scorer = PriorityScorer()
        scored_stops = scorer.score_stops(joined_stops)
        scored_lines = scorer.score_lines(line_stats)
        
        # Rank results
        top_priority_stops = scorer.rank_stops(scored_stops, top_stops)
        top_priority_lines = scorer.rank_lines(scored_lines, top_lines)
    
    # Display results in tabs
    tab1, tab2, tab3, tab4 = st.tabs([
        "🗺️ Interactive Map",
        "🚏 Priority Stops",
        "🚌 Priority Lines",
        "📊 Statistics"
    ])
    
    with tab1:
        display_map(climate_gdf, top_priority_stops, temp_threshold)
    
    with tab2:
        display_priority_stops(top_priority_stops)
    
    with tab3:
        display_priority_lines(top_priority_lines)
    
    with tab4:
        display_statistics(climate_gdf, scored_stops, scored_lines)


def display_map(climate_gdf: gpd.GeoDataFrame, stops_gdf: gpd.GeoDataFrame,
                temp_threshold: float):
    """Display interactive map with climate tiles and priority stops."""
    
    st.subheader("Interactive Map")
    st.markdown(f"""
    This map shows:
    - **Climate tiles** colored by temperature (red = hotter)
    - **Priority bus stops** sized and colored by priority score
    - Click on stops for detailed information
    """)
    
    with st.spinner("Creating map..."):
        visualizer = MapVisualizer()
        
        # Filter climate tiles to show only hot areas for clarity
        hot_tiles = climate_gdf[climate_gdf['temperature'] >= temp_threshold]
        
        # Create base map
        m = visualizer.create_base_map(zoom_start=11)
        
        # Add layers
        if len(hot_tiles) > 0:
            m = visualizer.add_climate_tiles(m, hot_tiles, opacity=0.4)
        
        m = visualizer.add_bus_stops(m, stops_gdf, color_by='priority_score', show_all=True)
        
        # Add layer control
        m = visualizer.add_layer_control(m)
    
    # Display map
    folium_static(m, width=1200, height=600)


def display_priority_stops(stops_gdf: gpd.GeoDataFrame):
    """Display ranked list of priority stops."""
    
    st.subheader("Priority Bus Stops for Cooling Interventions")
    
    # Prepare display dataframe
    display_cols = ['rank', 'stop_name', 'stop_id', 'temperature', 
                   'daily_passengers', 'priority_score', 'lines',
                   'has_shelter', 'has_bench']
    
    # Filter to existing columns
    display_cols = [col for col in display_cols if col in stops_gdf.columns]
    
    df_display = stops_gdf[display_cols].copy()
    
    # Format columns
    if 'temperature' in df_display.columns:
        df_display['temperature'] = df_display['temperature'].round(1)
    if 'priority_score' in df_display.columns:
        df_display['priority_score'] = df_display['priority_score'].round(1)
    
    # Rename for display
    column_names = {
        'rank': 'Rank',
        'stop_name': 'Stop Name',
        'stop_id': 'Stop ID',
        'temperature': 'Temperature (°C)',
        'daily_passengers': 'Daily Passengers',
        'priority_score': 'Priority Score',
        'lines': 'Lines',
        'has_shelter': 'Has Shelter',
        'has_bench': 'Has Bench'
    }
    
    df_display = df_display.rename(columns=column_names)
    
    # Display table
    st.dataframe(
        df_display,
        use_container_width=True,
        hide_index=True
    )
    
    # Download button
    csv = df_display.to_csv(index=False)
    st.download_button(
        label="📥 Download Priority Stops (CSV)",
        data=csv,
        file_name="priority_stops.csv",
        mime="text/csv"
    )


def display_priority_lines(lines_df: pd.DataFrame):
    """Display ranked list of priority lines."""
    
    st.subheader("Priority Bus Lines for Cooling Interventions")
    
    # Prepare display dataframe
    display_cols = ['rank', 'line', 'avg_temp', 'max_temp', 'total_passengers',
                   'num_stops', 'stops_without_shelter', 'priority_score']
    
    # Filter to existing columns
    display_cols = [col for col in display_cols if col in lines_df.columns]
    
    df_display = lines_df[display_cols].copy()
    
    # Format columns
    for col in ['avg_temp', 'max_temp', 'priority_score']:
        if col in df_display.columns:
            df_display[col] = df_display[col].round(1)
    
    # Rename for display
    column_names = {
        'rank': 'Rank',
        'line': 'Line',
        'avg_temp': 'Avg Temperature (°C)',
        'max_temp': 'Max Temperature (°C)',
        'total_passengers': 'Total Daily Passengers',
        'num_stops': 'Number of Stops',
        'stops_without_shelter': 'Stops Without Shelter',
        'priority_score': 'Priority Score'
    }
    
    df_display = df_display.rename(columns=column_names)
    
    # Display table
    st.dataframe(
        df_display,
        use_container_width=True,
        hide_index=True
    )
    
    # Download button
    csv = df_display.to_csv(index=False)
    st.download_button(
        label="📥 Download Priority Lines (CSV)",
        data=csv,
        file_name="priority_lines.csv",
        mime="text/csv"
    )


def display_statistics(climate_gdf: gpd.GeoDataFrame, 
                      stops_gdf: gpd.GeoDataFrame,
                      lines_df: pd.DataFrame):
    """Display overall statistics and charts."""
    
    st.subheader("Overall Statistics")
    
    # Temperature distribution
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### Temperature Distribution")
        temp_stats = climate_gdf['temperature'].describe()
        st.dataframe(temp_stats, use_container_width=True)
        
        # Histogram
        st.bar_chart(climate_gdf['temperature'].value_counts(bins=20).sort_index())
    
    with col2:
        st.markdown("#### Priority Score Distribution")
        score_stats = stops_gdf['priority_score'].describe()
        st.dataframe(score_stats, use_container_width=True)
        
        # Histogram
        st.bar_chart(stops_gdf['priority_score'].value_counts(bins=20).sort_index())
    
    # Summary metrics
    st.markdown("#### Summary Metrics")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        avg_passengers = stops_gdf['daily_passengers'].sum()
        st.metric("Total Daily Passengers (Top Stops)", f"{avg_passengers:,}")
    
    with col2:
        pct_no_shelter = (~stops_gdf['has_shelter']).sum() / len(stops_gdf) * 100
        st.metric("Stops Without Shelter", f"{pct_no_shelter:.1f}%")
    
    with col3:
        pct_no_bench = (~stops_gdf['has_bench']).sum() / len(stops_gdf) * 100
        st.metric("Stops Without Bench", f"{pct_no_bench:.1f}%")


if __name__ == "__main__":
    main()
