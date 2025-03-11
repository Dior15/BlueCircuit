import tmdbsimple as tmdb

with open("apikey.txt", "r") as file:
    tmdb.API_KEY = file.readline().strip()

class MoviePoster:
    def __init__(self):
        self.movies = tmdb.Movies()  # Initialize TMDB movies object
    
    # Fetch Top X movies from TMDB
    def getTopXMovies(self, x):
        popularMovies = self.movies.popular()
        topXMovies = popularMovies['results'][:x]
        return topXMovies

    # Gets full poster URL for a given movie dictionary
    def getPosterUrl(self, movie):
        if 'poster_path' in movie and movie['poster_path']:
            url = f"https://image.tmdb.org/t/p/w500{movie['poster_path']}"
        return url