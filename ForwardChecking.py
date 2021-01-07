import basicboard as bb
from basicboard import valid,find_empty
from time import time
import sys

pos_vals = [[[] for _ in range(9)] for _ in range(9)]
def pos_vals_init(board):
    for row in range(9):
        for col in range(9):
            for i in range(1,10):
                if valid(board,i,(row,col)):
                    pos_vals[row][col].append(i)


def solve_FC(board):
    find = find_empty(board)
    if not find:
        return True
    else:
        row,col = find[0],find[1]
    for i in pos_vals[row][col]:
        if valid(board,i,find):
            board[row][col] = i
            if solve_FC(board):
                return True
            board[row][col] = 0
    return False
    
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
    pos_vals_init(sudoku)
    ct = time()
    solve_FC(sudoku)
    et = time()
    bb.print_board(sudoku)
    print("Time taken = ", (et - ct))

    
    
