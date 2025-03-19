from flask import Flask, render_template, request
import tmdbsimple as tmdb
from movies import *
from search import *

# Set TMDB API key
with open("apikey.txt", "r") as file:
    tmdb.API_KEY = file.readline().strip()
    
# Initialize Flask app
app = Flask(__name__)

# Initialize search and poster classes
searchEngine = MovieSearch()
movieEngine = Movies()

@app.route('/')
def home():
    # Fetch trending movies
    top9Movies = movieEngine.getPopularXMovies(9)  # Get top 9 trending movies
    posterUrls = ""
    movieIds = []

    # Construct full image URLs for posters along with movie IDs
    for movie in top9Movies:
        movieIds.append(movie["id"])  # Movie ID
        posterUrls += movieEngine.getPosterUrl(movie) + " "  # Poster URL

    topRated = movieEngine.getTopRatedXMovies(1)  # Get top 9 rated movies
    topRatedPoster = movieEngine.getPosterUrl(topRated[0])  # Get top rated movie poster URL
    latest = movieEngine.getLatestMovie()  # Get latest movie
    latestPoster = movieEngine.getPosterUrl(latest)  # Get latest movie poster URL
    
    return render_template('home.html', posterUrls=posterUrls, movieIds=movieIds, topRated=topRated, topRatedPoster=topRatedPoster, latest=latest, latestPoster=latestPoster)

@app.route('/search', methods=['POST'])
def search():
    # Get user search input
    query = request.form.get('query')
    category = request.form.get('category')

    # Perform search based on category
    results = searchEngine.searchByCategory(query, category)

    if results is None:
        return "Invalid category", 400  # Error handling

    return render_template('results.html', results=results, category=category, query=query)

@app.route('/movie/<int:movie_id>')
def movie(movie_id):
    # Get movie details
    movie = movieEngine.getMovieDict(movie_id)

    return render_template('moviepage.html', title = movie['title'], runtime = movie['runtime'], genres = movie['genres'], poster_url = movie['posterUrl'], cast = movie['cast'],  crew = movie['crew'], director = movie['director'], releaseDate = movie['releaseDate'], synopsis = movie['synopsis'])

if __name__ == '__main__':
    app.run(debug=True)