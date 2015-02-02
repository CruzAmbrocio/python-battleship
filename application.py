"""This is the typical game called Battleship !!!"""
#coding:utf-8
import os
import time
import random
import sys
board = []
BOARD_U = []
SHIPS = {"Aircraft Carrier":5,
            "Battleship":4,
            "Submarine":3,
            "Destroyer":3,
            "Patrol Boat":2}
LETTER = {   "Aircraft Carrier": "|" + chr(27)+"[0;95m"+" A "+chr(27)+"[0m",
             "Battleship": "|"+chr(27)+"[0;92m"+" B "+chr(27)+"[0m",
             "Submarine": "|"+chr(27)+"[0;96m"+" S "+chr(27)+"[0m",
             "Destroyer": "|"+chr(27)+"[0;93m"+" D "+chr(27)+"[0m",
             "Patrol Boat": "|"+ chr(27)+"[0;94m"+" P "+chr(27)+"[0m"}

def for_def(board):
    for x in range(0,10):
        board.append(["|   "] * 10)
    print_board(board)

def print_board(board):
    print "   | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10"
    print "-------------------------------------------|"
    for row, cosa in enumerate(board):
        if row < 9:
            print row + 1, " " + "".join(cosa) + "|"
            print "-------------------------------------------|"
        else:
            print row + 1, "" + "".join(cosa) + "|"
            print "-------------------------------------------|"
    user_reply()



"""This is the typical game called Battleship !!!"""
#coding:utf-8
import os
import time
import random
import sys
board = []
BOARD_U = []
BOARD_C = []
SHIPS = {   "Aircraft Carrier":5,
            "Battleship":4,
            "Submarine":3,
            "Destroyer":3,
            "Patrol Boat":2}

LETTER = {   "Aircraft Carrier": "|" + chr(27)+"[0;95m"+" A "+chr(27)+"[0m",
             "Battleship": "|"+chr(27)+"[0;92m"+" B "+chr(27)+"[0m",
             "Submarine": "|"+chr(27)+"[0;96m"+" S "+chr(27)+"[0m",
             "Destroyer": "|"+chr(27)+"[0;93m"+" D "+chr(27)+"[0m",
             "Patrol Boat": "|"+ chr(27)+"[0;94m"+" P "+chr(27)+"[0m"}

def for_def(board):
    """Define measures the board  :::"""
    for x in range(0,10):
        board.append(["|   "] * 10)
    print_board(board)

def print_board(board):
    """Print the cells and board spaces  :::"""
    print "   | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10"
    print "-------------------------------------------|"
    for row, thing in enumerate(board):
        if row < 9:
            print row + 1, " " + "".join(thing) + "|"
            print "-------------------------------------------|"
        else:
            print row + 1, "" + "".join(thing) + "|"
            print "-------------------------------------------|"

def enter_row():
    """Check the row value entered by the user  :::"""
    while (True):
        try:
            guess_row = int(raw_input("Enter the row:   "))
            if guess_row >=1 and guess_row <=10:
                guess_row -=1
                return guess_row
                break
            else:
                print "This coordinate does not exist in the ocean   "
        except ValueError:
            print "Input coordinates in a range of 1 to 10   "

def enter_col():
    """Check the column value entered by the user  :::"""
    while (True):
        try:
            guess_col = int(raw_input("Enter the column:   "))
            if guess_col >=1 and guess_col <=10:
                guess_col -=1
                return guess_col
                break
            else:
                print "This coordinate does not exist in the ocean   "
        except ValueError:
            print"Input coordinates in a range of 1 to 10   "

