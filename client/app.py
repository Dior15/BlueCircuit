from flask import Flask, render_template, request
import tmdbsimple as tmdb
from poster import *
from search import *

# Set TMDB API key
with open("apikey.txt", "r") as file:
    tmdb.API_KEY = file.readline().strip()
    
# Initialize Flask app
app = Flask(__name__)

# Initialize search and poster classes
searchEngine = MovieSearch()
posterEngine = MoviePoster()

@app.route('/')
def home():
    # Fetch trending movies
    top9Movies = posterEngine.getTopXMovies(9)  # Get top 9 trending movies
    posterUrls = ""

    # Construct full image URLs for posters
    for movie in top9Movies:
        posterUrl = posterEngine.getPosterUrl(movie)
        posterUrls += posterUrl+" "

    return render_template('home.html', poster_urls=posterUrls)


@app.route('/search', methods=['POST'])
def search():
    # Get user search input
    query = request.form.get('query')
    category = request.form.get('category')

    # Perform search based on category
    results = searchEngine.searchByCategory(query, category)

    if results is None:
        return "Invalid category", 400  # Error handling

    return render_template('results.html', results=searchEngine.search.results, category=category, query=query)

@app.route('/login')
def login():
    return render_template('loginpage.html')

@app.route('/signup')
def signup():
    return render_template('accountcreationpage.html')

if __name__ == '__main__':
    app.run(debug=True)
