import pytest
from search import MovieSearch

# Initialize MovieSearch instance for testing
searchEngine = MovieSearch()

def testSearchMovies():
    # Test movie search with a valid query
    response = searchEngine.searchMovies("Inception")
    assert response is not None  # Ensure response exists
    assert isinstance(searchEngine.search.results, list)  # Ensure results are a list
    assert len(searchEngine.search.results) > 0  # Ensure there are results
    assert "title" in searchEngine.search.results[0]  # Ensure title is in response

def testSearchTv():
    # Test TV search with a valid query
    response = searchEngine.searchTv("Breaking Bad")
    assert response is not None
    assert isinstance(searchEngine.search.results, list)
    assert len(searchEngine.search.results) > 0
    assert "name" in searchEngine.search.results[0]  # TV shows have "name" instead of "title"

def testSearchPeople():
    # Test person search with a valid query
    response = searchEngine.searchPeople("Leonardo DiCaprio")
    assert response is not None
    assert isinstance(searchEngine.search.results, list)
    assert len(searchEngine.search.results) > 0
    assert "name" in searchEngine.search.results[0]  # People have "name" field

def testSearchInvalidCategory():
    # Test search with an invalid category
    response = searchEngine.searchByCategory("Test", "invalid")
    assert response is None  # Should return None for invalid categories

def testEmptyQuery():
    # Test search with an empty query
    response = searchEngine.searchMovies("")
    assert response is not None  # API should return a response
    assert isinstance(searchEngine.search.results, list)  # Should return a list