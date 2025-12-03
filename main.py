import logging
import sys
from src.climate_loader import ClimateDataLoader
from src.idfm_loader import IDFMDataLoader
from src.spatial_analysis import SpatialAnalyzer
from src.scoring import LineScorer

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


def main(year=2075, percentile=99):
    climate_loader = ClimateDataLoader()
    idfm_loader = IDFMDataLoader("data/idfm")
    spatial_analyzer = SpatialAnalyzer()
    PERCENTILE = percentile
    YEAR = year

    logger.info(
        f"Loading climate data from S3 and extracting top {100 - PERCENTILE}% hottest tiles..."
    )
    hot_squares = climate_loader.load_climate_tiles_from_s3(
        year=YEAR, percentile=PERCENTILE/100
    )
    temp_threshold = hot_squares["temperature"].min()
    logger.info(f"Loaded {len(hot_squares)} hot squares (2.5km tiles)")
    logger.info(f"Temperature threshold (90th percentile): {temp_threshold:.2f}°C")

    logger.info("Loading IDFM stops data...")
    stops_gdf = idfm_loader.load_stops_ref()
    logger.info(f"Loaded {len(stops_gdf)} bus stops")

    logger.info("Loading IDFM lines data...")
    lines_df = idfm_loader.load_lines()
    logger.info(f"Loaded {len(lines_df)} bus lines")

    logger.info("Finding stops in hot squares...")
    hot_squares.to_csv("data/output/hot_squares.csv", index=False)
    stops_in_hot_zones = spatial_analyzer.join_stops_with_climate(
        stops_gdf, hot_squares
    )
    logger.info(f"Found {len(stops_in_hot_zones)} stops in hot squares")
    stops_in_hot_zones.to_csv("data/output/stops_in_hot_zones.csv", index=False)

    hot_stops_lines = idfm_loader.get_stops_lines(stops_in_hot_zones)
    hot_lines_df = (
        hot_stops_lines.groupby("route_id")
        .agg({"temperature": "mean", "stop_id": "nunique"})
        .reset_index()
    )
    logger.info(f"Identified {len(hot_lines_df)} unique bus lines in hot zones")

    lines_df_hot_info = lines_df.merge(
        hot_lines_df, left_on="id_line", right_on="route_id", how="inner"
    )
    lines_df_hot_validations = idfm_loader.get_validations_lines(lines_df_hot_info)

    # Calculate priority scores using LineScorer
    logger.info("Calculating priority scores...")
    scorer = LineScorer(
        weights={
            "temperature": 0.30,
            "stops": 0.20,
            "air_conditioning": 0.25,
            "validations": 0.25,
        }
    )

    lines_df_hot_validations = scorer.calculate_priority_scores(
        lines_df_hot_validations
    )

    # Get summary statistics
    stats = scorer.get_summary_statistics(lines_df_hot_validations)
    logger.info("Scoring Statistics:")
    logger.info(f"  Total lines: {stats['total_lines']}")
    logger.info(f"  Lines without AC: {stats['lines_without_ac']}")
    logger.info(f"  Lines with partial AC: {stats['lines_partial_ac']}")
    logger.info(f"  Lines with full AC: {stats['lines_full_ac']}")
    logger.info(f"  Avg priority score: {stats['avg_priority_score']:.2f}")

    # Display results
    logger.info("=" * 80)
    logger.info("=== TOP 20 PRIORITY LINES TO EQUIP ===")
    logger.info("=" * 80)

    for idx, row in lines_df_hot_validations.head(20).iterrows():
        logger.info(f"Rank #{row['rank']}: {row['route_id']} - {row['name_line']}")
        logger.info(f"  Temperature: {row['temperature']:.2f}°C")
        logger.info(f"  Stops in hot zones: {row['stop_id']}")
        logger.info(f"  Air Conditioning: {row['air_conditioning']}")
        logger.info(f"  Number of validations JUNE 2025: {row['nb_validations']}")
        logger.info(f"  Priority Score: {row['priority_score']:.2f}")

    # Save results
    lines_df_hot_validations.to_csv("data/output/prioritized_lines.csv", index=False)
    logger.info("Saved prioritized lines to: data/output/prioritized_lines.csv")


if __name__ == "__main__":
    # Parse command line arguments if provided
    if len(sys.argv) > 1:
        year = int(sys.argv[1])
        percentile = int(sys.argv[2]) if len(sys.argv) > 2 else 99
        main(year=year, percentile=percentile)
    else:
        main()
