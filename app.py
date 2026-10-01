# import streamlit as st 
# import pickle
# import requests


# movies = pickle.load(open("movies.pkl", "rb"))
# movie_list = movies['title'].values
# # print(movie_list)

# similarity = pickle.load(open('similarity.pkl', 'rb'))

# def fetch_poster(movie_id):
#     # fetch the poster image from tmdb API by 'movie_id'
#     API_KEY="25f71cf582524bc946934ca889919766"
#     url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}"
    
#     data = requests.get(url).json()
#     return f"https://image.tmdb.org/t/p/w500/{data.get('poster_path')}"


# def recommend(movie_name):
#     movie_index = movies[movies['title'].apply(lambda x: x.lower()) == movie_name.lower()].index[0]

#     distances = similarity[movie_index]
#     movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

#     recommend_movies = []
#     for i in movies_list:
#         print(i[0], fetch_poster(i[0]))
#         recommend_movies.append(movies.iloc[i[0]].title)
#     return recommend_movies

# st.title("Movie recommendation system")

# selected_movie_name = st.selectbox(
#     "Select your movie",
#     movie_list
# )

# if st.button("Recommend"):
#     recommendation = recommend(selected_movie_name)

#     for i in recommendation:
#         st.write(i)


# # 25f71cf582524bc946934ca889919766

import streamlit as st
import pickle
import requests


# Load movie data and similarity matrix
movies = pickle.load(open("movies.pkl", "rb"))
similarity = pickle.load(open("similarity.pkl", "rb"))

movie_list = movies["title"].values


# TMDB API key
API_KEY = "25f71cf582524bc946934ca889919766"

# def fetch_poster(movie_id):
#     url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}"

#     try:
#         response = requests.get(url).json()
#         my_poster = response.get('poster_path') 
#         print(f"my_poster = https://image.tmdb.org/t/p/w500{my_poster}")
#         return f"https://image.tmdb.org/t/p/w500/4wnfTO8mvqcTU62YMkUeKq49VMT.jpg"

        

#     except requests.exceptions.RequestException as e:
#         print(f"Error fetching poster for movie ID {movie_id}: {e}")
#         # https://api.themoviedb.org/3/movie/12?api_key=25f71cf582524bc946934ca889919766
#         # https://image.tmdb.org/t/p/w500/cCovtlN16ykvyFYnzKyv3dFtceG.jpg
#         # print(f"url = https://image.tmdb.org/t/p/w500{data.get('poster_path')}")
#         return None

def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US"

    data = requests.get(url)
    data = data.json()

    poster_path = data["poster_path"]

    return f"https://image.tmdb.org/t/p/w500{poster_path}"

def recommend(movie_name):
    """
    Find movies similar to the selected movie.
    """

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

        # i[0] is the dataframe index
        movie = movies.iloc[i[0]]

        # IMPORTANT:
        # Use the actual TMDB movie ID, not the dataframe index
        movie_id = movie["movie_id"]

        poster = fetch_poster(movie_id)

        recommendations.append({
            "title": movie["title"],
            "poster": "https://image.tmdb.org/t/p/w500/cCovtlN16ykvyFYnzKyv3dFtceG.jpg"
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

    # Display recommendations in columns
    cols = st.columns(5)

    for col, movie in zip(cols, recommendations):

        with col:

            if movie["poster"]:
                st.image(movie["poster"], width=True)
            else:
                st.write("Poster not available")

            st.write(movie["title"])