import tmdbsimple as tmdb

# Set TMDB API key
with open("apikey.txt", "r") as file:
    tmdb.API_KEY = file.readline().strip()

class MovieSearch:
    def __init__(self):
        self.search = tmdb.Search()

    def searchMovies(self, query):
        movies = self.search.movie(query=query)
        filteredMovies = [movie for movie in movies['results'] if movie.get('vote_average', 0) >= 0.01]
        return sorted(filteredMovies, key=lambda x: x.get('popularity', 0), reverse=True)

    def searchTv(self, query):
        shows = self.search.tv(query=query)
        filteredShows = [show for show in shows['results'] if show.get('vote_average', 0) >= 0.01]
        return sorted(filteredShows, key=lambda x: x.get('popularity', 0), reverse=True)

    def searchPeople(self, query):
        people = self.search.person(query=query)

        # Filter people by popularity and known roles
        filteredPeople = []
        for person in people['results']:
            popularity = person.get('popularity', 0)

            if (popularity >= 0.01):
                filteredPeople.append(person)

        return sorted(filteredPeople, key=lambda x: x.get('popularity', 0), reverse=True)

    def searchByCategory(self, query, category):
        if category == "movie":
            return self.searchMovies(query)
        elif category == "tv":
            return self.searchTv(query)
        elif category == "person":
            return self.searchPeople(query)
        else:
            return None