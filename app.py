
import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import html

# Load and clean data
@st.cache_data
def load_data():
    anime = pd.read_csv("anime.csv")
    anime['genre'] = anime['genre'].fillna('')
    anime['name'] = anime['name'].apply(html.unescape).str.strip()
    return anime

# Recommender setup
def create_similarity_matrix(anime_df):
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(anime_df['genre'])
    cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
    return cosine_sim

# Recommendation function
def recommend_content(title, anime_df, cosine_sim, top_n=10):
    indices = pd.Series(anime_df.index, index=anime_df['name']).drop_duplicates()
    idx = indices.get(title)
    if idx is None:
        return None
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:top_n+1]
    anime_indices_top = [i[0] for i in sim_scores]
    return anime_df['name'].iloc[anime_indices_top]

# Streamlit UI
st.title("🎌 Anime Recommender")
st.write("Enter the name of an anime you've recently watched to get similar recommendations.")

# Load data
anime_df = load_data()
cosine_sim = create_similarity_matrix(anime_df)

# Input field instead of dropdown
user_input = st.text_input("Anime title you watched recently:")

# Show recommendations
if user_input:
    recommendations = recommend_content(user_input.strip(), anime_df, cosine_sim)
    if recommendations is None:
        st.warning("❌ Anime not found! Please check the spelling or try another title.")
    else:
        st.success("✅ Here are some anime you might enjoy:")
        for i, name in enumerate(recommendations, 1):
            st.write(f"{i}. {name}")
