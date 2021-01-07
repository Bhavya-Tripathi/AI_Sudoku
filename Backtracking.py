import basicboard as bb
from basicboard import valid,find_empty
from time import time
import sys

#Function that recursively solves the board
def solve(bo, var_selector):
    find = var_selector(bo) #Find empty cell
    # If the value was wrong
    if find == -1:
        return False
    if not find:
        return True #No empty cell means whole board is filled
    else:
        row, col, domain = find
        for i in domain: #Check each number from 1-9
            if valid(bo, i, (row, col)): #Check for validity
                bo[row][col] = i #Assign if valid, and recursively call it again.
                if solve(bo, var_selector):
                    # bb.print_board(bo)
                    return True
                bo[row][col] = 0 #if it doesn't solve, go back and assign another value.
    return False
# driver code
if __name__ == "__main__":
    
    if len(sys.argv) < 2:
        print("Defaulting to easy board")
        sudoku = bb.sample_board
    elif str(sys.argv[1]) == 'easy':
        sudoku = bb.sample_board
    elif str(sys.argv[1]) == 'medium':
        sudoku = bb.medium_board
    elif str(sys.argv[1]) == 'hard':
        sudoku = bb.hard_board   

    print("Solving this board")
    bb.print_board(sudoku)
    print("\n_________________________\n")
    ct = time()
    solve(sudoku, find_empty)
    et = time()
    bb.print_board(sudoku)
    print("Time taken = ", (et - ct))
