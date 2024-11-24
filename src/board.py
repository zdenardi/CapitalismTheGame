from .player import Player
from typing import List
import random
class Board():
    num_of_spaces: int = 40
    _players: List[Player] = []

    def get_players_pos(self):
        for player in self.players:
            print(str(player.get_pos()))
    
    def roll_dice(self,player:Player):
        d1 = random.randint(1,6)
        d2 = random.randint(1,6)
        print("Dice 1 is "+str(d1))
        print("Dice 2 is "+str(d2))
        if d1 == d2:
            print("Doubles!")
        total = d1+d2
        player.move_player(total)
        print("Moved Player: "+player.get_name()+" "+str(total)+" spots!")
        print(player.get_name()+" now at "+str(player.get_pos()))
    
    def add_player(self,player:Player):
        player_name = player.get_name()
        self._players.append(player)
        print(player_name+" has been added")

    


