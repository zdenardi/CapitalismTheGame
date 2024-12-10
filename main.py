from src.board import Board
from src.player import Player
from src.property import Property
import json
import curses

from curses import wrapper, window
from curses.textpad import Textbox, rectangle



def startGame(stdscr:window):
    board = Board()
    WAITING = False

    board_width = board.get_board_width()
    board_height = board.get_board_height()

    UI_WIDTH = int(curses.COLS - board_width)

    board.createBoard(stdscr)

    file = open("src/spaces.json")
    data = json.load(file)
    file.close()

    # Creates the nice border
    ui_text = curses.newwin(int(curses.LINES/2),40,2,board_width+2)
    rectangle(stdscr,1,board_width+1,25,board_width*2)

    player_win = curses.newwin(board_height-8,board_width-15,5,9)
    rectangle(stdscr,4,8,9,board_width-16)
    player_win.refresh()

    def print_ui_text(text:str):
        ui_text.addstr(text + "\n")
    
    print_ui_text("Starting...")
    def playerTurn(player:Player,amount_of_rolls:int = 1):
        if(amount_of_rolls == 1):
            print_ui_text(player.get_name() + " is taking their turn...")
        turn = True
        dbls = False
        dice = player.roll_dice()
        d1 = dice[0]
        d2 = dice[1]
        if d1 == d2:
            print_ui_text("Doubles!")
            amount_of_rolls = amount_of_rolls + 1
            dbls = True

        if(amount_of_rolls == 3):
            print_ui_text("Go to Jail")
            turn = False
            pass

        total = d1+d2
        player.move_player(total)
        print_ui_text("Moved Player: "+player.get_name()+" "+str(total)+" spots!")
        space = data[player.get_pos()]
        print_ui_text(player.get_name()+" now at "+str(space['name']))
        if(dbls):
            print_ui_text(player.get_name() + " gets to go again!")
            playerTurn(player,amount_of_rolls)
        turn = False

    print_ui_text( "Enter Player 1's name and press CTRL+G ")
    
    box = Textbox(player_win)

    stdscr.refresh()
    ui_text.refresh()
    player_win.refresh()
    WAITING = True

    while WAITING:
        box.edit()
        player_win.clear()
        stdscr.refresh()
        ui_text.refresh()
        player_win.refresh()
        WAITING = False
    
    player_name = box.gather().strip()

    p1 = Player(player_name)
    p2 = Player("Sarah")

    board.add_player(p1)
    board.add_player(p2)

    playerTurn(p1)
    playerTurn(p2)

    stdscr.getkey()


if __name__ == "__main__":
    wrapper(startGame)
