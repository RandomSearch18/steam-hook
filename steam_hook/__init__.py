# Entrypoint when using `flask --app steam_hook run`
from threading import Thread
from dotenv import load_dotenv
from steam_hook.steam_tracker import steam_tracker
from steam_hook.web_ui import app


def create_app(test_config=None):
    load_dotenv()
    Thread(target=steam_tracker, daemon=True).start()
    return app
