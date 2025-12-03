import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
import geopandas as gpd
from shapely import wkt
import os
import subprocess
import sys

# Configuration de la page
st.set_page_config(
    page_title="Priorisation Climatisation Bus IDFM",
    page_icon="🚌",
    layout="wide"
)

# Titre principal
st.title("🚌 Priorisation des lignes de bus pour la climatisation")
st.markdown("### Analyse basée sur les projections climatiques et le trafic")

# Sidebar pour les paramètres
st.sidebar.header("⚙️ Paramètres d'analyse")

# Sélection de l'année
year = st.sidebar.selectbox(
    "Année de projection climatique",
    options=list(range(2025, 2091, 5)),
    index=5  # 2075 par défaut
)

# Sélection du nombre de lignes à afficher
top_n = st.sidebar.slider(
    "Nombre de lignes à prioriser",
    min_value=5,
    max_value=50,
    value=20,
    step=5
)

# Percentile pour les zones chaudes
percentile = st.sidebar.slider(
    "Percentile des zones les plus chaudes",
    min_value=90,
    max_value=99,
    value=99,
    step=1,
    help="99 = top 1% des zones les plus chaudes"
)

# Bouton pour lancer l'analyse
if st.sidebar.button("🔄 Lancer l'analyse", type="primary"):
    with st.spinner(f"Analyse en cours pour l'année {year}..."):
        # Modifier main.py pour utiliser les paramètres choisis
        result = subprocess.run(
            [sys.executable, "main.py", str(year), str(percentile)],
            capture_output=True,
            text=True
        )
        
        if result.returncode == 0:
            st.sidebar.success("✅ Analyse terminée avec succès!")
        else:
            st.sidebar.error("❌ Erreur lors de l'analyse")
            st.sidebar.code(result.stderr)

# Chargement des fichiers de sortie
output_dir = "data/output"
hot_squares_file = os.path.join(output_dir, "hot_squares.csv")
stops_file = os.path.join(output_dir, "stops_in_hot_zones.csv")
lines_file = os.path.join(output_dir, "prioritized_lines.csv")

