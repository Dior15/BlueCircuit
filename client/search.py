import tmdbsimple as tmdb

# Set TMDB API key
with open("apikey.txt", "r") as file:
    tmdb.API_KEY = file.readline().strip()

class MovieSearch:
    def __init__(self):
        self.search = tmdb.Search()

    def searchMovies(self, query):
        allMovies = []
        for page in range(1, 4):  
            result = self.search.movie(query=query, page=page)
            if 'results' in result:
                allMovies.extend([movie for movie in result['results'] if movie.get('vote_average', 0) >= 0.01])
            elif not result.get('results'):
                break
        return sorted(allMovies, key=lambda x: x.get('vote_count', 0), reverse=True)

    def searchTv(self, query):
        allShows = []
        for page in range(1, 4):
            result = self.search.tv(query=query, page=page)
            if 'results' in result:
                filtered = [show for show in result['results'] if show.get('vote_average', 0) >= 0.01]
                allShows.extend(filtered)
            if not result.get('results'):
                break
        return sorted(allShows, key=lambda x: x.get('vote_count', 0), reverse=True)

    def searchPeople(self, query):
        allPeople = []
        for page in range(1, 4):
            result = self.search.person(query=query, page=page)
            if 'results' in result:
                for person in result['results']:
                    popularity = person.get('popularity', 0)
                    if popularity >= 0.1:
                        allPeople.append(person)
            if not result.get('results'):
                break
        return sorted(allPeople, key=lambda x: x.get('popularity', 0), reverse=True)

    def searchByCategory(self, query, category):
        if category == "movie":
            return self.searchMovies(query)
        elif category == "tv":
            return self.searchTv(query)
        elif category == "person":
            return self.searchPeople(query)
        else:
            return "Invalid category", 400