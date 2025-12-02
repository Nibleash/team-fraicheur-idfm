"""Module for performing spatial joins and analysis."""

from typing import Dict, List, Tuple
import geopandas as gpd
import pandas as pd
import numpy as np
from shapely.geometry import Point


class SpatialAnalyzer:
    """Perform spatial analysis between climate tiles and bus stops."""
    
    def __init__(self):
        """Initialize spatial analyzer."""
        pass
    
    def join_stops_with_climate(self, stops_gdf: gpd.GeoDataFrame, 
                                climate_gdf: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
        """
        Perform spatial join between bus stops and climate tiles.
        
        Args:
            stops_gdf: GeoDataFrame with bus stops
            climate_gdf: GeoDataFrame with climate tiles
            
        Returns:
            GeoDataFrame with stops joined to their corresponding climate data
        """
        # Ensure both have the same CRS
        if stops_gdf.crs != climate_gdf.crs:
            climate_gdf = climate_gdf.to_crs(stops_gdf.crs)
        
        # Perform spatial join
        joined = gpd.sjoin(stops_gdf, climate_gdf, how='inner', predicate='within')
        
        # Drop duplicate columns from the join
        joined = joined.drop(columns=['index_right'], errors='ignore')
        
        return joined
    
    def calculate_stop_heat_exposure(self, joined_gdf: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
        """
        Calculate heat exposure metrics for each stop.
        
        Args:
            joined_gdf: GeoDataFrame with stops joined to climate data
            
        Returns:
            GeoDataFrame with heat exposure metrics
        """
        # If a stop appears in multiple tiles (shouldn't happen but just in case),
        # take the maximum temperature
        if joined_gdf.duplicated(subset=['stop_id']).any():
            joined_gdf = joined_gdf.sort_values('temperature', ascending=False)
            joined_gdf = joined_gdf.drop_duplicates(subset=['stop_id'], keep='first')
        
        return joined_gdf
    
    def aggregate_by_line(self, stops_gdf: gpd.GeoDataFrame) -> pd.DataFrame:
        """
        Aggregate heat exposure and metrics by bus line.
        
        Args:
            stops_gdf: GeoDataFrame with stops and heat exposure data
            
        Returns:
            DataFrame with aggregated metrics per line
        """
        # Explode the lines column (since each stop can serve multiple lines)
        stops_exploded = stops_gdf.copy()
        stops_exploded['line'] = stops_exploded['lines'].str.split(',')
        stops_exploded = stops_exploded.explode('line')
        
        # Remove whitespace
        stops_exploded['line'] = stops_exploded['line'].str.strip()
        
        # Aggregate by line
        line_stats = stops_exploded.groupby('line').agg({
            'temperature': ['mean', 'max', 'min'],
            'daily_passengers': ['sum', 'mean'],
            'stop_id': 'count',
            'has_shelter': lambda x: (~x).sum(),  # Count stops without shelter
            'has_bench': lambda x: (~x).sum()  # Count stops without bench
        }).reset_index()
        
        # Flatten column names
        line_stats.columns = ['line', 'avg_temp', 'max_temp', 'min_temp', 
                             'total_passengers', 'avg_passengers_per_stop',
                             'num_stops', 'stops_without_shelter', 'stops_without_bench']
        
        return line_stats
    
    def find_hottest_areas(self, climate_gdf: gpd.GeoDataFrame, 
                          top_n: int = 10) -> gpd.GeoDataFrame:
        """
        Find the hottest areas in the region.
        
        Args:
            climate_gdf: GeoDataFrame with climate tiles
            top_n: Number of hottest tiles to return
            
        Returns:
            GeoDataFrame with hottest tiles
        """
        return climate_gdf.nlargest(top_n, 'temperature')
    
    def find_stops_in_hot_areas(self, stops_gdf: gpd.GeoDataFrame,
                                threshold_temp: float = 30.0) -> gpd.GeoDataFrame:
        """
        Find stops in areas exceeding temperature threshold.
        
        Args:
            stops_gdf: GeoDataFrame with stops and temperature data
            threshold_temp: Temperature threshold in Celsius
            
        Returns:
            Filtered GeoDataFrame with stops in hot areas
        """
        return stops_gdf[stops_gdf['temperature'] >= threshold_temp].copy()
    
    def calculate_distance_matrix(self, stops_gdf: gpd.GeoDataFrame,
                                  points_gdf: gpd.GeoDataFrame) -> np.ndarray:
        """
        Calculate distance matrix between stops and points of interest.
        
        Args:
            stops_gdf: GeoDataFrame with bus stops
            points_gdf: GeoDataFrame with points of interest
            
        Returns:
            Distance matrix (stops x points)
        """
        # Convert to projected CRS for accurate distance calculation
        stops_proj = stops_gdf.to_crs('EPSG:2154')  # Lambert 93 for France
        points_proj = points_gdf.to_crs('EPSG:2154')
        
        distances = np.zeros((len(stops_proj), len(points_proj)))
        for i, stop_geom in enumerate(stops_proj.geometry):
            for j, point_geom in enumerate(points_proj.geometry):
                distances[i, j] = stop_geom.distance(point_geom)
        
        return distances
