<!-- Animated Header -->
<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=30&duration=3000&pause=1000&color=F7B731&center=true&vCenter=true&width=600&lines=🎬+Movie+Recommendation+System;Built+with+Python+%26+ML;Powered+by+TMDB+Dataset" alt="Typing SVG" />

<br/>

![Status](https://img.shields.io/badge/Status-In%20Progress-yellow?style=for-the-badge&logo=github)
![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python&logoColor=white)
![ML](https://img.shields.io/badge/ML-Scikit--Learn-orange?style=for-the-badge&logo=scikitlearn&logoColor=white)
![Streamlit](https://img.shields.io/badge/UI-Streamlit-red?style=for-the-badge&logo=streamlit&logoColor=white)

</div>

---

## 🚀 Project Status

```
╔══════════════════════════════════════════════════════╗
║                                                      ║
║   ✅  Data Pipeline          ████████████  DONE      ║
║   ✅  Feature Engineering    ████████████  DONE      ║
║   ✅  Recommendation Logic   ████████████  DONE      ║
║   🔄  UI Development         ░░░░░░░░░░░░  NEXT UP   ║
║   🔄  Backend Integration    ░░░░░░░░░░░░  NEXT UP   ║
║                                                      ║
╚══════════════════════════════════════════════════════╝
```

---

## 🎯 What's Done

The **core recommendation engine is fully built** and working. Here's what's under the hood:

- 📦 **Dataset** — TMDB 5000 Movies & Credits (Kaggle)
- 🧹 **Data Cleaning & Merging** — Genres, cast, crew, keywords extracted
- 🧠 **Feature Engineering** — Tags built from movie metadata
- 📐 **Similarity Model** — Cosine similarity on vectorized features
- 🎬 **Recommendation Logic** — Top-N similar movies returned for any input title

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Language | Python 3.10+ |
| Data | Pandas, NumPy |
| ML | Scikit-learn (TF-IDF / CountVectorizer) |
| Dataset | TMDB 5000 via Kaggle |
| UI *(coming soon)* | Streamlit |
| Environment | Ubuntu Docker Container |

---

## 📁 Project Structure

```
movie_recommendation_work/
│
├── 📓 ml_movie_recommendation_system.ipynb   ✅ Core ML logic
├── 🐍 dataset.py                             ✅ Kaggle dataset downloader
├── 🌐 Python_frontend/                       🔄 Streamlit UI (in progress)
├── 📄 tmdb_5000_movies.csv                   ✅ Dataset
└── 📄 tmdb_5000_credits.csv                  ✅ Dataset
```

---

## 🔮 What's Coming Next

```python
# TODO: UI & Integration
next_steps = [
    "🎨 Build Streamlit frontend with movie search",
    "🖼️  Fetch movie posters via TMDB API",
    "🔗  Connect recommendation engine to UI",
    "🚀  Deploy to cloud / Docker container",
]
```

---

## 🧪 How to Run (Core Engine)

```bash
# 1. Clone the repo
git clone https://github.com/tanirsahoo/machine_learning_works.git
cd machine_learning_works

# 2. Install dependencies
pip install pandas numpy scikit-learn kagglehub jupyter

# 3. Launch notebook
jupyter notebook ml_movie_recommendation_system.ipynb
```

---

<div align="center">

**Made with ❤️ by [Tanir Sahoo](https://github.com/tanirsahoo)**  
*MTech Cognitive Systems · IIT Kanpur*

![Visitor](https://visitor-badge.laobi.icu/badge?page_id=tanirsahoo.machine_learning_works)

</div>