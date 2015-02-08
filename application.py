"""This is the typical game called Battleship !!!"""
#coding:utf-8
#!/usr/bin/env python
 # -*-coding: 850 -*-
import os
import time
import random
import sys
import pygame

pygame.mixer.init()


board = []
BOARD_U = []

BOARD_C = []
BOARD_C_2 = []

BOARD_PLAYER_1 = []
BOARD_PLAYER_1_A = []

BOARD_PLAYER_2 = []
BOARD_PLAYER_2_A = []

SHIPS = {   "Aircraft Carrier" : 5,
            "Battleship" : 4,
            "Submarine" : 3,
            "Destroyer" : 3,
            "Patrol Boat" : 2}

LETTER = {   "Aircraft Carrier" : "| A ",
             "Battleship" : "| B ",
             "Submarine" : "| S ",
             "Destroyer" : "| D ",
             "Patrol Boat" : "| P "}

TAMBORES = pygame.mixer.Sound("TAMBORES.wav")
LOADING = pygame.mixer.Sound("FONDO.wav")
MENU = pygame.mixer.Sound("MUNU.wav")
MUCHOS = pygame.mixer.Sound("MUCHOS.wav")
ACIERTO = pygame.mixer.Sound("ACIERTO.wav")
DESACIERTO = pygame.mixer.Sound("DISPAGUA.wav")
DISPAROS = pygame.mixer.Sound("DISPAROS.wav")

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

def place_user():
    print """
       _                                            
 _ __ | | __ _  ___ ___   _   _  ___  _   _ _ __    
| '_ \| |/ _` |/ __/ _ \ | | | |/ _ \| | | | '__|   
| |_) | | (_| | (_|  __/ | |_| | (_) | |_| | |      
| .__/|_|\__,_|\___\___|  \__, |\___/ \__,_|_|      
|_|                       |___/                     
                _     _                             
            ___| |__ (_)_ __  ___                   
           / __| '_ \| | '_ \/ __|                  
           \__ \ | | | | |_) \__ \  _ _ _           
           |___/_| |_|_| .__/|___/ (_|_|_)          
                       |_|                          
                                                    """

def boat_user():
    """Place the user boats  :::"""
    place_user()
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
                    place_user()
                    print_board(BOARD_U)
                    repeat = True
            elif boat_posi == "v":
                no_encounter2 = encounter_v(BOARD_U, SHIPS, boat, boat_row, boat_col)
                if no_encounter2 != False:
                    ship_vert = vertl(SHIPS, boat_row, boat_col)
                    vertl(boat_row,boat_col, boat)
                    clean()
                    place_user()
                    print_board(BOARD_U)
                    repeat = True
    print "already positioned your ships"
    print "   "
    print "------ It is time that the program position your ships to compertir with you"
    raw_input("\npress enter to place ...")
    boat_comp()

def boat_player_1():
    """Place the user boats  :::"""
    clean()
    for_def(BOARD_PLAYER_1_A)
    clean()
    place_user()
    print "Player 1 colova tus barcos "
    print "°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°"
    for_def(BOARD_PLAYER_1)
    for boat in SHIPS:
        repeat = False
        while repeat == False:
            print "Where you want to place a  '"+ chr(27)+"[0;95m"+boat+chr(27)+"[0m"+ "'  of  '" +chr(27)+"[0;91m"+str(SHIPS[boat])+chr(27)+"[0m"+ "'   boxes ::: !!..."
            boat_row = enter_row()
            boat_col = enter_col()
            boat_posi = ver_horiz()
            if boat_posi == "h":
                no_encounter = encounter_h(BOARD_PLAYER_1, SHIPS, boat, boat_row, boat_col)
                if no_encounter != False:
                    ship_Hori = hori1(SHIPS, boat_row, boat_col, boat)
                    hori1(boat_row,boat_col, boat,SHIPS)
                    clean()
                    place_user()
                    print "Player 1 colova tus barcos "
                    print "°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°"
                    print_board(BOARD_PLAYER_1)
                    repeat = True
            elif boat_posi == "v":
                no_encounter2 = encounter_v(BOARD_PLAYER_1, SHIPS, boat, boat_row, boat_col)
                if no_encounter2 != False:
                    ship_vert = vertl1(SHIPS, boat_row, boat_col)
                    vertl1(boat_row,boat_col, boat)
                    clean()
                    place_user()
                    print "Player 1 colova tus barcos "
                    print "°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°"
                    print_board(BOARD_PLAYER_1)
                    repeat = True
    print "already positioned your ships"
    print "   "
    print "------ It's time to put your competitor ens u board their ships so you can compete with you"
    raw_input("\npress enter to place ...")
    clean()
    boat_player_2()

