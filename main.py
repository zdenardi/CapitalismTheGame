from src.board import Board
from src.player import Player
from src.property import Property
import json

file = open('./src/spaces.json')
data = json.load(file)
file.close()
print("Starting")
p1 = Player("Zach")
p2 = Player("Sarah")

board = Board()
board.add_player(p1)
board.add_player(p2)


def playerTurn(player:Player,amount_of_roles:int = 1):
    if(amount_of_roles ==1):
        print(player.get_name() + " is taking their turn")
    turn = True
    dbls = False
    dice = player.roll_dice()
    d1 = dice[0]
    d2 = dice[1]
    if d1 == d2:
        print("Doubles!")
        amount_of_roles = amount_of_roles + 1
        dbls = True


    if(amount_of_roles == 3):
        print("Go to Jail")
        turn = False
        pass 

    total = d1+d2
    player.move_player(total)
    print("Moved Player: "+player.get_name()+" "+str(total)+" spots!")
    space = data[player.get_pos()]
    print(player.get_name()+" now at "+str(space['name']))
    if(dbls):
        print(player.get_name() + " gets to go again!")
        playerTurn(player,amount_of_roles)
    turn = False

playerTurn(p1)
playerTurn(p2)