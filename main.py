from src.board import Board
from src.player import Player
from src.property import Property
import json
from curses import wrapper,window

# file = open('./src/spaces.json')
# data = json.load(file)
# file.close()
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
    RIGHT_SIDE_RAIL = "["
    LEFT_SIDE_RAIL = "]"

    stdscr.clear()

    game_board = stdscr.subwin(BOARD_HEIGHT+2,BOARD_WIDTH+2,0,0)
    for w in range(0,BOARD_WIDTH-3):
        game_board.addch(0,w,TOP_BORDER)
        game_board.addch(BOARD_HEIGHT-2,w,BOTTOM_BORDER)
    for h in range(1,BOARD_HEIGHT-2):
        game_board.addch(h,0,SIDE)
        game_board.addch(h,BOARD_WIDTH-4,SIDE)
    def create_corner(w:window,starting_y,starting_x):
        corner = w.subwin(CORNER_H,CORNER_W,starting_y,starting_x)
        for y in range(1,CORNER_H):
            corner.addch(y,0,SIDE)
            corner.addch(y,6,SIDE)
        for x in range(1,6):
            corner.addch(3,x,BOTTOM_BORDER)

    def create_left_prop(w:window,starting_y,starting_x):
        prop = w.subwin(PROP_LR_H,PROP_LR_W,starting_y,starting_x)
        for y in range(0,2):
            prop.addch(y,0,LEFT_SIDE_RAIL)
        for x in range(1,6):
            prop.addch(1,x,BOTTOM_BORDER)
        
    def create_right_prop(w:window,starting_y,starting_x):
        prop = w.subwin(PROP_LR_H,PROP_LR_W,starting_y,starting_x)
        for y in range(0,2):
            prop.addch(y,6,RIGHT_SIDE_RAIL)
        for x in range(1,6):
            prop.addch(1,x,BOTTOM_BORDER)

    def create_top_prop(w:window,starting_y,starting_x):
        prop = w.subwin(PROP_TB_H,PROP_TB_W,starting_y,starting_x)
        # prop.addstr(1,1,"--")
        for x in range(0,4):
            prop.addstr(2,x,TOP_BOTTOM_RAIL)
        for y in range(0,3):
            prop.addstr(y,4,SIDE)
     

    def create_bottom_prop(w:window,starting_y,starting_x):
        prop = w.subwin(PROP_TB_H,PROP_LR_W,starting_y,starting_x)
        for x in range(0,4):
            prop.addch(0,x,TOP_BOTTOM_RAIL)
        for y in range(0,3):
            prop.addch(y,4,SIDE)
     
    
    
    free_parking = create_corner(stdscr,0,0)
    g2j = create_corner(stdscr,0,R_INSIDE_BORDER_X)
    go = create_corner(stdscr,21,R_INSIDE_BORDER_X)
    jail = create_corner(stdscr,21,0)

# create left and right side
    create_left_prop(stdscr,4,R_INSIDE_BORDER_X)
    create_right_prop(stdscr,4,0)

    for numOfProp in range(2,11):
        start_y = 4,
        create_left_prop(stdscr,2*numOfProp,R_INSIDE_BORDER_X)
        create_right_prop(stdscr,2*numOfProp,L_INSIDE_BORDER_X)

    create_top_prop(stdscr,1,CORNER_W-1)
    create_bottom_prop(stdscr,22,7)
    for num in range(3,11):
        create_top_prop(stdscr,1,PROP_TB_W*num-3)
        create_bottom_prop(stdscr,22,5*num-3)


    
    # game_board.border()
    stdscr.refresh()
    stdscr.getkey()



wrapper(createBoard)


