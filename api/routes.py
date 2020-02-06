# current_app in to have more flexible app
from flask import request, jsonify, current_app
from api.models import Movie, MovieSchema


@current_app.route('/', methods=['GET'])
def get_movies():
    """ setup query from database and sends via Get Method

    Attributes:
        all_movies: 
        movie_schema: 
        movies_schema: 
        result:

    :param {sting} route: 
        exp: /
    :param {string} request method: 
        
    :return: {Object} jsonify: data in json format
    """
    all_movies = Movie.query.all()
    # Init schema
    # schema for single movie
    movie_schema = MovieSchema()
    # schema to request all  movies
    movies_schema = MovieSchema(many=True)
    result = movies_schema.dump(all_movies)
    return jsonify(result)