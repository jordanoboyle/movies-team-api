from flask import Flask, request
import db

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'

@app.route("/movies.json")
def index():
    return db.movies_all()

@app.route("/movies.json", methods=["POST"])
def create():
    genre_id = request.form.get("genre_id")
    review_id = request.form.get("review_id")
    name = request.form.get("name")
    release_year = request.form.get("release_year")
    run_time = request.form.get("run_time")
    image_url = request.form.get("image_url")
    return db.movies_create(genre_id, review_id, name, release_year, run_time, image_url)