import tmdbsimple as tmdb

# Set TMDB API key
with open("apikey.txt", "r") as file:
    tmdb.API_KEY = file.readline().strip()

class MovieSearch:
    def __init__(self):
        self.search = tmdb.Search()

    def searchMovies(self, query):
        return self.search.movie(query=query)

    def searchTv(self, query):
        return self.search.tv(query=query)

    def searchPeople(self, query):
        return self.search.person(query=query)

    def searchByCategory(self, query, category):
        if category == "movie":
            return self.searchMovies(query)
        elif category == "tv":
            return self.searchTv(query)
        elif category == "person":
            return self.searchPeople(query)
        else:
            return None