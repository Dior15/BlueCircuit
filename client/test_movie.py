import pytest
from movies import Movies

# Initialize Movies instance for testing
movieEngine = Movies()

def testGetPopularXMovies():
    # Test fetching top X popular movies
    topMovies = movieEngine.getPopularXMovies(5)
    assert topMovies is not None
    assert isinstance(topMovies, list)
    assert len(topMovies) == 5
    assert "title" in topMovies[0]

def testGetTopRatedXMovies():
    # Test fetching top X top-rated movies
    topMovies = movieEngine.getTopRatedXMovies(5)
    assert topMovies is not None
    assert isinstance(topMovies, list)
    assert len(topMovies) == 5
    assert "title" in topMovies[0]

def testGetLatestMovie():
    # Test getting the most recent popular English movie
    latest = movieEngine.getLatestMovie()
    assert isinstance(latest, dict)
    assert "title" in latest

def testGetPosterUrl():
    # Test getting a valid poster URL
    topMovie = movieEngine.getPopularXMovies(1)[0]
    posterUrl = movieEngine.getPosterUrl(topMovie)
    assert isinstance(posterUrl, str)
    assert posterUrl.startswith("https://")

def testGetCast():
    # Test fetching cast with person IDs and names
    movieId = 27205  # Inception
    cast = movieEngine.getCast(movieId)
    assert isinstance(cast, list)
    assert len(cast) > 0
    assert isinstance(cast[0], dict)
    assert "id" in cast[0] and "name" in cast[0]

def testGetCrew():
    # Test fetching crew members
    movieId = 27205
    crew = movieEngine.getCrew(movieId)
    assert isinstance(crew, list)
    assert len(crew) > 0
    assert isinstance(crew[0], str)

def testGetDirector():
    # Test getting director's name
    movieId = 27205
    directors = movieEngine.getDirector(movieId)
    assert isinstance(directors, list)
    assert len(directors) > 0
    assert isinstance(directors[0], dict)
    assert "name" in directors[0] and "id" in directors[0]
    names = [d["name"] for d in directors]
    assert "Christopher Nolan" in names

def testGetReleaseDate():
    # Test getting release date
    movieId = 27205
    releaseDate = movieEngine.getReleaseDate(movieId)
    assert isinstance(releaseDate, str)
    assert len(releaseDate) >= 4  # At least year format

def testGetSynopsis():
    # Test getting movie overview
    movieId = 27205
    synopsis = movieEngine.getSynopsis(movieId)
    assert isinstance(synopsis, str)

def testMovieGetNumRatings():
    # Test number of votes
    movieId = 27205
    numRatings = movieEngine.getMovieNumRatings(movieId)
    assert isinstance(numRatings, int)

def testMovieGetRating():
    # Test rating percentage value
    movieId = 27205
    rating = movieEngine.getMovieRating(movieId)
    assert isinstance(rating, int)
    assert 0 <= rating <= 100

def testTvGetNumRatings():
    # Test number of votes
    tvId = 1668
    numRatings = movieEngine.getTvNumRatings(tvId)
    assert isinstance(numRatings, int)

def testTvGetRating():
    # Test rating percentage value
    tvId = 1668
    rating = movieEngine.getTvRating(tvId)
    assert isinstance(rating, int)
    assert 0 <= rating <= 100

def testGetRatingColor():
    # Test rating color by value
    assert movieEngine.getRatingColor(80) == "#00ff88"
    assert movieEngine.getRatingColor(60) == "#ffaa00"
    assert movieEngine.getRatingColor(30) == "#ff4444"

def testGetMovieDict():
    # Test full movie dictionary
    movieId = 27205
    movieDict = movieEngine.getMovieDict(movieId)
    assert isinstance(movieDict, dict)
    requiredKeys = ["title", "runtime", "genres", "posterUrl", "cast", "crew", "director", "releaseDate", "synopsis", "ratingCount", "rating", "ratingColor"]
    for key in requiredKeys:
        assert key in movieDict

def testGetTvDict():
    # Test TV show dictionary for a known show (Breaking Bad: ID 1396)
    tvId = 1396
    tvDict = movieEngine.getTVDict(tvId)
    assert isinstance(tvDict, dict)

    # Check required fields
    requiredKeys = ["title", "firstAirDate", "genres", "creator", "cast", "synopsis", "posterUrl", "rating", "ratingCount", "ratingColor"]
    for key in requiredKeys:
        assert key in tvDict

    assert isinstance(tvDict["cast"], list)
    assert isinstance(tvDict["title"], str)

def testGetPersonDict():
    # Test person dictionary for a known person (Leonardo DiCaprio: ID 6193)
    personId = 6193
    personDict = movieEngine.getPersonDict(personId)
    assert isinstance(personDict, dict)

    # Check required fields
    requiredKeys = ["name", "birthDate", "posterUrl", "occupation", "knownFor", "biography"]
    for key in requiredKeys:
        assert key in personDict

    assert isinstance(personDict["name"], str)
    assert personDict["name"] == "Leonardo DiCaprio"
