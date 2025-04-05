from flask import Flask, render_template, request, jsonify, session, redirect
from models import db, User, Watchlist
import tmdbsimple as tmdb
from werkzeug.security import generate_password_hash, check_password_hash
import webbrowser
from movies import *
from search import *
from login import *
from watchlist import *

# Set TMDB API key
with open("apikey.txt", "r") as file:
    tmdb.API_KEY = file.readline().strip()
    
# Initialize Flask app
app = Flask(__name__)

#Configure the app using SQLite
app.secret_key = "BlueCircuit"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
    
# Create the database tables
with app.app_context():
    db.create_all()

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

    topRated = movieEngine.getTopRatedXMovies(2)  # Get top 9 rated movies
    topRated = movieEngine.getTopRatedXMovies(2)  # Get top 9 rated movies
    topRatedPoster = movieEngine.getPosterUrl(topRated[0])  # Get top rated movie poster URL
    latest = movieEngine.getLatestMovie()  # Get latest movie
    latestPoster = movieEngine.getPosterUrl(latest)  # Get latest movie poster URL
    
    return render_template('home.html', posterUrls=posterUrls, movieIds=movieIds, topRated=topRated, topRatedPoster=topRatedPoster, latest=latest, latestPoster=latestPoster)

@app.route('/search', methods=['POST'])
def search():
    # Get user search input
    query = request.form.get('query')
    category = request.form.get('category')

    # Search by category
    results = searchEngine.searchByCategory(query, category)

    # Add poster URLs to each result using getPosterUrl
    for result in results:
        result['poster_url'] = movieEngine.getPosterUrl(result)

    return render_template('results.html', results=results, category=category, query=query)

@app.route('/movie/<int:movieId>')
def movie(movieId):
    # Get movie details
    movie = movieEngine.getMovieDict(movieId)
    
    is_saved = False
    if 'user_id' in session:
        is_saved = UserWatchlist.is_movie_saved(session['user_id'], movieId)

    return render_template('moviepage.html', **movie, movie_id=movieId, is_saved=is_saved)

@app.route('/tv/<int:tvId>')
def tv(tvId):
    # Get TV details
    tvShow = movieEngine.getTVDict(tvId)

    return render_template('tvpage.html', **tvShow)

@app.route('/person/<int:personId>')
def person(personId):
    # Get person details
    person = movieEngine.getPersonDict(personId)

    return render_template("personpage.html", **person)

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    response, status = UserLogin.login(
        username = data.get('username'),
        password = data.get('password')
    )
    return jsonify(response), status

@app.route('/signup', methods=['POST'])
def signup():
    data = request.json
    response, status = UserLogin.signup(
        email = data.get('email'), 
        username = data.get('username'), 
        password = data.get('password'), 
        confirmPassword = data.get('confirmPassword')
    )
    return jsonify(response), status

@app.route('/logout', methods=['POST'])
def logout():
    response, status = UserLogin.logout()
    return jsonify(response), status
 
@app.route('/check_login', methods=['GET'])
def check_login():
    response, status = UserLogin.check_login()
    return jsonify(response), status


@app.route('/watchlist', methods=['GET'])
def get_watchlist():
    if 'user_id' not in session:
        return redirect('/')
    
    user_id = session['user_id']
    
    #Get all movie ID's from the user's watchlist
    watchlist_entries = Watchlist.query.filter_by(user_id=user_id).all()
    movie_ids = [entry.movie_id for entry in watchlist_entries]
    
    # Get full movie details from the Movie Class
    movies = []
    for mid in movie_ids:
        movie = tmdb.Movies(mid).info()
        movie['poster_url'] = movieEngine.getPosterUrl(movie)
        movies.append(movie)
    
    return render_template('watchlist.html', movies=movies)

@app.route('/watchlist/add', methods=['POST'])
def add_to_watchlist():
    if 'user_id' not in session:
        return jsonify({'success': False, 'message': 'Login required'}), 401
    
    movie_id = request.json.get('movie_id')
    user_id = session['user_id']
    
    response, status = UserWatchlist.add_movie(user_id, movie_id)
    return jsonify(response), status

@app.route('/watchlist/remove', methods=['POST'])
def remove_watchlist():
    if 'user_id' not in session:
        return jsonify({'success': False, 'message': 'Login required'}), 401
    
    movie_id = request.json.get('movie_id')
    user_id = session['user_id']
    
    response, status = UserWatchlist.remove_movie(user_id, movie_id)
    return jsonify(response), status
     
if __name__ == '__main__':
    webbrowser.open("http://127.0.0.1:5000")
    app.run()