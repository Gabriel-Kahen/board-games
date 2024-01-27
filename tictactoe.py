board = [["-","-","-"],["-","-","-"],["-","-","-"]]

def print_board():
    print("\t0\t1\t2")
    for x in range(3):
        print("\n", x, end = "")
        for y in range(3):
            print("\t" + board[x][y], end ="")
        print()

def is_valid_move(row, col):
    if (row > 2 or col > 2 or row < 0 or col < 0):
        return False
    return board[row][col] == "-"
    
def make_move(player, row, col):
    if not is_valid_move(row, col):
        raise Exception("Not a valid move")
    board[row][col] = player

def undo_move(row, col):
    board[row][col] = "-"

def check_win(player):
    for x in range (3):
        if(board[0][x] == player and board[1][x] == player and board[2][x] == player):
            return True
        if(board[x][0] == player and board[x][1] == player and board[x][2] == player):
            return True
    if(board[0][0] == player and board[1][1] == player and board[2][2] == player):
            return True
    if(board[2][0] == player and board[1][1] == player and board[0][2] == player):
            return True
    return False
    
def check_tie():
    for x in range(3):
        for y in range(3):
            if(board[x][y] == "-"):
                return False
    return not(check_win("X") or check_win("O"))

def minimax(player, depth, alpha, beta):
    optimalRow = -1
    optimalColumn = -1
    if(check_win("O")):
            return (10, None, None)
    if(check_win("X")):
            return (-10, None, None)
    if(check_tie() or depth == 0):
            return (0, None, None)
    if(player == "O"):
        best = -10000
        for r in range(3):
            for c in range(3):
                if(is_valid_move(r, c)):
                    make_move("O", r, c)
                    val = minimax("X", depth - 1, alpha, beta)[0]
                    undo_move(r, c)
                    if val > best:
                        best = val
                        optimalRow = r
                        optimalColumn = c
                    alpha = max(alpha, best)
                    if alpha >= beta:
                        break
        return (best, optimalRow, optimalColumn)

    if(player == "X"):
        worst = 10000
        for r in range(3):
            for c in range(3):
                if(is_valid_move(r, c)):
                    make_move("X", r, c)
                    val = minimax("O", depth - 1, alpha, beta)[0]
                    undo_move(r, c)
                    if(val < worst):
                        worst = val
                        optimalRow = r
                        optimalColumn = c
                    beta = min(beta, worst)
                    if alpha >= beta:
                        break
        return (worst, optimalRow, optimalColumn)       
    
def play():
    player = "X"
    print_board()
    while(check_win("O") == False and check_win("X") == False and check_tie() == False):
        if(player == "X"):
            row = int(input("Enter a row "))
            column = int(input("Enter a column "))
            if(not is_valid_move(row, column)):
                print("Please enter a valid move")
                play()
            else:
                make_move(player, row, column)
                player = "O"
        else:
            print("Now the bot will go")
            val = minimax("O", 7, -1000, 1000) #change this depth to change difficulty. A depth of 7 has been unbeatable in my testing.
            make_move(player, val[1], val[2])
            player = "X"
        print_board()
        if(check_win("X")):
            print("You Win!")
        if(check_win("O")):
            print("The Bot Wins!")
        if(check_tie()):
            print("It's a Tie!")
    again = input("Would you like to play again?\n")
    if("N" not in again.upper()):
        global board
        board = [["-","-","-"],["-","-","-"],["-","-","-"]]
        play()
    else:
        print("Okay, see you later!")

play()