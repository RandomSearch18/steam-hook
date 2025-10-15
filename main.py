from dotenv import load_dotenv
from os import getenv

from steam_client import Steam


def main():
    steam = Steam(api_key=getenv("STEAM_API_KEY"))

    game = 504230
    user = getenv("STEAM_USER_ID")
    game_schema = steam.fetch_game_schema(appid=game)
    achievements = game_schema["game"]["availableGameStats"]["achievements"]
    print(game_schema)
    owned_games = steam.fetch_owned_games(steam_id=user)
    user_achievements = steam.fetch_player_achievements(app_id=game, steam_id=user)
    print(user_achievements)
    global_achievements = steam.fetch_global_achievement_percentages(app_id=game)
    print(global_achievements)


if __name__ == "__main__":
    load_dotenv()
    main()
