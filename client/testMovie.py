import pytest
from movies import *

# Initialize Movie instance for testing
movieEngine = Movies()

def testGetTopXMovies():
    """Test fetching top X popular movies"""
    topMovies = movieEngine.getTopXMovies(5)  # Get top 5 movies

    assert topMovies is not None  # Ensure response exists
    assert isinstance(topMovies, list)  # Ensure it's a list
    assert len(topMovies) == 5  # Ensure it returns exactly 5 movies
    assert "title" in topMovies[0]  # Ensure each movie has a title

def testGetPosterUrl():
    """Test fetching a valid poster URL"""
    topMovie = movieEngine.getTopXMovies(1)[0]  # Get the first movie
    posterUrl = movieEngine.getPosterUrl(topMovie)

    assert isinstance(posterUrl, str)  # Ensure the URL is a string
    assert posterUrl.startswith("https://image.tmdb.org/t/p/w500")  # Ensure correct TMDB URL format
    assert posterUrl.endswith(".jpg") or posterUrl.endswith(".png")  # Ensure it's an image URL

def testGetCast():
    """Test fetching the main cast of a movie"""
    movieId = 27205  # TMDB ID for Inception
    cast = movieEngine.getCast(movieId)

    assert isinstance(cast, list)  # Ensure cast is a list
    assert len(cast) > 0  # Ensure at least one cast member exists
    assert isinstance(cast[0], str)  # Ensure cast names are strings

def testGetCrew():
    """Test fetching the full crew of a movie"""
    movieId = 27205  # TMDB ID for Inception
    crew = movieEngine.getCrew(movieId)

    assert isinstance(crew, list)  # Ensure crew is a list
    assert len(crew) > 0  # Ensure at least one crew member exists
    assert isinstance(crew[0], str)  # Ensure crew names are strings

def testGetDirector():
    """Test fetching the director of a movie"""
    movieId = 27205  # TMDB ID for Inception
    director = movieEngine.getDirector(movieId)

    assert isinstance(director, str)  # Ensure director is a string
    assert director == "Christopher Nolan"  # Ensure correct director is returned

def testGetMovieDict():
    """Test fetching full movie details as a dictionary"""
    movieId = 27205  # TMDB ID for Inception
    movieDict = movieEngine.getMovieDict(movieId)

    assert isinstance(movieDict, dict)  # Ensure it returns a dictionary
    assert "title" in movieDict  # Ensure title key exists
    assert "runtime" in movieDict  # Ensure runtime key exists
    assert "genres" in movieDict  # Ensure genres key exists
    assert "posterUrl" in movieDict  # Ensure posterUrl key exists
    assert "cast" in movieDict  # Ensure cast key exists
    assert "crew" in movieDict  # Ensure crew key exists
    assert "director" in movieDict  # Ensure director key exists
