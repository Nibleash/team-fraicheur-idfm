# Team Fraicheur IDFM 🌡️

A Streamlit application to identify priority bus stops and lines for cooling interventions in Île-de-France based on climate projections and passenger data.

## Overview

This application helps urban planners and transit authorities identify bus stops and lines that are most vulnerable to heat and need cooling interventions (shelters, vegetation, cooling systems, etc.). It combines:

1. **Météo-France climate projections** (tas/tasmin/tasmax at 2.5 km resolution)
2. **IDFM bus stops and lines data** (locations, passenger volumes, amenities)
3. **Spatial analysis** to match stops with climate tiles
4. **Priority scoring** based on temperature, passenger volume, and lack of amenities

## Features

- 📊 Interactive year selection for climate projections (2025-2050)
- 🗺️ Interactive map visualization with climate tiles and priority stops
- 🚏 Ranked list of priority bus stops
- 🚌 Ranked list of priority bus lines
- 📈 Statistical analysis and temperature distribution
- 📥 Export results to CSV

## Project Structure

```
team-fraicheur-idfm/
├── src/
│   ├── app.py                          # Main Streamlit application
│   └── modules/
│       ├── __init__.py
│       ├── climate_loader.py           # Load Météo-France climate data
│       ├── idfm_loader.py             # Load IDFM stops/lines data
│       ├── spatial_analysis.py        # Spatial joins and analysis
│       ├── scoring.py                 # Priority scoring logic
│       └── visualization.py           # Map visualization
├── data/
│   ├── climate/                       # Climate projection files
│   ├── idfm/                         # IDFM transit data
│   ├── validation/                   # Validation datasets
│   └── README.md                     # Data documentation
├── requirements.txt                   # Python dependencies
└── README.md                         # This file
```

## Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Setup

1. Clone the repository:
```bash
git clone https://github.com/Nibleash/team-fraicheur-idfm.git
cd team-fraicheur-idfm
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. (Optional) Add your data files to the `data/` directory following the format in `data/README.md`. If no data files are provided, the app will generate sample data automatically.

## Usage

### Running the Application

```bash
streamlit run src/app.py
```

The application will open in your default web browser at `http://localhost:8501`.

### Using the Interface

1. **Select Year**: Choose a climate projection year (2025-2050)
2. **Select Climate Variable**: 
   - `tas`: Average temperature
   - `tasmin`: Minimum temperature
   - `tasmax`: Maximum temperature
3. **Set Temperature Threshold**: Filter areas exceeding this temperature
4. **Set Display Options**: Number of top priority stops/lines to show
5. **Click "Run Analysis"**: Generate results and visualizations

### Interpreting Results

#### Priority Score

The priority score (0-100) is calculated using weighted factors:
- **Temperature** (35%): Higher temperature = higher priority
- **Passenger Volume** (30%): More passengers = higher priority
- **Lack of Shelter** (20%): No shelter = higher priority
- **Lack of Bench** (15%): No bench = higher priority

#### Map View

- **Red tiles**: Hottest climate zones
- **Red/Orange circles**: High priority bus stops
- Click on stops for detailed information

## Data Format

### Climate Data

Place climate files in `data/climate/` with naming: `{variable}_{year}.csv`

Required columns:
- `lon`, `lat`: Coordinates (WGS84)
- `temperature`: Temperature in Celsius

### IDFM Stops Data

Place in `data/idfm/stops.csv`

Required columns:
- `stop_id`, `stop_name`, `lon`, `lat`
- `lines`: Comma-separated line IDs
- `daily_passengers`: Integer
- `has_shelter`, `has_bench`: Boolean

### IDFM Lines Data

Place in `data/idfm/lines.csv`

Required columns:
- `line_id`, `line_name`, `line_type`
- `total_stops`, `daily_frequency`: Integer

See `data/README.md` for complete format specifications.

## Technology Stack

- **Streamlit**: Web application framework
- **GeoPandas**: Geospatial data processing
- **DuckDB**: In-memory data queries
- **Folium**: Interactive maps
- **Pandas/NumPy**: Data analysis
- **Shapely**: Geometric operations

## Development

### Module Descriptions

- **climate_loader.py**: Loads and processes Météo-France climate projection data
- **idfm_loader.py**: Loads and processes IDFM bus stops and lines
- **spatial_analysis.py**: Performs spatial joins between stops and climate tiles
- **scoring.py**: Calculates priority scores for stops and lines
- **visualization.py**: Creates interactive Folium maps

### Extending the Application

To modify scoring weights, edit the `PriorityScorer` class initialization in `src/modules/scoring.py`:

```python
weights = {
    'temperature': 0.35,
    'passenger_volume': 0.30,
    'lack_of_shelter': 0.20,
    'lack_of_bench': 0.15
}
```

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

## License

This project is provided as-is for urban planning and climate adaptation purposes.

## Data Sources

- **Climate Data**: Météo-France DRIAS platform (http://www.drias-climat.fr/)
- **Transit Data**: Île-de-France Mobilités Open Data (https://data.iledefrance-mobilites.fr/)

## Acknowledgments

Created for identifying priority cooling interventions in the Île-de-France public transit system as part of climate adaptation efforts.