def boat_player_2():
    """Place the user boats  :::"""
    clean()
    for_def(BOARD_PLAYER_2_A)
    clean()
    place_user()
    print "Player 2 colova tus barcos "
    print "°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°"
    for_def(BOARD_PLAYER_2)
    for boat in SHIPS:
        repeat = False
        while repeat == False:
            print "Where you want to place a  '"+ chr(27)+"[0;95m"+boat+chr(27)+"[0m"+ "'  of  '" +chr(27)+"[0;91m"+str(SHIPS[boat])+chr(27)+"[0m"+ "'   boxes ::: !!..."
            boat_row = enter_row()
            boat_col = enter_col()
            boat_posi = ver_horiz()
            if boat_posi == "h":
                no_encounter = encounter_h(BOARD_PLAYER_2, SHIPS, boat, boat_row, boat_col)
                if no_encounter != False:
                    ship_Hori = hori2(SHIPS, boat_row, boat_col, boat)
                    hori2(boat_row,boat_col, boat,SHIPS)
                    clean()
                    place_user()
                    print "Player 2 colova tus barcos "
                    print "°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°"
                    print_board(BOARD_PLAYER_2)
                    repeat = True
            elif boat_posi == "v":
                no_encounter2 = encounter_v(BOARD_PLAYER_2, SHIPS, boat, boat_row, boat_col)
                if no_encounter2 != False:
                    ship_vert = vertl2(SHIPS, boat_row, boat_col)
                    vertl2(boat_row,boat_col, boat)
                    clean()
                    place_user()
                    print "Player 2 colova tus barcos "
                    print "°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°"
                    print_board(BOARD_PLAYER_2)
                    repeat = True
    print "already positioned your ships"
    print "   "
    raw_input("\npress enter to ontinue ...")
    clean()
    print "   "
    print "This is the PLAYER 2 board :::"
    print "   "
    print_board(BOARD_PLAYER_2_A)
    hit_player_1(board, boat)
    raw_input("\npress enter to place ...")
    statistics_c(BOARD_U)





def defin_row():
    """Check the row value entered by the user  :::"""
    while (True):
        try:
            ship_row = random_row()
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
            ship_col = random_col()
            print ship_col
            if ship_col >=1 and ship_col <=10:
                ship_col -=1
                return ship_col
                break
            else:
                print "This coordinate does not exist in the ocean   "
        except ValueError:
            print"Input coordinates in a range of 1 to 10   "

def random_row():
    return random.randint(0,9)

def random_col():
    return random.randint(0,9)

def hit_user(board, boat):
    print "Dispara... "
    guess_row=  enter_row()
    guess_col= enter_col()
    raw_input("\nDisparar...")
    DISPAROS.play()
    time.sleep(0.4)
    for coor in range(1):
        if BOARD_C[guess_row][guess_col] == "| A " or BOARD_C[guess_row][guess_col] == "| S " or BOARD_C[guess_row][guess_col] == "| B " or BOARD_C[guess_row][guess_col] == "| D " or BOARD_C[guess_row][guess_col] == "| P ":
            BOARD_C[guess_row][guess_col] = "| X "
            ACIERTO.play()
            BOARD_C_2[guess_row][guess_col] = "| X "
            ACIERTO.play()
        elif BOARD_C[guess_row][guess_col] == "| X " or BOARD_C[guess_row][guess_col]== "| + ":
            print chr(27)+"[0;91m"+" In this pocicion already placed a boat try again ... "+chr(27)+"[0m"
            hit_user(board,boat)
        else:
            BOARD_C[guess_row][guess_col] = "| + "
            DESACIERTO.play()
            BOARD_C_2[guess_row][guess_col] = "| + "
            DESACIERTO.play()
        clean()
        print "   "
        print "            This is the SYSTEM board :::"
        print "   "
        print_board(BOARD_C_2)
        statistics_c(BOARD_C)
        raw_input("\npress enter to place ...")
        clean()
        print "este es el tablero del usuario"
        print "  "
        print_board(BOARD_U)
    hit_user_com(board, boat)