def boat_user():
    """Place the user boats  :::"""
    for_def(BOARD_U)
    for boat in SHIPS:
        repeat = False
        while repeat == False:
            print "Where you want to place a  '"+ chr(27)+"[0;95m"+boat+chr(27)+"[0m"+ "'  of  '" +chr(27)+"[0;91m"+str(SHIPS[boat])+chr(27)+"[0m"+ "'   boxes ::: !!..."
            boat_row = enter_row()
            boat_col = enter_col()
            boat_posi = ver_horiz()
            if boat_posi == "h":
                no_encounter = encounter_h(BOARD_U, SHIPS, boat, boat_row, boat_col)
                if no_encounter != False:
                    ship_Hori = hori(SHIPS, boat_row, boat_col, boat)
                    hori(boat_row,boat_col, boat,SHIPS)
                    clean()
                    print_board(BOARD_U)
                    repeat = True
            elif boat_posi == "v":
                no_encounter2 = encounter_v(BOARD_U, SHIPS, boat, boat_row, boat_col)
                if no_encounter2 != False:
                    ship_vert = vertl(SHIPS, boat_row, boat_col)
                    vertl(boat_row,boat_col, boat)
                    clean()
                    print_board(BOARD_U)
                    repeat = True
    print "It is time that the program position your ships to compertir with you"
    raw_input("\npress enter to place ...")
    boat_comp()

def defin_row():
    """Check the row value entered by the user  :::"""
    while (True):
        try:
            ship_row = random_row(BOARD_C)
            print ship_row
            if ship_row >=1 and ship_row <=10:
                ship_row -=1
                return ship_row
                break
            else:
                print "This coordinate does not exist in the ocean   "
        except ValueError:
            print "Input coordinates in a range of 1 to 10 0000  "

def defin_col():
    """Check the column value entered by the user  :::"""
    while (True):
        try:
            ship_col = random_col(board)
            print ship_col
            if ship_col >=1 and ship_col <=10:
                ship_col -=1
                return ship_col
                break
            else:
                print "This coordinate does not exist in the ocean   "
        except ValueError:
            print"Input coordinates in a range of 1 to 10   "


def random_row(BOARD_C):
    return random.randint(0,10 )

def random_col(BOARD_C):
    return random.randint(0,10)

def shot_user_row():
    """Check the column value entered by the user  :::"""
    while (True):
        try:
            guess_col = int(raw_input("Enter the column:   "))
            if guess_col >=1 and guess_col <=10:
                guess_col -=1
                return guess_col
                break

            else:
                print "This coordinate does not exist in the ocean   "
        except ValueError:
            print"Input coordinates in a range of 1 to 10   "

def shot_user_col():

    while (True):
        try:
            guess_row = int(raw_input("Enter the column:   "))
            if guess_row >1 and guess_row <=10:
                guess_row-=1
                return guess_row
                break
            else:
                print"This coordinate does not exist in the ocean   "
        except ValueError:
            print"Input coordinates in a range of 1 to 10   "

def hit_shot(new):
    count=0
    try:
        for thing in range(new[boat]):
            if "|   " in board[c_x][c_y + thing]:
                count += 1 
    except: 
        print "There is already a boat here insert new coordinates"
    hit_shot(BOARD_U)
    for boat in SHIPS:
        repeat = False
        while repeat == False:
            print "Where you want to place a  '"+ chr(27)+"[0;95m"+boat+chr(27)+"[0m"+ "'  of  '" +chr(27)+"[0;91m"+str(SHIPS[boat])+chr(27)+"[0m"+ "'   boxes ::: !!..."
            boat_row = shot_user_row()
            boat_col = shot_user_col()
            boat_posi = ver_horiz()

            no_encounter = encounter_h(BOARD_U, SHIPS, boat, boat_row, boat_col)
            if no_encounter != False:
                ship_Hori = hori(SHIPS, boat_row, boat_col, boat)
                hori(boat_row,boat_col, boat,SHIPS)
                clean()
                print_board(BOARD_U)
                repeat = True
            no_encounter2 = encounter_v(BOARD_U, SHIPS, boat, boat_row, boat_col)
            if no_encounter2 != False:
                ship_vert = vertl(SHIPS, boat_row, boat_col)
                vertl(boat_row,boat_col, boat)
                clean()
                print_board(BOARD_U)
                repeat = True





