"""this is play Battle Ship"""
import random

board = []

for x in range(0,5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)

print "Let's play Battle Ship!!!  "
print_board(board)

def row_random(board):
    return random.randint(0,len(board)-1)

def column_random(board):
    return random.randint(0,len(board[0])-1)

ship_row = row_random(board)
ship_col = column_random(board)
print ship_row
print ship_col


# From now on everything should be in your loop!
# Be sure to indent!
for turn in range(4):
    guess_row = input("Guess row:")
    guess_column = input("Guess column:")

    if guess_row == ship_row and guess_column == ship_col:
        print "Congratulations! Hundiste my ship"
        break
    else:
        if (guess_row < 0 or guess_row > 4) or (guess_column < 0         or guess_column > 4):
            print "Wow, this is not even in the ocean."
        elif(board[guess_row][guess_column] == "X"):
            print "You already said that."
        else:
            print "No impactaste my ship!"
            board[guess_row][guess_column] = "X"
        if turn == 3:
            print "game over"
    # Displays (turn + 1) here!
        print turn + 1
