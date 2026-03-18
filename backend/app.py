from fastapi import FastAPI
import requests
import os
from dotenv import load_dotenv

watchlists = {}
current_id = 1

app = FastAPI()
load_dotenv()
TMDB_API_KEY = os.getenv("TMDB_API_KEY")
BASE_URL = "https://api.themoviedb.org/3/search/movie"
@app.get("/")
def read_root():
    return "Who's ready to watch some movies!!!!!???"


@app.get("/search")
def search_movies(query: str):
    ''' Search for movies based on query
    
    Parameters:
    - query: The search query string (e.g., movie title)
    Returns:
    - The Movie title and Movie id
    '''
    params = {
        "api_key": TMDB_API_KEY,
        "query": query
    }
    response = requests.get(BASE_URL, params=params)
    movie_list = []
    if response.status_code == 200:
        for movie in response.json().get("results", []):
            movie_title = movie.get("title", "No title found")
            movie_id = movie.get("id", "No ID found")
            movie_poster = movie.get("poster_path", "No poster found")
            movie_release_date = movie.get("release_date", "No release date found")
            movie_list.append({
                "title": movie_title,
                "id": movie_id,
                "poster": movie_poster,
                "release_date": movie_release_date
            })
        return movie_list
    else:
        return {"error": "Failed to fetch data from TMDB API"}

@app.get("/movie/{movie_id}")
def get_movie_details(movie_id: int):
    ''' Get details for a specific movie based on its ID
    
    Parameters:
    - movie_id: The ID of the movie to fetch details for
    Returns:
    - The movie details
    '''
    url = f"https://api.themoviedb.org/3/movie/{movie_id}"
    params = {
        "api_key": TMDB_API_KEY
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Failed to fetch data from TMDB API"}
    
@app.post("/watchlist")
def create_watchlist(watchlist_name: str):
    global current_id
    watchlist_id = current_id
    watchlists[watchlist_id] = {
        "name": watchlist_name,
        "movies": []
    }
    current_id += 1
    return {"message": f"Watchlist '{watchlist_name}' created with ID {watchlist_id}"}

def add_to_watchlist(watchlist_id: int, movie_id: int):
    # Implementation for adding movie to watchlist
    if watchlist_id not in watchlists:
        return {"error": "Watchlist not found"}
    movie_details = get_movie_details(movie_id)
    watchlists[watchlist_id]["movies"].append(movie_id)
    return {"message": f"Movie {movie_details.get('title', 'Unknown')} added to watchlist"}

if __name__ == "__main__":
    movies = search_movies("Godfather Part I")

    # for movie in movies:
    #     print(f"Title: {movie['title']}, ID: {movie['id']}, Poster: {movie['poster']}, Release Date: {movie['release_date']}") 
    create_watchlist("My Favorite Movies")
    print(add_to_watchlist(1, movies[0]['id']))
    movies = search_movies("Interstellar")
    add_to_watchlist(1, movies[0]['id'])

    movies = search_movies("Fight Club")
    add_to_watchlist(1, movies[0]['id'])
    
    print(f"{watchlists[1]['name']} Watchlist:")
    for movie_id in watchlists[1]["movies"]:
        print(get_movie_details(movie_id)["title"])