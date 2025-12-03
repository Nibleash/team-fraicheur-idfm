from pathlib import Path
import geopandas as gpd
import pandas as pd
from shapely.geometry import Point


class IDFMDataLoader:
    def __init__(self, data_dir: str):
        self.data_dir = Path(data_dir)

    def load_stops_ref(self) -> gpd.GeoDataFrame:
        stops_path = self.data_dir / "arrets.csv"

        if not stops_path.exists():
            raise FileNotFoundError(f"Data file {stops_path} not found.")

        df = pd.read_csv(stops_path, sep=";", dtype={"arrid": str})
        df_bus = df[df["arrtype"] == "bus"][
            ["arrid", "arrname", "arrgeopoint", "zdaid"]
        ]
        return self.convert_stops_to_geodataframe(df_bus)

    def load_lines(self) -> pd.DataFrame:
        lines_path = self.data_dir / "lignes.csv"

        if not lines_path.exists():
            raise FileNotFoundError(f"Data file {lines_path} not found.")

        df = pd.read_csv(lines_path, sep=";")
        mask = (df["transportsubmode"] != "nightBus") & (df["transportmode"] == "bus")
        return df[mask][["id_line", "name_line", "id_groupoflines", "air_conditioning"]]

    def convert_stops_to_geodataframe(self, df: pd.DataFrame) -> gpd.GeoDataFrame:
        df_copy = df.copy()
        coords = df_copy["arrgeopoint"].str.split(",", expand=True)
        df_copy["lat"] = coords[0].astype(float)
        df_copy["lon"] = coords[1].astype(float)

        geometries = [Point(row["lon"], row["lat"]) for _, row in df_copy.iterrows()]
        gdf = gpd.GeoDataFrame(df_copy, geometry=geometries, crs="EPSG:4326")
        return gdf

    def get_stops_lines(self, stops_gdf: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
        arrets_lignes_path = self.data_dir / "arrets-lignes.csv"

        if not arrets_lignes_path.exists():
            raise FileNotFoundError(f"Data file {arrets_lignes_path} not found.")

        df_arrets_lignes = pd.read_csv(arrets_lignes_path, sep=";")
        df_arrets_lignes_bus = df_arrets_lignes[df_arrets_lignes["mode"] == "Bus"]
        df_arrets_lignes_bus["route_id"] = df_arrets_lignes_bus["route_id"].str.replace(
            "IDFM:", "", regex=False
        )
        df_arrets_lignes_bus["stop_id"] = df_arrets_lignes_bus["stop_id"].str.replace(
            "IDFM:", "", regex=False
        )
        stops_for_line = df_arrets_lignes_bus[["route_id", "stop_id"]]

        result = stops_gdf.merge(
            stops_for_line, left_on="arrid", right_on="stop_id", how="inner"
        )

        return result

    def get_validations_lines(self, lines_df: pd.DataFrame) -> pd.DataFrame:
        validations_path = self.data_dir / "validations_adm.csv"

        if not validations_path.exists():
            raise FileNotFoundError(f"Data file {validations_path} not found.")

        df = pd.read_csv(validations_path)
        df_lines_validation = pd.merge(
            lines_df,
            df,
            left_on="id_groupoflines",
            right_on="ligne_adm",
            how="left",
        )
        return df_lines_validation.drop(columns=["ligne_adm"])
