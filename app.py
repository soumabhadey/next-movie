from flask import Flask, render_template, request
import find_similar

app = Flask(__name__)

API_KEY = ""  # Replace with your actual API key

@app.route("/", methods=["GET"])
def index():
    movie_name = request.args.get("movie_name")
    similar_movies = None

    if movie_name:
        similar_movies = find_similar.find_similar_movies(movie_name)

    return render_template("index.html", movie_name=movie_name, similar_movies=similar_movies, get_movie_poster=find_similar.get_movie_poster)

if __name__ == "__main__":
    app.run(debug=True)
