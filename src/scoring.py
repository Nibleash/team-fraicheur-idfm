import pandas as pd
from typing import Dict


class LineScorer:
    """Score bus lines based on temperature, number of stops, and air conditioning status."""
    
    def __init__(self, weights: Dict[str, float] = None):
        self.weights = weights or {
            "temperature": 0.40,
            "stops": 0.30,
            "air_conditioning": 0.30
        }
    
    def calculate_priority_scores(self, lines_df: pd.DataFrame) -> pd.DataFrame:
        df = lines_df.copy()
        
        # 1. Normalize temperature (0-1 scale)
        temp_min = df["temperature"].min()
        temp_max = df["temperature"].max()
        if temp_max > temp_min:
            df["temp_score"] = (df["temperature"] - temp_min) / (temp_max - temp_min)
        else:
            df["temp_score"] = 0.5
        
        # 2. Normalize number of stops (0-1 scale)
        stops_min = df["stop_id"].min()
        stops_max = df["stop_id"].max()
        if stops_max > stops_min:
            df["stops_score"] = (df["stop_id"] - stops_min) / (stops_max - stops_min)
        else:
            df["stops_score"] = 0.5
        
        # 3. Air conditioning score
        df["ac_score"] = df["air_conditioning"].apply(self.get_ac_score)
        
        # Calculate weighted priority score (0-100 scale)
        df["priority_score"] = (
            self.weights["temperature"] * df["temp_score"] +
            self.weights["stops"] * df["stops_score"] +
            self.weights["air_conditioning"] * df["ac_score"]
        ) * 100
        
        # Sort by priority score and add rank
        df = df.sort_values(by="priority_score", ascending=False)
        df["rank"] = range(1, len(df) + 1)
        
        return df
    
    def get_ac_score(self, ac_status: str) -> float:
        if ac_status in ["false", "unknown"] or pd.isna(ac_status):
            return 1.0  # Highest priority - no AC
        elif ac_status == "partial":
            return 0.5  # Medium priority - partial AC
        else:  # "true"
            return 0.0  # Lowest priority - already equipped
    
    def get_summary_statistics(self, scored_df: pd.DataFrame) -> Dict[str, float]:
        return {
            "total_lines": len(scored_df),
            "avg_priority_score": scored_df["priority_score"].mean(),
            "median_priority_score": scored_df["priority_score"].median(),
            "min_priority_score": scored_df["priority_score"].min(),
            "max_priority_score": scored_df["priority_score"].max(),
            "lines_without_ac": len(scored_df[scored_df["air_conditioning"].isin(["false", "unknown"])]),
            "lines_partial_ac": len(scored_df[scored_df["air_conditioning"] == "partial"]),
            "lines_full_ac": len(scored_df[scored_df["air_conditioning"] == "true"]),
        }
