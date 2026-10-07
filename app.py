import streamlit as st
import pickle
import requests
import os
from dotenv import load_dotenv

# Load data
movies = pickle.load(open("movies.pkl", "rb"))
similarity = pickle.load(open("similarity.pkl", "rb"))

movie_list = movies["title"].values

# TMDB API
load_dotenv()
API_KEY = os.getenv("TMDB_API_KEY")
session = requests.Session()


def fetch_poster(movie_id):
    url = (
        f"https://api.themoviedb.org/3/movie/"
        f"{movie_id}?api_key={API_KEY}&language=en-US"
    )

    try:
        response = session.get(url, timeout=10)
        response.raise_for_status()

        data = response.json()

        poster_path = data.get("poster_path")

        if poster_path:
            return f"https://image.tmdb.org/t/p/w500{poster_path}"

    except requests.RequestException as e:
        print("exception:", e)

    return None


def recommend(movie_name):
    movie_index = movies[
        movies["title"].apply(lambda x: x.lower()) == movie_name.lower()
    ].index[0]

    distances = similarity[movie_index]

    movies_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommendations = []

    for i in movies_list:
        movie = movies.iloc[i[0]]

        movie_id = movie["movie_id"]
        poster = fetch_poster(movie_id)

        recommendations.append({
            "title": movie["title"],
            "poster": poster
        })

    return recommendations


# Streamlit UI
st.title("Movie Recommendation System")

selected_movie_name = st.selectbox(
    "Select your movie",
    movie_list
)


if st.button("Recommend"):

    recommendations = recommend(selected_movie_name)

    cols = st.columns(5)

    for col, movie in zip(cols, recommendations):

        with col:

            if movie["poster"]:
                st.image(movie["poster"], width="stretch")
            else:
                st.write("Poster not available")

            st.write(movie["title"])