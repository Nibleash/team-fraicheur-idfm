# Data Directory

This directory contains data files for the Team Fraicheur IDFM application.

## Directory Structure

```
data/
├── climate/        # Météo-France climate projection data
├── idfm/          # IDFM bus stops and lines data
└── validation/    # Validation datasets
```

## Climate Data

Place Météo-France climate projection files in the `climate/` directory.

**Expected format:**
- Files: `{variable}_{year}.csv` (e.g., `tas_2030.csv`, `tasmax_2040.csv`)
- Variables: `tas` (average temp), `tasmin` (minimum temp), `tasmax` (maximum temp)
- Resolution: 2.5 km tiles
- Columns:
  - `lon`: Longitude (WGS84)
  - `lat`: Latitude (WGS84)
  - `temperature`: Temperature value in Celsius
  - Additional metadata columns as needed

**Example:**
```csv
lon,lat,temperature,variable,year
2.3522,48.8566,28.5,tas,2030
2.3747,48.8566,29.2,tas,2030
```

## IDFM Data

Place IDFM transit data files in the `idfm/` directory.

### Bus Stops (`stops.csv`)

**Columns:**
- `stop_id`: Unique stop identifier
- `stop_name`: Stop name
- `lon`: Longitude (WGS84)
- `lat`: Latitude (WGS84)
- `lines`: Comma-separated list of lines serving this stop
- `daily_passengers`: Estimated daily passenger count
- `has_shelter`: Boolean (True/False)
- `has_bench`: Boolean (True/False)

**Example:**
```csv
stop_id,stop_name,lon,lat,lines,daily_passengers,has_shelter,has_bench
STOP_001,Place de la Bastille,2.369,48.853,"Line_20,Line_29",3500,True,True
STOP_002,Gare de Lyon,2.373,48.844,"Line_20,Line_61",4200,True,False
```

### Bus Lines (`lines.csv`)

**Columns:**
- `line_id`: Unique line identifier
- `line_name`: Line name/number
- `line_type`: Type (Bus, Tram, Metro)
- `total_stops`: Number of stops on the line
- `daily_frequency`: Number of trips per day

**Example:**
```csv
line_id,line_name,line_type,total_stops,daily_frequency
Line_20,Ligne 20,Bus,25,120
Line_29,Ligne 29,Bus,18,80
```

## Validation Data

Place validation datasets in the `validation/` directory for model testing and verification.

## Sample Data

If no data files are provided, the application will automatically generate sample data for demonstration purposes. The sample data uses realistic patterns for the Île-de-France region with:
- Climate tiles covering the region with urban heat island effects
- Bus stops concentrated around Paris with decreasing density outward
- Realistic passenger volumes and amenity distributions

## Data Sources

### Météo-France Climate Projections
- Source: Météo-France DRIAS platform
- Website: http://www.drias-climat.fr/
- License: Check specific data licensing terms

### IDFM Transit Data
- Source: Île-de-France Mobilités Open Data
- Website: https://data.iledefrance-mobilites.fr/
- License: Open Database License (ODbL)

## Notes

- All geographic coordinates should be in WGS84 (EPSG:4326)
- Temperature values should be in Celsius
- Ensure data files are properly formatted CSV with headers
- Missing values should be handled appropriately (NA, empty, or specific values)
