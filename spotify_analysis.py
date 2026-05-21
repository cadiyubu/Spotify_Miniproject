"""
spotify_analysis.py
====================
Warner Music GroupBy — Spotify Hit Formula
SQL + Python Mini-Project | Ironhack Data Analytics Bootcamp
Team: Claire & Diana | May 2026

Modular helper functions that mirror exactly what is done inside
Spotify_top50_merged.ipynb. Import this file to reuse any step
without re-running the full notebook.

Sections
--------
1. Imports & Configuration
2. Data Loading & Cleaning     → clean_col_names(), convert_numeric()
3. Descriptive Statistics      → build_std_table()
4. Genre & Ranking Analysis    → build_genre_pivot(), build_rank_pivot(),
                                  get_genre_popularity()
5. Cluster Analysis            → assign_clusters(), build_cluster_plot_df()
6. Visualisations              → plot_cv_barplot(), plot_genre_heatmap(),
                                  plot_genre_clustermap(),
                                  plot_cluster_vs_top_songs()
"""

# ── 1. Imports & Configuration ───────────────────────────────────────────────
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler

CSV_PATH = "spotifytop50.csv"

# Exact list used throughout the notebook
NUMERIC_FEATURES = [
    "beats_per_minute", "energy", "danceability", "loudness_db",
    "liveness", "valence", "length", "acousticness", "speechiness",
    "popularity",
]

# The three focus metrics for H2 genre / cluster analysis
FOCUS_METRICS = ["beats_per_minute", "valence", "speechiness"]

# Genre cluster assignments (from Section 4 of the notebook)
CLUS1 = ["electropop", "reggaeton", "panamanian pop", "trap music"]
CLUS2 = ["edm", "big room", "canadian hip hop", "atl hip hop",
          "dance pop", "country rap", "escape room"]
CLUS3 = ["boy band", "canadian pop", "latin", "r&b en espanol", "brostep",
          "australian pop", "reggaeton flow", "pop house", "dfw rap", "pop"]


# ── 2. Data Loading & Cleaning ───────────────────────────────────────────────

def clean_col_names(df: pd.DataFrame) -> pd.DataFrame:
    """
    Standardise column names to snake_case and apply specific renames.

    Mirrors the exact function defined in the notebook (Section 2).
    Returns a new DataFrame — original is unchanged.

    Example
    -------
    >>> sp_df = clean_col_names(raw_df)
    """
    df2 = df.copy()
    df2.columns = df2.columns.map(lambda x: x.lower().replace(".", "_"))
    df2 = df2.rename(columns={
        "loudness__db__": "loudness_db",
        "length_":        "length",
        "acousticness__": "acousticness",
        "speechiness_":   "speechiness",
        "valence_":        "valence",
    })
    return df2


