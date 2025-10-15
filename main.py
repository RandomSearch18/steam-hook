from threading import Thread
from dotenv import load_dotenv
from steam_tracker import steam_tracker
from web_ui import run_web_ui


def main():
    Thread(target=steam_tracker, daemon=True).start()
    run_web_ui()


if __name__ == "__main__":
    load_dotenv()
    main()
