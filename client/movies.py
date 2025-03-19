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
        allMovies = []
        for page in range(1, int(x*2)):  
            popularMovies = self.movies.popular(page=page)
            allMovies.extend(popularMovies['results'])
        
        # Filter and sort movies
        filteredMovies = [
            movie for movie in allMovies 
            if movie['vote_count'] > 10
            and movie['adult'] == False
        ]
        sortedMovies = sorted(filteredMovies, key=lambda x: x['popularity'], reverse=True)
        
        return sortedMovies[:x]
    
    def getTopRatedXMovies(self, x):
        moviesList = []
        currentYear = datetime.today().year  # Get the current year

        for page in range(1, int(x*2)):
            response = self.movies.top_rated(page=page)  # Fetch a new page
            moviesList.extend(response.get('results', []))  # Add to our movie list

        filteredMovies = [
            movie for movie in moviesList 
            if 'release_date' in movie and movie['release_date']  # Ensure release_date exists
            and int(movie['release_date'][:4]) >= (currentYear - 1)  # Only last year's movies
        ]
        sortedMovies = sorted(filteredMovies, key=lambda x: x.get('popularity', 0), reverse=True)

        return sortedMovies[:x]  # Return only the top X movies

    
    def getLatestMovie(self):
        # Get the most recently released popular english movie
        popularMovies = self.movies.popular()
        englishMovies = [movie for movie in popularMovies['results'] if movie['original_language'] == 'en']
        latestMovie = max(englishMovies, key=lambda x: x['release_date'])
        return latestMovie

    def getPosterUrl(self, movie):
        # Get full poster URL or a placeholder if unavailable
        if 'poster_path' in movie and movie['poster_path']:
            url = f"https://image.tmdb.org/t/p/w500{movie['poster_path']}"
        return url

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
            "synopsis": self.getSynopsis(movieId)   
        }
