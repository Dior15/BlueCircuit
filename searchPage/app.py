from flask import Flask, render_template, request
import tmdbsimple as tmdb

# Set your TMDB API key
with open("apikey.txt", "r") as file:
    tmdb.API_KEY = file.readline().strip()
tmdb.REQUESTS_TIMEOUT = 1

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    query = request.form.get('query')
    category = request.form.get('category')

    search = tmdb.Search()

    if category == "movie":
        response = search.movie(query=query)
    elif category == "tv":
        response = search.tv(query=query)
    elif category == "person":
        response = search.person(query=query)
    else:
        return "Invalid category selected", 400

    return render_template('results.html', results=search.results, category=category, query=query)

if __name__ == '__main__':
    app.run(debug=True)
