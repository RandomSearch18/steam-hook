from steam.webapi import WebAPI
from dotenv import load_dotenv
from os import getenv


def main():
    steam = WebAPI(key=getenv("STEAM_API_KEY"))

    game = 504230
    user = 
    game_schema = steam.call("ISteamUserStats.GetSchemaForGame", appid=game)
    achievements = game_schema["game"]["availableGameStats"]["achievements"]
    print(game_schema)
    user_achievements = steam.call(
        "ISteamUserStats.GetPlayerAchievements", appid=game, steamid=user
    )
    print(user_achievements)
    global_achievements = steam.call(
        "ISteamUserStats.GetGlobalAchievementPercentagesForApp", gameid=game
    )
    print(global_achievements)


if __name__ == "__main__":
    load_dotenv()
    main()
