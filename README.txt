# 🎵 Warner Music Records — Spotify Hit Formula
### SQL Mini-Project | Ironhack Data Analytics Bootcamp
**Team:** Claire & Diana | **Date:** May 2026

---

## 📌 Business Context

Warner Music Records (WMR) needs a **data-driven investment filter** to identify songs
with high commercial potential before committing A&R resources. This project builds a
**SQL + Python analytical pipeline** over Spotify's Top 50 (2019) to extract audio
feature patterns that predict chart success.

---

## 🎯 Research Questions & Hypotheses

### Hypothesis 1 — Universal Hit Formula
> *The Spotify Top 50 songs share a universal audio profile formula
> that WMR can use as an investment filter.*

**Findings:** The Top 50 songs do cluster around a consistent audio signature:
- **Danceability:** mean 71 ± 12 — consistently high
- **Energy:** mean 64 ± 14 — moderate-to-high
- **Loudness:** mean −5.7 dB ± 2.1 — compressed, radio-ready
- **Liveness:** mean 14.7 ± 11 — low (studio productions dominate)
- **Acousticness:** mean 22 ± 19 — low-to-moderate
- **BPM:** mean 120 ± 31 — wide spread (formula is NOT BPM-dependent)

**Conclusion:** **Partially confirmed.** A universal baseline was identified
(high danceability + low liveness + compressed loudness), but the spread is
high enough that a *genre-aware* filter will outperform a single universal rule.

---

### Hypothesis 2 — Genre-Specific Formula
> *The audio feature signature of a hit song differs significantly across
> genres, requiring genre-specific investment criteria.*

**Key genre clusters (by popularity tier):**

| Tier | Genres | Signature |
|------|--------|-----------|
| Elite (92–95) | dfw rap, trap, electropop | High energy + dark valence (< 30) |
| Mid-High (89–91) | latin, reggaeton, pop house | High energy + bright valence (> 60) |
| Solid (85–89) | pop, dance pop, edm | Balanced energy + moderate valence |
| Lower (74–83) | canadian pop, boy band, australian pop | Varied — no dominant signature |

**Conclusion:** **Confirmed.** Genre-specific audio profiles exist and differ
meaningfully. WMR should apply **genre-aware filters** when evaluating demos.

---

## 🗃️ Dataset

| Source | File | Records |
|--------|------|---------|
| Kaggle — Top 50 Spotify 2019 | spotifytop50.csv | 50 rows × 13 features |

**Features:** TrackName, ArtistName, Genre, BeatsPerMinute, Energy, Danceability,
Loudness_dB, Liveness, Valence, Length, Acousticness, Speechiness, Popularity

> **Limitation:** Single-year snapshot (2019), 50 songs only, no non-hit control group.
> Results are descriptive; causal claims cannot be made without a comparison dataset.

---

## 🗂️ Project Structure

```
Deliverables/
  README.txt                   ← this file
  spotifytop50.csv             ← raw dataset (Kaggle)
  SpotifyTopSongs.sql          ← ERD schema
  Spotify_data_dump.sql        ← Sql script to fill database
  Miro_ERD.png                 ← Entity Relationship Diagram
  spotify_analysis.py          ← modular Python functions 
  Spotify_top50_merged.ipynb   ← main analysis notebook 
  WMR_Spotify_Presentation.    ← final slide deck in Google slides
  barplot_popularity_by_genre.png ← saved visualisation
```

---

## 🏗️ Database Schema

**Tables:** `Spotifysong`, `Metrics`  
**Relationship:** 1:1 via `metricId` (FK from `Spotifysong` → `Metrics`)

```
Spotifysong:  SongId (PK) | TrackName | Artist | Genre | Popularity | metricId (FK)
Metrics:      metricId (PK) | bpm | energy | danceability | loudness | liveness
                            | valence | length | acousticness | speechiness
```

See `Miro_ERD.png` for the full ERD diagram.

---

## ⚙️ Setup & Reproduction

### 1. Clone / download the project

```bash
git clone https://github.com/cadiyubu/Spotify_Miniproject.git

```

### 2. Install Python dependencies

```bash
pip install pandas matplotlib seaborn scipy -python jupyter
```

### 5. Run the notebook

```bash
jupyter notebook Spotify_top50_merged.ipynb
```


## 📊 Visualisations

| Plot | File | What it shows |
|------|------|---------------|
| Feature heatmap by genre | (notebook) | Audio signatures per genre |
| Popularity tiers heatmap | (notebook) | Features vs ranking band |


---

## 💡 WMR Investment Filter (Working Recommendation)

Based on this analysis, a song that matches the **Top 50 median profile** should satisfy:

```
danceability  ≥  65
energy        ≥  55
loudness_db   ≥ -8.0   
liveness      ≤  20    
acousticness  ≤  40
```

Apply **genre-specific thresholds** on top:
- **Latin/Reggaeton:** add valence ≥ 60, BPM 90–180
- **Trap/Hip-Hop:** drop valence constraint; speechiness 10–35
- **Pop/Dance-Pop:** danceability ≥ 70, energy ≥ 60

---

## ⚠️ Limitations 

1. **Small sample:** 50 songs is descriptive only — no statistical power for causal inference.
2. **No control group:** without non-charting songs, we cannot isolate what *makes* a hit.
3. **Single year:** genre trends shift; 2019 profiles may differ from 2024 patterns.


---

## 🔗 Links

- **Dataset:** https://www.kaggle.com/datasets/leonardopena/top50spotify2019
- **Presentation:** https://docs.google.com/presentation/d/1LXfLc5Ft7tx5OLupdoYuSwVAtXERqVSfF7fpXfVVEhg/edit?slide=id.p1#slide=id.p1
- **GitHub Repo:** 
