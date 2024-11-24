from src.board import Board
from src.player import Player
from src.property import Property

print("Starting")
p1 = Player("Zach")
p2 = Player("Sarah")

board = Board()
board.add_player(p1)
board.add_player(p2)
p1.roll_dice()
p2.roll_dice()
p1.roll_dice()
p2.roll_dice()
