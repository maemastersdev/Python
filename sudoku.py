from pprint import pprint


def find_next_empty(puzzle):
    # finds the next row, col on the puzzle thats not filled yet --> rep with -1
    # reurn row, col tuple (or (none, none) if there is none)

    #keep in mind that we are using 0-8 for our indices
    for r in range(9):
        for c in range(9): # range(9) is 0,1,2,...8
            if puzzle[r][c]== -1:
                return r,c

    return None, None

def is_valid(puzzle, guess, row, col):
    # figures out whether the guess at row/col of the puzzle is a valid guess
    # returns True if it is valid, False otherwise

    # lets start with the row:
    row_vals = puzzle[row]
    if guess in row_vals:
        return False

    # now the columns
    col_vals = []
    for i in range(9):
        col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False

    # and then the square which is more challenging
    # want t know where the 3x3 square starts
    # and iterate over the 3 values in the row/column
    row_start = (row//3) * 3 #1//3=0 5//3=1 ...
    col_start = (col//3) * 3

    for r in range(row_start, row_start+3):
        for c in range(col_start, col_start+3):
            if puzzle[r][c] == guess:
                return False

    return True

def solve_sudoku(puzzle):
    # solve sudoku using a backtracking technique
    # our puzzle is a list of lists, where each inner list is a row in our sudoku puzzle
    # return whether a solution exists
    # mutates puzzle to be the solution (if a solution exists)

    # step 1: choose somewhere on the puzzle to make a guess
    row, col = find_next_empty(puzzle)

    # step 1.1: if there's nowhere left, then we're done because we only allow valid inputs
    if row is None:
        return True

    # step 2: if there is a place to put a number, then make a guess between 1 and 9
    for guess in range(1, 10): # range(1,10) is 1,2,3,...
    # step 3: check if this is a valid guess
        if is_valid(puzzle, guess, row, col):
            # step 3.1: if this is a valig guess, then place it at that spot on the puzzle
            puzzle[row][col] = guess
            # step 4: then we recursively call our solver
            if solve_sudoku(puzzle):
                return True

    # step 5: if not valid or if nothing gets returned true, then we need to backtrack and try a new number
        puzzle[row][col] = -1 #reset the guess

    # step 6: if none of the numbers tat we try work, unsolvable!

if __name__ == '__main__':
    example_board = [
        [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
        [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
        [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

        [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
        [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

        [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [6, 7, -1,   1, -1, 5,   -1, 4, -1],
        [1, -1, 9,   -1, -1, -1,   2, -1, -1]
    ]
    print(solve_sudoku(example_board))
    pprint(example_board)
