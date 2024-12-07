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
    ui_win = curses.newwin(curses.LINES, UI_WIDTH, 0, board_width)
    ui_win.border()

    line_height = 1

    p1 = Player("Zach")
    p2 = Player("Sarah")

    board = Board()
    board.add_player(p1)
    board.add_player(p2)
    line_height = 1

    def print_ui_window(text: str, line_height: int):
        ui_win.addstr(line_height, 2, text + "/n")
        line_height = line_height + 1

    print_ui_window("Hello", line_height)
    print_ui_window("Two", line_height)

    # def playerTurn(player:Player,amount_of_rolls:int = 1):
    #     if(amount_of_rolls == 1):
    #         print(player.get_name() + " is taking their turn")
    #     turn = True
    #     dbls = False
    #     dice = player.roll_dice()
    #     d1 = dice[0]
    #     d2 = dice[1]
    #     if d1 == d2:
    #         print("Doubles!")
    #         amount_of_rolls = amount_of_rolls + 1
    #         dbls = True

    #     if(amount_of_rolls == 3):
    #         print("Go to Jail")
    #         turn = False
    #         pass

    #     total = d1+d2
    #     player.move_player(total)
    #     print("Moved Player: "+player.get_name()+" "+str(total)+" spots!")
    #     space = data[player.get_pos()]
    #     print(player.get_name()+" now at "+str(space['name']))
    #     if(dbls):
    #         print(player.get_name() + " gets to go again!")
    #         playerTurn(player,amount_of_rolls)
    #     turn = False

    # playerTurn(p1)
    # playerTurn(p2)

    stdscr.refresh()
    ui_win.refresh()
    stdscr.getkey()


wrapper(startGame())
