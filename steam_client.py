from steam.webapi import WebAPI

# A map of internal achievement names to whether the player has achieved them
type GameAchievementsDict = dict[str, bool]
# A map of game IDs to achievement dictionaries
type PlayerAchievementsMatrix = dict[int, GameAchievementsDict]


class Steam:
    """A Steam API wrapper customised for our uses"""

    def __init__(self, api_key: str):
        # self.api_key = api_key
        self.client = WebAPI(key=api_key)
        # A map of Steam (player) IDs to their achievement matrices
        self.players_achievements_matrices: dict[int, PlayerAchievementsMatrix] = {}

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

    def fetch_owned_games(self, steam_id: int):
        return self.client.call(
            "IPlayerService.GetOwnedGames",
            steamid=steam_id,
            include_appinfo=True,
            include_extended_appinfo=False,
            include_played_free_games=True,
            appids_filter=[],
            include_free_sub=True,
            language="en",
        )

    def fetch_recently_played_games(self, steam_id: int):
        return self.client.call(
            "IPlayerService.GetRecentlyPlayedGames", steamid=steam_id
        )

    def update_player_achievement_matrix(self, steam_id: int):
        if steam_id in self.players_achievements_matrices:
            # TODO
            pass
        else:
            # Fetch all their games so that we have all info possible to use as a base for comparisons (in the future)
            games = self.fetch_owned_games(steam_id)["games"]
