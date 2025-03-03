from flask import Flask, render_template, request
import tmdbsimple as tmdb

# Set TMDB API key
with open("apikey.txt", "r") as file:
    tmdb.API_KEY = file.readline().strip()
    
# Initialize Flask app
app = Flask(__name__)

@app.route('/')
def home():
    # Fetch trending movies
    popular_movies = tmdb.Movies().popular()
    top_9_movies = popular_movies['results'][:9]  # Get top 9 trending movies
    poster_urls = ""

    # Construct full image URLs for posters
    for movie in top_9_movies:
        poster_url = f"https://image.tmdb.org/t/p/w500{movie['poster_path']}"  # Movie poster
        poster_urls += poster_url+" "

    # return render_template('trending-carousel-temp.html', poster_urls=poster_urls)
    return render_template('home.html', poster_urls=poster_urls)

@app.route('/search', methods=['POST'])
def search():
    # Get user search input
    query = request.form.get('query')
    category = request.form.get('category')

    search = tmdb.Search()

    # Perform search based on category
    if category == "movie":
        search.movie(query=query)
    elif category == "tv":
        search.tv(query=query)
    elif category == "person":
        search.person(query=query)
    else:
        return "Invalid category", 400  # Error handling

    return render_template('results.html', results=search.results, category=category, query=query)

if __name__ == '__main__':
    app.run(debug=True)
