# 🎬 Movie Recommendation System

Ever wondered how Netflix recommends movies?  
This project builds a **Content-Based Movie Recommendation System** that suggests similar movies based on user selection.

---

## 🚀 How It Works

1️⃣ User selects a movie from the dropdown  
2️⃣ System analyzes movie metadata (genres, keywords, cast, crew)  
3️⃣ TF-IDF Vectorization is applied  
4️⃣ Cosine Similarity calculates closeness between movies  
5️⃣ Top 5 similar movies are recommended instantly  

---

## 🧠 Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit (for UI)
- TMDB Dataset

---

## 🎯 Key Features

✔ Content-Based Filtering  
✔ Cosine Similarity Algorithm  
✔ Precomputed Similarity Matrix  
✔ Interactive Streamlit UI  
✔ Fast Recommendation Response  

---

## 📊 Dataset

- 5000+ movies from TMDB
- Features used: Genres, Keywords, Cast, Crew
- Cleaned and preprocessed for accurate similarity computation

---

## 💻 Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
