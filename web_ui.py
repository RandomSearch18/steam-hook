from flask import Flask
from steam_tracker import steam_wrapper

app = Flask(__name__)


@app.route("/")
def index():
    steam = steam_wrapper()
    return f"Hello :p {steam.players_achievements_matrices if steam else 'Steam not initialized'}"


def run_web_ui():
    app.run(host="0.0.0.0", port=5000)
