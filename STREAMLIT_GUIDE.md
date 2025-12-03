# Guide d'utilisation de l'application Streamlit

## Installation des dépendances

Installez les nouvelles dépendances :

```bash
pip install -r requirements.txt
```

## Lancement de l'application

Pour démarrer l'application Streamlit :

```bash
streamlit run streamlit_app.py
```

L'application s'ouvrira automatiquement dans votre navigateur par défaut à l'adresse `http://localhost:8501`.

## Utilisation

### 1. Configuration des paramètres (barre latérale)

- **Année de projection climatique** : Choisissez une année entre 2070 et 2079
- **Nombre de lignes à prioriser** : Sélectionnez combien de lignes afficher (5 à 50)
- **Percentile des zones les plus chaudes** : Ajustez le seuil (90-99%, par défaut 99 = top 1%)

### 2. Lancer l'analyse

Cliquez sur le bouton **"🔄 Lancer l'analyse"** pour exécuter l'analyse avec les paramètres choisis.

**Note** : La première exécution peut prendre quelques minutes car elle télécharge les données climatiques depuis le bucket S3.

### 3. Visualisation des résultats

L'application affiche :

- **Statistiques globales** : Nombre de carreaux chauds, arrêts concernés, lignes identifiées, température maximale
- **Carte interactive** : 
  - Polygones rouges = zones chaudes (2.5km × 2.5km)
  - Points bleus = arrêts de bus dans ces zones
  - Survol/clic pour plus d'informations
- **Tableau des lignes prioritaires** : Liste complète avec toutes les métriques
- **Détails des 5 lignes top** : Cartes détaillées avec métriques clés
- **Analyse climatisation** : Répartition de l'équipement actuel
- **Export des données** : Téléchargez les résultats en CSV

## Fonctionnalités principales

### Carte interactive
- Zoom et navigation
- Popups informatifs sur chaque élément
- Légende pour identifier les éléments
- Dégradé de couleur pour la température

### Priorisation des lignes
- Score calculé selon :
  - Température moyenne (30%)
  - Nombre d'arrêts en zone chaude (20%)
  - État de la climatisation (25%)
  - Nombre de validations (25%)

### Export des données
- Top N lignes prioritaires
- Liste des arrêts en zone chaude
- Carreaux de chaleur identifiés

## Structure des fichiers de sortie

Les analyses génèrent 3 fichiers dans `data/output/` :

1. **hot_squares.csv** : Carreaux de 2.5km² les plus chauds
2. **stops_in_hot_zones.csv** : Arrêts situés dans ces zones
3. **prioritized_lines.csv** : Lignes classées par score de priorité

## Dépannage

Si l'application ne démarre pas :
- Vérifiez que toutes les dépendances sont installées
- Assurez-vous d'être dans le bon répertoire
- Vérifiez que le port 8501 n'est pas déjà utilisé

Si l'analyse échoue :
- Vérifiez votre connexion internet (accès S3 requis)
- Consultez les logs dans le terminal
- Vérifiez que les fichiers IDFM sont présents dans `data/idfm/`