def boat_comp():
    """Place the user boats  :::"""
    for_def(BOARD_C)
    for boat in SHIPS:
        repeat = False
        while repeat == False:
            print "Where you want to place a  '"+ chr(27)+"[0;95m"+boat+chr(27)+"[0m"+ "'  of  '" +chr(27)+"[0;91m"+str(SHIPS[boat])+chr(27)+"[0m"+ "'   boxes ::: !!..."
            boat_row = defin_row()
            boat_col = defin_col()
            boat_posi = ver_horiz_aleat()
            if boat_posi == "h":
                no_encounter = encounter_h2(BOARD_C, SHIPS, boat, boat_row, boat_col)
                if no_encounter != False:
                    ship_Hori = horizon_comp(SHIPS, boat_row, boat_col, boat)
                    horizon_comp(boat_row,boat_col, boat,SHIPS)
                    clean()
                    print_board(BOARD_C)
                    repeat = True
            elif boat_posi == "v":
                no_encounter2 = encounter_v2(BOARD_C, SHIPS, boat, boat_row, boat_col)
                if no_encounter2 != False:
                    ship_vert = vertical_comp(SHIPS, boat_row, boat_col)
                    vertical_comp(boat_row,boat_col, boat)
                    clean() 
                    print_board(BOARD_C)
                    repeat = True
    raw_input("\npress enter to place ...")
    clean()
    print """
     __ _                 _   _                     
    / _\ |__   ___   ___ | |_(_)_ __   __ _   _ _ _ 
    \ \| '_ \ / _ \ / _ \| __| | '_ \ / _` | (_|_|_)
    _\ \ | | | (_) | (_) | |_| | | | | (_| |  _ _ _ 
    \__/_| |_|\___/ \___/ \__|_|_| |_|\__, | (_|_|_)
                                      |___/         
    """
    print "   "
    print "Shooting"
    raw_input("\npress enter to place ...")
    shot_user_row()
    shot_user_col()
    hit_shot()





def encounter_v2(board, new, boat, c_x, c_y):
    count = 0 

    try:
        for thing in range(new[boat]):
            if "|   " in board[c_x + thing][c_y]:
                count += 1 
    except: 
        print "There is already a boat here insert new coordinates"
        return False

    if count == new[boat]: 
        return True
    else: 
        print "There is already a boat here insert new coordinates"
        return False 

def encounter_h2(board,new, boat, c_x, c_y):
    count = 0
    try:
        for thing in range(new[boat]):
            if "|   " in board[c_x][c_y + thing]:
                count += 1 
    except: 
        print "There is already a boat here insert new coordinates"
        return False

    if count == new[boat]: 
        return True
    else: 
        print "There is already a boat here insert new coordinates"
        return False 

def horizon_comp( c_x, c_y, boat,new):
    """characters placed horizontally boats  :::"""
    try:
        for coor in range(SHIPS[boat]):
            BOARD_C[c_x][c_y + coor] = LETTER[boat]
    except:
        try:
            for coor in range(SHIPS[boat]):
                BOARD_C[c_x][c_y + coor] = "|   "
        except:
            print "coordinate table is out of the ocean"

def vertical_comp(c_x, c_y, boat):
    """characters placed vertically boats  :::"""
    try:
        for coor in range(SHIPS[boat]):
            BOARD_C[c_x + coor][c_y] = LETTER[boat]
    except:
        try:
            for coor in range(SHIPS[boat]):
                BOARD_C[c_x + coor][c_y] = "|   "
        except:
            print "coordinate table is out of the ocean"

def ver_horiz_aleat():
    """Check the orientation in which the user wishes to place the boats  :::"""
    print "Enter the orientation of ships:   "
    while True:
        print ""
        orien_alet = ["v", "h"]
        reply = random.choice(orien_alet)
        reply_low = reply.lower()
        print reply_low
        if reply_low == "h":
            return "h"
            break
        elif reply_low == "v":
            return "v"
            break
        else:
            print ""
            print "Enter valid characters"




def encounter_v(board, new, boat, c_x, c_y):
    count = 0 

    try:
        for thing in range(new[boat]):
            if "|   " in board[c_x + thing][c_y]:
                count += 1 
    except: 
        print "There is already a boat here insert new coordinates"
        return False
    if count == new[boat]: 
        return True
    else: 
        print "There is already a boat here insert new coordinates"
        return False 




