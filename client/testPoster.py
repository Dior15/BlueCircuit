import pytest
from poster import MoviePoster

# Initialize MoviePoster instance for testing
posterEngine = MoviePoster()

def testGetTopXMovies():
    # Test fetching top X movies
    topMovies = posterEngine.getTopXMovies(5)  # Get top 5 movies
    assert topMovies is not None  # Ensure response exists
    assert isinstance(topMovies, list)  # Ensure it's a list
    assert len(topMovies) == 5  # Ensure it returns exactly 5 movies
    assert "title" in topMovies[0]  # Ensure each movie has a title

def testGetPosterUrl():
    # Test fetching poster URL
    movie = posterEngine.getTopXMovies(1)[0]  # Get top movie
    assert movie is not None # Ensure movie exists
    assert posterEngine.getPosterUrl(movie).endswith(".jpg") == True # Ensure URL ends with .jpg
    assert posterEngine.getPosterUrl(movie).startswith("https://") == True # Ensure URL starts with https://