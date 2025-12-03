from typing import Optional
import geopandas as gpd
import pandas as pd
from shapely.geometry import box
import xarray as xr
import numpy as np
import s3fs


class ClimateDataLoader:
    TILE_SIZE = 0.0225
    
    def __init__(self, data_dir: str):
        pass
        
    def load_climate_tiles_from_s3(
        self, 
        year: int, 
        variable: str = "tasAdjust",
        scenario: str = "ssp370",
        percentile: Optional[float] = None
    ) -> gpd.GeoDataFrame:
        """
        Load climate data from Météo France S3 bucket and return as GeoDataFrame.
        
        Args:
            year: Year to extract data for
            variable: Climate variable (default: tasAdjust for adjusted temperature)
            scenario: Climate scenario (default: ssp370)
            percentile: If provided (e.g., 0.90), return only tiles above this percentile
            
        Returns:
            GeoDataFrame with climate tiles (2.5km squares) and mean summer temperatures
        """
        # Calculate decade range for file selection
        decade = (year // 10)
        year_range = (decade * 10, decade * 10 + 9)
        
        # Connect to S3 bucket
        fs = s3fs.S3FileSystem(
            anon=True,
            client_kwargs={
                'endpoint_url': 'https://object.files.data.gouv.fr'
            }
        )
        
        # Construct URL for the climate data
        url = (
            f"meteofrance-drias/SocleM-Climat-2025/CPRCM/METROPOLE/ALPX-3/"
            f"CNRM-ESM2-1/r1i1p1f2/CNRM-AROME46t1/{scenario}/day/{variable}/"
            f"version-hackathon-102025/{variable}_FR-Metro_CNRM-ESM2-1_{scenario}_"
            f"r1i1p1f2_CNRM-MF_CNRM-AROME46t1_v1-r1_MF-CDFt-ANASTASIA-ALPX-3-1991-2020_"
            f"day_{year_range[0]}0101-{year_range[1]}1231.nc"
        )
        
        # Open dataset
        ds = xr.open_dataset(fs.open(url, 'rb'), engine='h5netcdf')
        
        # Filter to Île-de-France region
        lat, lon = ds.lat.load(), ds.lon.load()
        mask = ((lat >= 48.1) & (lat <= 49.1) & (lon >= 1.4) & (lon <= 3.6))
        
        y_idx, x_idx = np.where(mask.values)
        y_slice = slice(y_idx.min(), y_idx.max() + 1)
        x_slice = slice(x_idx.min(), x_idx.max() + 1)
        
        # Extract summer months (June, July, August) for the specified year
        ds_jja_idf = ds.sel(
            time=(ds.time.dt.year == year) & ds.time.dt.month.isin([6, 7, 8])
        ).isel(y=y_slice, x=x_slice).load()
        
        # Convert to DataFrame
        df = ds_jja_idf.to_dataframe().reset_index()
        df_summer_idf = df[["time", "lon", "lat", variable]].drop_duplicates()
        
        # Convert Kelvin to Celsius
        df_summer_idf["temperature"] = df_summer_idf[variable] - 273.15
        
        # Calculate mean temperature per grid cell (tile)
        df_mean_temp = df_summer_idf.groupby(["lon", "lat"]).agg({
            "temperature": "mean"
        }).reset_index()
        
        # Filter to percentile if specified
        if percentile is not None:
            threshold = df_mean_temp["temperature"].quantile(percentile)
            df_mean_temp = df_mean_temp[df_mean_temp["temperature"] >= threshold].copy()
            df_mean_temp = df_mean_temp.sort_values("temperature", ascending=False)
        
        # Convert to GeoDataFrame with 2.5km tiles
        return self.convert_to_geodataframe(df_mean_temp)
    
    def convert_to_geodataframe(self, df: pd.DataFrame) -> gpd.GeoDataFrame:
        half_tile = self.TILE_SIZE / 2
        geometries = [box(row["lon"] - half_tile, row["lat"] - half_tile, 
                         row["lon"] + half_tile, row["lat"] + half_tile) 
                     for _, row in df.iterrows()]
        gdf = gpd.GeoDataFrame(df, geometry=geometries, crs="EPSG:4326")
        return gdf
