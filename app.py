from flask import Flask, render_template, request
import find_similar

app = Flask(__name__)

# @app.route("/", methods=["GET", "POST"])
# def index():
#     similar_movies = None
#     if request.method == "POST":
#         movie_name = request.form["movie_name"]
#         similar_movies = find_similar.find_similar_movies(movie_name)

#     return render_template("index.html", similar_movies=similar_movies)




@app.route("/", methods=["GET"])
def index():
    movie_name = request.args.get("movie_name")
    similar_movies = None

    if movie_name:
        similar_movies = find_similar.find_similar_movies(movie_name)

    return render_template("index.html", movie_name=movie_name, similar_movies=similar_movies)