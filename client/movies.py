import tmdbsimple as tmdb
from datetime import datetime

# Set API key from file
with open("apikey.txt", "r") as file:
    tmdb.API_KEY = file.readline().strip()

class Movies:
    def __init__(self):
        # Initialize movie object by fetching details from TMDB based on movie ID
        self.movies = tmdb.Movies()

    def getPopularXMovies(self,x):
        allMovies = {}
        uniqueMovieIds = set()  # Set to track movie IDs and avoid duplicates

        for page in range(1, int(x*2)):
            popularMovies = self.movies.popular(page=page)
            movieResults = popularMovies.get('results', [])

            for movie in movieResults:
                if (
                    movie.get('id') not in allMovies # Ensure unique movies
                    and movie.get('vote_count', 0) >= 10  # At least 10 votes
                    and not movie.get('adult', False)  # Exclude adult movie
                ):  
                    allMovies[movie['id']] = movie

        # Sort by popularity (highest first)
        sortedMovies = sorted(allMovies.values(), key=lambda x: x.get('popularity', 0), reverse=True)

        return sortedMovies[:x]
    
    def getTopRatedXMovies(self, x):
        allMovies = {}
        currentYear = datetime.today().year  # Get the current year

        for page in range(1, int(x*2)):
            topRatedMovies = self.movies.top_rated(page=page)  # Fetch a new page
            movieResults = topRatedMovies.get('results', [])

            for movie in movieResults:
                if (
                    movie.get('id') not in allMovies # Ensure unique movies
                    and 'release_date' in movie and movie['release_date']  # Ensure release_date exists
                    and int(movie['release_date'][:4]) >= (currentYear - 1)  # Only last year's movies
                ):  
                    allMovies[movie['id']] = movie

        sortedMovies = sorted(allMovies.values(), key=lambda x: x.get('popularity', 0), reverse=True)

        return sortedMovies[:x]  # Return only the top X movies

    
    def getLatestMovie(self):
        # Get the most recently released popular english movie
        popularMovies = self.movies.popular()
        englishMovies = [movie for movie in popularMovies['results'] if movie['original_language'] == 'en']
        latestMovie = max(englishMovies, key=lambda x: x['release_date'])
        return latestMovie

    def getPosterUrl(self, media):

        # Validate movie input to prevent crashes
        if not isinstance(media, dict):
            return "https://via.placeholder.com/500x750?text=No+Image+Available"  # Default placeholder

        # Get the poster path if it exists
        path = media.get('poster_path') or media.get('profile_path') # Uses .get() to prevent KeyErrors

        if path:  # Ensure posterPath is not None or empty
            return f"https://image.tmdb.org/t/p/w500{path}"

        # Return a placeholder image if no valid poster is available
        return "https://via.placeholder.com/500x750?text=No+Image+Available"

    def getCast(self, movieId):
        # Get the main cast (first 5 actors)
        creditsData = tmdb.Movies(movieId).credits()
        return [member["name"] for member in creditsData.get("cast", [])[:5]]

    def getCrew(self, movieId):
        # Get all crew members
        creditsData = tmdb.Movies(movieId).credits()
        return [member["name"] for member in creditsData.get("crew", [])]

    def getDirector(self, movieId):
        # Find the director from the crew list
        creditsData = tmdb.Movies(movieId).credits()
        for member in creditsData.get("crew", []):
            if member["job"] == "Director":
                return member["name"]
        return "Unknown Director"  # Return default if no director is found
    
    def getReleaseDate(self, movieId):
        # Get the release date of the movie
        movieData = tmdb.Movies(movieId).info()
        return movieData.get("release_date", "Unknown Release Date")
    
    def getSynopsis(self, movieId):
        # Get the movie synopsis
        movieData = tmdb.Movies(movieId).info()
        return movieData.get("overview", "No synopsis available")
    
    def getNumRatings(self, movieId):
        movieData = tmdb.Movies(movieId).info()
        return movieData.get("vote_count", None)
    
    def getRating(self, movieId):
        movieData = tmdb.Movies(movieId).info()
        return movieData.get("vote_average", None)

    def getMovieDict(self, movieId):
        # Return movie details as a dictionary
        movieData = tmdb.Movies(movieId).info()  # Fetch movie details

        return {
            "title": movieData.get("title", "Unknown Title"),  # Movie title,
            "runtime": movieData.get("runtime", "N/A"),  # Runtime in minutes,
            "genres": [genre["name"] for genre in movieData.get("genres", [])],
            "posterUrl": self.getPosterUrl(movieData),
            "cast": self.getCast(movieId),
            "crew": self.getCrew(movieId),
            "director": self.getDirector(movieId),
            "releaseDate": self.getReleaseDate(movieId),
            "synopsis": self.getSynopsis(movieId),
            "ratingCount": self.getNumRatings(movieId),
            "rating": self.getRating(movieId)
        }