def encounter_h(board,new, boat, c_x, c_y):
    count = 0
    try:
        for thing in range(new[boat]):
            if "|   " in board[c_x][c_y + thing]:
                count += 1 
    except: 
        print "There is already a boat here insert new coordinates"
        return False
    if count == new[boat]: 
        return True
    else: 
        print "There is already a boat here insert new coordinates"
        return False 

def hori( c_x, c_y, boat,new):
    """characters placed horizontal boats  :::"""
    try:
         for coor in range(SHIPS[boat]):
            BOARD_U[c_x][c_y + coor] = LETTER[boat]
    except:
        try:
            for coor in range(SHIPS[boat]):
                BOARD_U[c_x + coor][c_y] = "|   "
        except:
            print "coordinate table is out of the ocean"

def vertl(c_x, c_y, boat):
    """characters placed vertically boats  :::"""
    try:
        for coor in range(SHIPS[boat]):
            BOARD_U[c_x + coor][c_y] = LETTER[boat]
    except:
        try:
            for coor in range(SHIPS[boat]):
                BOARD_U[c_x + coor][c_y] = "|   "
        except:
            print "coordinate table is out of the ocean"

def ver_horiz():
    """Check the orientation in which the user wishes to place the boats  :::"""
    print "Enter the orientation of ships:   "
    while True:
        print ""
        reply_user = raw_input(" v/h: ")
        reply_low = reply_user.lower()
        if reply_low == "h":
            return "h"
            break
        elif reply_low == "v":
            return "v"
            break
        else:
            print ""
            print "Enter valid characters"


def clean():
    """Used to clean the screen"""
    clear = lambda: os.system ("clear") 
    clear()

def reset():
    """Used to reset the screen"""
    reset=lambda: os.system ("reset")
    reset()




def welcome():
    """This is the first image of the game"""
    print """

                       ..:::aad8888888baa:::                        
                    .::::d:?88888888888?::8b::::                    
                  .:::d8888:?88888888??a888888b:::                  
                .:::d8888888a8888888aa8888888888b:::                
               ::::dP::::::::88888888888::::::::Yb::::              
              ::::dP:::::::::Y888888888P:::::::::Yb::::             
             ::::d8:::::::::::Y8888888P:::::::::::8b::::            
            .::::88::::::::::::Y88888P::::::::::::88::::            
            :::::Y8baaaaaaaaaa88P:T:Y88aaaaaaaaaad8P:::::           
            :::::::Y88888888888P::|::Y88888888888P:::::::           
            ::::::::::::::::888:::|:::888::::::::::::::::           
            `:::::::::::::::8888888888888b::::::::::::::'           
             :::::::::::::::88888888888888::::::::::::::            
              :::::::::::::d88888888888888:::::::::::::             
               ::::::::::::88::88:::88::88::::::::::::              
                `::::::::::88::88:::88::88::::::::::'               
                  `::::::::88::88:::88::88::::::::'                 
                    `::::::88::88:::88::88::::::'                   
      ___          _     _     _              _      _              
     | _ )  __ _  | |_  | |_  | |  ___   ___ | |_   (_)  _ __  ™    
     | _ \ / _` | |  _| |  _| | | / -_) (_-< | ' \  | | | '_ \      
     |___/ \__,_|  \__|  \__| |_| \___| /__/ |_||_| |_| | .__/      
                                                        |_|         """
    time.sleep(0.7)

def color_wel():
    """To change color to welcome"""
    welcome()
    clean()
    print"    "
    print"    "+chr(27)+"[0;92m"+""
    welcome()
    clean()
    print"    "
    print"    "+chr(27)+"[0;95m"+""
    welcome()
    clean()
    print"    "
    print"    "+chr(27)+"[0;91m"+""
    welcome()
    clean()
    print"    "
    print"    "+chr(27)+"[0;96m"+""
    welcome()
    clean()
