from threading import Thread
from dotenv import load_dotenv
from steam_hook.steam_tracker import steam_tracker
from steam_hook.web_ui import app

def initialize_app():
    load_dotenv()
    Thread(target=steam_tracker, daemon=True).start()
    return app

def main():
    # Entrypoint when not using the Flask CLI
    app = initialize_app()
    app.run(host="0.0.0.0", port=5000)


if __name__ == "__main__":
    main()
