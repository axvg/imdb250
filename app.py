from flask import Flask, render_template, request
from db import Movie

app = Flask(__name__)

@app.route('/')
def index():
    movie_name = request.args.get("name", "")
    actor_name = request.args.get("actor", "")
    movies = None
    if movie_name:
        movies = Movie.find_by_name(movie_name)
    elif actor_name:
        movies = Movie.find_by_actor(actor_name)
    return render_template("gui.html", name=movie_name or actor_name, data=movies)