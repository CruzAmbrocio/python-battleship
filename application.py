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

class battleship(object):
    """Class name"""
    def __init__(self):
        self.board = []
        self.BOARD_U = []

        self.BOARD_C = []
        self.BOARD_C_2 = []

        self.BOARD_PLAYER_1 = []
        self.BOARD_PLAYER_1_A = []

        self.BOARD_PLAYER_2 = []
        self.BOARD_PLAYER_2_A = []

        self.SHIPS = {   "Aircraft Carrier" : 5,
                    "Battleship" : 4,
                    "Submarine" : 3,
                    "Destroyer" : 3,
                    "Patrol Boat" : 2}

        self.LETTER = {   "Aircraft Carrier" : "| A ",
                     "Battleship" : "| B ",
                     "Submarine" : "| S ",
                     "Destroyer" : "| D ",
                     "Patrol Boat" : "| P "}

        self.WELCOME = pygame.mixer.Sound("WELCOME.wav")
        self.LOADING = pygame.mixer.Sound("LOADING.wav")
        self.SINGLE = pygame.mixer.Sound("SINGLE.wav")
        self.MULTIPLAYER = pygame.mixer.Sound("MULTIPLAYER.wav")
        self.MENU = pygame.mixer.Sound("MENU.wav")
        self.ACIERTO = pygame.mixer.Sound("ACIERTO.wav")
        self.DESACIERTO = pygame.mixer.Sound("DISPAGUA.wav")
        self.DISPAROS = pygame.mixer.Sound("DISPAROS.wav")
        self.GAMEOVER = pygame.mixer.Sound("GAMEOVER.wav")

    def for_def(self,board):
        """Define measures the board  :::"""
        for x in range(0,10):
            board.append(["|   "] * 10)
        self.print_board(board)

    def print_board(self,board):
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

    def enter_row(self):
        """Check the row value entered by the user  :::"""
        while (True):
            guess_row = raw_input(chr(27) + "[0;94m" + "Enter the row:   " + chr(27) + "[0m")
            if guess_row == "exit":
                self.clean()
                self.menu()
                break
            else:
                try:
                    guess_row = int(guess_row)
                    if guess_row >=1 and guess_row <=10:
                        guess_row -=1
                        return guess_row
                        break
                    else:
                        print chr(27) + "[0;91m" + "This coordinate does not exist in the ocean  "\
                        + chr(27) + "[0m"
                except ValueError:
                    print chr(27) + "[0;91m" + "Input coordinates in a range of 1 to 10   "\
                    + chr(27) + "[0m"

    def enter_col(self):
        """Check the column value entered by the user  :::"""
        while (True):
            guess_col = raw_input(chr(27) + "[0;94m" + "Enter the column:   " + chr(27) + "[0m")
            if guess_col == "exit":
                self.clean()
                self.menu()
                break
            else:
                try:
                    guess_col = int(guess_col)
                    if guess_col >=1 and guess_col <=10:
                        guess_col -=1
                        return guess_col
                        break
                    else:
                        print "[0;91m" + "This coordinate does not exist in the ocean   " + chr(27)+"[0m"
                except ValueError:
                    print chr(27) + "[0;91m" + "Input coordinates in a range of 1 to 10   " + chr(27)+"[0m"

    def place_user(self):
        print chr(27) + "[0;96m" + """
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
                                                            
                                                            """ + chr(27) + "[0m"

    def boat_user(self):
        """Place the user boats  :::"""
        self.place_user()
        self.for_def(self.BOARD_U)
        for boat in self.SHIPS:
            repeat = False
            while repeat == False:
                print "Where you want to place a  '" + chr(27) + "[0;95m" + boat + chr(27) + "[0m" +\
                "'  of  '" + chr(27) + "[0;91m" + str(self.SHIPS[boat]) + chr(27) + "[0m" + "'   boxes!!..."
                boat_row = self.enter_row()
                boat_col = self.enter_col()
                boat_posi = self.ver_horiz()
                if boat_posi == "h":
                    no_encounter = self.encounter_h(self.BOARD_U, self.SHIPS, boat, boat_row, boat_col)
                    if no_encounter != False:
                        ship_Hori = self.hori(self.SHIPS, boat_row, boat_col, boat)
                        self.hori(boat_row,boat_col, boat,self.SHIPS)
                        self.clean()
                        self.place_user()
                        self.print_board(self.BOARD_U)
                        repeat = True
                elif boat_posi == "v":
                    no_encounter2 = self.encounter_v(self.BOARD_U, self.SHIPS, boat, boat_row, boat_col)
                    if no_encounter2 != False:
                        ship_vert = self.vertl(self.SHIPS, boat_row, boat_col)
                        self.vertl(boat_row,boat_col, boat)
                        self.clean()
                        self.place_user()
                        self.print_board(self.BOARD_U)
                        repeat = True
        print chr(27) + "[0;96m" + "                         Already positioned your ships" + chr(27) + "[0m"
        print "   "
        print chr(27) + "[0;96m" + "------ It is time that the program position your ships to compertir with you -------" + chr(27) + "[0m"
        raw_input(chr(27) + "[0;95m" + "\n<<<<< Press enter to continue ...   >>>>>" + chr(27) + "[0m")
        self.boat_comp()

    def boat_player_1(self):
        """Place the Player 1 boats in multiplayer :::"""
        self.clean()
        self.for_def(self.BOARD_PLAYER_1_A)
        self.clean()
        self.place_user()
        print chr(27)+"[0;96m" + """      Player 1 puts your ships 
    °°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
                                                        """+chr(27)+"[0m"
        self.for_def(self.BOARD_PLAYER_1)
        for boat in self.SHIPS:
            repeat = False
            while repeat == False:
                print "Where you want to place a  '"+ chr(27)+"[0;95m"+boat+chr(27)+"[0m"+ "'  of  '" +chr(27)+"[0;91m"+str(self.SHIPS[boat])+chr(27)+"[0m"+ "'   boxes ::: !!..."
                boat_row = self.enter_row()
                boat_col = self.enter_col()
                boat_posi = self.ver_horiz()
                if boat_posi == "h":
                    no_encounter = self.encounter_h(self.BOARD_PLAYER_1, self.SHIPS, boat, boat_row, boat_col)
                    if no_encounter != False:
                        ship_Hori = self.hori1(self.SHIPS, boat_row, boat_col, boat)
                        self.hori1(boat_row,boat_col, boat,self.SHIPS)
                        self.clean()
                        self.place_user()
                        print chr(27)+"[0;96m" + """      Player 1 puts your ships 
    °°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
                                                                        """+chr(27)+"[0m"
                        self.print_board(self.BOARD_PLAYER_1)
                        repeat = True
                elif boat_posi == "v":
                    no_encounter2 = self.encounter_v(self.BOARD_PLAYER_1, self.SHIPS, boat, boat_row, boat_col)
                    if no_encounter2 != False:
                        ship_vert = self.vertl1(self.SHIPS, boat_row, boat_col)
                        self.vertl1(boat_row,boat_col, boat)
                        self.clean()
                        self.place_user()
                        print chr(27)+"[0;96m" + """      Player 1 puts your ships 
    °°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
                                                                        """+chr(27)+"[0m"
                        self.print_board(self.BOARD_PLAYER_1)
                        repeat = True
        print chr(27) + "[0;96m" + "                         Already positioned your ships" + chr(27) + "[0m"
        print "   "
        print chr(27) + "[0;92m" + "It is time that your competitor position your boat so you can compete with you ...." + chr(27) + "[0m"
        raw_input("\n<<<<< Press enter to continue ...   >>>>>")
        self.clean()
        self.boat_player_2()

    def boat_player_2(self):
        """Place the Player 2 boats in multiplayer :::"""
        self.clean()
        self.for_def(self.BOARD_PLAYER_2_A)
        self.clean()
        self.place_user()
        print chr(27)+"[0;93m" + """      Player 2 puts your ships 
    °°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
                                                        """+chr(27)+"[0m"
        self.for_def(self.BOARD_PLAYER_2)
        for boat in self.SHIPS:
            repeat = False
            while repeat == False:
                print "Where you want to place a  '"+ chr(27)+"[0;95m"+boat+chr(27)+"[0m"+ "'  of  '" +chr(27)+"[0;91m"+str(self.SHIPS[boat])+chr(27)+"[0m"+ "'   boxes ::: !!..."
                boat_row = self.enter_row()
                boat_col = self.enter_col()
                boat_posi = self.ver_horiz()
                if boat_posi == "h":
                    no_encounter = self.encounter_h(self.BOARD_PLAYER_2, self.SHIPS, boat, boat_row, boat_col)
                    if no_encounter != False:
                        ship_Hori = self.hori2(self.SHIPS, boat_row, boat_col, boat)
                        self.hori2(boat_row,boat_col, boat,self.SHIPS)
                        self.clean()
                        self.place_user()
                        print chr(27)+"[0;93m" + """      Player 2 puts your ships 
    °°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
                                                                        """+chr(27)+"[0m"
                        self.print_board(self.BOARD_PLAYER_2)
                        repeat = True
                elif boat_posi == "v":
                    no_encounter2 = self.encounter_v(self.BOARD_PLAYER_2, self.SHIPS, boat, boat_row, boat_col)
                    if no_encounter2 != False:
                        ship_vert = self.vertl2(self.SHIPS, boat_row, boat_col)
                        self.vertl2(boat_row,boat_col, boat)
                        self.clean()
                        self.place_user()
                        print chr(27)+"[0;93m" + """      Player 2 puts your ships 
    °°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
                                                                        """+chr(27)+"[0m"
                        self.print_board(self.BOARD_PLAYER_2)
                        repeat = True
        print chr(27) + "[0;96m" + "                         Already positioned your ships" + chr(27) + "[0m"
        print "   "
        raw_input("\n<<<<< Press enter to continue ...   >>>>>")
        self.clean()
        print "   "
        print chr(27)+"[0;93m" + "<<<<< This is the PLAYER 2 board ::: >>>>>"+chr(27)+"[0m"
        print "   "
        self.print_board(self.BOARD_PLAYER_2_A)
        self.hit_player_1(self.board, boat)
        raw_input("\n<<<<< Press enter to place ...   >>>>>")
        self.statistics_c(self.BOARD_U)

    def defin_row(self):
        """Check the row value entered by the system   :::"""
        while (True):
            try:
                ship_row = self.random_row()
                print ship_row
                if ship_row >=1 and ship_row <=10:
                    ship_row -=1
                    return ship_row
                    break
                else:
                    print "   "
            except ValueError:
                print "   "

    def defin_col(self):
        """Check the column value entered by the system   :::"""
        while (True):
            try:
                ship_col = self.random_col()
                print ship_col
                if ship_col >=1 and ship_col <=10:
                    ship_col -=1
                    return ship_col
                    break
                else:
                    print "   "
            except ValueError:
                print"   "

    def random_row(self):
        """create a random number to the system"""
        return random.randint(0,9)

    def random_col(self):
        """create a random number to the system"""
        return random.randint(0,9)

    def hit_user(self,board, boat):
        """Here is done and valid User shooting"""
        print chr(27) + "[0;96m" + "Enter the coordinates where you want to shoot ....  " + chr(27) + "[0m"
        guess_row = self.enter_row()
        guess_col = self.enter_col()
        raw_input(chr(27) + "[0;93m" + "\nShoot ...." + chr(27) + "[0m")
        self.DISPAROS.play()
        time.sleep(0.4)
        for coor in range(1):
            if self.BOARD_C[guess_row][guess_col] == "| A " or self.BOARD_C[guess_row][guess_col] == "| S " or self.BOARD_C[guess_row][guess_col] == "| B " or self.BOARD_C[guess_row][guess_col] == "| D " or self.BOARD_C[guess_row][guess_col] == "| P ":
                self.BOARD_C[guess_row][guess_col] = "| X "
                self.ACIERTO.play()
                self.BOARD_C_2[guess_row][guess_col] = "| X "
                self.ACIERTO.play()
            elif self.BOARD_C[guess_row][guess_col] == "| X ":
                print chr(27) + "[0;91m" + " In this pocicion already placed a boat try again ....    " + chr(27) + "[0m"
                self.hit_user(board,boat)
            elif self.BOARD_C[guess_row][guess_col] == "| + ":
                print chr(27) + "[0;91m" + " You've shot in these coordinates....   " + chr(27) + "[0m"
                self.hit_user(board,boat)
            else:
                self.BOARD_C[guess_row][guess_col] = "| + "
                self.DESACIERTO.play()
                self.BOARD_C_2[guess_row][guess_col] = "| + "
                self.DESACIERTO.play()
            self.clean()
            print "   "
            print chr(27) + "[0;92m" + "            This is the SYSTEM board :::" + chr(27) + "[0m"
            print "   "
            self.print_board(self.BOARD_C_2)
            self.statistics_c(self.BOARD_C)
            raw_input(chr(27) + "[0;95m" + "\n<<<<< Press enter to continue ...   >>>>>" + chr(27) + "[0m")
            self.clean()
            print chr(27) + "[0;96m" + "            This is the YOU board :::" + chr(27) + "[0m"
            print "  "
            self.print_board(self.BOARD_U)
        self.hit_user_com(board, boat)

    def hit_user_com(self,board, boat):
        raw_input(chr(27) + "[0;93m" + "\nShoot ...." + chr(27) + "[0m")
        guess_row = self.random_row()
        guess_col = self.random_col()
        self.DISPAROS.play()
        time.sleep(0.4)
        for coor in range(1):
            if self.BOARD_U[guess_row][guess_col] == "| A " or self.BOARD_U[guess_row][guess_col] == "| S " or self.BOARD_U[guess_row][guess_col] == "| B " or self.BOARD_U[guess_row][guess_col] == "| D " or self.BOARD_U[guess_row][guess_col] == "| P ":
                self.BOARD_U[guess_row][guess_col] = "| X "
                self.ACIERTO.play()
            elif self.BOARD_C[guess_row][guess_col] == "| X " or self.BOARD_C[guess_row][guess_col]== "| + ":
                self.hit_user_com(board,boat)
            else:
                self.BOARD_U[guess_row][guess_col] = "| + "
                self.DESACIERTO.play()
            self.clean()
            print "   "
            print chr(27) + "[0;96m" + "            This is the YOU board :::" + chr(27) + "[0m"
            print "   "
            self.print_board(self.BOARD_U)
            self.statistics(self.BOARD_U)
            raw_input(chr(27) + "[0;95m" + "\n<<<<< Press enter to continue ...   >>>>>" + chr(27) + "[0m")
            self.clean()
            print chr(27) + "[0;92m" + "            This is the SYSTEM board :::" + chr(27) + "[0m"
            print "  "
            self.print_board(self.BOARD_C_2)
        self.hit_user(board, boat)

    def hit_player_2(self,board, boat):
        print "Enter the coordinates where you want to shoot ....  "
        print "   "
        print "   "
        print chr(27) + "[0;93m" + "PLAYER 2 shooting :::" + chr(27) + "[0m"
        guess_row = self.enter_row()
        guess_col = self.enter_col()
        raw_input(chr(27) + "[0;93m" + "\nShoot ...." + chr(27) + "[0m")
        self.DISPAROS.play()
        time.sleep(0.4)
        for coor in range(1):
            if self.BOARD_PLAYER_1[guess_row][guess_col] == "| A " or self.BOARD_PLAYER_1[guess_row][guess_col] == "| S " or self.BOARD_PLAYER_1[guess_row][guess_col] == "| B " or self.BOARD_PLAYER_1[guess_row][guess_col] == "| D " or self.BOARD_PLAYER_1[guess_row][guess_col] == "| P ":
                self.BOARD_PLAYER_1[guess_row][guess_col] = "| X "
                self.ACIERTO.play()
                self.BOARD_PLAYER_1_A[guess_row][guess_col] = "| X "
                self.ACIERTO.play()
            elif self.BOARD_PLAYER_1[guess_row][guess_col] == "| X " or self.BOARD_PLAYER_1[guess_row][guess_col]== "| + ":
                print chr(27)+"[0;91m"+" In this pocicion already placed a boat try again ... "+chr(27)+"[0m"
                self.hit_player_1(board, boat)
            else:
                self.BOARD_PLAYER_1[guess_row][guess_col] = "| + "
                self.DESACIERTO.play()
                self.BOARD_PLAYER_1_A[guess_row][guess_col] = "| + "
                self.DESACIERTO.play()
            self.clean()
            print "   "
            print chr(27) + "[0;96m" + "            This is the PLAYER 1 board :::" + chr(27) + "[0m"
            print "   "
            self.print_board(self.BOARD_PLAYER_1_A)
            self.statistics_2(self.BOARD_PLAYER_2)
            raw_input(chr(27) + "[0;95m" + "\n<<<<< Press enter to continue ...   >>>>>" + chr(27) + "[0m")
            self.clean()
            print chr(27) + "[0;93m" + "            This is the PLAYER 2 board :::" + chr(27) + "[0m"
            print "  "
            self.print_board(self.BOARD_PLAYER_2_A)
            self.hit_player_1(board, boat)

    def hit_player_1(self,board, boat):
        """Here the shooting player 1 are made and validated"""
        print "Enter the coordinates where you want to shoot ....  "
        print "   "
        print "   "
        print chr(27) + "[0;96m" + "PLAYER 1 shooting :::" + chr(27) + "[0m"
        guess_row= self.enter_row()
        guess_col= self.enter_col()
        raw_input(chr(27) + "[0;96m" + "\nShoot ...." + chr(27) + "[0m")
        self.DISPAROS.play()
        time.sleep(0.4)
        for coor in range(1):
            if self.BOARD_PLAYER_2[guess_row][guess_col] == "| A " or self.BOARD_PLAYER_2[guess_row][guess_col] == "| S " or self.BOARD_PLAYER_2[guess_row][guess_col] == "| B " or self.BOARD_PLAYER_2[guess_row][guess_col] == "| D " or self.BOARD_PLAYER_2[guess_row][guess_col] == "| P ":
                self.BOARD_PLAYER_2[guess_row][guess_col] = "| X "
                self.ACIERTO.play()
                self.BOARD_PLAYER_2_A[guess_row][guess_col] = "| X "
                self.ACIERTO.play()
            elif self.BOARD_PLAYER_2[guess_row][guess_col] == "| X ":
                print chr(27)+"[0;91m"+" In this pocicion already placed a boat try again ... "+chr(27)+"[0m"
            elif self.BOARD_PLAYER_2[guess_row][guess_col] == "| + ":
                print chr(27) + "[0;91m" + " You've shot in these coordinates....   " + chr(27) + "[0m"
                self.hit_player_1(board, boat)
            else:
                self.BOARD_PLAYER_2[guess_row][guess_col] = "| + "
                self.DESACIERTO.play()
                self.BOARD_PLAYER_2_A[guess_row][guess_col] = "| + "
                self.DESACIERTO.play()
            self.clean()
            print "   "
            print chr(27) + "[0;93m" + "            This is the PLAYER 2 board :::" + chr(27) + "[0m"
            print "   "
            self.print_board(self.BOARD_PLAYER_2_A)
            self.statistics_1(self.BOARD_PLAYER_1)
            raw_input(chr(27) + "[0;95m" + "\n<<<<< Press enter to continue ...   >>>>>" + chr(27) + "[0m")
            self.clean()
            print chr(27) + "[0;96m" + "            This is the PLAYER 2 board :::" + chr(27) + "[0m"
            print "  "
            self.print_board(self.BOARD_PLAYER_1_A)
        self.hit_player_2(board, boat)


    def clean_board(self):
        """This function clears the boards"""
        self.board = []
        self.BOARD_U = []

        self.BOARD_C = []
        self.BOARD_C_2 = []

        self.BOARD_PLAYER_1 = []
        self.BOARD_PLAYER_1_A = []

        self.BOARD_PLAYER_2 = []
        self.BOARD_PLAYER_2_A = []

    def play_again(self):
        self.clean_board()
        self.clean()
        print """
       ___ _                                 _                  
      / _ \ | __ _ _   _    __ _  __ _  __ _(_)_ __    _ _ _    
     / /_)/ |/ _` | | | |  / _` |/ _` |/ _` | | '_ \  (_|_|_)   
    / ___/| | (_| | |_| | | (_| | (_| | (_| | | | | |  _ _ _    
    \/    |_|\__,_|\__, |  \__,_|\__, |\__,_|_|_| |_| (_|_|_)   
                   |___/         |___/                          """
        print "You want to do:   "
        print "presiona - 1 - para juegar silgle player"
        print "presiona - 2 - para jugar multiplayer"
        print "presiona - 3 - para regresar al menu principal"
        try:
            reply = int(raw_input("Choose an option:  "))
            if reply == 1:
                self.name_user()
            elif reply == 2:
                self.wel_multiplayer()
            elif reply == 3:
                self.menu()
            elif chooseopt <= 0:
                print chr(27)+"[0;91m"+" * Enter a valid option :   "+chr(27)+"[0m"
            elif chooseopt > 3:
                print chr(27)+"[0;91m"+" * Enter a valid option :   "+chr(27)+"[0m"
        except ValueError:
            print chr(27)+"[0;91m"+" * Enter a valid option :   "+chr(27)+"[0m"
            self.play_again()

    def you_lost(self):
        """game over printed message"""
        self.GAMEOVER.play()
        print """
        ██╗   ██╗ ██████╗ ██╗   ██╗            ██╗      ██████╗ ███████╗████████╗   
        ╚██╗ ██╔╝██╔═══██╗██║   ██║            ██║     ██╔═══██╗██╔════╝╚══██╔══╝   
         ╚████╔╝ ██║   ██║██║   ██║            ██║     ██║   ██║███████╗   ██║      
          ╚██╔╝  ██║   ██║██║   ██║            ██║     ██║   ██║╚════██║   ██║      
           ██║   ╚██████╔╝╚██████╔╝            ███████╗╚██████╔╝███████║   ██║      
           ╚═╝    ╚═════╝  ╚═════╝             ╚══════╝ ╚═════╝ ╚══════╝   ╚═╝      

                 ██████╗  █████╗ ███╗   ███╗███████╗           
                ██╔════╝ ██╔══██╗████╗ ████║██╔════╝           
                ██║  ███╗███████║██╔████╔██║█████╗             
                ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝             
                ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗           
                 ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝           
                                                               
                 ██████╗ ██╗   ██╗███████╗██████╗              
                ██╔═══██╗██║   ██║██╔════╝██╔══██╗             
                ██║   ██║██║   ██║█████╗  ██████╔╝             
                ██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗             
                ╚██████╔╝ ╚████╔╝ ███████╗██║  ██║    ██╗██╗██╗
                 ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝    ╚═╝╚═╝╚═╝
                                                               
                                                               """
        raw_input(chr(27) + "[0;95m" + "\n<<<<< Press enter to continue ...   >>>>>" + chr(27) + "[0m")
        self.clean()
        self.play_again()

    def statistics(self,BOARD_C):
        """computer prints statistics"""
        count = 0
        aircraft = 0
        battleship = 0
        destroyer = 0
        submarine = 0
        patrol = 0
        while count != 10:
            for col in range(10):
                if " A " in self.BOARD_U[count][col]:
                    aircraft += 1
                if " B " in self.BOARD_U[count][col]:
                    battleship += 1
                if " D " in self.BOARD_U[count][col]:
                    destroyer += 1
                if " S " in self.BOARD_U[count][col]:
                    submarine += 1
                if " P " in self.BOARD_U[count][col]:
                    patrol += 1
            count += 1
        print ""
        print ""
        print "    SHIP         boxes      missing boats"
        print "  Aircraft:         5      " + chr(27) + "[0;91m" + str(aircraft) + chr(27) + "[0m"
        print "  Battleship:       4      " + chr(27) + "[0;91m" + str(battleship) + chr(27) + "[0m"
        print "  Submarine:        3      " + chr(27) + "[0;91m" + str(submarine) + chr(27) + "[0m"
        print "  destroyer:        3      " + chr(27) + "[0;91m" + str(destroyer) + chr(27) + "[0m"
        print "  patrol:           2      " + chr(27) + "[0;91m" + str(patrol) + chr(27) + "[0m"
        if aircraft == 0 and battleship == 0 and submarine == 0 and destroyer == 0 and patrol == 0:
            self.GAMEOVER.play()
            self.you_lost()

    def you_win(self):
        """prints the message that the user won"""
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
        raw_input(chr(27) + "[0;95m" + "\n<<<<< Press enter to continue ...   >>>>>" + chr(27) + "[0m")
        self.clean()
        self.play_again()

    def statistics_c(self,BOARD_U):
        """computer prints statistics"""
        count = 0
        aircraft = 0
        battleship = 0
        destroyer = 0
        submarine = 0
        patrol = 0
        while count != 10:
            for col in range(10):
                if " A " in self.BOARD_C[count][col]:
                    aircraft += 1
                if " B " in self.BOARD_C[count][col]:
                    battleship += 1
                if " D " in self.BOARD_C[count][col]:
                    destroyer += 1
                if " S " in self.BOARD_C[count][col]:
                    submarine += 1
                if " P " in self.BOARD_C[count][col]:
                    patrol += 1
            count += 1
        print ""
        print ""
        print "    SHIP         boxes      missing boats"
        print "  Aircraft:         5      " + chr(27) + "[0;91m" + str(aircraft) + chr(27) + "[0m"
        print "  Battleship:       4      " + chr(27) + "[0;91m" + str(battleship) + chr(27) + "[0m"
        print "  Submarine:        3      " + chr(27) + "[0;91m" + str(submarine) + chr(27) + "[0m"
        print "  destroyer:        3      " + chr(27) + "[0;91m" + str(destroyer) + chr(27) + "[0m"
        print "  patrol:           2      " + chr(27) + "[0;91m" + str(patrol) + chr(27) + "[0m"

        if aircraft == 0 and battleship == 0 and submarine == 0 and destroyer == 0 and patrol == 0:
            self.you_win()

    def statistics_1(self,BOARD_PLAYER_1):
        """Prints statistics for player 1"""
        count = 0
        aircraft = 0
        battleship = 0
        destroyer = 0
        submarine = 0
        patrol = 0
        while count != 10:
            for col in range(10):
                if " A " in self.BOARD_PLAYER_2[count][col]:
                    aircraft += 1
                if " B " in self.BOARD_PLAYER_2[count][col]:
                    battleship += 1
                if " D " in self.BOARD_PLAYER_2[count][col]:
                    destroyer += 1
                if " S " in self.BOARD_PLAYER_2[count][col]:
                    submarine += 1
                if " P " in self.BOARD_PLAYER_2[count][col]:
                    patrol += 1
            count += 1
        print ""
        print ""
        print "    SHIP         boxes      missing boats"
        print "  Aircraft:         5      " + chr(27) + "[0;91m" + str(aircraft) + chr(27) + "[0m"
        print "  Battleship:       4      " + chr(27) + "[0;91m" + str(battleship) + chr(27) + "[0m"
        print "  Submarine:        3      " + chr(27) + "[0;91m" + str(submarine) + chr(27) + "[0m"
        print "  destroyer:        3      " + chr(27) + "[0;91m" + str(destroyer) + chr(27) + "[0m"
        print "  patrol:           2      " + chr(27) + "[0;91m" + str(patrol) + chr(27) + "[0m"
        if aircraft == 0 and battleship == 0 and submarine == 0 and destroyer == 0 and patrol == 0:
            print """
    ██████╗ ██╗      █████╗ ██╗   ██╗███████╗██████╗     ██████╗    
    ██╔══██╗██║     ██╔══██╗╚██╗ ██╔╝██╔════╝██╔══██╗    ╚════██╗   
    ██████╔╝██║     ███████║ ╚████╔╝ █████╗  ██████╔╝     █████╔╝   
    ██╔═══╝ ██║     ██╔══██║  ╚██╔╝  ██╔══╝  ██╔══██╗    ██╔═══╝    
    ██║     ███████╗██║  ██║   ██║   ███████╗██║  ██║    ███████╗   
    ╚═╝     ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝    ╚══════╝   
                                                                    
                ██╗    ██╗██╗███╗   ██╗███████╗                     
                ██║    ██║██║████╗  ██║██╔════╝                     
                ██║ █╗ ██║██║██╔██╗ ██║███████╗                     
                ██║███╗██║██║██║╚██╗██║╚════██║                     
                ╚███╔███╔╝██║██║ ╚████║███████║                     
                 ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝╚══════╝                     """
            raw_input(chr(27) + "[0;95m" + "\n<<<<< Press enter to continue ...   >>>>>" + chr(27) + "[0m")
            self.clean()
            self.play_again()

    def statistics_2(self,BOARD_PLAYER_2):
        """Prints statistics for player 2"""
        count = 0
        aircraft = 0
        battleship = 0
        destroyer = 0
        submarine = 0
        patrol = 0
        while count != 10:
            for col in range(10):
                if " A " in self.BOARD_PLAYER_1[count][col]:
                    aircraft += 1
                if " B " in self.BOARD_PLAYER_1[count][col]:
                    battleship += 1
                if " D " in self.BOARD_PLAYER_1[count][col]:
                    destroyer += 1
                if " S " in self.BOARD_PLAYER_1[count][col]:
                    submarine += 1
                if " P " in self.BOARD_PLAYER_1[count][col]:
                    patrol += 1
            count += 1
        print ""
        print ""
        print "    SHIP         boxes      missing boats"
        print "  Aircraft:         5      " + chr(27) + "[0;91m" + str(aircraft) + chr(27) + "[0m"
        print "  Battleship:       4      " + chr(27) + "[0;91m" + str(battleship) + chr(27) + "[0m"
        print "  Submarine:        3      " + chr(27) + "[0;91m" + str(submarine) + chr(27) + "[0m"
        print "  destroyer:        3      " + chr(27) + "[0;91m" + str(destroyer) + chr(27) + "[0m"
        print "  patrol:           2      " + chr(27) + "[0;91m" + str(patrol) + chr(27) + "[0m"
        if aircraft == 0 and battleship == 0 and submarine == 0 and destroyer == 0 and patrol == 0:
            print """
    ██████╗ ██╗      █████╗ ██╗   ██╗███████╗██████╗      ██╗   
    ██╔══██╗██║     ██╔══██╗╚██╗ ██╔╝██╔════╝██╔══██╗    ███║   
    ██████╔╝██║     ███████║ ╚████╔╝ █████╗  ██████╔╝    ╚██║   
    ██╔═══╝ ██║     ██╔══██║  ╚██╔╝  ██╔══╝  ██╔══██╗     ██║   
    ██║     ███████╗██║  ██║   ██║   ███████╗██║  ██║     ██║   
    ╚═╝     ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝     ╚═╝   
                                                                
                ██╗    ██╗██╗███╗   ██╗███████╗                 
                ██║    ██║██║████╗  ██║██╔════╝                 
                ██║ █╗ ██║██║██╔██╗ ██║███████╗                 
                ██║███╗██║██║██║╚██╗██║╚════██║                 
                ╚███╔███╔╝██║██║ ╚████║███████║                 
                 ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝╚══════╝                 """
            raw_input(chr(27) + "[0;95m" + "\n<<<<< Press enter to continue ...   >>>>>" + chr(27) + "[0m")
            self.clean()
            self.play_again()

    def boat_comp_ready(self):
        """ print message that the computer positioned its boats """
        print chr(27) + "[0;92m" + """
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
                                   |___/           """+ chr(27) + "[0m"

    def boat_comp(self):
        """Place the user boats  :::"""
        self.for_def(self.BOARD_C)
        self.for_def(self.BOARD_C_2)
        for boat in self.SHIPS:
            repeat = False
            while repeat == False:
                print "Where you want to place a  '" + chr(27) + "[0;95m" + boat + chr(27) + "[0m" + "'  of  '" +chr(27)+"[0;91m"+str(self.SHIPS[boat])+chr(27)+"[0m"+ "'   boxes ::: !!..."
                boat_row = self.defin_row()
                boat_col = self.defin_col()
                boat_posi = self.ver_horiz_aleat()
                if boat_posi == "h":
                    no_encounter = self.encounter_h(self.BOARD_C, self.SHIPS, boat, boat_row, boat_col)
                    if no_encounter != False:
                        ship_Hori = self.horizon_comp(self.SHIPS, boat_row, boat_col, boat)
                        self.horizon_comp(boat_row,boat_col, boat,self.SHIPS)
                        self.clean()
                        self.boat_comp_ready()
                        repeat = True
                elif boat_posi == "v":
                    no_encounter2 = self.encounter_v(self.BOARD_C, self.SHIPS, boat, boat_row, boat_col)
                    if no_encounter2 != False:
                        ship_vert = self.vertical_comp(self.SHIPS, boat_row, boat_col)
                        self.vertical_comp(boat_row,boat_col, boat)
                        self.clean() 
                        self.boat_comp_ready()
                        repeat = True
        raw_input(chr(27) + "[0;95m" + "\n<<<<< Press enter to continue ...   >>>>>" + chr(27) + "[0m")
        self.reset()
        print chr(27) + "[0;93m" + """
         __ _                 _   _                         
        / _\ |__   ___   ___ | |_(_)_ __   __ _   _ _ _     
        \ \| '_ \ / _ \ / _ \| __| | '_ \ / _` | (_|_|_)    
        _\ \ | | | (_) | (_) | |_| | | | | (_| |  _ _ _     
        \__/_| |_|\___/ \___/ \__|_|_| |_|\__, | (_|_|_)    
                                          |___/             

               ___ _             _                          
              / _ \ | __ _ _   _(_)_ __   __ _              
             / /_)/ |/ _` | | | | | '_ \ / _` |             
            / ___/| | (_| | |_| | | | | | (_| |  _ _ _      
            \/    |_|\__,_|\__, |_|_| |_|\__, | (_|_|_)     
                           |___/         |___/              

                                                                """ + chr(27) + "[0m"
        raw_input(chr(27) + "[0;95m" + "\n<<<<< Press enter to continue ...   >>>>>" + chr(27) + "[0m")
        self.clean()
        print "   "
        print chr(27) + "[0;92m" + "            This is the SYSTEM board :::" + chr(27) + "[0m"
        print "   "
        self.print_board(self.BOARD_C_2)
        self.hit_user(self.board, boat)
        raw_input(chr(27) + "[0;95m" + "\n<<<<< Press enter to continue ...   >>>>>" + chr(27) + "[0m")
        self.statistics_c(self.BOARD_U)

    def ready(self):
        """printed message all ready to play"""
        self.clean()
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
        raw_input(chr(27) + "[0;95m" + "\n<<<<< Press enter to continue ...   >>>>>" + chr(27) + "[0m")
        self.clean()
        print "   "
        self.print_board(self.BOARD_PLAYER_2_A)
        self.hit_player_1(board, boat)
        raw_input(chr(27) + "[0;95m" + "\n<<<<< Press enter to continue ...   >>>>>" + chr(27) + "[0m")
        self.statistics_2(self.BOARD_PLAYER_2)


    def horizon_comp(self,c_x, c_y, boat,new):
        """characters placed horizontally boats  :::"""
        try:
            for coor in range(self.SHIPS[boat]):
                self.BOARD_C[c_x][c_y + coor] = self.LETTER[boat]
        except:
            try:
                for coor in range(self.SHIPS[boat]):
                    self.BOARD_C[c_x][c_y + coor] = "|   "
            except:
                print chr(27) + "[0;9m" + "\n<<<<< coordinate table is out of the ocean   >>>>>" + chr(27) + "[0m"

    def vertical_comp(self,c_x, c_y, boat):
        """characters placed vertically boats  :::"""
        try:
            for coor in range(self.SHIPS[boat]):
                self.BOARD_C[c_x + coor][c_y] = self.LETTER[boat]
        except:
            try:
                for coor in range(self.SHIPS[boat]):
                    self.BOARD_C[c_x + coor][c_y] = "|   "
            except:
                print chr(27) + "[0;9m" + "\n<<<<< coordinate table is out of the ocean   >>>>>" + chr(27) + "[0m"

    def ver_horiz_aleat(self):
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
                print chr(27) + "[0;9m" + "\n<<<<< Enter valid characters   >>>>>" + chr(27) + "[0m"

    def encounter_v(self,board, new, boat, c_x, c_y):
        count = 0 
        try:
            for thing in range(new[boat]):
                if "|   " in board[c_x + thing][c_y]:
                    count += 1 
        except: 
            print chr(27) + "[0;9m" + "\n<<<<< There is already a boat here insert new coordinates   >>>>>" + chr(27) + "[0m"
            return False
        if count == new[boat]: 
            return True
        else: 
            print chr(27) + "[0;9m" + "\n<<<<< There is already a boat here insert new coordinates   >>>>>" + chr(27) + "[0m"
            return False 

    def encounter_h(self,board,new, boat, c_x, c_y):
        count = 0
        try:
            for thing in range(new[boat]):
                if "|   " in board[c_x][c_y + thing]:
                    count += 1 
        except: 
            print chr(27) + "[0;9m" + "\n<<<<< There is already a boat here insert new coordinates   >>>>>" + chr(27) + "[0m"
            return False
        if count == new[boat]: 
            return True
        else: 
            print chr(27) + "[0;9m" + "\n<<<<< There is already a boat here insert new coordinates   >>>>>" + chr(27) + "[0m"
            return False 

    def hori(self,c_x, c_y, boat,new):
        """characters placed horizontal boats  :::"""
        try:
             for coor in range(self.SHIPS[boat]):
                self.BOARD_U[c_x][c_y + coor] = self.LETTER[boat]
        except:
            try:
                for coor in range(self.SHIPS[boat]):
                    self.BOARD_U[c_x + coor][c_y] = "|   "
            except:
                print chr(27) + "[0;9m" + "\n<<<<< coordinate table is out of the ocean   >>>>>" + chr(27) + "[0m"

    def vertl(self,c_x, c_y, boat):
        """characters placed vertically boats  :::"""
        try:
            for coor in range(self.SHIPS[boat]):
                self.BOARD_U[c_x + coor][c_y] = self.LETTER[boat]
        except:
            try:
                for coor in range(self.SHIPS[boat]):
                    self.BOARD_U[c_x + coor][c_y] = "|   "
            except:
                print chr(27) + "[0;9m" + "\n<<<<< coordinate table is out of the ocean   >>>>>" + chr(27) + "[0m"

    def hori1(self,c_x, c_y, boat,new):
        """characters placed horizontal boats  :::"""
        try:
             for coor in range(self.SHIPS[boat]):
                self.BOARD_PLAYER_1[c_x][c_y + coor] = self.LETTER[boat]
        except:
            try:
                for coor in range(self.SHIPS[boat]):
                    self.BOARD_PLAYER_1[c_x + coor][c_y] = "|   "
            except:
                print "coordinate table is out of the ocean"

    def vertl1(self,c_x, c_y, boat):
        """characters placed vertically boats  :::"""
        try:
            for coor in range(self.SHIPS[boat]):
                self.BOARD_PLAYER_1[c_x + coor][c_y] = self.LETTER[boat]
        except:
            try:
                for coor in range(self.SHIPS[boat]):
                    self.BOARD_PLAYER_1[c_x + coor][c_y] = "|   "
            except:
                print "coordinate table is out of the ocean"

    def hori2(self,c_x, c_y, boat,new):
        """characters placed horizontal boats  :::"""
        try:
             for coor in range(self.SHIPS[boat]):
                self.BOARD_PLAYER_2[c_x][c_y + coor] =self.LETTER[boat]
        except:
            try:
                for coor in range(self.SHIPS[boat]):
                    self.BOARD_PLAYER_2[c_x + coor][c_y] = "|   "
            except:
                print "coordinate table is out of the ocean"

    def vertl2(self,c_x, c_y, boat):
        """characters placed vertically boats  :::"""
        try:
            for coor in range(self.SHIPS[boat]):
                self.BOARD_PLAYER_2[c_x + coor][c_y] = self.LETTER[boat]
        except:
            try:
                for coor in range(self.SHIPS[boat]):
                    self.BOARD_PLAYER_2[c_x + coor][c_y] = "|   "
            except:
                print "coordinate table is out of the ocean"

    def ver_horiz(self ):
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
            print chr(27) + "[0;9m" + "\n<<<<< Enter valid characters v/h   >>>>>" + chr(27) + "[0m"

    def clean(self):
        """Used to clean the screen"""
        os.system ("clear")


    def reset(self):
        """Used to reset the screen"""
        os.system ("reset")


    def exit(self):
        self.clean()
        print chr(27)+"[5;96m"+"""
         ☻ /     
        /█      
        / \     
        Bye ::: ...
            """+chr(27)+"[0m"
        time.sleep(2)
        self.reset()
        sys.exit(1)

    def initial(self):
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
        time.sleep(0.8)

    def instructions(self):
        """This is the game instructions"""
        self.clean()
        print chr(27) + "[0;94m" + """
                 <<<< Battlehip >>>>                                    
     was adapted to a single console view.                              
             The game is in two forms:                                  
    Single Player:                                                      
                                                                        
    You must compete with the program.                                  
    'You must place your ships so that the                              
          program will be difficult to sink your bracos                 
    You must choose your coordinates in "X" and "Y"                     
         numbers 1-10 choosing                                          
         the orientation of your ships                                  
    -The Program randomly placed their boats                            
    -The Game takes a turn to you and other program                     
    -To Do shoot you must insert numbers                                
         coordinates correspond to                                      
         "X" and "Y" which is where you go to shoot                     
    -The Program makes his shot randomly trying to                      
         find your ships                                                
    -In Each shift statistics will be shown in the                      
         the amount shown                                               
         of boxes that occupies the boat and you                        
          You have given a shot.                                        
    You're wasting gave you to give without ships:                      """ + chr(27) + "[0m"

        print"""                 -Ready:                                """
        raw_input(chr(27) + "[0;95m" + "\n<<<<< Press enter to continue ...   >>>>>" + chr(27) + "[0m")
        self.clean()
        print chr(27) + "[0;94m" + """
                    Multiplayer:                                        

    -In This mode will require two players                              
          where they compete with each other:                           
    Each player must place your ships so                                
         that his opponent is you                                       
          difficult to sink the ships of another                        
    They must choose the coordinates "X" and "Y"                        
         numbers 1-10 choosing                                          
          orientation of their boats
    -The Program gives a turn to another player 1 and player 2          
    -To Shoot when they touch turn players                              
         should add two numbers that correspond                         
      to the coordinates "X" and "Y" indicating an                      
          place on board where your shot is going.                      
    -In Each shift statistics will be shown in                          
         where the number of squares shown                              
          occupying the ship and you have given a shot.                 
    You're wasting your stay there first without boats:                 """ + chr(27) + "[0m"
        print"""                 -Ready:                                """
        print chr(27) + "[0;96m" + "Press - 1 - to go to the main menu :::   " + chr(27) + "[0m"
        options = raw_input(chr(27) + "[0;96m" + "Choose an options:  " + chr(27) + "[0m")
        if options == "1":
            self.clean()
            self.menu()
        else:
            self.clean()
            print chr(27) + "[0;91m"+"  <<< * Enter a valid option 4: >>>   " + chr(27)+"[0m"
            self.instructions()

    def by(self):
        """about the game"""
        self.clean()
        print """

     ██████╗██████╗ ███████╗ █████╗ ████████╗███████╗██████╗     ██████╗ ██╗   ██╗          
    ██╔════╝██╔══██╗██╔════╝██╔══██╗╚══██╔══╝██╔════╝██╔══██╗    ██╔══██╗╚██╗ ██╔╝██╗       
    ██║     ██████╔╝█████╗  ███████║   ██║   █████╗  ██║  ██║    ██████╔╝ ╚████╔╝ ╚═╝       
    ██║     ██╔══██╗██╔══╝  ██╔══██║   ██║   ██╔══╝  ██║  ██║    ██╔══██╗  ╚██╔╝  ██╗       
    ╚██████╗██║  ██║███████╗██║  ██║   ██║   ███████╗██████╔╝    ██████╔╝   ██║   ╚═╝       
     ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═════╝     ╚═════╝    ╚═╝             
                                                                                            
                             ██████╗██████╗ ██╗   ██╗███████╗                               
                            ██╔════╝██╔══██╗██║   ██║╚══███╔╝                               
                            ██║     ██████╔╝██║   ██║  ███╔╝                                
                            ██║     ██╔══██╗██║   ██║ ███╔╝                                 
                            ╚██████╗██║  ██║╚██████╔╝███████╗                               
                             ╚═════╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝                               
                                                                                            
             █████╗ ███╗   ███╗██████╗ ██████╗  ██████╗  ██████╗██╗ ██████╗                 
            ██╔══██╗████╗ ████║██╔══██╗██╔══██╗██╔═══██╗██╔════╝██║██╔═══██╗                
            ███████║██╔████╔██║██████╔╝██████╔╝██║   ██║██║     ██║██║   ██║                
            ██╔══██║██║╚██╔╝██║██╔══██╗██╔══██╗██║   ██║██║     ██║██║   ██║                
            ██║  ██║██║ ╚═╝ ██║██████╔╝██║  ██║╚██████╔╝╚██████╗██║╚██████╔╝                
            ╚═╝  ╚═╝╚═╝     ╚═╝╚═════╝ ╚═╝  ╚═╝ ╚═════╝  ╚═════╝╚═╝ ╚═════╝                 
              ___          _     _     _              _      _                              
             | _ )  __ _  | |_  | |_  | |  ___   ___ | |_   (_)  _ __    ™                  
             | _ \ / _` | |  _| |  _| | | / -_) (_-< | ' \  | | | '_ \                      
             |___/ \__,_|  \__|  \__| |_| \___| /__/ |_||_| |_| | .__/                      
                                                                |_|                         
                                                                                            """ 
        raw_input(chr(27) + "[0;95m" + "\n<<<<< Press enter to continue ...   >>>>>" + chr(27) + "[0m")
        self.reset()
        self.menu()

    def find(self,option):
        dic_menu = {"1": self.name_user,  "2": self.wel_multiplayer, "3": self.instructions, "4": self.by, "5": self.exit}
        count = 0
        if option in dic_menu:
            self.clean()
            return dic_menu[option]
        else:
            print ""
            print chr(27)+"[0;91m"+" * Enter a valid option 3:   "+chr(27)+"[0m"
            print ""
            self.clean()
            self.MENU.stop()
            return self.menu

    def menu(self):
        self.LOADING.stop()
        self.MENU.play()
        self.clean_board()
        reply = False
        while reply == False:
            print """
               /\/\   ___ _ __  _   _                   
     _____    /    \ / _ \ '_ \| | | |          _____   
    |_____|  / /\/\ \  __/ | | | |_| |  _ _ _  |_____|  
             \/    \/\___|_| |_|\__,_| (_|_|_)          
                                                        

            principal menu"""
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
            option = raw_input(" Choose an option::: ")
            reply = self.find(option)
            reply()
            break

    def name_user(self):
        """This is a user name """
        self.clean()
        self.MENU.stop()
        self.SINGLE.play(15)
        print """
               ___       _   _   _           _     _      ™   
              / __\ __ _| |_| |_| | ___  ___| |__ (_)_ __     
             /__\/// _` | __| __| |/ _ \/ __| '_ \| | '_ \    
            / \/  \ (_| | |_| |_| |  __/\__ \ | | | | |_) |   
            \_____/\__,_|\__|\__|_|\___||___/_| |_|_| .__/    
                                                    |_|       
                                                              """
        name = raw_input("             What its your name ?   ")
        self.reset()
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
        raw_input(chr(27) + "[0;95m" + "\n<<<<< Press enter to continue ...   >>>>>" + chr(27) + "[0m")
        self.reset()
        self.boat_user()

    def wel_multiplayer(self):
        self.clean()
        self.MENU.stop()
        self.MULTIPLAYER.play(25)
        print chr(27) + "[0;91m" + """
                      _ _   _       _                           
          /\/\  _   _| | |_(_)_ __ | | __ _ _   _  ___ _ __     
         /    \| | | | | __| | '_ \| |/ _` | | | |/ _ \ '__|    
        / /\/\ \ |_| | | |_| | |_) | | (_| | |_| |  __/ |       
        \/    \/\__,_|_|\__|_| .__/|_|\__,_|\__, |\___|_|       
                             |_|            |___/               
              ___       _   _   _           _     _             
             / __\ __ _| |_| |_| | ___  ___| |__ (_)_ __    ™   
            /__\/// _` | __| __| |/ _ \/ __| '_ \| | '_ \       
           / \/  \ (_| | |_| |_| |  __/\__ \ | | | | |_) |      
           \_____/\__,_|\__|\__|_|\___||___/_| |_|_| .__/       
                                                   |_|          
                                                                """  + chr(27) + "[0m"
        raw_input(chr(27) + "[0;95m" + "\n<<<<< Press enter to continue ...   >>>>>" + chr(27) + "[0m")
        self.reset()
        self.boat_player_1()

    def welcome(self):
        """This is the first image of the game"""
        self.WELCOME.play()
        self.clean()
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
                ::::::::::::::::888:::|:::8888:::::::::::::::           
                `:::::::::::::::88888888888888::::::::::::::'           
                 :::::::::::::::88888888888888::::::::::::::            
                  ::::::::::::::88888888888888:::::::::::::             
                   :::::::::::::88::88::88::88::::::::::::              
                    `:::::::::::88::88::88::88::::::::::'               
                      `:::::::::88::88::88::88::::::::'                 
                        `:::::::88::88::88::88::::::'                   
          ___          _     _     _              _      _              
         | _ )  __ _  | |_  | |_  | |  ___   ___ | |_   (_)  _ __  ™    
         | _ \ / _` | |  _| |  _| | | / -_) (_-< | ' \  | | | '_ \      
         |___/ \__,_|  \__|  \__| |_| \___| /__/ |_||_| |_| | .__/      
                                                            |_|         """
        time.sleep(2)

    def repeat_bar(self):
        """This is the bar to load the game"""
        self.LOADING.play()
        self.clean()
        print"    "
        print"    "
        print """
    |    _  _. _|*._  _ 
    |___(_)(_](_]|[ )(_]
                     ._|""" + chr(27) + "[0;91m" + " "
        print "   "
        print "█" * 5
        self.initial()
        self.clean()
        print"    "
        print"    "
        print """
    |    _  _. _|*._  _ 
    |___(_)(_](_]|[ )(_]
                     ._|""" + chr(27) + "[0;91m" + "☠"
        print "   "
        print "█" * 10
        self.initial()
        self.clean()
        print"    "
        print"    "
        print """
    |    _  _. _|*._  _ 
    |___(_)(_](_]|[ )(_]
                     ._|""" + chr(27) + "[0;92m" + "☠ ☠"
        print "   "
        print "█" * 15
        self.initial()
        self.clean()
        print"    "
        print"    "
        print """
    |    _  _. _|*._  _ 
    |___(_)(_](_]|[ )(_]
                     ._|""" + chr(27) + "[0;93m" + "☠ ☠ ☠"
        print "   "
        print "█" * 20
        self.initial()
        self.clean()
        print"    "
        print"    "
        print """
    |    _  _. _|*._  _ 
    |___(_)(_](_]|[ )(_]
                     ._|""" + chr(27) + "[0;91m" + " "
        print "   "
        print "█" * 25
        self.initial()
        self.clean()
        print"    "
        print"    "
        print """
    |    _  _. _|*._  _ 
    |___(_)(_](_]|[ )(_]
                     ._|""" + chr(27) + "[0;96m" + "☠"
        print "   "
        print "█"*30
        self.initial()
        self.clean()
        print"    "
        print"    "
        print """
    |    _  _. _|*._  _ 
    |___(_)(_](_]|[ )(_]
                     ._|""" + chr(27) + "[0;95m" + "☠ ☠"
        print "   "
        print "█"*35
        self.initial()
        self.clean()
        print"    "
        print"    "
        print """
    |    _  _. _|*._  _ 
    |___(_)(_](_]|[ )(_]
                     ._|""" + chr(27) + "[0;96m" + "☠ ☠ ☠"
        print "   "
        print "█" * 40
        self.initial()
        self.clean()
        print"    "
        print"    "
        print """
    |    _  _. _|*._  _ 
    |___(_)(_](_]|[ )(_]
                     ._|""" + chr(27) + "[0;91m" + " "
        print "   "
        print "█" * 45
        self.initial()
        self.clean()
        print"    "
        print"    "
        print """
    |    _  _. _|*._  _ 
    |___(_)(_](_]|[ )(_]
                     ._|""" + chr(27) + "[0;97m" + "☠"
        print "   "
        print "█" * 50
        self.initial()
        self.clean()
        print"    "
        print"    "
        print """
    |    _  _. _|*._  _ 
    |___(_)(_](_]|[ )(_]
                     ._|""" + chr(27) + "[0;92m" + "☠ ☠"
        print "   "
        print "█" * 55
        self.initial()
        self.clean()
        print"    "
        print"    "
        print """
    |    _  _. _|*._  _ 
    |___(_)(_](_]|[ )(_]
                     ._|""" + chr(27) + "[0;94m" + "☠ ☠ ☠"
        print "   "
        print "█" * 60  + chr(27) + "[0m"
        self.initial()
        self.clean()
        self.menu()

    def init(self):
        self.clean()
        self.welcome()
        self.repeat_bar()
        self.menu()

play = battleship()
play.init()