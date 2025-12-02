"""Module for loading and processing IDFM bus stops and lines data."""

import os
from pathlib import Path
from typing import Dict, List, Optional
import geopandas as gpd
import pandas as pd
import numpy as np
from shapely.geometry import Point
import duckdb


class IDFMDataLoader:
    """Load and process IDFM bus stops and lines data."""
    
    def __init__(self, data_dir: str):
        """
        Initialize the IDFM data loader.
        
        Args:
            data_dir: Directory containing IDFM data files
        """
        self.data_dir = Path(data_dir)
        self.conn = duckdb.connect(':memory:')
    
    def load_stops(self) -> gpd.GeoDataFrame:
        """
        Load IDFM bus stops data.
        
        Returns:
            GeoDataFrame with bus stop locations and metadata
        """
        stops_path = self.data_dir / 'stops.csv'
        
        if not stops_path.exists():
            # Generate sample data if file doesn't exist
            return self._generate_sample_stops()
        
        # Load actual data
        df = pd.read_csv(stops_path)
        return self._convert_stops_to_geodataframe(df)
    
    def load_lines(self) -> pd.DataFrame:
        """
        Load IDFM bus lines data.
        
        Returns:
            DataFrame with bus line information
        """
        lines_path = self.data_dir / 'lines.csv'
        
        if not lines_path.exists():
            # Generate sample data if file doesn't exist
            return self._generate_sample_lines()
        
        # Load actual data
        return pd.read_csv(lines_path)
    
    def _generate_sample_stops(self) -> gpd.GeoDataFrame:
        """
        Generate sample bus stop data for demonstration.
        Creates bus stops distributed across Île-de-France.
        
        Returns:
            GeoDataFrame with sample bus stops
        """
        # Generate stops in and around Paris
        np.random.seed(42)
        n_stops = 500
        
        # Paris center coordinates
        center_lon, center_lat = 2.3522, 48.8566
        
        stops = []
        for i in range(n_stops):
            # Generate stops with higher density near center
            radius = np.random.exponential(0.15)
            angle = np.random.uniform(0, 2 * np.pi)
            
            lon = center_lon + radius * np.cos(angle)
            lat = center_lat + radius * np.sin(angle)
            
            # Assign to random lines
            n_lines = np.random.randint(1, 4)
            lines = [f"Line_{np.random.randint(1, 100)}" for _ in range(n_lines)]
            
            # Generate passenger data
            daily_passengers = np.random.randint(100, 5000)
            
            stops.append({
                'stop_id': f"STOP_{i:04d}",
                'stop_name': f"Arrêt {i}",
                'lon': lon,
                'lat': lat,
                'geometry': Point(lon, lat),
                'lines': ','.join(lines),
                'daily_passengers': daily_passengers,
                'has_shelter': np.random.choice([True, False], p=[0.7, 0.3]),
                'has_bench': np.random.choice([True, False], p=[0.6, 0.4])
            })
        
        gdf = gpd.GeoDataFrame(stops, crs='EPSG:4326')
        return gdf
    
    def _generate_sample_lines(self) -> pd.DataFrame:
        """
        Generate sample bus line data.
        
        Returns:
            DataFrame with sample bus lines
        """
        lines = []
        for i in range(1, 100):
            lines.append({
                'line_id': f"Line_{i}",
                'line_name': f"Ligne {i}",
                'line_type': np.random.choice(['Bus', 'Tram', 'Metro'], p=[0.7, 0.2, 0.1]),
                'total_stops': np.random.randint(10, 50),
                'daily_frequency': np.random.randint(20, 200)
            })
        
        return pd.DataFrame(lines)
    
    def _convert_stops_to_geodataframe(self, df: pd.DataFrame) -> gpd.GeoDataFrame:
        """Convert DataFrame with coordinates to GeoDataFrame."""
        geometries = [Point(row['lon'], row['lat']) for _, row in df.iterrows()]
        gdf = gpd.GeoDataFrame(df, geometry=geometries, crs='EPSG:4326')
        return gdf
    
    def get_high_traffic_stops(self, stops_gdf: gpd.GeoDataFrame, 
                               percentile: float = 75) -> gpd.GeoDataFrame:
        """
        Filter stops with high passenger traffic.
        
        Args:
            stops_gdf: GeoDataFrame with bus stops
            percentile: Percentile threshold for high traffic
            
        Returns:
            Filtered GeoDataFrame with high traffic stops
        """
        threshold = stops_gdf['daily_passengers'].quantile(percentile / 100)
        return stops_gdf[stops_gdf['daily_passengers'] >= threshold].copy()
    
    def get_stops_by_line(self, stops_gdf: gpd.GeoDataFrame, 
                          line_id: str) -> gpd.GeoDataFrame:
        """
        Get all stops for a specific line.
        
        Args:
            stops_gdf: GeoDataFrame with bus stops
            line_id: Line identifier
            
        Returns:
            Filtered GeoDataFrame with stops on the line
        """
        return stops_gdf[stops_gdf['lines'].str.contains(line_id, na=False)].copy()
