from src.board import Board
from src.player import Player
from src.property import Property
import json
from curses import wrapper, window
import curses


def startGame():
    stdscr = curses.initscr()
    board = Board()

    board_width = board.get_board_width()
    board_height = board.get_board_height()

    UI_WIDTH = int(curses.COLS - board_width)

    board.createBoard(stdscr)

    file = open("src/spaces.json")
    data = json.load(file)
    file.close()

    ui_win = curses.newwin(curses.LINES, UI_WIDTH, 0, board_width)
    # Creates the nice border
    ui_win.border()
    # This is creating text subwindow inside the UI_WIN
    ui_text = ui_win.subwin(curses.LINES-2,UI_WIDTH-4,2,board_width+2)


    p1 = Player("Zach")
    p2 = Player("Sarah")

    board = Board()
    board.add_player(p1)
    board.add_player(p2)

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

    playerTurn(p1)
    playerTurn(p2)

    stdscr.refresh()
    ui_win.refresh()
    stdscr.getkey()


wrapper(startGame())
