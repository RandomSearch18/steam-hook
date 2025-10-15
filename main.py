from time import sleep
from dotenv import load_dotenv
from os import getenv

from steam_client import Steam


def handle_newly_earned_achievement(steam_id: int, app_id: int, achievement_id: str):
    print(
        f"Player {steam_id} has just earned achievement {achievement_id} in game {app_id}"
    )


def main():
    steam_api_key = getenv("STEAM_API_KEY")
    if not steam_api_key:
        raise ValueError("No STEAM_API_KEY found in environment variables")
    steam = Steam(api_key=steam_api_key)
    steam.handle_newly_earned_achievement = handle_newly_earned_achievement

    # game_schema = steam.fetch_game_schema(appid=game)
    # achievements = game_schema["game"]["availableGameStats"]["achievements"]
    # print(game_schema)
    # owned_games = steam.fetch_owned_games(steam_id=user)
    # user_achievements = steam.fetch_player_achievements(app_id=game, steam_id=user)
    # print(user_achievements)
    # global_achievements = steam.fetch_global_achievement_percentages(app_id=game)
    # print(global_achievements)
    while True:
        user_id = int(getenv("STEAM_USER_ID"))
        steam.update_player_achievement_matrix(steam_id=user_id)
        sleep(10)


if __name__ == "__main__":
    load_dotenv()
    main()
