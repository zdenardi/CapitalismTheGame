# Class of player
import itertools

class Player:
    id: int
    _name:str
    _pos: int = 0
    _money: int = 1500

    id_iter = itertools.count()
  

    def __init__(self, name):
        self._id = next(Player.id_iter)
        self._name = name


    def get_pos(self):
        return self._pos
    
    def get_name(self):
        return self._name
    
    def move_player(self, no_of_spaces: int):
        self._pos = self._pos + no_of_spaces
        return self._pos
    
    
