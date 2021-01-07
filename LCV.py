import time as t
import math
from Backtracking import solve
import basicboard as bb
from basicboard import valid, find_empty
import sys

neighbours = {}

def find_domains(sudoku):
    domains_dict = {}
    # domains dictionary of the form (row, col):{set of domains}
    # domains for all empty cells initialised to {1,2....9}
    for i in range(len(sudoku)):
        for j in range(len(sudoku)):
            neighbours[i,j] = []
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
                        neighbours[k].append((i,j))
                        if sudoku[i][j] in domains_dict[k]:
                            domains_dict[k].discard(sudoku[i][j])
    return domains_dict
def mrv_domains(sudoku):
    
    domains_dict = find_domains(sudoku)
    # finding the value with the minimum domain length
    min_remaining_val = None;
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
    # print(min_domains)
    return min_domains


def var_selector(sudoku):
    min_domains = mrv_domains(sudoku)
    if not min_domains:
        return None
    if min_domains == -1:
        return -1
    var = min_domains.popitem()
    # USING LCV
    domain = order_domain_values(sudoku, (var[0][0], var[0][1]))
    # returns row, column, domain
    return var[0][0], var[0][1], domain


def conflicts(sudoku, var, val):
    count = 0
    row, col = var
    domains_dict = find_domains(sudoku)
    for i in neighbours[var]:
        if i in domains_dict.keys():
            if len(domains_dict[i]) > 1 and val in domains_dict[i]:
                count +=1
    return count
def order_domain_values(sudoku, var):
    domains_dict = find_domains(sudoku)
    if len(domains_dict[var]) == 1:
        return domains_dict[var]

    return sorted(domains_dict[var], key=lambda val: conflicts(sudoku, var, val))

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
