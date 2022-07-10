from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_restx import Api, Resource

from schemas import movie_schema, movies_schema
from models import *


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#app.config['JSON_AS_ASCII'] = False
db = SQLAlchemy(app)

api = Api(app)
movie_ns = api.namespace('movies')


@movie_ns.route('/')
class MovieView(Resource):
    def get(self):
        all_movies = db.session.query(Movie.id, Movie.title, Movie.description, Movie.rating, Movie.trailer, Genre.name.label('genre'), Director.name.label('director')).join(Genre).join(Director).all()
        return movies_schema.dump(all_movies)


if __name__ == '__main__':
    app.run(debug=True)
