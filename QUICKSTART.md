# Quick Start Guide

This guide will help you get the Team Fraicheur IDFM application up and running in minutes.

## Prerequisites

- Python 3.8 or higher
- pip package manager
- Internet connection (for dependency installation)

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Nibleash/team-fraicheur-idfm.git
   cd team-fraicheur-idfm
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

   This will install all required packages including Streamlit, GeoPandas, DuckDB, and visualization libraries.

## Running the Application

1. **Start the Streamlit app:**
   ```bash
   streamlit run src/app.py
   ```

2. **Access the application:**
   - The app will automatically open in your default browser
   - If not, navigate to: `http://localhost:8501`

## Using the Application

### Step 1: Configure Analysis Parameters

In the left sidebar, set:
- **Year**: Choose a climate projection year (2025-2050)
- **Climate Variable**: Select temperature type
  - `tas`: Average temperature
  - `tasmin`: Minimum temperature  
  - `tasmax`: Maximum temperature
- **Temperature Threshold**: Set the heat threshold (default: 30°C)
- **Display Options**: Number of top priority stops/lines

### Step 2: Run Analysis

Click the **"🔍 Run Analysis"** button to:
1. Load climate data and bus stop information
2. Perform spatial joins
3. Calculate priority scores
4. Generate visualizations

### Step 3: Explore Results

Navigate through the tabs:

#### 🗺️ Interactive Map
- View climate tiles colored by temperature
- See priority bus stops as markers
- Click on stops for detailed information

#### 🚏 Priority Stops
- See ranked list of bus stops needing cooling
- View temperature, passenger volume, and amenities
- Download results as CSV

#### 🚌 Priority Lines
- See ranked list of bus lines needing cooling
- View aggregated statistics per line
- Download results as CSV

#### 📊 Statistics
- Temperature distribution across region
- Priority score distribution
- Summary metrics

## Sample Data

The application automatically generates sample data if no actual data files are present. This allows you to:
- Test the application immediately
- Understand the expected data format
- Develop your own data processing pipelines

## Adding Real Data

To use actual climate and transit data:

1. **Climate Data**: Place Météo-France files in `data/climate/`
   - Format: `{variable}_{year}.csv` (e.g., `tas_2030.csv`)
   - Required columns: `lon`, `lat`, `temperature`

2. **IDFM Stops**: Place file in `data/idfm/stops.csv`
   - Required columns: `stop_id`, `stop_name`, `lon`, `lat`, `lines`, `daily_passengers`, `has_shelter`, `has_bench`

3. **IDFM Lines**: Place file in `data/idfm/lines.csv`
   - Required columns: `line_id`, `line_name`, `line_type`, `total_stops`, `daily_frequency`

See `data/README.md` for detailed format specifications.

## Troubleshooting

### Port Already in Use
If port 8501 is already in use:
```bash
streamlit run src/app.py --server.port 8502
```

### Module Import Errors
Ensure you're in the project root directory and have installed all dependencies:
```bash
pip install -r requirements.txt
```

### Memory Issues with Large Datasets
For large datasets, consider:
- Filtering data before loading
- Using DuckDB for data preprocessing
- Reducing the number of displayed results

## Next Steps

- Customize priority scoring weights in `src/modules/scoring.py`
- Add new visualization layers in `src/modules/visualization.py`
- Extend spatial analysis in `src/modules/spatial_analysis.py`
- Integrate additional data sources

## Support

For issues, questions, or contributions, please visit the GitHub repository.
