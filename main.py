from src.board import Board
from src.player import Player
from src.property import Property
from src.game import Game
import curses

from curses import wrapper, window
from curses.textpad import Textbox, rectangle



def startGame(stdscr:window):
    game = Game(stdscr)

    board = game.get_board()
    ui_win = game.get_ui_win()
    player_win = game.get_player_win()

    WAITING = False

    board.createBoard(stdscr)

    game.print_ui_text("Starting...")

    game.print_ui_text( "Enter Player 1's name and press CTRL+G ")
    
    box = Textbox(player_win)

    stdscr.refresh()
    ui_win.refresh()
    

    WAITING = True

    while WAITING:
        box.edit()
        WAITING = False
    
    player_name = box.gather().strip()

    player_win.clear()
    stdscr.refresh()

    p1 = Player(player_name)
    p2 = Player("Sarah")

    game.add_player(p1)
    game.add_player(p2)

    game.playerTurn(p1)
    game.playerTurn(p2)

    stdscr.getkey()


if __name__ == "__main__":
    wrapper(startGame)
