#Author: Vasanta and Gift Christian
#Date: 10/03/2023, updated on 02/01/2024, updated again on 17/10/2025
#(added new testing code)
# Course: CS 1 - Introduction to Programming and Computation-02 By Professor Balkcom
#Purpose: N-queens validation problem solution. Also checks for valid queen placements using if statements and looping over the board.

from cs1lib import *
from random import randint

WIN_SIZE = 500
N = 4
CELL_SIZE = WIN_SIZE // N
first = True
end = False
board_lol = []

#Create NxN board with empty cells (all cells are false)
def initialize_empty_board():
    i = 0
    while i < N:
        board_lol.append([])
        j = 0
        while j < N:
            board_lol[i].append(False)
            j = j + 1

        i = i + 1


#Capture mouse location and find the cell and flip
#the true-false flag

def my_mpress(mx, my):
    col = mx // CELL_SIZE
    row = my // CELL_SIZE

    board_lol[row][col] = not board_lol[row][col]

# The function that takes a list of lists
# representation of the board
# and draw the chessboard. It draws placed
# queens as red circles.

def draw_board(glol, n):
    # clear background
    set_clear_color(1, 1, 1)
    clear()

    if len(glol) != n:
        print("Wrong outer list length", n)
        return
    sqr_width = WIN_SIZE // n
    i = 0
    while i < n:
        if len(glol[i]) != n:
            print("Wrong inner list length")
            return
        j = 0
        while j < n:
            if (j+i) % 2 == 0:
                set_fill_color(1, 1, 1)
            else:
                set_fill_color(0.5, 0.5, 0.5)

            sqr_x = i * sqr_width
            sqr_y = j * sqr_width
            draw_rectangle(sqr_y, sqr_x, sqr_width, sqr_width)

            #Check if that cell has a queen and draw a
            #circle in red.
            if glol[i][j] == True:
                set_fill_color(0.9, 0, 0)
                draw_circle(sqr_y+sqr_width//2, sqr_x+sqr_width//2, sqr_width//10)


                # print(sqr_y+sqr_width//2, sqr_x+sqr_width//2, sqr_width//10)
                # print(board_lol)

            j = j +1
        i = i + 1

# This function takes a list of lists representing
# the N*N chessboard with N queens placed randomly on
# board and returns True if no two queens
# attach each other. Otherwise, it returns False.


def my_mpress(mx, my):
    col = mx // CELL_SIZE
    row = my // CELL_SIZE

    board_lol[row][col] = not board_lol[row][col]


# Checkers for rows, columns and diagonals
# Row checker
def row_checker(glol):
    for row in range(0, len(glol)):         # Iterate through each list in the list of lists
        count = 0                           # Initialize count of queens in the row
        for col in range(len(glol[row])):   # Iterate through each element in the row
            if glol[row][col]:              # If there is a queen in that cell
                count += 1                  # Increment the count
        if count >= 2:                      # If more than 1 queen found in the inner list
            return False                    # If more than 1 queen found in the inner list, return False
    return True                             # If no rows have more than 1 queen, return True

# Column checker
def column_checker(glol):                   
    num_cols = len(glol[0])
    for col in range(num_cols):             # Iterate through each column index
        count = 0                           # Initialize count of queens in the column
        for row in range(len(glol)):        # Iterate through each list in the list of lists
            if glol[row][col]:              # If there is a queen in that cell
                count += 1                  # Increment the count
        if count >= 2:                      # If more than 1 queen found in the column
            return False                    # If more than 1 queen found in the column, return False
    return True                             # If no columns have more than 1 queen, return True

# Backslash diagonal checker
def backslash_diagonal_checker(glol):                       
    for row_1 in range(len(glol)):                                                  # Iterate through each list in the list of lists
        for col_1 in range(len(glol[row_1])):                                       # Iterate through each element in the row
            if glol[row_1][col_1]:                                                  # If there is a queen in that cell
                for row_2 in range(row_1 + 1, len(glol)):                           # Iterate through each subsequent list (i+1) in the list of lists
                    for col_2 in range(len(glol[row_2])):                           # Iterate through each element in the subsequent list
                        if glol[row_2][col_2] and (row_1 - col_1 == row_2 - col_2): # If there is a queen in that cell and the difference between row and column indices is the same
                             return False                                            # If so, return False 
    return True                                                                     # If no conflicts found, return True 


# Forwardslash diagonal checker
def forwardslash_diagonal_checker(glol):                                            
    for row_1 in range(len(glol)):                                                      # Iterate through each list in the list of lists
        for col_1 in range(len(glol[row_1])):                                           # Iterate through each element in the row
            if glol[row_1][col_1]:                                                      # If there is a queen in that cell
                for row_2 in range(row_1 + 1, len(glol)):                               # Iterate through each subsequent list (i+1) in the list of lists
                    for col_2 in range(len(glol[row_2])):                               # Iterate through each element in the subsequent list
                        if glol[row_2][col_2] and (row_1 + col_1 == row_2 + col_2):     # If there is a queen in that cell and the sum of row and column indices is the same
                            return False                                                # If so, return False
    return True                                                                         # If no conflicts found, return True 

# Overall board checker
def check_board(glol):
    if row_checker(glol) == False:                          # Check rows first
        return False                                        # If row check fails, return False
    elif column_checker(glol) == False:                     # Then check columns
        return False
    elif backslash_diagonal_checker(glol) == False:         # Then check backslash diagonals
        return False
    elif forwardslash_diagonal_checker(glol) == False:      # Then check forwardslash diagonals
        return False
    else:                                                   # If all checks pass
        return True                                         # Return True


#Main draw function
def my_draw():
    global first, end
    if first:
        set_clear_color(1, 1, 1)
        clear()
        first = False

    check = check_board(board_lol)
    end = not check # end is true when check_board returns False

    draw_board(board_lol, N)
    if end:
        # clear()
        # set_clear_color(1, 1, 1)
        draw_board(board_lol, N)
        set_font_size(50)
        draw_text("The End", 150, 250)


initialize_empty_board()
start_graphics(my_draw, width=WIN_SIZE, height=WIN_SIZE, mouse_press=my_mpress)