color_wel()
def initial():
    """This is the screen to load the game"""
    print" "
    print """
         ______       _   _   _           _     _                    
         | ___ \     | | | | | |         | |   (_)                   
         | |_/ / __ _| |_| |_| | ___  ___| |__  _ _ __               
         | ___ \/ _` | __| __| |/ _ \/ __| '_ \| | '_ \              
         | |_/ / (_| | |_| |_| |  __/\__ \ | | | | |_) |             
         \____/ \__,_|\__|\__|_|\___||___/_| |_|_| .__/              
                                                 | |                
                        oo                       |_|     ™           
                          o ooo        _                             
                             oo oo    | | #)---<                     
                              oo     _| |_#_          |              
                                o   | U-187 |         |              
  __              __________________|       |_________|________      
 |   \____-------/                                      _    ☠ \     
X     ____                O   O   O   O   O   O      --<_>      )    
 |__ /    -------\____________________________________________ /     """
    time.sleep(0.7)

def instructions():
    """This is the game instructions"""
    print"""
Descripción
Tableros
Cada jugador maneja dos tableros divididos en casillas. Cada tablero     
representa una zona diferente del mar abierto: la propia y la contraria. 
 En uno de los tableros, el jugador coloca sus barcos y registra los     
  «tiros» del oponente; en el otro, se registran los tiros propios,      
  al tiempo que se deduce la posición de los barcos del contrincantes    
Naves                                                                    
                                                                         
                                                                         
                                                                         
                                                                         
                                                                         
    """
    print "    "
    print "Press - 1 - to go to the main menu :::   "
    options = raw_input("Choose an options:  ")
    if options == "1":
        clean()
        menu()
    else:
        clean()
        print chr(27)+"[0;91m"+" * Enter a valid option 4:   "+chr(27)+"[0m"
        instructions()

def menu():
    """this is principal menu"""
    chooseopt = 0
    print """
           /\/\   ___ _ __  _   _                   
 _____    /    \ / _ \ '_ \| | | |          _____   
|_____|  / /\/\ \  __/ | | | |_| |  _ _ _  |_____|  
         \/    \/\___|_| |_|\__,_| (_|_|_)          
                                                    """
    """principal menu"""
    time.sleep(0.03)
    print "What to do? ...  "
    time.sleep(0.03)
    print "Press - 1 - for single player :::   "
    time.sleep(0.03)
    print "Press - 2 - for multiplayer :::   "
    time.sleep(0.03)
    print "Press - 3 - for instructions :::   "
    time.sleep(0.03)
    print "Press - 4 - about:::   "
    time.sleep(0.03)
    print "Press - 5 - to exit the game :::   "
    time.sleep(0.03)
    print "     "
    time.sleep(0.03)
    while chooseopt != 5:
        try:
            chooseopt = int(raw_input("Choose an option:  "))
            if chooseopt == 5:
                clean()
                print chr(27)+"[5;96m"+"""
                 ☻ /     
                /█      
                / \     
                Bye ::: ...
                    """+chr(27)+"[0m"
                time.sleep(2)
                reset()
                sys.exit(1)
            elif chooseopt == 1:
                clean()
                name_user()
            elif chooseopt == 2:
                clean()
                print board
            elif chooseopt == 3:
                clean()
                instructions()
            elif chooseopt == 4:
                clean()
            elif chooseopt <= 0:
                print chr(27)+"[0;91m"+" * Enter a valid option 1:   "+chr(27)+"[0m"
            elif chooseopt > 5:
                print chr(27)+"[0;91m"+" * Enter a valid option 2:   "+chr(27)+"[0m"
        except ValueError:
            print chr(27)+"[0;91m"+" * Enter a valid option 3:   "+chr(27)+"[0m"
