"""This is the typical game called Battleship !!!"""
#coding:utf-8
import os
import time
import random

BOARD = []
for x in range(0,5):
    BOARD.append(["O"] * 5)

def clean():
    clear = lambda: os.system ("clear") 
    clear()

def reset():
    reset=lambda: os.system ("reset")
    reset()

def initial():
    print" "
    print """
            ______       _   _   _           _     _       
            | ___ \     | | | | | |         | |   (_)      
            | |_/ / __ _| |_| |_| | ___  ___| |__  _ _ __  
            | ___ \/ _` | __| __| |/ _ \/ __| '_ \| | '_ \ 
            | |_/ / (_| | |_| |_| |  __/\__ \ | | | | |_) |
            \____/ \__,_|\__|\__|_|\___||___/_| |_|_| .__/ 
                                                    | |    
                                                    |_|   """
    time.sleep(0.6)
def welcome():
    print """
                                     # #  ( )
                                  ___#_#___|__
                              _  |____________|  _
                       _=====| | |            | | |==== _
                 =====| |.---------------------------. | |====
   <--------------------'   .  .  .  .  .  .  .  .   '--------------/
     \                                                             /
      \_______________________________________________WWS_________/
  wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww
wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww
   wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww """
    print"""
                          _                                
            __      _____| | ___ ___  _ __ ___   ___       
            \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \      
             \ V  V /  __/ | (_| (_) | | | | | |  __/_ _ _ 
              \_/\_/ \___|_|\___\___/|_| |_| |_|\___(_|_|_)"""
    time.sleep(3)

def repeat_bar():
    reset()
    print"    "
    print"    "
    print "Loading."
    print "█"*5
    initial()
    clean()
    print"    "
    print"    "
    print "Loading.."
    print "█"*10
    initial()
    clean()
    print"    "
    print"    "
    print "Loading..."
    print "█"*15
    initial()
    clean()
    print"    "
    print"    "
    print "Loading...."
    print "█"*20
    initial()
    clean()
    print"    "
    print"    "
    print "Loading."
    print "█"*25
    initial()
    clean()
    print"    "
    print"    "
    print "Loading.."
    print "█"*30
    initial()
    clean()
    print"    "
    print"    "
    print "Loading..."
    print "█"*35
    initial()
    clean()
    print"    "
    print"    "
    print "Loading...."
    print "█"*40
    initial()
    clean()
    print"    "
    print"    "
    print "Loading."
    print "█"*45
    initial()
    clean()
    print"    "
    print"    "
    print "Loading.."
    print "█"*50
    initial()
    clean()
    print"    "
    print"    "
    print "Loading..."
    print "█"*55
    initial()
    clean()
    print"    "
    print"    "
    print "Loading..."
    print "█"*60
    reset()
    welcome()
repeat_bar()

def codigo():
    raw_input("\nPRESIONE ENTER PARA CONTINUAR...")
    os.system("clear")
    print_board(BOARD)()
    codigo()


BOARD = []
for x in range(0,5):
    BOARD.append(["O"] * 5)


clean()
def print_board(BOARD):
    for row in BOARD:
        print " ".join(row)
print "::: Battle-Ship :::"
print "Let's play Battle Ship!!!  "
time.sleep(0.5)
print_board(BOARD)

def row_random(BOARD):
    return random.randint(0,len(BOARD)-1)

def column_random(BOARD):
    return random.randint(0,len(BOARD[0])-1)

ship_row = row_random(BOARD)
ship_col = column_random(BOARD)
print "_________"
print ship_row
print ship_col

# From now on everything should be in your loop!
# Be sure to indent!
for turn in range(4):
    guess_row = input("Guess row:")
    guess_column = input("Guess column:")

    if guess_row == ship_row and guess_column == ship_col:
        print "Congratulations! Sink my ship"
        break
    else:
        if (guess_row < 0 or guess_row > 4) or (guess_column < 0 or guess_column > 4):
            print "Wow, this is not even in the ocean."
        elif(BOARD[guess_row][guess_column] == "X"):
            print "You already said that."
        else:
            print "Not hit my ship!"
            BOARD[guess_row][guess_column] = "X"
        if turn == 3:
            print "Game Over"
    # Displays (turn + 1) here!
        print turn + 1

