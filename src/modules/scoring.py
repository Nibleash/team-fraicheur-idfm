"""Module for calculating priority scores for bus stops and lines."""

from typing import Dict, List, Tuple
import geopandas as gpd
import pandas as pd
import numpy as np


class PriorityScorer:
    """Calculate priority scores for cooling interventions."""
    
    def __init__(self, weights: Dict[str, float] = None):
        """
        Initialize priority scorer.
        
        Args:
            weights: Dictionary with weights for different factors
        """
        # Default weights
        self.weights = weights or {
            'temperature': 0.35,
            'passenger_volume': 0.30,
            'lack_of_shelter': 0.20,
            'lack_of_bench': 0.15
        }
        
        # Validate weights sum to 1.0
        total = sum(self.weights.values())
        if not np.isclose(total, 1.0):
            raise ValueError(f"Weights must sum to 1.0, got {total}")
    
    def score_stops(self, stops_gdf: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
        """
        Calculate priority scores for individual bus stops.
        
        Args:
            stops_gdf: GeoDataFrame with stops and their attributes
            
        Returns:
            GeoDataFrame with added priority_score column
        """
        stops = stops_gdf.copy()
        
        # Normalize temperature (0-1 scale)
        temp_min = stops['temperature'].min()
        temp_max = stops['temperature'].max()
        if temp_max > temp_min:
            stops['temp_score'] = (stops['temperature'] - temp_min) / (temp_max - temp_min)
        else:
            stops['temp_score'] = 0.5
        
        # Normalize passenger volume (0-1 scale)
        pass_min = stops['daily_passengers'].min()
        pass_max = stops['daily_passengers'].max()
        if pass_max > pass_min:
            stops['passenger_score'] = (stops['daily_passengers'] - pass_min) / (pass_max - pass_min)
        else:
            stops['passenger_score'] = 0.5
        
        # Binary scores for amenities (0 or 1)
        stops['shelter_score'] = (~stops['has_shelter']).astype(float)
        stops['bench_score'] = (~stops['has_bench']).astype(float)
        
        # Calculate weighted priority score
        stops['priority_score'] = (
            self.weights['temperature'] * stops['temp_score'] +
            self.weights['passenger_volume'] * stops['passenger_score'] +
            self.weights['lack_of_shelter'] * stops['shelter_score'] +
            self.weights['lack_of_bench'] * stops['bench_score']
        )
        
        # Normalize to 0-100 scale
        stops['priority_score'] = stops['priority_score'] * 100
        
        return stops
    
    def score_lines(self, line_stats: pd.DataFrame) -> pd.DataFrame:
        """
        Calculate priority scores for bus lines.
        
        Args:
            line_stats: DataFrame with aggregated line statistics
            
        Returns:
            DataFrame with added priority_score column
        """
        lines = line_stats.copy()
        
        # Normalize average temperature (0-1 scale)
        temp_min = lines['avg_temp'].min()
        temp_max = lines['avg_temp'].max()
        if temp_max > temp_min:
            lines['temp_score'] = (lines['avg_temp'] - temp_min) / (temp_max - temp_min)
        else:
            lines['temp_score'] = 0.5
        
        # Normalize total passengers (0-1 scale)
        pass_min = lines['total_passengers'].min()
        pass_max = lines['total_passengers'].max()
        if pass_max > pass_min:
            lines['passenger_score'] = (lines['total_passengers'] - pass_min) / (pass_max - pass_min)
        else:
            lines['passenger_score'] = 0.5
        
        # Normalize stops without amenities (0-1 scale)
        shelter_max = lines['stops_without_shelter'].max()
        if shelter_max > 0:
            lines['shelter_score'] = lines['stops_without_shelter'] / shelter_max
        else:
            lines['shelter_score'] = 0.0
        
        bench_max = lines['stops_without_bench'].max()
        if bench_max > 0:
            lines['bench_score'] = lines['stops_without_bench'] / bench_max
        else:
            lines['bench_score'] = 0.0
        
        # Calculate weighted priority score
        lines['priority_score'] = (
            self.weights['temperature'] * lines['temp_score'] +
            self.weights['passenger_volume'] * lines['passenger_score'] +
            self.weights['lack_of_shelter'] * lines['shelter_score'] +
            self.weights['lack_of_bench'] * lines['bench_score']
        )
        
        # Normalize to 0-100 scale
        lines['priority_score'] = lines['priority_score'] * 100
        
        return lines
    
    def rank_stops(self, stops_gdf: gpd.GeoDataFrame, top_n: int = 50) -> gpd.GeoDataFrame:
        """
        Rank and return top priority stops.
        
        Args:
            stops_gdf: GeoDataFrame with stops and priority scores
            top_n: Number of top stops to return
            
        Returns:
            Filtered and sorted GeoDataFrame with top priority stops
        """
        ranked = stops_gdf.sort_values('priority_score', ascending=False)
        ranked['rank'] = range(1, len(ranked) + 1)
        return ranked.head(top_n)
    
    def rank_lines(self, line_stats: pd.DataFrame, top_n: int = 20) -> pd.DataFrame:
        """
        Rank and return top priority lines.
        
        Args:
            line_stats: DataFrame with line statistics and priority scores
            top_n: Number of top lines to return
            
        Returns:
            Filtered and sorted DataFrame with top priority lines
        """
        ranked = line_stats.sort_values('priority_score', ascending=False)
        ranked['rank'] = range(1, len(ranked) + 1)
        return ranked.head(top_n)
    
    def get_priority_categories(self, scores: pd.Series) -> pd.Series:
        """
        Categorize priority scores into Low, Medium, High, Critical.
        
        Args:
            scores: Series with priority scores
            
        Returns:
            Series with priority categories
        """
        return pd.cut(scores, 
                     bins=[0, 25, 50, 75, 100],
                     labels=['Low', 'Medium', 'High', 'Critical'],
                     include_lowest=True)