def hit_user_com(board, boat):
    guess_row = random_row()
    guess_col = random_col()
    raw_input("\nDisparar...")
    DISPAROS.play()
    time.sleep(0.4)
    for coor in range(1):
        if BOARD_U[guess_row][guess_col] == "| A " or BOARD_U[guess_row][guess_col] == "| S " or BOARD_U[guess_row][guess_col] == "| B " or BOARD_U[guess_row][guess_col] == "| D " or BOARD_U[guess_row][guess_col] == "| P ":
            BOARD_U[guess_row][guess_col] = "| X "
            ACIERTO.play()
        elif BOARD_C[guess_row][guess_col] == "| X " or BOARD_C[guess_row][guess_col]== "| + ":
            print chr(27)+"[0;91m"+" In this pocicion already placed a boat try again ... "+chr(27)+"[0m"
            hit_user_com(board,boat)
        else:
            BOARD_U[guess_row][guess_col] = "| + "
            DESACIERTO.play()
        clean()
        print "   "
        print "This is the YOU board :::"
        print "   "
        print_board(BOARD_U)
        statistics(BOARD_U)
        raw_input("\npress enter to place ...")
        clean()
        print "este es el tablero de la computadora "
        print "  "
        print_board(BOARD_C_2)
    hit_user(board, boat)


def hit_player_2(board, boat):
    print "Dispara...2 "
    guess_row = enter_row()
    guess_col = enter_col()
    raw_input("\nDisparar...2")
    DISPAROS.play()
    time.sleep(0.4)
    for coor in range(1):
        if BOARD_PLAYER_1[guess_row][guess_col] == "| A " or BOARD_PLAYER_1[guess_row][guess_col] == "| S " or BOARD_PLAYER_1[guess_row][guess_col] == "| B " or BOARD_PLAYER_1[guess_row][guess_col] == "| D " or BOARD_PLAYER_1[guess_row][guess_col] == "| P ":
            BOARD_PLAYER_1[guess_row][guess_col] = "| X "
            ACIERTO.play()
            BOARD_PLAYER_1_A[guess_row][guess_col] = "| X "
            ACIERTO.play()
        elif BOARD_PLAYER_1[guess_row][guess_col] == "| X " or BOARD_PLAYER_1[guess_row][guess_col]== "| + ":
            print chr(27)+"[0;91m"+" In this pocicion already placed a boat try again ... "+chr(27)+"[0m"
            hit_player_1(board, boat)
        else:
            BOARD_PLAYER_1[guess_row][guess_col] = "| + "
            DESACIERTO.play()
            BOARD_PLAYER_1_A[guess_row][guess_col] = "| + "
            DESACIERTO.play()
        clean()
        print "   "
        print "            This is the PLAYER 2 board :::"
        print "   "
        print_board(BOARD_PLAYER_1_A)
        statistics_2(BOARD_PLAYER_1)
        raw_input("\npress enter to place ...")
        clean()
        print "este es el tablero del jugador 2"
        print "  "
        print_board(BOARD_PLAYER_2_A)
    hit_player_2(board, boat)