def name_user():
    """This is a user name """
    print """
           ___       _   _   _           _     _      ™   
          / __\ __ _| |_| |_| | ___  ___| |__ (_)_ __     
         /__\/// _` | __| __| |/ _ \/ __| '_ \| | '_ \    
        / \/  \ (_| | |_| |_| |  __/\__ \ | | | | |_) |   
        \_____/\__,_|\__|\__|_|\___||___/_| |_|_| .__/    
                                                |_|       
                                                          """
    name = raw_input("             What its your name ?   ")
    reset()
    print"""
           __    __     _                              
          / / /\ \ \___| | ___ ___  _ __ ___   ___     
          \ \/  \/ / _ \ |/ __/ _ \| '_ ` _ \ / _ \    
           \  /\  /  __/ | (_| (_) | | | | | |  __/    
            \/  \/ \___|_|\___\___/|_| |_| |_|\___|    
                                                       
                    >>>*  %s  *<<<                     
          _          _   _             _               
         | |        | | ( )           | |              
         | |     ___| |_|/ ___   _ __ | | __ _ _   _   
         | |    / _ \ __| / __| | '_ \| |/ _` | | | |  
         | |___|  __/ |_  \__ \ | |_) | | (_| | |_| |  
         |______\___|\__| |___/ | .__/|_|\__,_|\__, |  
                                | |             __/ |  
                                |_|            |___/   """  %(name.title())
    print "  "
    print "Now you must position your ships do it the strategic way you think it will be difficult to be sunk"
    raw_input("\nPress Enter to continue ...")
    reset()
    boat_user()
def repeat_bar():
    """This is the bar to load the game"""
    clean()
    welcome()
    reset()
    print"    "
    print"    "
    print """
|    _  _. _|*._  _ 
|___(_)(_](_]|[ )(_]
                 ._|"""+chr(27)+"[0;91m"+""
    print "█"*5
    initial()
    clean()
    print"    "
    print"    "
    print """
|    _  _. _|*._  _ 
|___(_)(_](_]|[ )(_]
                 ._|"""+chr(27)+"[0;91m"+"☠"
    print "█"*10
    initial()
    clean()
    print"    "
    print"    "
    print """
|    _  _. _|*._  _ 
|___(_)(_](_]|[ )(_]
                 ._|"""+chr(27)+"[0;92m"+"☠ ☠"
    print "█"*15
    initial()
    clean()
    print"    "
    print"    "
    print """
|    _  _. _|*._  _ 
|___(_)(_](_]|[ )(_]
                 ._|"""+chr(27)+"[0;93m"+"☠ ☠ ☠"
    print "█"*20
    initial()
    clean()
    print"    "
    print"    "
    print """
|    _  _. _|*._  _ 
|___(_)(_](_]|[ )(_]
                 ._|"""
    print "█"*25
    initial()
    clean()
    print"    "
    print"    "
    print """
|    _  _. _|*._  _ 
|___(_)(_](_]|[ )(_]
                 ._|"""+chr(27)+"[0;96m"+"☠"
    print "█"*30
    initial()
    clean()
    print"    "
    print"    "
    print """
|    _  _. _|*._  _ 
|___(_)(_](_]|[ )(_]
                 ._|"""+chr(27)+"[0;95m"+"☠ ☠"
    print "█"*35
    initial()
    clean()
    print"    "
    print"    "
    print """
|    _  _. _|*._  _ 
|___(_)(_](_]|[ )(_]
                 ._|"""+chr(27)+"[0;96m"+"☠ ☠ ☠"
    print "█"*40
    initial()
    clean()
    print"    "
    print"    "
    print """
|    _  _. _|*._  _ 
|___(_)(_](_]|[ )(_]
                 ._|"""
    print "█"*45
    initial()
    clean()
    print"    "
    print"    "
    print """
|    _  _. _|*._  _ 
|___(_)(_](_]|[ )(_]
                 ._|"""+chr(27)+"[0;97m"+"☠"
    print "█"*50
    initial()
    clean()
    print"    "
    print"    "
    print """
|    _  _. _|*._  _ 
|___(_)(_](_]|[ )(_]
                 ._|"""+chr(27)+"[0;92m"+"☠ ☠"
    print "█"*55
    initial()
    clean()
    print"    "
    print"    "
    print """
|    _  _. _|*._  _ 
|___(_)(_](_]|[ )(_]
                 ._|"""+chr(27)+"[0;94m"+"☠ ☠ ☠"
    print "█"*60
    initial()
    reset()
    menu()
repeat_bar()
