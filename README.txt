# 🎵 Warner Music GroupBy — Spotify Hit Formula
### SQL + Python Mini-Project | Ironhack Data Analytics Bootcamp
**Team:** Claire & Diana | **Date:** May 2026

---

## 📌 Business Context

**Warner Music GroupBy (WMG)** commits A&R resources to new artists before those artists chart.
The question: can audio features of already-charting songs reveal a pattern that helps WMG
filter future investment decisions?

---

## 🎯 Research Questions & Hypotheses

### Hypothesis 1 — Universal Hit Formula
> *The Spotify Top 50 songs share a universal audio profile that WMG can use as an
> investment filter.*

**Key findings from descriptive stats (std_table with CV %):**

| Feature          | Mean   | CV (%) | Signal  |
|------------------|--------|--------|---------|
| danceability     | 71     | 16.7%  | STRONG  |
| energy           | 64     | 22.2%  | MODERATE|
| loudness_db      | −5.7   | 36.4%  | MODERATE|
| liveness         | 14.7   | 75.9%  | WEAK    |
| acousticness     | 22     | 85.7%  | WEAK    |
| speechiness      | 12.5   | 89.4%  | WEAK    |
| beats_per_minute | 120    | 25.7%  | MODERATE|
| popularity       | 87.5   | 5.1%   | (target)|

**Conclusion:** Partially confirmed. Danceability clusters tightly (CV 17%) — a solid
anchor for the universal filter. BPM and Valence show high spread and should NOT be
fixed thresholds.

---

### Hypothesis 2 — Genre-Specific Formula
> *The hit formula differs by genre, requiring genre-specific investment criteria.*

Analysis focused on the three metrics that differentiated most across the top 5 songs:
**Beats Per Minute (BPM)**, **Valence**, and **Speechiness**.

A `clustermap` (Ward linkage, MinMax-normalised) revealed three macro-clusters:

| Cluster | Genres | Shared Profile |
|---------|--------|----------------|
| High Beats / High Speechiness | electropop, reggaeton, panamanian pop, trap music | High speechiness + high BPM |
| Mellow / Low-Tempo | edm, big room, canadian hip hop, atl hip hop, dance pop, country rap, escape room | Lower BPM, mixed valence |
| High Valence | boy band, canadian pop, latin, r&b en español, brostep, australian pop, reggaeton flow, pop house, dfw rap, pop | High valence, varied tempo |

These clusters were then compared against the mean metrics of the Top 5 songs (Rank 0.0)
in a grouped bar chart (`clusterVsTopsong_metrics.png`).

**Conclusion:** Confirmed. Genre-specific audio profiles differ meaningfully. WMG should
apply genre-aware filters when evaluating demos.

---

## 🗃️ Dataset

| Source | File | Records |
|--------|------|---------|
| Kaggle — Top 50 Spotify 2019 | spotifytop50.csv | 50 rows × 13 features |

**Features:** Track.Name, Artist.Name, Genre, Beats.Per.Minute, Energy, Danceability,
Loudness..dB.., Liveness, Valence., Length., Acousticness.., Speechiness., Popularity

After cleaning: track_name, artist_name, genre, beats_per_minute, energy, danceability,
loudness_db, liveness, valence, length, acousticness, speechiness, popularity

> **Limitation:** Single-year snapshot (2019), 50 songs only, no non-hit control group.
> Results are descriptive; causal claims cannot be made without a comparison dataset.

---

## 🗂️ Project Files

```
Deliverables/
  README.txt                       ← this file
  spotifytop50.csv                 ← raw dataset (Kaggle)
  Spotify_top50_merged.ipynb       ← main analysis notebook (DO NOT EDIT)
  spotify_analysis.py              ← modular Python functions used in the notebook
  SpotifyTopSongs.sql              ← SQL schema (ERD, created in MySQL Workbench)
  Spotify_data_dump.sql            ← SQL data load script (MySQL Workbench)
  Miro_ERD.png                     ← Entity Relationship Diagram (Miro)
  ERD_drawDB.png                   ← Entity Relationship Diagram (DrawDB)
  SpotifyHitFormula.key            ← presentation (Keynote)
  barplot_popularity_by_genre.png  ← saved chart: avg popularity per genre
  heatmap.png                      ← saved chart: audio features heatmap by genre
  cv_plot.png                      ← saved chart: coefficient of variation barplot
  genre_clustermap.png             ← saved chart: MinMax-normalised genre clustermap
  clusterVsTopsong_metrics.png     ← saved chart: cluster means vs Top 5 songs
```

---

## 🗄️ SQL

The database schema was designed and populated manually using **MySQL Workbench**.
Two tables (`Spotifysong` and `Metrics`) are linked 1:1 via `metricId`.
See `SpotifyTopSongs.sql` for the schema, `Spotify_data_dump.sql` for the data load,
and `Miro_ERD.png` / `ERD_drawDB.png` for the ERD diagrams.

---

## 📋 Notebook Structure

| Section | Focus |
|---------|-------|
| 1. Setup & Data Loading | Imports, CSV load, shape preview |
| 2. Data Quality & Cleaning | Column renaming (`clean_col_names`), type casting (`convert_numeric`), null/duplicate audit |
| 3. Formula Analysis (H1) | `std_table` with CV (%), CV barplot, scatter plots vs popularity |
| 4. Genre Analysis (H2) | Genre heatmap, rank-binned pivot, clustermap, cluster vs Top 5 comparison |
| 5. Conclusions & Obstacles | WMG filter recommendation, limitations |

---

## ⚙️ Setup & Reproduction

### 1. Clone / download the project

```bash
git clone https://github.com/cadiyubu/Spotify_Miniproject.git
```

### 2. Install Python dependencies

```bash
pip install pandas numpy matplotlib seaborn scikit-learn jupyter
```

### 3. Run the notebook

```bash
jupyter notebook Spotify_top50_merged.ipynb
```

The notebook auto-loads `spotifytop50.csv` from the same directory.
All charts are rendered inline and saved as `.png` files.

---

## 📊 Visualisations Produced

| File | Description |
|------|-------------|
| `cv_plot.png` | CV (%) barplot — which features are most consistent across the Top 50 |
| `heatmap.png` | Heatmap of mean audio features by genre (pop-variants first) |
| `barplot_popularity_by_genre.png` | Average popularity per genre, sorted descending |
| `genre_clustermap.png` | MinMax-normalised clustermap (BPM, valence, speechiness) with Ward dendrogram |
| `clusterVsTopsong_metrics.png` | Grouped bar: cluster means vs Top 5 song mean metrics |

---

## ⚠️ Limitations & Next Steps

1. **Small sample:** 50 songs is descriptive only — no statistical power for causal inference.
2. **No control group:** without non-charting songs we cannot isolate what *makes* a hit.
3. **Single year:** genre trends shift; 2019 profiles may differ from current patterns.


---

## 🔗 Links

- **Dataset:** https://www.kaggle.com/datasets/leonardopena/top50spotify2019
- **GitHub Repo:** https://github.com/cadiyubu/Spotify_Miniproject
- **Presentation:** https://docs.google.com/presentation/d/1LXfLc5Ft7tx5OLupdoYuSwVAtXERqVSfF7fpXfVVEhg/edit#slide=id.p1
