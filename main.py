from src.board import Board
from src.player import Player
from src.property import Property
import json
from curses import wrapper,window

# Get property JSON
file = open('./src/spaces.json')
data = json.load(file)
file.close()
# Break up data to their own constants 
BOTTOM_SPACES = data[1:10]
LEFT_SPACES = data[11:20]
RIGHT_SPACES = data[31:40]
TOP_ROW_SPACES = data[21:30]

BOTTOM_SPACES.reverse() # must be reversed for logic of render
LEFT_SPACES.reverse()   # must be reversed for logic of render


# print("Starting")
# p1 = Player("Zach")
# p2 = Player("Sarah")

# board = Board()
# board.add_player(p1)
# board.add_player(p2)


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
       
def createBoard(stdscr:window):
    L_INSIDE_BORDER_X = 0
    R_INSIDE_BORDER_X = 51
    CORNER_H = 4
    CORNER_W = 8
    PROP_LR_H = 2
    PROP_LR_W = 8
    PROP_TB_H = 4
    PROP_TB_W = 5

    BOARD_WIDTH = (CORNER_W*2) + (PROP_TB_W *9)
    BOARD_HEIGHT = (2 * CORNER_H) + (9 * PROP_LR_H)
    
    TOP_BORDER ="_"
    BOTTOM_BORDER="_"
    SIDE = "|"
    TOP_BOTTOM_RAIL = "="
    LEFT_SIDE_RAIL = "["
    RIGHT_SIDE_RAIL = "]"

    stdscr.clear()

    game_board = stdscr.subwin(BOARD_HEIGHT+2,BOARD_WIDTH+2,0,0)
    for w in range(0,BOARD_WIDTH-3):
        game_board.addch(0,w,TOP_BORDER)
        game_board.addch(BOARD_HEIGHT-2,w,BOTTOM_BORDER)
    for h in range(1,BOARD_HEIGHT-2):
        game_board.addch(h,0,SIDE)
        game_board.addch(h,BOARD_WIDTH-4,SIDE)

    def create_corner(w:window,starting_y,starting_x,corner_name:str="--"):
        corner = w.subwin(CORNER_H,CORNER_W,starting_y,starting_x)
        corner.addstr(2,2,corner_name)
        for y in range(1,CORNER_H):
            corner.addch(y,0,SIDE)
            corner.addch(y,6,SIDE)
        for x in range(1,6):
            corner.addch(3,x,BOTTOM_BORDER)

    def create_right_prop(w:window,starting_y,starting_x,prop_abr:str="--"):
        prop = w.subwin(PROP_LR_H,PROP_LR_W,starting_y,starting_x)
        prop.addstr(0,2,prop_abr)
        for y in range(0,2):
            prop.addch(y,0,LEFT_SIDE_RAIL)
        for x in range(1,6):
            prop.addch(1,x,BOTTOM_BORDER)
        
    def create_left_prop(w:window,starting_y,starting_x,prop_abr:str="--"):
        prop = w.subwin(PROP_LR_H,PROP_LR_W,starting_y,starting_x)
        prop.addstr(0,2,prop_abr)

        for y in range(0,2):
            prop.addch(y,6,RIGHT_SIDE_RAIL)
        for x in range(1,6):
            prop.addch(1,x,BOTTOM_BORDER)

    def create_top_prop(w:window,starting_y,starting_x,prop_abr:str="--"):
        prop = w.subwin(PROP_TB_H,PROP_TB_W,starting_y,starting_x)
        prop.addstr(1,1,prop_abr)
        for x in range(0,4):
            prop.addstr(2,x,TOP_BOTTOM_RAIL)
        for y in range(0,3):
            prop.addstr(y,4,SIDE)
     
    def create_bottom_prop(w:window,starting_y,starting_x,prop_abr:str="--"):
        prop = w.subwin(PROP_TB_H,PROP_LR_W,starting_y,starting_x)
        prop.addstr(1,1,prop_abr)
        for x in range(0,4):
            prop.addch(0,x,TOP_BOTTOM_RAIL)
        for y in range(0,3):
            prop.addch(y,4,SIDE)
     
    def get_property_abbr(words:str):
        if(words == "Community Chest"): return "CC"
        if(words =="Chance"): return "??" 
        first_letters = ""
        for word in words.split(): 
            first_letters = first_letters+word[0]
        return first_letters
# create corners
    free_parking = create_corner(stdscr,0,0,'0-0')
    g2j = create_corner(stdscr,0,R_INSIDE_BORDER_X,'!!!')
    go = create_corner(stdscr,21,R_INSIDE_BORDER_X,'GO!')
    jail = create_corner(stdscr,21,0,'|||')

# create left and right side
    create_right_prop(stdscr,4,R_INSIDE_BORDER_X)
    create_left_prop(stdscr,4,0)

    for i in range(2,11):
        left_abr = get_property_abbr(LEFT_SPACES[i-2]['name'])
        right_abr = get_property_abbr(RIGHT_SPACES[i-2]['name'])
        create_left_prop(stdscr,2*i,L_INSIDE_BORDER_X,left_abr)

        create_right_prop(stdscr,2*i,R_INSIDE_BORDER_X,right_abr)

# create top and bottom
    spacer = CORNER_W-1

    for i in range(0,9):
        top_abbr = get_property_abbr(TOP_ROW_SPACES[i]['name'])
        bottom_abbr = get_property_abbr(BOTTOM_SPACES[i]['name'])
        create_top_prop(stdscr,1,spacer,top_abbr)
        create_bottom_prop(stdscr,22,spacer,bottom_abbr)
        spacer = spacer + PROP_TB_W

    stdscr.refresh()
    stdscr.getkey()


wrapper(createBoard)


