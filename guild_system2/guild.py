# The Guild class receives a name (string). 
# The Guild should also have one instance attribute players (an empty list which will contain the players of the guild). 
# The class also has 3 additional methods:
# -	assign_player(player: Player)
# o	Adds the player to the guild and returns "Welcome player {player_name} to the guild {guild_name}". 
# Remember to change the player's guild in the player class.
# o	If he is already in the guild, returns "Player {player_name} is already in the guild."
# o	If the player is in another guild, returns "Player {player_name} is in another guild."
# -	kick_player(player_name: str)
# o	Removes the player from the guild and returns "Player {player_name} has been removed from the guild.". 
# Remember to change the player's guild in the player class to "Unaffiliated".
# o	If there is no such player in the guild, returns "Player {player_name} is not in the guild."
# -	guild_info()
# o	Returns the guild's information, including the players in the guild, in the format:
# "Guild: {guild_name}
# {first_player's info}
# …
# {Nplayer's info}"




class Guild:
    def __init__(self, name):
        self.name = name
        self.players = []

    def assign_player(self, player):
        if player.guild == self.name:
            return f"Player {player.name} is already in the guild."
        elif player.guild != "Unaffiliated":
            return f"Player {player.name} is in another guild."
        else:
            player.guild = self.name
            self.players.append(player)
            return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name):
        for player in self.players:
            if player.name == player_name:
                player.guild = "Unaffiliated"
                self.players.remove(player)
                return f"Player {player_name} has been removed from the guild."
        return f"Player {player_name} is not in the guild."

    def guild_info(self):
        # result = f"Guild: {self.name} \n"
        # for player in self.players:
        #     result += player.player_info()
        # return result
        players = '\n'.join([player.player_info() for player in self.players])
        return f"Guild: {self.name}\n{players}"

