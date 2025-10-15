from steam.webapi import WebAPI


class Steam:
    """A Steam API wrapper customised for our uses"""

    def __init__(self, api_key: str):
        # self.api_key = api_key
        self.client = WebAPI(key=api_key)

    def fetch_game_schema(self, appid: int):
        return self.client.call("ISteamUserStats.GetSchemaForGame", appid=appid)

    def fetch_player_achievements(self, app_id: int, steam_id: int):
        return self.client.call(
            "ISteamUserStats.GetPlayerAchievements", appid=app_id, steamid=steam_id
        )

    def fetch_global_achievement_percentages(self, app_id: int):
        return self.client.call(
            "ISteamUserStats.GetGlobalAchievementPercentagesForApp", gameid=app_id
        )
