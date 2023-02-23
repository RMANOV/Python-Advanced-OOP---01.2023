# Steam User
# Create a class called SteamUser. Upon initialization, it should receive a username (string) and games (list). 
# It should also have an attribute called played_hours (0 by default). Add three methods to the class:
# -	play(game, hours)
# o	If the game is in the game list, increase the played_hours by the given hours and return "{username} is playing {game}"
# o	Otherwise, return "{game} is not in library"
# -	buy_game(game)
# o	If the game is not in the game list, add it and return "{username} bought {game}"
# o	Otherwise, return "{game} is already in your library"
# -	status() - returns the following:
#     "{username} has {games_count} games. Total play time: {played_hours}"


class SteamUser:
    def __init__(self, username, games):
        self.username = username
        self.games = games
        self.played_hours = 0

    def play(self, game, hours):
        if game in self.games:
            self.played_hours += hours
            return f"{self.username} is playing {game}"
        else:
            return f"{game} is not in library"

    def buy_game(self, game):
        if game not in self.games:
            self.games.append(game)
            return f"{self.username} bought {game}"
        else:
            return f"{game} is already in your library"

    def status(self):
        return f"{self.username} has {len(self.games)} games. Total play time: {self.played_hours}"
