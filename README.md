# Team Fraicheur IDFM 🌡️🚌

A Python application to identify priority bus lines for air conditioning equipment based on climate projections and current equipment status in Île-de-France.

## Overview

This tool helps transit authorities prioritize bus line upgrades by identifying lines that:
- Pass through the hottest areas (top 1% hottest 2.5km tiles)
- Have many stops in these hot zones
- Currently lack air conditioning

It combines:

1. **Météo-France climate projections** from S3 (summer temperatures at 2.5 km resolution, scenario SSP370)
2. **IDFM bus network data** (stops locations, lines, air conditioning status)
3. **Spatial analysis** to identify stops in hot zones
4. **Priority scoring** based on temperature, number of affected stops, and AC status

## Features

- 🌡️ Loads climate data directly from Météo-France S3 bucket (no local files needed)
- 🗺️ Identifies top 1% hottest 2.5km tiles in Île-de-France
- 🚏 Spatially joins bus stops with hot zones
- 🚌 Aggregates by bus line with temperature and stop count
- 🎯 Scores lines based on configurable weights (temperature: 40%, stops: 30%, AC status: 30%)
- 📊 Exports results to CSV files

## Project Structure

```
team-fraicheur-idfm/
├── src/
│   ├── climate_loader.py              # Load climate data from S3
│   ├── idfm_loader.py                 # Load IDFM stops/lines data
│   ├── spatial_analysis.py            # Spatial joins and analysis
│   └── scoring.py                     # Priority scoring logic
├── data/
│   └── idfm/                          # IDFM transit data
│       ├── arrets.csv                 # Bus stops
│       ├── lignes.csv                 # Bus lines
│       └── arrets-lignes.csv          # Stops-lines mapping
├── main.py                            # Main analysis script
├── requirements.txt                   # Python dependencies
└── README.md                          # This file
```

## Installation

### Prerequisites

- Python 3.9 or higher
- pip package manager
- Internet connection (to access Météo-France S3 bucket)

### Setup

1. Clone the repository:
```bash
git clone https://github.com/Nibleash/team-fraicheur-idfm.git
cd team-fraicheur-idfm
```

2. Create a virtual environment (recommended):
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Download IDFM data files and place them in `data/idfm/`:
   - `arrets.csv` - Bus stops
   - `lignes.csv` - Bus lines
   - `arrets-lignes.csv` - Stops-lines mapping

## Usage

### Running the Analysis

```bash
python main.py
```

The script will:
1. Load climate data from Météo-France S3 bucket for the specified year (2075)
2. Extract the top 1% hottest 2.5km tiles in summer (June-August)
3. Load IDFM bus stops and lines data
4. Perform spatial join to find stops in hot zones
5. Calculate priority scores for each bus line
6. Display results in console and save to CSV files

### Output Files

The analysis generates three CSV files:
- `hot_squares.csv` - The hottest climate tiles (coordinates and temperature)
- `stops_in_hot_zones.csv` - Bus stops located in hot zones
- `prioritized_lines.csv` - Bus lines ranked by priority score

### Configuration

Edit `main.py` to adjust parameters:

```python
YEAR = 2075           # Climate projection year
PERCENTILE = 0.99     # Top 1% hottest tiles (0.90 = top 10%)

# Scoring weights
scorer = LineScorer(weights={
    "temperature": 0.40,        # 40% weight
    "stops": 0.30,              # 30% weight  
    "air_conditioning": 0.30    # 30% weight
})
```

## Priority Scoring Methodology

The priority score (0-100) is calculated using weighted factors:

### Temperature Score (40%)
- Normalized average temperature of all stops in hot zones
- Higher temperature = higher priority

### Stops Score (30%)
- Number of stops the line has in hot zones
- More stops = higher priority (more riders affected)

### Air Conditioning Score (30%)
- **No AC or Unknown** (1.0): Highest priority - line urgently needs equipment
- **Partial AC** (0.5): Medium priority - line partially equipped
- **Full AC** (0.0): Lowest priority - line already fully equipped

**Formula**: `priority_score = (0.40 × temp_score + 0.30 × stops_score + 0.30 × ac_score) × 100`

## Data Format

### IDFM Data Files

#### arrets.csv (Bus Stops)
Required columns:
- `ArRId`: Stop ID
- `ArRGeopoint`: Coordinates as "latitude, longitude"
- `ArRType`: Stop type (filter for "bus")

#### lignes.csv (Bus Lines)
Required columns:
- `id_line`: Line ID
- `name_line`: Line name/number
- `transportmode`: Transport mode (filter for "bus")
- `air_conditioning`: "true", "partial", "false", or "unknown"

#### arrets-lignes.csv (Stops-Lines Mapping)
Required columns:
- `route_id`: Line ID (with "IDFM:" prefix - will be removed)
- `stop_id`: Stop ID (with "IDFM:" prefix - will be removed)
- `mode`: Transport mode (filter for "Bus")

### Climate Data

Climate data is automatically loaded from Météo-France S3 bucket:
- Source: `meteofrance-drias` bucket on `object.files.data.gouv.fr`
- Variable: `tasAdjust` (adjusted temperature)
- Scenario: SSP370
- Resolution: 2.5km tiles
- Coverage: Île-de-France region (lat: 48.1-49.1, lon: 1.4-3.6)

## Technology Stack

- **xarray**: Load NetCDF climate data
- **s3fs**: Access Météo-France S3 bucket
- **GeoPandas**: Geospatial data processing
- **Pandas/NumPy**: Data analysis
- **Shapely**: Geometric operations (2.5km box tiles)

## Module Descriptions

### climate_loader.py
Loads climate data from Météo-France S3 bucket:
- Connects to S3 anonymously
- Loads NetCDF files with xarray
- Filters to Île-de-France region
- Extracts summer months (JJA)
- Calculates mean temperature per tile
- Converts to GeoDataFrame with 2.5km box geometries

### idfm_loader.py
Loads IDFM transit data:
- Parses CSV files with stops and lines
- Converts geopoint strings to coordinates
- Filters for bus mode only
- Creates Point geometries for stops
- Maps stops to lines

### spatial_analysis.py
Performs geospatial operations:
- Spatial join between stops (points) and climate tiles (polygons)
- Finds all stops within hot zones

### scoring.py
Calculates priority scores:
- Normalizes temperature and stop count and validations
- Assigns AC status scores
- Computes weighted priority score
- Ranks lines by priority

## Example Output

```
Rank #1: C01848 - R
  Temperature: 21.70°C
  Stops in hot zones: 2
  Air Conditioning: unknown
  Priority Score: 85.23

Rank #2: C01097 - 61
  Temperature: 21.64°C
  Stops in hot zones: 28
  Air Conditioning: partial
  Priority Score: 74.56
```

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

## License

This project is provided as-is for urban planning and climate adaptation purposes.

## Data Sources

- **Climate Data**: Météo-France DRIAS 2025 / SocleM-Climat platform (https://object.files.data.gouv.fr/meteofrance-drias/)
- **Transit Data**: Île-de-France Mobilités Open Data (https://data.iledefrance-mobilites.fr/)

## Acknowledgments

Created for identifying priority cooling interventions in the Île-de-France public transit system as part of climate adaptation efforts.