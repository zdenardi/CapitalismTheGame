from .player import Player
from typing import List
class Board():
    _players: List[Player] = []

    def get_players_pos(self):
        for player in self.players:
            print(str(player.get_pos()))
    
    def add_player(self,player:Player):
        player_name = player.get_name()
        self._players.append(player)
        print(player_name+" has been added")

        

# corner is 6 long
# propertyTB is 4 long
# property LR is 6 long
# each side has two corners and 9 properties 
# each side has 12 sides/walls. WccccccWccccW 
# 12+36+12 "characters" = 60
# (y,x)

# Top border = 60 '_' (0,0 -> 0,60)
# Outside border R '|' (1,1 -> 59,1)
# Bottom Border '‾' (1,60 -> 60->60)
# Outside border L '|' (1,59->59,59)

# FP - 1,1 -> 6,6

    def create_corner(self):
        top_bottom = " "*6
        second_line = " TEST "

    def create_top_property(self):
        top_line = " "* 4
        second_line = " ?? "
        third_line = "="*4

    def create_bottom_property(self):
        top_line = " "* 4
        second_line = " ?? "
        third_line = " "*4
    
    def create_left_right_property(self):
        top_line = " ?? "
        bottom_line = " "*6



