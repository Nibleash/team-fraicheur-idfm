"""Module for loading and processing Météo-France climate projection data."""

import os
from pathlib import Path
from typing import Dict, List, Optional, Tuple
import geopandas as gpd
import pandas as pd
import numpy as np
from shapely.geometry import box
import duckdb


class ClimateDataLoader:
    """Load and process Météo-France climate projection data (tas/tasmin/tasmax)."""
    
    # 2.5 km tile size in degrees (approximate at Paris latitude)
    TILE_SIZE = 0.0225
    
    def __init__(self, data_dir: str):
        """
        Initialize the climate data loader.
        
        Args:
            data_dir: Directory containing climate data files
        """
        self.data_dir = Path(data_dir)
        self.conn = duckdb.connect(':memory:')
        
    def load_climate_tiles(self, year: int, variable: str = 'tas') -> gpd.GeoDataFrame:
        """
        Load climate data tiles for a specific year.
        
        Args:
            year: Year for climate projection
            variable: Climate variable ('tas', 'tasmin', 'tasmax')
            
        Returns:
            GeoDataFrame with climate tiles (2.5 km resolution) and temperature values
        """
        # Look for data files
        data_path = self.data_dir / f"{variable}_{year}.csv"
        
        if not data_path.exists():
            # Generate sample data if file doesn't exist
            return self._generate_sample_climate_data(year, variable)
        
        # Load actual data
        df = pd.read_csv(data_path)
        return self._convert_to_geodataframe(df)
    
    def _generate_sample_climate_data(self, year: int, variable: str) -> gpd.GeoDataFrame:
        """
        Generate sample climate data for demonstration purposes.
        Creates a grid of 2.5 km tiles covering Île-de-France region.
        
        Args:
            year: Year for projection
            variable: Climate variable name
            
        Returns:
            GeoDataFrame with sample climate tiles
        """
        # Île-de-France approximate bounds (in WGS84)
        lon_min, lon_max = 1.4, 3.6
        lat_min, lat_max = 48.1, 49.2
        
        # Use class constant for tile size
        tile_size = self.TILE_SIZE
        
        # Seed for reproducible sample data
        np.random.seed(42 + year)
        
        # Generate grid
        lons = np.arange(lon_min, lon_max, tile_size)
        lats = np.arange(lat_min, lat_max, tile_size)
        
        tiles = []
        for lon in lons:
            for lat in lats:
                # Create tile geometry
                tile_geom = box(lon, lat, lon + tile_size, lat + tile_size)
                
                # Generate temperature based on location and year
                # Higher temperatures in city center and future years
                center_lon, center_lat = 2.3522, 48.8566  # Paris center
                distance_from_center = np.sqrt((lon - center_lon)**2 + (lat - center_lat)**2)
                
                # Base temperature with urban heat island effect
                base_temp = 25 - (distance_from_center * 2)
                
                # Add year effect (warming trend)
                year_effect = (year - 2020) * 0.5
                
                # Add some randomness
                random_effect = np.random.randn() * 2
                
                temperature = base_temp + year_effect + random_effect
                
                tiles.append({
                    'geometry': tile_geom,
                    'lon': lon,
                    'lat': lat,
                    'temperature': temperature,
                    'variable': variable,
                    'year': year,
                    'tile_id': f"{variable}_{lon:.4f}_{lat:.4f}"
                })
        
        gdf = gpd.GeoDataFrame(tiles, crs='EPSG:4326')
        return gdf
    
    def _convert_to_geodataframe(self, df: pd.DataFrame) -> gpd.GeoDataFrame:
        """Convert DataFrame with coordinates to GeoDataFrame."""
        geometries = [box(row['lon'], row['lat'], 
                         row['lon'] + self.TILE_SIZE, row['lat'] + self.TILE_SIZE) 
                     for _, row in df.iterrows()]
        gdf = gpd.GeoDataFrame(df, geometry=geometries, crs='EPSG:4326')
        return gdf
    
    def get_heat_threshold_tiles(self, gdf: gpd.GeoDataFrame, 
                                 threshold: float = 30.0) -> gpd.GeoDataFrame:
        """
        Filter tiles above a heat threshold.
        
        Args:
            gdf: GeoDataFrame with temperature data
            threshold: Temperature threshold in Celsius
            
        Returns:
            Filtered GeoDataFrame with hot tiles
        """
        return gdf[gdf['temperature'] >= threshold].copy()
    
    def get_temperature_statistics(self, gdf: gpd.GeoDataFrame) -> Dict[str, float]:
        """
        Calculate temperature statistics.
        
        Args:
            gdf: GeoDataFrame with temperature data
            
        Returns:
            Dictionary with min, max, mean, and std temperature
        """
        return {
            'min': gdf['temperature'].min(),
            'max': gdf['temperature'].max(),
            'mean': gdf['temperature'].mean(),
            'std': gdf['temperature'].std()
        }
