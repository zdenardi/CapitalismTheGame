# Class of player
import itertools
import random

class Player:
    _id: int
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
    
    def roll_dice(self):
        d1 = random.randint(1,6)
        d2 = random.randint(1,6)
        print("Dice 1 is "+str(d1))
        print("Dice 2 is "+str(d2))
        if d1 == d2:
            print("Doubles!")
        total = d1+d2
        self.move_player(total)
        print("Moved Player: "+self.get_name()+" "+str(total)+" spots!")
        print(self.get_name()+" now at "+str(self.get_pos()))
    