def hit_player_1(board, boat):
    print "Dispara... 1"
    guess_row=  enter_row()
    guess_col= enter_col()
    raw_input("\nDisparar...1")
    DISPAROS.play()
    time.sleep(0.4)
    for coor in range(1):
        if BOARD_PLAYER_2[guess_row][guess_col] == "| A " or BOARD_PLAYER_2[guess_row][guess_col] == "| S " or BOARD_PLAYER_2[guess_row][guess_col] == "| B " or BOARD_PLAYER_2[guess_row][guess_col] == "| D " or BOARD_PLAYER_2[guess_row][guess_col] == "| P ":
            BOARD_PLAYER_2[guess_row][guess_col] = "| X "
            ACIERTO.play()
            BOARD_PLAYER_2_A[guess_row][guess_col] = "| X "
            ACIERTO.play()
        elif BOARD_PLAYER_2[guess_row][guess_col] == "| X " or BOARD_PLAYER_2[guess_row][guess_col]== "| + ":
            print chr(27)+"[0;91m"+" In this pocicion already placed a boat try again ... "+chr(27)+"[0m"
            hit_player_1(board, boat)
        else:
            BOARD_PLAYER_2[guess_row][guess_col] = "| + "
            DESACIERTO.play()
            BOARD_PLAYER_2_A[guess_row][guess_col] = "| + "
            DESACIERTO.play()
        clean()
        print "   "
        print "            This is the PLAYER 2 board :::"
        print "   "
        print_board(BOARD_PLAYER_2_A)
        statistics_2(BOARD_PLAYER_2)
        raw_input("\npress enter to place ...")
        clean()
        print "este es el tablero del jugador 1"
        print "  "
        print_board(BOARD_PLAYER_1_A)
    hit_player_2(board, boat)

def play_again():
    count = 0
    while count != 10:
        for col in range(9):
            if " A " in BOARD_U[count][col]:
                del BOARD_U[count][col]
            if " B " in BOARD_U[count][col]:
                del BOARD_U[count][col]
            if " D " in BOARD_U[count][col]:
                del BOARD_U[count][col]
            if " S " in BOARD_U[count][col]:
                del BOARD_U[count][col]
            if " P " in BOARD_U[count][col]:
                del BOARD_U[count][col]
            if " A " in BOARD_C[count][col]:
                del BOARD_C[count][col]
            if " B " in BOARD_C[count][col]:
                del BOARD_C[count][col]
            if " D " in BOARD_C[count][col]:
                del BOARD_C[count][col]
            if " S " in BOARD_C[count][col]:
                del BOARD_C[count][col]
            if " P " in BOARD_C[count][col]:
                del BOARD_C[count][col]
            if " A " in BOARD_C_2[count][col]:
                del BOARD_C_2[count][col]
            if " B " in BOARD_C_2[count][col]:
                del BOARD_C_2[count][col]
            if " D " in BOARD_C_2[count][col]:
                del BOARD_C_2[count][col]
            if " S " in BOARD_C_2[count][col]:
                del BOARD_C_2[count][col]
            if " P " in BOARD_C_2[count][col]:
                del BOARD_C_2[count][col]
        count += 1
    print """
   ___ _                                 _                  
  / _ \ | __ _ _   _    __ _  __ _  __ _(_)_ __    _ _ _    
 / /_)/ |/ _` | | | |  / _` |/ _` |/ _` | | '_ \  (_|_|_)   
/ ___/| | (_| | |_| | | (_| | (_| | (_| | | | | |  _ _ _    
\/    |_|\__,_|\__, |  \__,_|\__, |\__,_|_|_| |_| (_|_|_)   
               |___/         |___/                          """
    print "You want to do:   "
    print "presiona - 1 - para juegar de nuevo "
    print "presiona - 2 - para regresar al menu principal"
    BOARD_PLAYER_2_A
    if reply == "1":
        name_user()
    elif reply == "2":
        menu()
    else:
        print chr(27)+"[0;91m"+" * Enter a valid option :   "+chr(27)+"[0m"
        play_again()

def you_lost():
    print """
    ██╗   ██╗ ██████╗ ██╗   ██╗            ██╗      ██████╗ ███████╗████████╗   
    ╚██╗ ██╔╝██╔═══██╗██║   ██║            ██║     ██╔═══██╗██╔════╝╚══██╔══╝   
     ╚████╔╝ ██║   ██║██║   ██║            ██║     ██║   ██║███████╗   ██║      
      ╚██╔╝  ██║   ██║██║   ██║            ██║     ██║   ██║╚════██║   ██║      
       ██║   ╚██████╔╝╚██████╔╝            ███████╗╚██████╔╝███████║   ██║      
       ╚═╝    ╚═════╝  ╚═════╝             ╚══════╝ ╚═════╝ ╚══════╝   ╚═╝      """
    raw_input("\npress enter to continue ...")
    play_again()

