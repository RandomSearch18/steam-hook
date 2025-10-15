from flask import Flask, render_template
from steam_tracker import steam_wrapper

app = Flask(__name__)


@app.route("/")
def index():
    steam = steam_wrapper()
    return render_template("debug.html", steam=steam)


def run_web_ui():
    app.run(host="0.0.0.0", port=5000)
