from flask import Flask, render_template
from steam_hook.steam_tracker import steam_wrapper

app = Flask(__name__)


@app.route("/")
def index():
    steam = steam_wrapper()
    return render_template("debug.html", steam=steam)
