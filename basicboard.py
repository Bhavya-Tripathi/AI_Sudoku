from random import randint
import time

board = [
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
] 

#Sample Easy Board. Solves really quick
sample_board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

# Medium board. Not as quick as easy but fast nonetheless
medium_board = [
    [3,0,0,4,0,0,0,0,2],
    [0,5,1,0,0,7,0,9,0],
    [0,0,9,0,0,0,8,3,0],
    [0,9,0,7,0,8,0,0,5],
    [0,0,0,0,0,0,0,0,0],
    [8,0,0,2,0,4,0,6,0],
    [0,4,2,0,0,0,1,0,0],
    [0,7,0,1,0,0,3,2,0],
    [5,0,0,0,0,6,0,0,9]
]
#Tough board. Takes basic backtracking around 45+ seconds. It is processing, just takes some time
hard_board = [
    [0,6,1,0,0,7,0,0,3],
    [0,9,2,0,0,3,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,8,5,3,0,0,0,0],
    [0,0,0,0,0,0,5,0,4],
    [5,0,0,0,0,8,0,0,0],
    [0,4,0,0,0,0,0,0,1],
    [0,0,0,1,6,0,8,0,0],
    [6,0,0,0,0,0,0,0,0]
]

#Function that finds the first "empty" cell, and returns its row and column position. Takes the board as argument
def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo)):
            if bo[i][j] == 0:
                return i, j, range(1, 10)  # row, col, numbers from 1-9
    return None


#Function to print the board all fancy way. Takes the board as argument
def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")
        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")


#Function that checks the validity of placing the given num (number) at given pos (position, a tuple(row, col)). Board also as argument.
def valid(bo, num, pos):
    # Check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False
    # Check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False
    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False
    return True

#Function generates new board from the given board. Just replaces the numbers throughout. The postions of 0's remains the same.
def gen_new(bo):
    replace = [0]
    new_board = board
    while len(replace) != 10:
        num = randint(1,9)
        if num not in replace:
            replace.append(num)
    for i in range(9):
        for j in range(9):
            new_board[i][j] = replace[bo[i][j]]
        # print(" ")  
    return new_board

        
# Uncomment the following lines to get a new board every time
# sample_board = gen_new(sample_board)
medium_board = gen_new(medium_board)
# hard_board = gen_new(hard_board)

