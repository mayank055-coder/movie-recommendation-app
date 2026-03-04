import os
import pickle
import streamlit as st
import requests
import gdown

# -------------------- PAGE CONFIG --------------------
st.set_page_config(
    page_title="Movie Recommender",
    page_icon="🎬",
    layout="wide"
)

# -------------------- DOWNLOAD similarity.pkl --------------------
similarity_file_id = "1axlel82q9MFMGP7x4JjKTP4lNxzTpBDh"
similarity_url = f"https://drive.google.com/uc?id={similarity_file_id}"

if not os.path.exists("similarity.pkl"):
    with st.spinner("Downloading recommendation model... ⏳"):
        gdown.download(similarity_url, "similarity.pkl", quiet=False)

# -------------------- LOAD DATA --------------------
movies = pickle.load(open('movie_list.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

# -------------------- FUNCTIONS --------------------
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=547fc9d04473ff2f05785b0138caf102&language=en-US"
    data = requests.get(url).json()
    poster_path = data.get('poster_path')

    if poster_path:
        return "https://image.tmdb.org/t/p/w500/" + poster_path
    else:
        return "https://via.placeholder.com/500x750?text=No+Image"

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(
        list(enumerate(similarity[index])),
        reverse=True,
        key=lambda x: x[1]
    )

    recommended_movie_names = []
    recommended_movie_posters = []

    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_names.append(movies.iloc[i[0]].title)
        recommended_movie_posters.append(fetch_poster(movie_id))

    return recommended_movie_names, recommended_movie_posters

# -------------------- UI --------------------
st.markdown(
    """
    <h1 style='text-align: center; color: #ff4b4b;'>
    🎬 Movie Recommender System
    </h1>
    <p style='text-align: center; font-size:18px;'>
    Get personalized movie recommendations instantly 🍿
    </p>
    """,
    unsafe_allow_html=True
)

st.divider()

movie_list = movies['title'].values

selected_movie = st.selectbox(
    "🔍 Search or select a movie",
    movie_list
)

if st.button('✨ Show Recommendations'):

    with st.spinner("Finding best matches for you... 🎯"):
        names, posters = recommend(selected_movie)

    st.subheader("🎥 Recommended Movies")

    cols = st.columns(5)

    for i in range(5):
        with cols[i]:
            st.image(posters[i])
            st.caption(names[i])

st.divider()
st.markdown(
    "<center>Built with ❤️ using Streamlit</center>",
    unsafe_allow_html=True
)