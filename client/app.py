from flask import Flask, render_template, request, jsonify
import tmdbsimple as tmdb
import csv, os
from movies import *
from search import *

# Set TMDB API key
with open("apikey.txt", "r") as file:
    tmdb.API_KEY = file.readline().strip()
    
# Initialize Flask app
app = Flask(__name__)

file_path = "client\\UsernamesAndPasswords.csv"

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
    username = request.json.get('username')
    password = request.json.get('password')
    
    if not username or not password:
        return jsonify({'success': False, 'message':'Username and password are required'}), 400
    
    #Check if the csv file exists
    if not os.path.exists(file_path):
        return jsonify({'success': False, 'message':'User does not exist'}), 404
    
    #Read the CSV file to check user credentials
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == username:
                if row[1] == password:
                    return jsonify({'success': True, 'messsage': 'Login Successful!'}), 200
                else:
                    return jsonify({'success': False, 'message': 'Incorrect password'}), 401
        #If user is not found
        return jsonify({'success': False, 'message': 'User does not exist'}), 404
    
@app.route('/signup', methods=['POST'])
def signup():
    email = request.json.get('email')
    username = request.json.get('username')
    password = request.json.get('password')
    confirmPassword = request.json.get('confirmPassword')
    
    if not email or not username or not password:
        return jsonify({'success': False, 'message': 'Email, username and password are required'}), 400
    
    #check if the username is already taken
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == username:
                return jsonify({'success': False, 'message': 'Username already taken'}), 409
            
    #If username and password match, then user already exists
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == username and row[1] == password:
                return jsonify({'success': False, 'message': 'User already exists'}), 409
    
    #If passwords do not match 
    if password != confirmPassword:
        return jsonify({'success': False, 'message': 'Passwords do not match!'}), 400        
            
    #If add the new user, add to the csv file
    with open(file_path, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([username, password])
        
    return jsonify({'success': True, 'message': 'Signup successful!'}), 201

if __name__ == '__main__':
    app.run(debug=True)