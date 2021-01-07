import time as t
import math,sys
from Backtracking import solve
import basicboard as bb
from basicboard import valid, find_empty

def mrv_domains(sudoku):
    domains_dict = {}
    # domains dictionary of the form (row, col):{set of domains}
    # domains for all empty cells initialised to {1,2....9}
    for i in range(len(sudoku)):
        for j in range(len(sudoku)):
            if sudoku[i][j] == 0:
                domains_dict[i, j] = set(range(1, 10))

    for i in range(len(sudoku)):
        for j in range(len(sudoku)):
            # if type(sudoku[i][j]) is not set:
                qs = range(3)
                block_i = int(i / 3)
                block_i_set = {block_i * 3 + q for q in qs}
                block_j = int(j / 3)
                block_j_set = {block_j * 3 + q for q in qs}
                # discarding those values from the domain that are already present in the same row, column or block
                for k in domains_dict.keys():
                    # Are in same row
                    # or
                    # in same column
                    # or
                    # in same block
                    if k[0] == i or k[1] == j or (k[0] in block_i_set and k[1] in block_j_set):
                        if sudoku[i][j] in domains_dict[k]:
                            domains_dict[k].discard(sudoku[i][j])

    # finding the value with the minimum domain length
    min_remaining_val = None
    for domain in domains_dict.values():
        if min_remaining_val is not None:
            min_remaining_val = min(min_remaining_val, len(domain))
        else:
            min_remaining_val = len(domain)
    
    # Sudoku can't be solved
    if min_remaining_val == 0:
        if find_empty(sudoku):
            return -1
        return None
    min_domains = {k: domains_dict[k]
                   for k in domains_dict.keys()
                   if len(domains_dict[k]) == min_remaining_val}
    return min_domains


def var_selector(sudoku):
    min_domains = mrv_domains(sudoku)
    if not min_domains:
        return None
    if min_domains == -1:
        return -1
    var = min_domains.popitem()
    # returns row, column, domain
    return var[0][0], var[0][1], var[1]


def search(sudoku):
    return solve(sudoku, var_selector)

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
    ct = t.time()
    search(sudoku)
    et = t.time()
    bb.print_board(sudoku)
    print("Time taken = ", (et - ct))


