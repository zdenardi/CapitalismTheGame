from src.board import Board
from src.player import Player
from src.property import Property
from src.game import Game
import curses

from curses import wrapper, window
from curses.textpad import Textbox, rectangle


def startGame(stdscr: window):
    game = Game(stdscr)

    board = game.get_board()
    ui_win = game.get_ui_win()
    player_win = game.get_player_win()

    WAITING = False

    board.createBoard(stdscr)

    game.print_ui_text("Starting...")

    first_player = game.getUserInput("Enter Player 1's name and press CTRL+G ")
    second_player = game.getUserInput("Enter Player 2's name and press CTRL+G ")
    p1 = Player(first_player)
    p2 = Player(second_player)

    game.add_player(p1)
    game.add_player(p2)

    game.playerTurn(p1)
    game.playerTurn(p2)

    stdscr.getkey()


if __name__ == "__main__":
    wrapper(startGame)
