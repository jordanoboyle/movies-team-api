from flask import Flask, request
import db

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'

@app.route("/movies.json", endpoint="index_movies")
def index_movies():
    return db.movies_all()

@app.route("/movies.json", methods=["POST"])
def create():
    genre_id     = request.form.get("genre_id")
    review_id    = request.form.get("review_id")
    name         = request.form.get("name")
    release_year = request.form.get("release_year")
    run_time     = request.form.get("run_time")
    image_url    = request.form.get("image_url")
    return db.movies_create(genre_id, review_id, name, release_year, run_time, image_url)

@app.route("/movies/<id>.json")
def show(id):
    return db.movies_find_by_id(id)

@app.route("/movies/<id>.json", methods=["PATCH"])
def update(id):
    genre_id     = request.form.get("genre_id")
    review_id    = request.form.get("review_id")
    name         = request.form.get("name")
    release_year = request.form.get("release_year")
    run_time     = request.form.get("run_time")
    image_url    = request.form.get("image_url")
    return db.movies_update_by_id(id, genre_id, review_id, name, release_year, run_time, image_url)

@app.route("/movies/<id>.json", methods=["DELETE"])
def destroy(id):
    return db.movies_destroy_by_id(id)


#GENRE Routes
@app.route("/genres.json", endpoint="index_genre")
def index_genre():
    return db.genres_all()

@app.route("/genres.json", methods=["POST"], endpoint="create_genre")
def create_genre():
    name = request.form.get("name",)
    return db.genres_create(name,)

@app.route("/genres/<id>", endpoint="show_genre")
def show_genre(id):
    return db.genres_find_by_id(id)

@app.route("/genres/<id>.json", methods=["PATCH"], endpoint="update_genre")
def update_genre(id):
    name = request.form.get("name")
    return db.genres_update_by_id(id, name)

@app.route("/genres/<id>.json", methods=["DELETE"], endpoint="delete_genre")
def delete_genre(id):
    return db.genres_destroy_by_id(id)
