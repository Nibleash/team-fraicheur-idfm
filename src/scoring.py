import pandas as pd
from typing import Dict


class LineScorer:
    """Score bus lines based on temperature, number of stops, and air conditioning status."""

    def __init__(self, weights: Dict[str, float] = None):
        self.weights = weights or {
            "temperature": 0.30,
            "stops": 0.20,
            "air_conditioning": 0.25,
            "validations": 0.25,
        }

    def calculate_priority_scores(self, lines_df: pd.DataFrame) -> pd.DataFrame:
        df = lines_df.copy()

        # 1. Normalize temperature (0-1 scale)
        temp_min = df["temperature"].min()
        temp_max = df["temperature"].max()
        df["temp_score"] = (df["temperature"] - temp_min) / (temp_max - temp_min)

        # 2. Normalize number of stops (0-1 scale)
        stops_min = df["stop_id"].min()
        stops_max = df["stop_id"].max()
        df["stops_score"] = (df["stop_id"] - stops_min) / (stops_max - stops_min)

        # 3. Normalize number of validations (0-1 scale)
        nb_validations_min = df["nb_validations"].min()
        nb_validations_max = df["nb_validations"].max()
        df["validations_score"] = (df["nb_validations"] - nb_validations_min) / (
            nb_validations_max - nb_validations_min
        )

        # 4. Air conditioning score
        df["ac_score"] = df["air_conditioning"].apply(self.get_ac_score)

        # Calculate weighted priority score (0-100 scale)
        df["priority_score"] = (
            self.weights["temperature"] * df["temp_score"]
            + self.weights["stops"] * df["stops_score"]
            + self.weights["air_conditioning"] * df["ac_score"]
            + self.weights["validations"] * df["validations_score"]
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
            "lines_without_ac": len(
                scored_df[scored_df["air_conditioning"].isin(["false", "unknown"])]
            ),
            "lines_partial_ac": len(
                scored_df[scored_df["air_conditioning"] == "partial"]
            ),
            "lines_full_ac": len(scored_df[scored_df["air_conditioning"] == "true"]),
        }
