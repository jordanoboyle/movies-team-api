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
    name = request.form.get("name")
    release_year = request.form.get("release_year")
    run_time = request.form.get("run_time")
    image_url = request.form.get("image_url")
    return db.movies_create(name, release_year, run_time, image_url)

@app.route("/movies/<id>.json")
def show(id):
    return db.movies_find_by_id(id)

@app.route("/movies/<id>.json", methods=["PATCH"])
def update(id):
    name = request.form.get("name")
    release_year = request.form.get("release_year")
    run_time = request.form.get("run_time")
    image_url = request.form.get("image_url")
    return db.movies_update_by_id(id, name, release_year, run_time, image_url)

@app.route("/movies/<id>.json", methods=["DELETE"])
def destroy(id):
    return db.movies_destroy_by_id(id)