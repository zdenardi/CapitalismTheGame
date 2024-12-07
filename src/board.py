from .player import Player
from typing import List
import json
from curses import wrapper, window


class Board:
    _players: List[Player] = []
    _L_INSIDE_BORDER_X: int = 0
    _R_INSIDE_BORDER_X: int = 51
    _CORNER_H: int = 4
    _CORNER_W: int = 8
    _PROP_LR_H: int = 2
    _PROP_LR_W: int = 8
    _PROP_TB_H: int = 4
    _PROP_TB_W: int = 5

    _BOARD_WIDTH: int = (_CORNER_W * 2) + (_PROP_TB_W * 9)
    _BOARD_HEIGHT: int = (2 * _CORNER_H) + (9 * _PROP_LR_H)

    def get_players_pos(self):
        for player in self.players:
            print(str(player.get_pos()))

    def add_player(self, player: Player):
        player_name = player.get_name()
        self._players.append(player)
        print(player_name + " has been added")

    def createBoard(self, stdscr: window):
        # Get property JSON
        file = open("src/spaces.json")
        data = json.load(file)
        file.close()

        # Break up data to their own constants
        BOTTOM_SPACES = data[1:10]
        LEFT_SPACES = data[11:20]
        RIGHT_SPACES = data[31:40]
        TOP_ROW_SPACES = data[21:30]

        BOTTOM_SPACES.reverse()  # must be reversed for logic of render
        LEFT_SPACES.reverse()  # must be reversed for logic of render

        TOP_BORDER = "_"
        BOTTOM_BORDER = "_"
        SIDE = "|"
        TOP_BOTTOM_RAIL = "="
        LEFT_SIDE_RAIL = "["
        RIGHT_SIDE_RAIL = "]"

        stdscr.clear()

        game_board = stdscr.subwin(self._BOARD_HEIGHT + 2, self._BOARD_WIDTH + 2, 0, 0)
        for w in range(0, self._BOARD_WIDTH - 3):
            game_board.addch(0, w, TOP_BORDER)
            game_board.addch(self._BOARD_HEIGHT - 2, w, BOTTOM_BORDER)
        for h in range(1, self._BOARD_HEIGHT - 2):
            game_board.addch(h, 0, SIDE)
            game_board.addch(h, self._BOARD_WIDTH - 4, SIDE)

        # Creates corner spaces
        def create_corner(
            w: window, starting_y: int, starting_x: int, corner_name: str = "--"
        ):
            corner = w.subwin(self._CORNER_H, self._CORNER_W, starting_y, starting_x)
            corner.addstr(2, 2, corner_name)
            for y in range(1, self._CORNER_H):
                corner.addch(y, 0, SIDE)
                corner.addch(y, 6, SIDE)
            for x in range(1, 6):
                corner.addch(3, x, BOTTOM_BORDER)

        # Creates right Side spaces
        def create_right_prop(
            w: window, starting_y: int, starting_x: int, prop_abr: str = "--"
        ):
            prop = w.subwin(self._PROP_LR_H, self._PROP_LR_W, starting_y, starting_x)
            prop.addstr(0, 2, prop_abr)
            for y in range(0, 2):
                prop.addch(y, 0, LEFT_SIDE_RAIL)
            for x in range(1, 6):
                prop.addch(1, x, BOTTOM_BORDER)

        # Creates Left side spaces
        def create_left_prop(
            w: window, starting_y: int, starting_x: int, prop_abr: str = "--"
        ):
            prop = w.subwin(self._PROP_LR_H, self._PROP_LR_W, starting_y, starting_x)
            prop.addstr(0, 2, prop_abr)

            for y in range(0, 2):
                prop.addch(y, 6, RIGHT_SIDE_RAIL)
            for x in range(1, 6):
                prop.addch(1, x, BOTTOM_BORDER)

        # Creates top line spaces
        def create_top_prop(
            w: window, starting_y: int, starting_x: int, prop_abr: str = "--"
        ):
            prop = w.subwin(self._PROP_TB_H, self._PROP_TB_W, starting_y, starting_x)
            prop.addstr(1, 1, prop_abr)
            for x in range(0, 4):
                prop.addstr(2, x, TOP_BOTTOM_RAIL)
            for y in range(0, 3):
                prop.addstr(y, 4, SIDE)

        # creates bottom line spaces
        def create_bottom_prop(
            w: window, starting_y: int, starting_x: int, prop_abr: str = "--"
        ):
            prop = w.subwin(self._PROP_TB_H, self._PROP_LR_W, starting_y, starting_x)
            prop.addstr(1, 1, prop_abr)
            for x in range(0, 4):
                prop.addch(0, x, TOP_BOTTOM_RAIL)
            for y in range(0, 3):
                prop.addch(y, 4, SIDE)

        # Using the spaces.json, gets the name of the space and shortens
        def get_property_abbr(words: str):
            if words == "Community Chest":
                return "CC"
            if words == "Chance":
                return "??"
            first_letters = ""
            for word in words.split():
                first_letters = first_letters + word[0]
            return first_letters

        # create corners
        free_parking = create_corner(stdscr, 0, 0, "0-0")
        g2j = create_corner(stdscr, 0, self._R_INSIDE_BORDER_X, "!!!")
        go = create_corner(stdscr, 21, self._R_INSIDE_BORDER_X, "GO!")
        jail = create_corner(stdscr, 21, 0, "|||")

        # create left and right side
        create_right_prop(stdscr, 4, self._R_INSIDE_BORDER_X)
        create_left_prop(stdscr, 4, 0)

        for i in range(2, 11):
            left_abr = get_property_abbr(LEFT_SPACES[i - 2]["name"])
            right_abr = get_property_abbr(RIGHT_SPACES[i - 2]["name"])
            create_left_prop(stdscr, 2 * i, self._L_INSIDE_BORDER_X, left_abr)

            create_right_prop(stdscr, 2 * i, self._R_INSIDE_BORDER_X, right_abr)

        # create top and bottom
        spacer = self._CORNER_W - 1

        for i in range(0, 9):
            top_abbr = get_property_abbr(TOP_ROW_SPACES[i]["name"])
            bottom_abbr = get_property_abbr(BOTTOM_SPACES[i]["name"])
            create_top_prop(stdscr, 1, spacer, top_abbr)
            create_bottom_prop(stdscr, 22, spacer, bottom_abbr)
            spacer = spacer + self._PROP_TB_W

        return stdscr

    def get_board_width(self):
        return self._BOARD_WIDTH

    def get_board_height(self):
        return self._BOARD_HEIGHT
