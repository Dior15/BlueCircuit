import tmdbsimple as tmdb

# Set API key from file
with open("apikey.txt", "r") as file:
    tmdb.API_KEY = file.readline().strip()

class Movies:
    def __init__(self):
        # Initialize movie object by fetching details from TMDB based on movie ID
        self.movies = tmdb.Movies()

    def getTopXMovies(self, x):
        popularMovies = self.movies.popular()
        topXMovies = popularMovies['results'][:x]
        return topXMovies

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
