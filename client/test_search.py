from search import MovieSearch

# Initialize MovieSearch instance for testing
searchEngine = MovieSearch()

def hasDuplicates(results, key="id"):
    seen = set()
    for item in results:
        if key not in item:
            continue
        if item[key] in seen:
            return True
        seen.add(item[key])
    return False

def testSearchMovies():
    response = searchEngine.searchMovies("Inception")
    assert response is not None
    assert isinstance(response, list)
    assert len(response) > 0
    assert "title" in response[0]
    assert not hasDuplicates(response), "Duplicate movies found in searchMovies"

def testSearchTv():
    response = searchEngine.searchTv("Breaking Bad")
    assert response is not None
    assert isinstance(response, list)
    assert len(response) > 0
    assert "name" in response[0]
    assert not hasDuplicates(response), "Duplicate TV shows found in searchTv"

def testSearchPeople():
    response = searchEngine.searchPeople("Leonardo DiCaprio")
    assert response is not None
    assert isinstance(response, list)
    assert len(response) > 0
    assert "name" in response[0]
    assert not hasDuplicates(response), "Duplicate people found in searchPeople"

def testSearchInvalidCategory():
    response = searchEngine.searchByCategory("Test", "invalid")
    assert isinstance(response, tuple)
    assert response[1] == 400  # Should return error status code for invalid category

def testEmptyQuery():
    response = searchEngine.searchMovies("")
    assert response is not None
    assert isinstance(response, list)