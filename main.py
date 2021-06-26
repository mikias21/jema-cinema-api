from flask import Flask, jsonify, request, make_response

# movie data 
from scrappers.recent_uploaded import get_recent_content
from scrappers.movies import get_movies
from scrappers.series import get_series
from scrappers.cinema import get_cinema
from scrappers.recommeded import get_recommended

app = Flask(__name__)

@app.route("/api/movies/home", methods=['GET'])
def get_home_content():
    if request.method == 'GET':
        home_content = {
            'recommended': get_recommended(),
            'recent': get_recent_content(),
            'cinema': get_cinema(),
            'movies': get_movies(),
            'series': get_series()
        }
        resp = make_response(home_content)
        resp.headers.set("Access-Control-Allow-Origin", "*")
        resp.headers.set("Access-Control-Allow-Methods", "GET")
        resp.headers.set("Access-Control-Allow-Headers", "*")
        return resp


if __name__ == "__main__":
    app.run(port=9090)
    app.debug(True)

