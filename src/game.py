import curses
import json


from .player import Player
from .board import Board
from typing import List

from curses import wrapper, window
from curses.textpad import Textbox, rectangle

class Game:
    _players: List[Player] = []
    _board: Board
    _ui_win: window
    _player_win: window

    def __init__(self,stdscr:window) -> None:
        self._board = Board()
        self._board.createBoard(stdscr)
        BOARD_H = self._board.get_board_height()
        BOARD_W = self._board.get_board_width()
        # Create border and ui_text window
        self._ui_win = curses.newwin(int(curses.LINES/2),40,2,BOARD_W+2)
        rectangle(stdscr,1,BOARD_W+1,25,BOARD_W*2)
        # Create border and player input window
        self._player_win = curses.newwin(BOARD_H-10,BOARD_W-19,5,9)
        rectangle(stdscr,4,8,9,BOARD_W-17)
        
        # self._ui_win.refresh()
        # self._player_win.refresh()
        stdscr.refresh()
        pass
        
    def get_board(self):
        return self._board
    
    def get_ui_win(self)->window:
        return self._ui_win
    
    def get_player_win(self)->window:
        return self._player_win
    
    def add_player(self, player: Player):
        player_name = player.get_name()
        self._players.append(player)
        self.print_ui_text(player_name + " has been added")

    def get_players_pos(self):
        # Should probably get player by id right?
        for player in self.players:
            return player.get_post()
    
    def print_ui_text(self,text:str):
        self._ui_win.addstr(text + "\n")
    
    def playerTurn(self,player:Player,amount_of_rolls:int = 1):
        file = open("src/spaces.json")
        data = json.load(file)
        file.close()

        if(amount_of_rolls == 1):
            self.print_ui_text(player.get_name() + " is taking their turn...")
        turn = True
        dbls = False
        [d1,d2] = player.roll_dice()
        self.print_ui_text("Dice 1 is "+str(d1))
        self.print_ui_text("Dice 2 is "+str(d2))
        if d1 == d2:
            self.print_ui_text("Doubles!")
            amount_of_rolls = amount_of_rolls + 1
            dbls = True

        if(amount_of_rolls == 3):
            self.print_ui_text("Go to Jail")
            turn = False
            pass

        total = d1+d2
        player.move_player(total)
        self.print_ui_text("Moved Player: "+player.get_name()+" "+str(total)+" spots!")
        space = data[player.get_pos()]
        self.print_ui_text(player.get_name()+" now at "+str(space['name']))
        self._ui_win.refresh()
        if(dbls):
            self.print_ui_text(player.get_name() + " gets to go again!")
            self.playerTurn(player,amount_of_rolls)
        
        turn = False