def statistics(BOARD_C):
    count = 0
    aircraft = 0
    battleship = 0
    destroyer = 0
    submarine = 0
    patrol = 0
    while count != 10:
        for col in range(10):
            if " A " in BOARD_U[count][col]:
                aircraft += 1
            if " B " in BOARD_U[count][col]:
                battleship += 1
            if " D " in BOARD_U[count][col]:
                destroyer += 1
            if " S " in BOARD_U[count][col]:
                submarine += 1
            if " P " in BOARD_U[count][col]:
                patrol += 1
        count += 1
    print ""
    print ""
    print "    SHIP         boxes      missing boats"
    print "  Aircraft:         5      ", aircraft
    print "  Battleship:       4      ", battleship
    print "  Submarine:        3      ", submarine
    print "  destroyer:        3      ", destroyer
    print "  patrol:           2      ", patrol
    if aircraft == 0 and battleship == 0 and submarine == 0 and destroyer == 0 and patrol == 0:
        you_lost()

def you_win():
    print """
            ___             __    __   _____      __                
    /\_/\  /___\ /\ /\     / / /\ \ \  \_   \  /\ \ \               
    \_ _/ //  /// / \ \    \ \/  \/ /   / /\/ /  \/ /               
     / \ / \_// \ \_/ /     \  /\  / /\/ /_  / /\  /                
     \_/ \___/   \___/       \/  \/  \____/  \_\ \/                 
                                                                    
     _____           _____  __          ___    _              __    
    /__   \  /\  /\  \_   \/ _\        / _ \  /_\    /\/\    /__\   
      / /\/ / /_/ /   / /\/\ \        / /_\/ //_\\  /    \  /_\     
     / /   / __  / /\/ /_  _\ \      / /_\\ /  _  \/ /\/\ \//__     
     \/    \/ /_/  \____/  \__/      \____/ \_/ \_/\/    \/\__/     """
    raw_input("\npress enter to continue ...")
    play_again()

def statistics_c(BOARD_U):
    count = 0
    aircraft = 0
    battleship = 0
    destroyer = 0
    submarine = 0
    patrol = 0
    while count != 10:
        for col in range(10):
            if " A " in BOARD_C[count][col]:
                aircraft += 1
            if " B " in BOARD_C[count][col]:
                battleship += 1
            if " D " in BOARD_C[count][col]:
                destroyer += 1
            if " S " in BOARD_C[count][col]:
                submarine += 1
            if " P " in BOARD_C[count][col]:
                patrol += 1
        count += 1
    print ""
    print ""
    print "    SHIP         boxes      missing boats"
    print "  Aircraft:         5      ", aircraft
    print "  Battleship:       4      ", battleship
    print "  Submarine:        3      ", submarine
    print "  destroyer:        3      ", destroyer
    print "  patrol:           2      ", patrol

    if aircraft == 0 and battleship == 0 and submarine == 0 and destroyer == 0 and patrol == 0:
        you_win()

def statistics_1(BOARD_PLAYER_1):
    count = 0
    aircraft = 0
    battleship = 0
    destroyer = 0
    submarine = 0
    patrol = 0
    while count != 10:
        for col in range(10):
            if " A " in BOARD_PLAYER_2[count][col]:
                aircraft += 1
            if " B " in BOARD_PLAYER_2[count][col]:
                battleship += 1
            if " D " in BOARD_PLAYER_2[count][col]:
                destroyer += 1
            if " S " in BOARD_PLAYER_2[count][col]:
                submarine += 1
            if " P " in BOARD_PLAYER_2[count][col]:
                patrol += 1
        count += 1
    print ""
    print ""
    print "    SHIP         boxes      missing boats"
    print "  Aircraft:         5      ", aircraft
    print "  Battleship:       4      ", battleship
    print "  Submarine:        3      ", submarine
    print "  destroyer:        3      ", destroyer
    print "  patrol:           2      ", patrol
    if aircraft == 0 and battleship == 0 and submarine == 0 and destroyer == 0 and patrol == 0:
        you_lost()

