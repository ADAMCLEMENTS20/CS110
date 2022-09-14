#----------------------------------------------------------------------------------
# Author:
#   ___             _              _
#  | . \ ___  ___ _| |_ ___  _ _ _| |_
#  | | |/ . \<_-<  | | / ._>| '_> | |
#  |___/\___//__/  |_| \___.|_|   |_|
#
# Summary: This function takes in a two dimensional tic-tac-toe board.
#   The board is assumed to be square (it is not tested). This then prints
#   the current state of the board, where a 1 is an "X", a -1 is an "O" and
#   a zero is not owned. The board locations are labeled by a 1 to size*size
#
#  For example, a 4x4 empty board would be displayed as:
#    1  |   2  |   3  |   4
# ----------------------------
#    5  |   6  |   7  |   8
# ----------------------------
#    9  |  10  |  11  |  12
# ----------------------------
#   13  |  14  |  15  |  16
#
#  While a 3x3 board with some occupied locations would be:
#    X  |   X  |   3
# ---------------------
#    4  |   O  |   O
# ---------------------
#    7  |   8  |   9
#
# INPUT:
#    tttB = a two dimensional square list of integers. Each element is either
#            a -1 (owned by "O"), a 1 (owned by "X") or a 0 (empty).
# OUTPUT:
#    No variables are outputted. A tic-tac-toe board is displayed to standard
#      output
#----------------------------------------------------------------------------------
def displayBoard(tttB):
    n = len(tttB) # Get the size of the board
    print('')
    for i in range(n):
        # Print the X, O or blank for the ith row
        for j in range(n):
            if tttB[i][j] == 1:
                print('   X  |',end='')
            elif tttB[i][j] == -1:
                print('   O  |', end='')
            else:
                print(' ','{:2d}'.format(i*n+j+1),' |', end='')
        # Get rid of the extra "|" at the end of a row, and if it is not the last
        #   row, print a separating line
        print('\b')
        if i!= n-1:
            for j in range(n):
                print('-------',end = '')
            print('')
    print('')