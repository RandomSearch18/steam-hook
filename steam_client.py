from typing import Callable
from requests import HTTPError
from steam.webapi import WebAPI

# A map of internal achievement names to whether the player has achieved them
type GameEarnedAchievements = set[str]
# A map of game IDs to achievement dictionaries
type PlayerAchievementsMatrix = dict[int, GameEarnedAchievements]


class Steam:
    """A Steam API wrapper customised for our uses"""

    def __init__(self, api_key: str):
        # self.api_key = api_key
        self.client = WebAPI(key=api_key)
        # A map of Steam (player) IDs to their achievement matrices
        self.players_achievements_matrices: dict[int, PlayerAchievementsMatrix] = {}
        self.handle_newly_earned_achievement: Callable[[int, int, str]] = (
            lambda steam_id, app_id, achievement_id: None
        )

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
            "IPlayerService.GetRecentlyPlayedGames", steamid=steam_id, count=0
        )

    def create_achievement_set_for_game(
        self, app_id: int, steam_id: int
    ) -> GameEarnedAchievements:
        try:
            player_achievements_data = self.fetch_player_achievements(
                app_id=app_id, steam_id=steam_id
            )["playerstats"]
        except HTTPError as error:
            # Some games don't have stats at all, and get angry if you ask them about it
            # (Error message from API is "Requested app has no stats")
            if error.response.status_code == 400:
                return set()
            else:
                raise error
        if "achievements" not in player_achievements_data:
            # Some games don't have achievements
            return set()
        player_achievements = player_achievements_data["achievements"]
        achievements_set = {
            achievement["apiname"]
            for achievement in player_achievements
            if achievement["achieved"]
        }
        return achievements_set

    def update_player_achievement_matrix(self, steam_id: int):
        if steam_id in self.players_achievements_matrices:
            our_matrix = self.players_achievements_matrices[steam_id]
            # Assuming that the player will only have earn achievements on recently-played games, we use fetch_global_achievement_percentages()
            # TODO
            games = self.fetch_recently_played_games(steam_id)["response"]["games"]
            for game in games:
                app_id = game["appid"]
                if app_id not in our_matrix:
                    # This is probably a newly-purchased game! We should discover its achievements
                    achievements_dict = self.create_achievement_set_for_game(
                        app_id=app_id, steam_id=steam_id
                    )
                    our_matrix[app_id] = achievements_dict
                else:
                    old_achievements = our_matrix[app_id]
                    new_achievements = self.create_achievement_set_for_game(
                        app_id=app_id, steam_id=steam_id
                    )
                    # TODO: compare!
                    newly_earned = new_achievements - old_achievements
                    for achievement_id in newly_earned:
                        self.handle_newly_earned_achievement(
                            steam_id, app_id, achievement_id
                        )
                    our_matrix[app_id] = new_achievements
                    return our_matrix
        else:
            # Fetch all their games so that we have all info possible to use as a base for comparisons (in the future)
            games = self.fetch_owned_games(steam_id)["response"]["games"]
            achievements_matrix: PlayerAchievementsMatrix = {}
            for game in games:
                app_id = game["appid"]
                achievements_dict = self.create_achievement_set_for_game(
                    app_id=app_id, steam_id=steam_id
                )
                achievements_matrix[app_id] = achievements_dict
            self.players_achievements_matrices[steam_id] = achievements_matrix
        return self.players_achievements_matrices[steam_id]