def statistics_2(BOARD_PLAYER_2):
    count = 0
    aircraft = 0
    battleship = 0
    destroyer = 0
    submarine = 0
    patrol = 0
    while count != 10:
        for col in range(10):
            if " A " in BOARD_PLAYER_1[count][col]:
                aircraft += 1
            if " B " in BOARD_PLAYER_1[count][col]:
                battleship += 1
            if " D " in BOARD_PLAYER_1[count][col]:
                destroyer += 1
            if " S " in BOARD_PLAYER_1[count][col]:
                submarine += 1
            if " P " in BOARD_PLAYER_1[count][col]:
                patrol += 1
        count += 1
    print ""
    print ""
    print "    SHIP         boxes      missing boats"
    print "  Aircraft:         5      ", aircraft
    print "  Battleship:       4      ", battleship
    print "  Submarine:        3      ", submarine
    print "  destroyer:        3      ", destroyer
    print "  patrol:           2      ", patrol
    if aircraft == 0 and battleship == 0 and submarine == 0 and destroyer == 0 and patrol == 0:
        you_lost()

def boat_comp_ready():
    print """
            ___                     _          
           / __\ ___   __ _ _ __ __| |         
          /__\/// _ \ / _` | '__/ _` |         
         / \/  \ (_) | (_| | | | (_| |         
         \_____/\___/ \__,_|_|  \__,_|         
                                               
                                          _    
  ___  _ __  _ __   ___  _ __   ___ _ __ | |_  
 / _ \| '_ \| '_ \ / _ \| '_ \ / _ \ '_ \| __| 
| (_) | |_) | |_) | (_) | | | |  __/ | | | |_  
 \___/| .__/| .__/ \___/|_| |_|\___|_| |_|\__| 
      |_|   |_|                                
                             _                 
          _ __ ___  __ _  __| |_   _           
         | '__/ _ \/ _` |/ _` | | | |          
         | | |  __/ (_| | (_| | |_| |  _ _ _   
         |_|  \___|\__,_|\__,_|\__, | (_|_|_)  
                               |___/           """
def boat_comp():
    """Place the user boats  :::"""
    for_def(BOARD_C)
    for_def(BOARD_C_2)
    for boat in SHIPS:
        repeat = False
        while repeat == False:
            print "Where you want to place a  '"+ chr(27)+"[0;95m"+boat+chr(27)+"[0m"+ "'  of  '" +chr(27)+"[0;91m"+str(SHIPS[boat])+chr(27)+"[0m"+ "'   boxes ::: !!..."
            boat_row = defin_row()
            boat_col = defin_col()
            boat_posi = ver_horiz_aleat()
            if boat_posi == "h":
                no_encounter = encounter_h(BOARD_C, SHIPS, boat, boat_row, boat_col)
                if no_encounter != False:
                    ship_Hori = horizon_comp(SHIPS, boat_row, boat_col, boat)
                    horizon_comp(boat_row,boat_col, boat,SHIPS)
                    clean()
                    boat_comp_ready()
                    repeat = True
            elif boat_posi == "v":
                no_encounter2 = encounter_v(BOARD_C, SHIPS, boat, boat_row, boat_col)
                if no_encounter2 != False:
                    ship_vert = vertical_comp(SHIPS, boat_row, boat_col)
                    vertical_comp(boat_row,boat_col, boat)
                    clean() 
                    boat_comp_ready()
                    repeat = True
    raw_input("\npress enter to place ...")
    reset()
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
    clean()
    print "este es el tablero del la pc "
    print """
           ___ _             _                     
          / _ \ | __ _ _   _(_)_ __   __ _         
         / /_)/ |/ _` | | | | | '_ \ / _` |        
        / ___/| | (_| | |_| | | | | | (_| |  _ _ _ 
        \/    |_|\__,_|\__, |_|_| |_|\__, | (_|_|_)
                       |___/         |___/         """
    raw_input("\npress enter to ontinue ...")
    clean()
    print "   "
    print "This is the SYSTEM board :::"
    print "   "
    print_board(BOARD_C_2)
    hit_user(board, boat)
    raw_input("\npress enter to place ...")
    statistics_c(BOARD_U)