def convert_numeric(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cast all audio-feature columns to numeric using pd.to_numeric().

    Mirrors the exact function defined in the notebook (Section 2).
    Returns a new DataFrame — original is unchanged.

    Example
    -------
    >>> sp_df = convert_numeric(sp_df)
    """
    df2 = df.copy()
    numeric_data = [
        "beats_per_minute", "energy", "danceability", "loudness_db",
        "liveness", "valence", "length", "acousticness", "speechiness",
        "popularity",
    ]
    for col in numeric_data:
        df2[col] = pd.to_numeric(df2[col])
    return df2


def load_and_clean(path: str = CSV_PATH) -> pd.DataFrame:
    """
    Convenience loader: read CSV → drop unnamed index → clean names → cast numeric.

    Returns a clean DataFrame ready for analysis.
    """
    df = pd.read_csv(path)
    df = df.drop(columns=[c for c in df.columns if "Unnamed" in str(c)])
    df = clean_col_names(df)
    df = convert_numeric(df)
    return df


# ── 3. Descriptive Statistics ────────────────────────────────────────────────

def build_std_table(df: pd.DataFrame) -> pd.DataFrame:
    """
    Build the summary statistics table used in Section 3 (H1 analysis).

    Computes mean, std, min, max and adds CV (%) = std / |mean| * 100.
    Popularity row is retained (to match the notebook) but can be dropped
    afterwards with: std_table = std_table.drop(index='popularity')

    Returns
    -------
    pd.DataFrame  — indexed by feature name, columns: mean, std, min, max, CV (%)

    Example
    -------
    >>> std_table = build_std_table(sp_df)
    >>> std_table_sorted = std_table.drop(index='popularity').sort_values('CV (%)')
    """
    numeric_data = [
        "beats_per_minute", "energy", "danceability", "loudness_db",
        "liveness", "valence", "length", "acousticness", "speechiness",
        "popularity",
    ]
    std_table = round(df[numeric_data].describe().T[["mean", "std", "min", "max"]], 2)
    std_table["CV (%)"] = (std_table["std"] / std_table["mean"].abs() * 100).round(1)
    return std_table


# ── 4. Genre & Ranking Analysis ──────────────────────────────────────────────

def build_genre_pivot(df: pd.DataFrame,
                      features: list = None) -> pd.DataFrame:
    """
    Build a pivot table of mean audio features per genre.

    Reorders rows so pop-variant genres appear first, matching the
    approach used in Section 3.1 / Section 4 of the notebook.

    Parameters
    ----------
    df       : cleaned Spotify DataFrame
    features : list of feature column names to include (default: NUMERIC_FEATURES)

    Returns
    -------
    pd.DataFrame  — rows = genres, columns = features

    Example
    -------
    >>> results = build_genre_pivot(sp_df, numeric_data)
    >>> sns.heatmap(results, annot=False)
    """
    if features is None:
        features = NUMERIC_FEATURES

    all_genres = list(df["genre"].unique())
    pop_genres  = [g for g in all_genres if "pop" in g]
    other_genres = [g for g in all_genres if "pop" not in g]
    ordered = pop_genres + other_genres

    pivot = df.pivot_table(index="genre", values=features, aggfunc="mean")
    pivot = pivot.reindex(index=ordered)
    return pivot


def build_rank_pivot(df: pd.DataFrame,
                     features: list = None,
                     bin_size: int = 5) -> tuple:
    """
    Bin songs into rank bands of `bin_size` (sorted by popularity desc) and
    compute mean (and max/min) per band.

    Mirrors the logic from Section 3 of the notebook:
        means_binned_by_5['rank'] = [np.floor(n/5) for n in range(50)]

    Returns
    -------
    (binned_means_pivot, binned_means_pivot_all, values_top_songs)
      - binned_means_pivot      : mean per rank band
      - binned_means_pivot_all  : mean + max + min per rank band (stacked)
      - values_top_songs        : first 10 rows of the stacked table (rank 0 metrics)

    Example
    -------
    >>> pivot, pivot_all, top = build_rank_pivot(sp_df, numeric_data)
    >>> sns.heatmap(pivot, annot=False)
    """
    if features is None:
        features = NUMERIC_FEATURES

    ranked = df.sort_values("popularity", ascending=False).copy()
    ranked["rank"] = [np.floor(n / bin_size) for n in range(len(ranked))]

    pivot = ranked.pivot_table(index="rank", values=features, aggfunc="mean")
    pivot_all = ranked.pivot_table(index="rank", values=features,
                                   aggfunc=["mean", "max", "min"])
    top_songs = pivot_all.stack().head(10)
    return pivot, pivot_all, top_songs


def get_genre_popularity(df: pd.DataFrame) -> pd.DataFrame:
    """
    Return genres sorted by average popularity (descending).

    Used to produce barplot_popularity_by_genre.png.

    Example
    -------
    >>> gp = get_genre_popularity(sp_df)
    >>> sns.barplot(data=gp, x='genre', y='avg_popularity', palette='YlOrRd',
    ...             order=gp['genre'])
    """
    return (
        df.groupby("genre")["popularity"]
        .mean()
        .round(1)
        .sort_values(ascending=False)
        .reset_index()
        .rename(columns={"popularity": "avg_popularity"})
    )

