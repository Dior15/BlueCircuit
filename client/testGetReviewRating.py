import pytest
from movies import *

movieEngine = Movies()

def testGetReview():
  # Test getting the reviews of a movie
  reviews = movieEngine.getTopXMovies(1)[0].getReviews()
  assert len(reviews) >= 0

def testGetRating(): 
  rating = movieEngine.getTopXMovies(1)[0].getRating()
  assert 0 <= rating
  assert rating <= 5