def ready():
    clean()
    print"""
       _     _ _                      _         _           
      /_\   | | |  _ __ ___  __ _  __| |_   _  | |_ ___     
     //_\\   | | | | '__/ _ \/ _` |/ _` | | | | | __/ _ \    
    /  _  \ | | | | | |  __/ (_| | (_| | |_| | | || (_) |   
    \_/ \_/ |_|_| |_|  \___|\__,_|\__,_|\__, |  \__\___/    
                                        |___/               
                      _                                     
                _ __ | | __ _ _   _                         
               | '_ \| |/ _` | | | |                        
               | |_) | | (_| | |_| |   _ _ _                
               | .__/|_|\__,_|\__, |  (_|_|_)               
               |_|            |___/                         
                                                            """
    raw_input("\npress enter to place ...")
    clean()
    print "   "
    print_board(BOARD_PLAYER_2_A)
    hit_player_1(board, boat)
    raw_input("\npress enter to place ...")
    statistics_2(BOARD_PLAYER_2)


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

def hori1( c_x, c_y, boat,new):
    """characters placed horizontal boats  :::"""
    try:
         for coor in range(SHIPS[boat]):
            BOARD_PLAYER_1[c_x][c_y + coor] = LETTER[boat]
    except:
        try:
            for coor in range(SHIPS[boat]):
                BOARD_PLAYER_1[c_x + coor][c_y] = "|   "
        except:
            print "coordinate table is out of the ocean"

def vertl1(c_x, c_y, boat):
    """characters placed vertically boats  :::"""
    try:
        for coor in range(SHIPS[boat]):
            BOARD_PLAYER_1[c_x + coor][c_y] = LETTER[boat]
    except:
        try:
            for coor in range(SHIPS[boat]):
                BOARD_PLAYER_1[c_x + coor][c_y] = "|   "
        except:
            print "coordinate table is out of the ocean"

def hori2( c_x, c_y, boat,new):
    """characters placed horizontal boats  :::"""
    try:
         for coor in range(SHIPS[boat]):
            BOARD_PLAYER_2[c_x][c_y + coor] = LETTER[boat]
    except:
        try:
            for coor in range(SHIPS[boat]):
                BOARD_PLAYER_2[c_x + coor][c_y] = "|   "
        except:
            print "coordinate table is out of the ocean"

def vertl2(c_x, c_y, boat):
    """characters placed vertically boats  :::"""
    try:
        for coor in range(SHIPS[boat]):
            BOARD_PLAYER_2[c_x + coor][c_y] = LETTER[boat]
    except:
        try:
            for coor in range(SHIPS[boat]):
                BOARD_PLAYER_2[c_x + coor][c_y] = "|   "
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
    print"    "
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
    clean()
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
    time.sleep(0.5)

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
    MENU.play().set_volume(0.1)
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
                wel_multiplayer()
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
    print chr(27)+"[0;91m"+"""
             Now you must position your ships do it
the strategic way you think it will be difficult to be sunk"""+chr(27)+"[0m"
    raw_input("\nPress Enter to continue ...")
    reset()
    boat_user()

def wel_multiplayer():
    print"""
                  _ _   _       _                           
      /\/\  _   _| | |_(_)_ __ | | __ _ _   _  ___ _ __     
     /    \| | | | | __| | '_ \| |/ _` | | | |/ _ \ '__|    
    / /\/\ \ |_| | | |_| | |_) | | (_| | |_| |  __/ |       
    \/    \/\__,_|_|\__|_| .__/|_|\__,_|\__, |\___|_|       
                         |_|            |___/               
          ___       _   _   _           _     _             
         / __\ __ _| |_| |_| | ___  ___| |__ (_)_ __        
        /__\/// _` | __| __| |/ _ \/ __| '_ \| | '_ \       
       / \/  \ (_| | |_| |_| |  __/\__ \ | | | | |_) |      
       \_____/\__,_|\__|\__|_|\___||___/_| |_|_| .__/       
                                               |_|          
                                                            """
    raw_input("          Press Enter to continue ...")
    reset()
    boat_player_1()


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
    MENU.play(-1)
repeat_bar()
