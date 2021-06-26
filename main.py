from flask import Flask, jsonify, request, make_response
import flask

# movie data 
from home_scrapper import get_recommended_content, get_latest_movies, get_trending, get_latest_tv, get_recommended_tv_shows

app = Flask(__name__)

@app.route("/api/movies/home", methods=['GET'])
def get_home_content():
    if request.method == 'GET':
        home_content = {
            'recommended': get_recommended_content(),
            'latest_movies': get_latest_movies(),
            'trending': get_trending(),
            'latest_tv': get_latest_tv(),
            'recommended_tv': get_recommended_tv_shows()
        }
        resp = make_response(home_content)
        resp.headers.set("Access-Control-Allow-Origin", "*")
        resp.headers.set("Access-Control-Allow-Methods", "GET")
        resp.headers.set("Access-Control-Allow-Headers", "*")
        return resp



if __name__ == "__main__":
    app.run(port=9090)
    app.debug(True)

