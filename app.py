from flask import Flask, render_template, request
from db import Movie

app = Flask(__name__)


@app.route('/')
def index():
    movie_name = request.args.get("name", "")
    movies = Movie.find_by_name(movie_name) if movie_name else None
    return render_template("gui.html", name=movie_name, data=movies)
