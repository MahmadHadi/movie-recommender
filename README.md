# Movie Recommendation System

A simple movie recommendation system built using Python and Machine Learning.

The project recommends movies based on the movie selected by the user. It uses movie data from the TMDB dataset and calculates how similar movies are to each other using their features.

I built this project to practice machine learning, data preprocessing, similarity-based recommendations, and deploying a small ML project using Streamlit.

## Demo

The application is built with Streamlit, where you can select a movie and get 5 similar movie recommendations along with their posters.

## Tech Stack

- Python
- NumPy
- Pandas
- Scikit-learn
- Streamlit
- TMDB API
- Google Colab

## How It Works

1. Movie data is loaded from the TMDB dataset.
2. Relevant movie information such as genres, keywords, cast, crew, and overview is processed.
3. The movie features are converted into a format that can be compared.
4. Similarity between movies is calculated using machine learning techniques.
5. When a user selects a movie, the system finds the most similar movies.
6. The TMDB API is used to fetch movie posters.

## 📂 Project Structure

```text
movie-recommender/
│
├── app.py
├── movies.pkl
├── similarity.pkl
├── requirements.txt
├── README.md
└── .gitignore
```

##  Run Locally

Clone the repository:

```bash
git clone https://github.com/MahmadHadi/movie-recommender.git
```

Go to the project directory:

```bash
cd movie-recommender
```

Create a virtual environment:

```bash
python3 -m venv .venv
```

Activate it:

```bash
source .venv/bin/activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Add your TMDB API key in `app.py`:

```python
API_KEY = "YOUR_TMDB_API_KEY"
```

Run the application:

```bash
streamlit run app.py
```

## Note

Some movies may not have a poster available through TMDB, so the application shows `Poster not available` for those movies.

## What I Learned

Through this project, I practiced:

- Data preprocessing with Pandas
- Working with NumPy
- Building a recommendation system
- Calculating movie similarity
- Using APIs in Python
- Creating a simple ML web application with Streamlit
- Managing Python dependencies with a virtual environment

## Author

**Mahmadhadi Nayani**

GitHub: [MahmadHadi](https://github.com/MahmadHadi)
