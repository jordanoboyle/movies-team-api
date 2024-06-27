from flask import Flask, request
from flask_cors import CORS
import db

app = Flask(__name__)
CORS(app)
CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route("/movies.json", endpoint="index_movies")
def index_movies():
    return db.movies_all()

@app.route("/movies.json", methods=["POST"])
def create_movies():
    name = request.form.get("name")
    release_year = request.form.get("release_year")
    run_time = request.form.get("run_time")
    image_url = request.form.get("image_url")
    return db.movies_create(name, release_year, run_time, image_url)

@app.route("/movies/<id>.json")
def show_movie(id):
    return db.movies_find_by_id(id)

@app.route("/movies/<id>.json", methods=["PATCH"])
def update_movie(id):
    name = request.form.get("name")
    release_year = request.form.get("release_year")
    run_time = request.form.get("run_time")
    image_url = request.form.get("image_url")
    return db.movies_update_by_id(id, name, release_year, run_time, image_url)

@app.route("/movies/<id>.json", methods=["DELETE"])
def destroy_movie(id):
    return db.movies_destroy_by_id(id)


#GENRES Routes
@app.route("/genres.json", endpoint="index_genres")
def index_genres():
    return db.genres_all()

@app.route("/genres.json", methods=["POST"], endpoint="create_genre")
def create_genre():
    movie_id = request.form.get("movie_id",)
    name = request.form.get("name",)
    return db.genres_create(movie_id, name)

@app.route("/genres/<id>.json", endpoint="show_genre")
def show_genre(id):
    return db.genres_find_by_id(id)

@app.route("/genres/<id>.json", methods=["PATCH"], endpoint="update_genre")
def update_genre(id):
    movie_id = request.form.get("movie_id")
    name = request.form.get("name")
    return db.genres_update_by_id(id, movie_id, name)

@app.route("/genres/<id>.json", methods=["DELETE"], endpoint="delete_genre")
def delete_genre(id):
    return db.genres_destroy_by_id(id)

#REVIEWS Routes
@app.route("/reviews.json", endpoint="index_reviews")
def index_reviews():
    return db.reviews_all()

@app.route("/reviews.json", methods=["POST"])
def create_review():
    movie_id = request.form.get("movie_id")
    user_id = request.form.get("user_id")
    title = request.form.get("title")
    body = request.form.get("body")
    rating = request.form.get("rating")
    return db.reviews_create(movie_id, user_id, title, body, rating)

@app.route("/reviews/<id>.json")
def show_review(id):
    return db.reviews_find_by_id(id)

@app.route("/reviews/<id>.json", methods=["PATCH"])
def update_review(id):
    movie_id = request.form.get("movie_id")
    user_id = request.form.get("user_id")
    title = request.form.get("title")
    body = request.form.get("body")
    rating = request.form.get("rating")
    return db.reviews_update_by_id(id, movie_id, user_id, title, body, rating)

@app.route("/reviews/<id>.json", methods=["DELETE"])
def destroy_review(id):
    return db.reviews_destroy_by_id(id)