# Movie List Ordering System
A full-stack web application that allows users to search for movies, create custom watchlists, and generate an optimized viewing order. This project focuses on combining clean backend API design with an interactive React frontend.

## Features
- Search for movies using the TMDb API
- **Backend**
    - /search → Fetch movies from TMDb
    - /movie/{id} → Get detailed movie info
    - Watchlist system (in-memory):
        - Create watchlists
        - Add movies to watchlists
        - Retrieve watchlists
- **Frontend**
    - Search bar with real-time input handling
    - Fetches data from backend
    - Dynamically renders movie results
    - Responsive grid layout for movie posters

## Technologies
- **Backend**
    - FastAPI
    - Python
    - TMDb API

- **Frontend**
    - React (Vite)
    - JavaScript
    - HTML/CSS


## Future Improvements

- Smart ordering using:
    - Sequels / prequels
    - Release chronology
    - User preferences

- Persistent database (SQL)

- User authentication

- Multi-watchlist support