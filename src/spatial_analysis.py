import geopandas as gpd

class SpatialAnalyzer:
    def __init__(self):
        pass
    
    def join_stops_with_climate(self, stops_gdf: gpd.GeoDataFrame, 
                                climate_gdf: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
        if stops_gdf.crs != climate_gdf.crs:
            climate_gdf = climate_gdf.to_crs(stops_gdf.crs)
        
        joined = gpd.sjoin(stops_gdf, climate_gdf, how="inner", predicate="within")
        
        if "index_right" in joined.columns:
            joined = joined.drop(columns=["index_right"])
            
        return joined