# Vérifier que les fichiers existent
if all(os.path.exists(f) for f in [hot_squares_file, stops_file, lines_file]):
    
    # Charger les données
    @st.cache_data
    def load_data():
        hot_squares_df = pd.read_csv(hot_squares_file)
        hot_squares_df['geometry'] = hot_squares_df['geometry'].apply(wkt.loads)
        hot_squares_gdf = gpd.GeoDataFrame(hot_squares_df, geometry='geometry', crs='EPSG:4326')
        
        stops_df = pd.read_csv(stops_file)
        stops_df['geometry'] = stops_df['geometry'].apply(wkt.loads)
        stops_gdf = gpd.GeoDataFrame(stops_df, geometry='geometry', crs='EPSG:4326')
        
        lines_df = pd.read_csv(lines_file)
        
        return hot_squares_gdf, stops_gdf, lines_df
    
    hot_squares_gdf, stops_gdf, lines_df = load_data()
    
    # Section: Statistiques globales
    st.header("📊 Statistiques globales")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Carreaux chauds (2.5km²)", len(hot_squares_gdf))
    
    with col2:
        st.metric("Arrêts concernés", len(stops_gdf))
    
    with col3:
        st.metric("Lignes identifiées", len(lines_df))
    
    with col4:
        temp_max = hot_squares_gdf['temperature'].max()
        st.metric("Température max", f"{temp_max:.2f}°C")
    
    # Section: Carte interactive
    st.header("🗺️ Carte des zones chaudes et arrêts")
    
    # Créer la carte centrée sur l'Île-de-France
    center_lat = hot_squares_gdf.geometry.centroid.y.mean()
    center_lon = hot_squares_gdf.geometry.centroid.x.mean()
    
    m = folium.Map(
        location=[center_lat, center_lon],
        zoom_start=11,
        tiles='OpenStreetMap'
    )
    
    # Ajouter les carreaux chauds (polygones)
    for idx, row in hot_squares_gdf.iterrows():
        # Créer un popup avec les informations
        popup_text = f"""
        <b>Carreau chaud</b><br>
        Température: {row['temperature']:.2f}°C<br>
        Lon: {row['lon']:.4f}, Lat: {row['lat']:.4f}
        """
        
        # Définir la couleur en fonction de la température
        temp_norm = (row['temperature'] - hot_squares_gdf['temperature'].min()) / \
                    (hot_squares_gdf['temperature'].max() - hot_squares_gdf['temperature'].min())
        color = f"rgb({int(255 * temp_norm)}, {int(100 * (1-temp_norm))}, 0)"
        
        folium.GeoJson(
            row['geometry'],
            style_function=lambda x, color=color: {
                'fillColor': color,
                'color': 'red',
                'weight': 2,
                'fillOpacity': 0.4
            },
            popup=folium.Popup(popup_text, max_width=250)
        ).add_to(m)
    
    # Ajouter les arrêts (points)
    for idx, row in stops_gdf.iterrows():
        popup_text = f"""
        <b>{row['arrname']}</b><br>
        Arrêt ID: {row['arrid']}<br>
        Température zone: {row['temperature']:.2f}°C
        """
        
        folium.CircleMarker(
            location=[row['geometry'].y, row['geometry'].x],
            radius=3,
            popup=folium.Popup(popup_text, max_width=250),
            color='yellow',
            fill=True,
            fillColor='yellow',
            fillOpacity=0.5,
            opacity=0.5
        ).add_to(m)
    
    # Ajouter une légende
    legend_html = """
    <div style="position: fixed; 
                top: 10px; right: 10px; width: 200px; height: 120px; 
                background-color: white; border:2px solid grey; z-index:9999; 
                font-size:14px; padding: 10px">
    <b>Légende</b><br>
    <i style="background:rgba(255,100,0,0.4);width:20px;height:10px;display:inline-block;border:2px solid red"></i> Zones chaudes<br>
    <i style="background:yellow;width:10px;height:10px;border-radius:50%;display:inline-block"></i> Arrêts de bus<br>
    </div>
    """
    m.get_root().html.add_child(folium.Element(legend_html))
    
    # Afficher la carte
    st_folium(m, width=1400, height=600)
    
    # Section: Top lignes à équiper
    st.header(f"🏆 Top {top_n} lignes à équiper en priorité")
    
    top_lines = lines_df.head(top_n)
    
    # Afficher sous forme de tableau
    display_df = top_lines[['rank', 'route_id', 'name_line', 'temperature', 
                             'stop_id', 'air_conditioning', 'nb_validations', 
                             'priority_score']].copy()
    
    display_df.columns = ['Rang', 'ID Ligne', 'Nom', 'Temp. moy. (°C)', 
                          'Nb arrêts', 'Climatisation', 'Validations (juin 2025)', 
                          'Score priorité']
    
    # Formater les colonnes
    display_df['Temp. moy. (°C)'] = display_df['Temp. moy. (°C)'].apply(lambda x: f"{x:.2f}")
    display_df['Score priorité'] = display_df['Score priorité'].apply(lambda x: f"{x:.1f}")
    display_df['Validations (juin 2025)'] = display_df['Validations (juin 2025)'].apply(
        lambda x: f"{int(x):,}".replace(',', ' ') if pd.notna(x) else 'N/A'
    )
    
    st.dataframe(
        display_df,
        use_container_width=True,
        height=600,
        hide_index=True
    )
    
    # Section: Détails des 5 premières lignes
    st.header("📋 Détails des 5 lignes les plus prioritaires")
    
    for idx, row in top_lines.head(5).iterrows():
        with st.expander(f"#{int(row['rank'])} - Ligne {row['route_id']} : {row['name_line']}"):
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric("Score de priorité", f"{row['priority_score']:.1f}/100")
                st.metric("Température moyenne", f"{row['temperature']:.2f}°C")
            
            with col2:
                st.metric("Arrêts en zone chaude", int(row['stop_id']))
                st.metric("Climatisation", row['air_conditioning'])
            
            with col3:
                validations = f"{int(row['nb_validations']):,}".replace(',', ' ') if pd.notna(row['nb_validations']) else 'N/A'
                st.metric("Validations (juin 2025)", validations)
                
                # Indicateur de transport mode
                if 'transportmode' in row:
                    st.info(f"Mode: {row['transportmode']}")
    
    # Section: Analyse de la climatisation
    st.header("❄️ État de la climatisation des lignes")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Graphique en camembert
        ac_counts = lines_df['air_conditioning'].value_counts()
        st.subheader("Répartition de la climatisation")
        
        # Créer un dataframe pour le graphique
        ac_chart_data = pd.DataFrame({
            'État': ac_counts.index,
            'Nombre de lignes': ac_counts.values
        })
        st.bar_chart(ac_chart_data.set_index('État'))
    
    with col2:
        st.subheader("Statistiques")
        total_lines = len(lines_df)
        no_ac = len(lines_df[lines_df['air_conditioning'] == 'false'])
        partial_ac = len(lines_df[lines_df['air_conditioning'] == 'partial'])
        full_ac = len(lines_df[lines_df['air_conditioning'] == 'true'])
        
        st.metric("Lignes sans climatisation", f"{no_ac} ({no_ac/total_lines*100:.1f}%)")
        st.metric("Lignes climatisation partielle", f"{partial_ac} ({partial_ac/total_lines*100:.1f}%)")
        st.metric("Lignes entièrement climatisées", f"{full_ac} ({full_ac/total_lines*100:.1f}%)")
    
    # Section: Export des données
    st.header("💾 Téléchargement des données")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        csv_lines = top_lines.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📥 Télécharger top lignes (CSV)",
            data=csv_lines,
            file_name=f"top_{top_n}_lignes_{year}.csv",
            mime="text/csv"
        )
    
    with col2:
        csv_stops = stops_gdf.drop(columns=['geometry']).to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📥 Télécharger arrêts (CSV)",
            data=csv_stops,
            file_name=f"arrets_zones_chaudes_{year}.csv",
            mime="text/csv"
        )
    
    with col3:
        csv_squares = hot_squares_gdf.drop(columns=['geometry']).to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📥 Télécharger carreaux (CSV)",
            data=csv_squares,
            file_name=f"carreaux_chauds_{year}.csv",
            mime="text/csv"
        )

else:
    st.warning("⚠️ Aucune donnée disponible. Veuillez lancer une analyse en cliquant sur le bouton dans la barre latérale.")
    st.info("📝 L'analyse peut prendre quelques minutes lors de la première exécution.")

# Footer
st.markdown("---")
st.markdown("*Application développée pour l'analyse de priorisation de climatisation des bus IDFM*")
