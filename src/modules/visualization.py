"""Module for creating map visualizations."""

from typing import Dict, List, Optional, Tuple
import geopandas as gpd
import pandas as pd
import folium
from folium import plugins
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors


class MapVisualizer:
    """Create interactive maps for climate and transit data visualization."""
    
    def __init__(self, center_lat: float = 48.8566, center_lon: float = 2.3522):
        """
        Initialize map visualizer.
        
        Args:
            center_lat: Latitude for map center (default: Paris)
            center_lon: Longitude for map center (default: Paris)
        """
        self.center_lat = center_lat
        self.center_lon = center_lon
    
    def create_base_map(self, zoom_start: int = 10) -> folium.Map:
        """
        Create base Folium map.
        
        Args:
            zoom_start: Initial zoom level
            
        Returns:
            Folium Map object
        """
        m = folium.Map(
            location=[self.center_lat, self.center_lon],
            zoom_start=zoom_start,
            tiles='OpenStreetMap'
        )
        return m
    
    def add_climate_tiles(self, m: folium.Map, climate_gdf: gpd.GeoDataFrame,
                         opacity: float = 0.5) -> folium.Map:
        """
        Add climate tiles to map with temperature color coding.
        
        Args:
            m: Folium Map object
            climate_gdf: GeoDataFrame with climate tiles
            opacity: Opacity for tile overlay
            
        Returns:
            Updated Folium Map object
        """
        # Create colormap
        min_temp = climate_gdf['temperature'].min()
        max_temp = climate_gdf['temperature'].max()
        
        colormap = folium.LinearColormap(
            colors=['blue', 'green', 'yellow', 'orange', 'red'],
            vmin=min_temp,
            vmax=max_temp,
            caption='Temperature (°C)'
        )
        
        # Add tiles to map
        style_function = lambda feature: {
            'fillColor': colormap(feature['properties']['temperature']),
            'color': 'gray',
            'weight': 0.5,
            'fillOpacity': opacity
        }
        
        folium.GeoJson(
            climate_gdf,
            name='Climate Tiles',
            style_function=style_function,
            tooltip=folium.GeoJsonTooltip(
                fields=['temperature', 'tile_id'],
                aliases=['Temperature (°C):', 'Tile ID:']
            )
        ).add_to(m)
        
        colormap.add_to(m)
        
        return m
    
    def add_bus_stops(self, m: folium.Map, stops_gdf: gpd.GeoDataFrame,
                     color_by: str = 'priority_score',
                     show_all: bool = True) -> folium.Map:
        """
        Add bus stops to map.
        
        Args:
            m: Folium Map object
            stops_gdf: GeoDataFrame with bus stops
            color_by: Column to use for color coding ('priority_score', 'temperature')
            show_all: If False, only show top priority stops
            
        Returns:
            Updated Folium Map object
        """
        # Filter if needed
        if not show_all and 'rank' in stops_gdf.columns:
            stops_to_plot = stops_gdf[stops_gdf['rank'] <= 50]
        else:
            stops_to_plot = stops_gdf
        
        # Define color scheme based on priority score or temperature
        if color_by == 'priority_score' and 'priority_score' in stops_to_plot.columns:
            values = stops_to_plot['priority_score']
            colors = ['green', 'yellow', 'orange', 'red']
            caption = 'Priority Score'
        elif color_by == 'temperature' and 'temperature' in stops_to_plot.columns:
            values = stops_to_plot['temperature']
            colors = ['blue', 'green', 'yellow', 'orange', 'red']
            caption = 'Temperature (°C)'
        else:
            # Default color
            for idx, row in stops_to_plot.iterrows():
                folium.CircleMarker(
                    location=[row.geometry.y, row.geometry.x],
                    radius=5,
                    popup=self._create_stop_popup(row),
                    color='blue',
                    fill=True,
                    fillOpacity=0.7
                ).add_to(m)
            return m
        
        # Create colormap
        colormap = folium.LinearColormap(
            colors=colors,
            vmin=values.min(),
            vmax=values.max(),
            caption=caption
        )
        
        # Add stops
        for idx, row in stops_to_plot.iterrows():
            color = colormap(values.loc[idx])
            folium.CircleMarker(
                location=[row.geometry.y, row.geometry.x],
                radius=6,
                popup=self._create_stop_popup(row),
                color=color,
                fill=True,
                fillColor=color,
                fillOpacity=0.8,
                weight=2
            ).add_to(m)
        
        return m
    
    def _create_stop_popup(self, row: pd.Series) -> str:
        """Create HTML popup for bus stop."""
        html = f"""
        <div style="font-family: Arial; font-size: 12px;">
            <b>{row['stop_name']}</b><br>
            <b>ID:</b> {row['stop_id']}<br>
        """
        
        if 'temperature' in row:
            html += f"<b>Temperature:</b> {row['temperature']:.1f}°C<br>"
        
        if 'daily_passengers' in row:
            html += f"<b>Daily Passengers:</b> {row['daily_passengers']:,}<br>"
        
        if 'priority_score' in row:
            html += f"<b>Priority Score:</b> {row['priority_score']:.1f}<br>"
        
        if 'rank' in row:
            html += f"<b>Rank:</b> #{row['rank']}<br>"
        
        if 'lines' in row:
            html += f"<b>Lines:</b> {row['lines']}<br>"
        
        if 'has_shelter' in row:
            shelter = "Yes" if row['has_shelter'] else "No"
            html += f"<b>Shelter:</b> {shelter}<br>"
        
        if 'has_bench' in row:
            bench = "Yes" if row['has_bench'] else "No"
            html += f"<b>Bench:</b> {bench}<br>"
        
        html += "</div>"
        return html
    
    def create_heatmap(self, stops_gdf: gpd.GeoDataFrame, 
                       weight_col: str = 'priority_score') -> plugins.HeatMap:
        """
        Create heatmap layer from stops data.
        
        Args:
            stops_gdf: GeoDataFrame with bus stops
            weight_col: Column to use for heat intensity
            
        Returns:
            Folium HeatMap plugin
        """
        heat_data = []
        for idx, row in stops_gdf.iterrows():
            if weight_col in row:
                heat_data.append([row.geometry.y, row.geometry.x, row[weight_col]])
            else:
                heat_data.append([row.geometry.y, row.geometry.x, 1.0])
        
        return plugins.HeatMap(heat_data, name='Heatmap', radius=15)
    
    def add_layer_control(self, m: folium.Map) -> folium.Map:
        """
        Add layer control to map.
        
        Args:
            m: Folium Map object
            
        Returns:
            Updated Folium Map object
        """
        folium.LayerControl().add_to(m)
        return m
