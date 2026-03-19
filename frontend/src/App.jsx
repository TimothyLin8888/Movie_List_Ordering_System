import { useState } from 'react'
import './App.css'
import Navbar from './Navbar.jsx';


function App() {
  const [query, setQuery] = useState("");
  const [movies, setMovies] = useState([]);

  function handleSearch(e){
    e.preventDefault();

    fetch(`http://localhost:8000/search?query=${query}`)
    .then(res => res.json())
    .then(data => setMovies(data));
  }
  return (
    <div className="App">
      <div>
        <Navbar />
      </div>
      <div>
        <h1>Movie List Maker</h1>
        <form role="search" id="movie-search-form" onSubmit={handleSearch}>
          <label htmlFor="movie-search" className="sr-only">
            Search for a movie:
          </label>
          <input type="search" value={query} onChange={(e) => setQuery(e.target.value)} 
          id="movie-search" name="q" placeholder="Search movies..."/>
          <button type="submit">Search</button>
        </form>
      </div>

      <div className="movie-grid">
        {movies.map((movie) => (
          <div key={movie.id}>
            <h3>{movie.title}</h3>
            
            {movie.poster && (
              <img
                src={`https://image.tmdb.org/t/p/w500${movie.poster}`}
                alt={movie.title}
                style={{ width: "150px" }}
              />
            )}
          </div>
        ))}
      </div>
    </div>
  )
}

export default App
