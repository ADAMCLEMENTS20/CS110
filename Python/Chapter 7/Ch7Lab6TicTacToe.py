#--------------------------------------
#Adam Clements
#Tic Tac Toe
#create a 3x3, 4x4, and 5x5 game of tic tac toe using Dr. Dostert's displayBoard function
#-ask for the board size
#-create a square list of that board
#-ask for the first player to select a spot to place their mark (X or O)
#check if the player has a row, column, or diagonal completed
#ask the 2nd player for a location
#check if theyve won
#if neither wins, make it a tie
#--------------------------------------
#create variables
boardsize = 0
board = []
#place in the function
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
#make a variable for the input
d = 0
while d < 2 or d > 5:
    #ask for board size
    d = int(input("Board Size (Min 3, Max 5): "))
    if d < 2 or d > 5:
        print("Invalid board size, please enter again.")
    #make the board a 3x3 if d = 3 as well as maxcount and boardsize
    elif d == 3:

        board = [[0, 0, 0,], [0, 0, 0], [0, 0, 0]]
        boardsize = 3
        maxcount = 9
        #same for 4
    elif d == 4:

        board = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        boardsize = 4
        maxcount = 16
        #same for 5
    elif d == 5:

        board = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
        boardsize = 5
        maxcount = 25
#make more variables that will be used later
invalid = True
running = True
player = 2
playerturn = 0
count = 0
#start the main game loop
while running:
    #start a loop to ensure a valid input
    while invalid:
        player = player + 1
        if player%2 == 1:
            playerturn = 1
        elif player%2 == 0:
            playerturn = -1
        displayBoard(board)
        #ask which spot to place the mark
        x = int(input("What spot would you like to play? "))
        #set the value in the square list to mark the spot
        if boardsize == 3:
            if x == 1 and board[0][0] == 0:
                board[0][0] = playerturn
                invalid = False
            elif x == 2 and board[0][1] == 0:
                board[0][1] = playerturn
                invalid = False
            elif x == 3 and board[0][2] == 0:
                board[0][2] = playerturn
                invalid = False
            elif x == 4 and board[1][0] == 0:
                board[1][0] = playerturn
                invalid = False
            elif x == 5 and board[1][1] == 0:
                board[1][1] = playerturn
                invalid = False
            elif x == 6 and board[1][2] == 0:
                board[1][2] = playerturn
                invalid = False
            elif x == 7 and board[2][0] == 0:
                board[2][0] = playerturn
                invalid = False
            elif x == 8 and board[2][1] == 0:
                board[2][1] = playerturn
                invalid = False
            elif x == 9 and board[2][2] == 0:
                board[2][2] = playerturn
                invalid = False
            else:
                print("Invalid input, try again.")
        #set the value in the square list to mark the spot
        elif boardsize == 4:
            if x == 1 and board[0][0] == 0:
                board[0][0] = playerturn
                invalid = False
            elif x == 2 and board[0][1] == 0:
                board[0][1] = playerturn
                invalid = False
            elif x == 3 and board[0][2] == 0:
                board[0][2] = playerturn
                invalid = False
            elif x == 4 and board[0][3] == 0:
                board[0][3] = playerturn
                invalid = False
            elif x == 5 and board[1][0] == 0:
                board[1][0] = playerturn
                invalid = False
            elif x == 6 and board[1][1] == 0:
                board[1][1] = playerturn
                invalid = False
            elif x == 7 and board[1][2] == 0:
                board[1][2] = playerturn
                invalid = False
            elif x == 8 and board[1][3] == 0:
                board[1][3] = playerturn
                invalid = False
            elif x == 9 and board[2][0] == 0:
                board[2][0] = playerturn
                invalid = False
            elif x == 10 and board[2][1] == 0:
                board[2][1] = playerturn
                invalid = False
            elif x == 11 and board[2][2] == 0:
                board[2][2] = playerturn
                invalid = False
            elif x == 12 and board[2][3] == 0:
                board[2][3] = playerturn
                invalid = False
            elif x == 13 and board[3][0] == 0:
                board[3][0] = playerturn
                invalid = False
            elif x == 14 and board[3][1] == 0:
                board[3][1] = playerturn
                invalid = False
            elif x == 15 and board[3][2] == 0:
                board[3][2] = playerturn
                invalid = False
            elif x == 16 and board[3][3] == 0:
                board[3][3] = playerturn
                invalid = False
            else:
                print("Invalid input, try again.")
        #set the value in the square list to mark the spot
        elif boardsize == 5:
            if x == 1 and board[0][0] == 0:
                board[0][0] = playerturn
                invalid = False
            elif x == 2 and board[0][1] == 0:
                board[0][1] = playerturn
                invalid = False
            elif x == 3 and board[0][2] == 0:
                board[0][2] = playerturn
                invalid = False
            elif x == 4 and board[0][3] == 0:
                board[0][3] = playerturn
                invalid = False
            elif x == 5 and board[0][4] == 0:
                board[0][4] = playerturn
                invalid = False
            elif x == 6 and board[1][0] == 0:
                board[1][0] = playerturn
                invalid = False
            elif x == 7 and board[1][1] == 0:
                board[1][1] = playerturn
                invalid = False
            elif x == 8 and board[1][2] == 0:
                board[1][2] = playerturn
                invalid = False
            elif x == 9 and board[1][3] == 0:
                board[1][3] = playerturn
                invalid = False
            elif x == 10 and board[1][4] == 0:
                board[1][4] = playerturn
                invalid = False
            elif x == 11 and board[2][0] == 0:
                board[2][0] = playerturn
                invalid = False
            elif x == 12 and board[2][1] == 0:
                board[2][1] = playerturn
                invalid = False
            elif x == 13 and board[2][2] == 0:
                board[2][2] = playerturn
                invalid = False
            elif x == 14 and board[2][3] == 0:
                board[2][3] = playerturn
                invalid = False
            elif x == 15 and board[2][4] == 0:
                board[2][4] = playerturn
                invalid = False
            elif x == 16 and board[3][0] == 0:
                board[3][0] = playerturn
                invalid = False
            elif x == 17 and board[3][1] == 0:
                board[3][1] = playerturn
                invalid = False
            elif x == 18 and board[3][2] == 0:
                board[3][2] = playerturn
                invalid = False
            elif x == 19 and board[3][3] == 0:
                board[3][3] = playerturn
                invalid = False
            elif x == 20 and board[3][4] == 0:
                board[3][4] = playerturn
                invalid = False
            elif x == 21 and board[4][0] == 0:
                board[4][0] = playerturn
                invalid = False
            elif x == 22 and board[4][1] == 0:
                board[4][1] = playerturn
                invalid = False
            elif x == 23 and board[4][2] == 0:
                board[4][2] = playerturn
                invalid = False
            elif x == 24 and board[4][3] == 0:
                board[4][3] = playerturn
                invalid = False
            elif x == 25 and board[4][4] == 0:
                board[4][4] = playerturn
                invalid = False
            else:
                print("Invalid input, try again.")
    displayBoard(board)
    count += 1
    invalid = True
    #check if either player has won
    if boardsize == 3:

        if (board[0][0] == board[0][1] == board[0][2] == 1) or (board[1][0] == board[1][1] == board[1][2] == 1) or (board[2][0] == board[2][1] == board[2][2] == 1) or (board[0][0] == board[1][0] == board[2][0] == 1) or (board[0][1] == board[1][1] == board[2][1] == 1) or (board[0][2] == board[1][2] == board[2][2] == 1) or (board[0][0] == board[1][1] == board[2][2] == 1) or (board[0][2] == board[1][1] == board[2][0] == 1):
            print("Player 1 Wins!")
            running = False
        if (board[0][0] == board[0][1] == board[0][2] == -1) or (board[1][0] == board[1][1] == board[1][2] == -1) or (board[2][0] == board[2][1] == board[2][2] == -1) or (board[0][0] == board[1][0] == board[2][0] == -1) or (board[0][1] == board[1][1] == board[2][1] == -1) or (board[0][2] == board[1][2] == board[2][2] == -1) or (board[0][0] == board[1][1] == board[2][2] == -1) or (board[0][2] == board[1][1] == board[2][0] == -1):
            print("Player 2 Wins!")
            running = False
    if boardsize == 4:

        if (board[0][0] == board[0][1] == board[0][2] == board[0][3] == 1) or (board[1][0] == board[1][1] == board[1][2] == board[1][3] == 1) or (board[2][0] == board[2][1] == board[2][2] == board[2][3] == 1) or (board[3][0] == board[3][1] == board[3][2] == board[3][3] == 1) or (board[0][0] == board[1][0] == board[2][0] == board[3][0] == 1) or (board[0][1] == board[1][1] == board[2][1] == board[3][1] == 1) or (board[0][2] == board[1][2] == board[2][2] == board[3][2] == 1) or (board[0][3] == board[1][3] == board[2][3] == board[3][3] == 1) or (board[0][0] == board[1][1] == board[2][2] == board[3][3] == 1) or (board[0][3] == board[1][2] == board[2][1] == board[3][0] == 1):
            print("Player 1 Wins!")
            running = False
        if (board[0][0] == board[0][1] == board[0][2] == board[0][3] == -1) or (board[1][0] == board[1][1] == board[1][2] == board[1][3] == -1) or (board[2][0] == board[2][1] == board[2][2] == board[2][3] == -1) or (board[3][0] == board[3][1] == board[3][2] == board[3][3] == -1) or (board[0][0] == board[1][0] == board[2][0] == board[3][0] == -1) or (board[0][1] == board[1][1] == board[2][1] == board[3][1] == -1) or (board[0][2] == board[1][2] == board[2][2] == board[3][2] == -1) or (board[0][3] == board[1][3] == board[2][3] == board[3][3] == -1) or (board[0][0] == board[1][1] == board[2][2] == board[3][3] == -1) or (board[0][3] == board[1][2] == board[2][1] == board[3][0] == -1):
            print("Player 2 Wins!")
            running = False
    if boardsize == 5:

        if (board[0][0] == board[0][1] == board[0][2] == board[0][3] == board[0][4] == 1) or (board[1][0] == board[1][1] == board[1][2] == board[1][3] == board[1][4] == 1) or (board[2][0] == board[2][1] == board[2][2] == board[2][3] == board[2][4] == 1) or (board[3][0] == board[3][1] == board[3][2] == board[3][3] == board[3][4] == 1) or (board[4][0] == board[4][1] == board[4][2] == board[4][3] == board[4][4] == 1) or (board[0][0] == board[1][0] == board[2][0] == board[3][0] == board[4][0] == 1) or (board[0][1] == board[1][1] == board[2][1] == board[3][1] == board[4][1] == 1) or (board[0][2] == board[1][2] == board[2][2] == board[3][2] == board[4][2] == 1) or (board[0][3] == board[1][3] == board[2][3] == board[3][3] == board[4][3] == 1) or (board[0][4] == board[1][4] == board[2][4] == board[3][4] == board[4][4] == 1) or (board[0][0] == board[1][1] == board[2][2] == board[3][3] == board[4][4] == 1) or (board[0][4] == board[1][3] == board[2][2] == board[3][1] == board[4][0] == 1):
            print("Player 1 Wins!")
            running = False
        if (board[0][0] == board[0][1] == board[0][2] == board[0][3] == board[0][4] == -1) or (board[1][0] == board[1][1] == board[1][2] == board[1][3] == board[1][4] == -1) or (board[2][0] == board[2][1] == board[2][2] == board[2][3] == board[2][4] == -1) or (board[3][0] == board[3][1] == board[3][2] == board[3][3] == board[3][4] == -1) or (board[4][0] == board[4][1] == board[4][2] == board[4][3] == board[4][4] == -1) or (board[0][0] == board[1][0] == board[2][0] == board[3][0] == board[4][0] == -1) or (board[0][1] == board[1][1] == board[2][1] == board[3][1] == board[4][1] == -1) or (board[0][2] == board[1][2] == board[2][2] == board[3][2] == board[4][2] == -1) or (board[0][3] == board[1][3] == board[2][3] == board[3][3] == board[4][3] == -1) or (board[0][4] == board[1][4] == board[2][4] == board[3][4] == board[4][4] == -1) or (board[0][0] == board[1][1] == board[2][2] == board[3][3] == board[4][4] == -1) or (board[0][4] == board[1][3] == board[2][2] == board[3][1] == board[4][0] == -1):
            print("Player 2 Wins!")
            running = False
    #check if the whole board is full, without a win
    if count == maxcount:
        print("Tie!")
        running = False

