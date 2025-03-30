import tmdbsimple as tmdb
from models import Watchlist, db
from flask import session

# Set TMDB API key
with open("apikey.txt", "r") as file:
    tmdb.API_KEY = file.readline().strip()
    
class UserWatchlist:
    def add_movie(user_id, movie_id):
        if not movie_id:
            return {'success': False, 'message': 'Movie ID is required'}, 400
        
        existing = Watchlist.query.filter_by(user_id=user_id, movie_id=movie_id).first()
        if existing:
            return {'success': False, 'message': 'Movie already in watchlist'}, 400
        
        new_item = Watchlist(user_id=user_id, movie_id=movie_id)
        db.session.add(new_item)
        db.session.commit()
        return {'success': True, 'message': 'Movie added to watchlist'}, 201
    
    def remove_movie(user_id, movie_id):
        if not movie_id:
            return {'success': False, 'message': 'Movie ID is required'}, 400
        
        entry = Watchlist.query.filter_by(user_id=user_id, movie_id=movie_id).first()
        if not entry:
            return {'success': False, 'message': 'Movie not found in watchlist'}, 404
        
        db.session.delet(entry)
        db.session.commit()
        return {'success': True, 'message': 'Movie removed from wathchlist'}, 200