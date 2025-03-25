from flask import Flask, render_template, request, jsonify, session
import tmdbsimple as tmdb
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import csv, os
from movies import *
from search import *

# Set TMDB API key
with open("apikey.txt", "r") as file:
    tmdb.API_KEY = file.readline().strip()
    
# Initialize Flask app
app = Flask(__name__)

#Configure the app using SQLite
app.secret_key = "BlueCircuit"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# User Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)

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

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = request.json.get('username')
    password = request.json.get('password')
    
    #Prommpt users to enter required fields
    if not username or not password:
        return jsonify({'success': False, 'message':'Username and password are required'}), 400
    
    user = User.query.filter((User.username == username) | (User.email == username)).first()
    
    if not user:
        return jsonify({'success': False, 'message':'User does not exist'}), 404
    
    #Check hased password
    if not check_password_hash(user.password_hash, password):
        return jsonify({'success': False, 'message' : 'Incorrect password'}), 401
    
    #Store user session
    session['user_id'] = user.id
    
    return jsonify({'success': True, 'message': 'Login successful!'}), 200

    
@app.route('/signup', methods=['POST'])
def signup():
    data = request.json
    email = request.json.get('email')
    username = request.json.get('username')
    password = request.json.get('password')
    confirmPassword = request.json.get('confirmPassword')
    
    if not email or not username or not password or not confirmPassword:
        return jsonify({'success': False, 'message': 'Email, username and password are required'}), 400
    
    if password != confirmPassword:
        return jsonify({'success' : False, 'message': 'Passwords do not match'}), 400
    
    #Check if user exists
    if User.query.filter_by(username=username).first() or User.query.filter_by(email=email).first():
        return jsonify({'success': False, 'message': 'User already exists'}), 409
    
    
    #Hash the passwords and save the user
    hashed_password = generate_password_hash(password)
    new_user = User(username=username, email=email, password_hash=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({'success': True, 'message': 'Signup successful!'}), 201

@app.route('/logout', methods=['POST'])
def logout():
     session.pop('user_id', None)
     return jsonify({'success': True, 'message': 'Logged out successfully'}), 200
 
@app.route('/check_login', methods=['GET'])
def check_login():
    if 'user' in session:
        return jsonify({'logged_in': True, 'user': session['user']}), 200
    return jsonify({'logged_in': False}), 200
     
if __name__ == '__main__':
    app.run(debug=True)