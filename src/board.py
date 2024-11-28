from .player import Player
from typing import List
class Board():
    num_of_spaces: int = 40
    _players: List[Player] = []

    def get_players_pos(self):
        for player in self.players:
            print(str(player.get_pos()))
    
    def add_player(self,player:Player):
        player_name = player.get_name()
        self._players.append(player)
        print(player_name+" has been added")

    


