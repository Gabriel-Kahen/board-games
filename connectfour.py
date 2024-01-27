board = [["-","-","-","-","-","-","-"],["-","-","-","-","-","-","-"],["-","-","-","-","-","-","-"],["-","-","-","-","-","-","-"],["-","-","-","-","-","-","-"],["-","-","-","-","-","-","-"]]

def print_board():
    for i in range(7):
        print(i, "\t", end="")
    print("\n")
    for r in range(6):
        for c in range(7):
            print(board[r][c], "\t", end ="")
        print("\n")

def rows_taken(c):
    count = 0
    for r in range(6):
        if not board[r][c] == "-":
            count+=1
    return count
 
def is_valid_move(c):
    if(c > 6 or c < 0 or rows_taken(c) == 6):
        return False
    return True

def make_move(player, c):
    if not is_valid_move(c):
        raise Exception("Not a valid move")
    board[5 - rows_taken(c)][c] = player
    
def undo_move(c):
    board[6 - rows_taken(c)][c] = "-"
    
def check_tie():
    for c in range(7):
        if(board[0][c] == "-"):
            return False
    return True

#all win checking code and current score calculation courtesy of code.org
def check_horizontal_win(player):
    streak = 0
    for row in range(len(board)):
        for col in range(len(board[row]) - 1):
            if board[row][col] == player and board[row][col] == board[row][col + 1]:
                streak += 1 
            else:
                streak = 0
            if streak == 3:
                return True
        streak = 0
    return False

def check_vertical_win(player):
    streak = 0
    for row in range(7):
        for col in range(5):
            if board[col][row] == player and board[col][row] == board[col + 1][row]:
                streak += 1 
            else:
                streak = 0
            if streak == 3:
                return True
        streak = 0
    return False

def check_diagonal_win(player):
    for row in range(len(board)):
        for col in range(len(board[0])):
            try:
                if board[row][col] == player and board[row + 1][col + 1] == player and board[row + 2][col+2] == player and board[row + 3][col + 3] == player:
                  return True
                if board[row][col] == player and board[row + 1][col-1] == player and board[row + 2][col-2] == player and board[row + 3][col-3] == player and col - 3 >= 0:
                    return True
            except IndexError:
                try:
                  if board[row][col] == player and board[row + 1][col-1] == player and board[row + 2][col-2] == player and board[row + 3][col-3] == player and col - 3 >= 0:
                    return True
                except IndexError:
                    next
                next
    return False

def check_win(player):
    return check_diagonal_win(player) or check_vertical_win(player) or check_horizontal_win(player)

def check_three_row(player):
    streak = 0
    total_threes = 0
    for row in range(len(board)):
        for col in range(len(board[row]) - 1):
            if board[row][col] == player and board[row][col] == board[row][col + 1]:
                streak += 1 
            else:
                streak = 0
            try:
                if (streak == 2 and board[row][col + 1] == "-") or (streak == 2 and board[row][col - streak - 1] == "-"):
                    total_threes += 1
            except:
                next
    return total_threes

def check_three_col(player):
    streak = 0
    total_threes = 0

    for row in range(7):
        for col in range(5):
            if board[col][row] == player and board[col][row] == board[col + 1][row]:
                streak += 1 
            else:
                streak = 0
            try:
                if (streak == 2 and board[col + 1][row] == "-") or (streak == 2 and board[col - streak - 1][row] == "-"):
                    total_threes += 1
            except: 
                next
    return total_threes

def check_three_diag(player):
    total_threes = 0
    for row in range(len(board)):
        for col in range(len(board[0])):
            try:
                if board[row][col] == player and board[row + 1][col + 1] == player and board[row + 2][col+2] == player and board[row + 3][col + 3] == "-":
                  total_threes += 1
                if board[row][col] == player and board[row + 1][col-1] == player and board[row + 2][col-2] == player and board[row + 3][col-3] == "-":
                    total_threes += 1
                if board[row][col] == player and board[row + 1][col-1] == player and board[row + 2][col-2] == player and board[row - 1][col + 1] == "-":
                    total_threes += 1
                if board[row][col] == player and board[row + 1][col + 1] == player and board[row + 2][col+2] == player and board[row -1][col -1] == "-":
                    total_threes += 1
            except IndexError:
                try:
                    if board[row][col] == player and board[row + 1][col-1] == player and board[row + 2][col-2] == player and board[row + 3][col-3] == "-":
                        total_threes += 1
                except:
                    try:
                        if board[row][col] == player and board[row + 1][col-1] == player and board[row + 2][col-2] == player and board[row - 1][col + 1] == "-":
                            total_threes += 1
                    except:
                        try:
                            if board[row][col] == player and board[row + 1][col + 1] == player and board[row + 2][col+2] == player and board[row -1][col -1] == "-":
                                total_threes += 1
                        except:
                            next
                next
    return total_threes

def check_two_row(player):
    streak = 0
    total_twos = 0
    for row in range(len(board)):
        for col in range(len(board[row]) - 1):
            if board[row][col] == player and board[row][col] == board[row][col + 1]:
                streak += 1 
            else:
                streak = 0
            try:
                if (streak == 1 and board[row][col + 1] == "-") or (streak == 1 and board[row][col - streak - 1] == "-"):
                    total_twos += 1
            except:
                next
    return total_twos

def check_two_col(player):
    streak = 0
    total_two = 0

    for row in range(7):
        for col in range(5):
            if board[col][row] == player and board[col][row] == board[col + 1][row]:
                streak += 1 
            else:
                streak = 0
            try:
                if (streak == 1 and board[col + 1][row] == "-") or (streak == 1 and board[col - streak - 1][row] == "-"):
                    total_two += 1
            except: 
                next
    return total_two

def check_two_diag(player):
    total_two = 0
    for row in range(len(board)):
        for col in range(len(board[0])):
            try:
                if board[row][col] == player and board[row + 1][col + 1] == player and board[row + 2][col+2] == "-":
                  total_two += 1
                if board[row][col] == player and board[row + 1][col-1] == player and board[row + 2][col-2] == "-":
                    total_two += 1
                if board[row][col] == player and board[row + 1][col-1] == player and board[row + 2][col-2] == "-":
                    total_two += 1
                if board[row][col] == player and board[row + 1][col + 1] == player and board[row + 2][col+2] == "-":
                    total_two += 1
            except IndexError:
                try:
                    if board[row][col] == player and board[row + 1][col-1] == player and board[row + 2][col-2] == "-":
                        total_two += 1
                except:
                    try:
                        if board[row][col] == player and board[row + 1][col-1] == player and board[row + 2][col-2] == "-":
                            total_two += 1
                    except:
                        try:
                             if board[row][col] == player and board[row + 1][col + 1] == player and board[row + 2][col+2] == "-":
                                total_two += 1
                        except:
                            next
                next
    return total_two

def check_one_row(player):
    total_ones = 0
    for row in range(len(board)):
        for col in range(len(board[row]) - 1):
            try:
                if (board[row][col] == player and board[row][col + 1] == "-" and board[row][col- 1] == "-"):
                    total_ones += 1
            except:
                next
    return total_ones

def check_one_col(player):
    total_ones = 0
    for row in range(7):
        for col in range(5):
            try:
                if (board[col][row] == player and board[col + 1][row] == "-" and board[col - 1][row] == "-"):
                    total_ones += 1
            except: 
                next
    return total_ones

def check_one_diag(player):
    total_one = 0
    for row in range(len(board)):
        for col in range(len(board[0])):
            try:
                if board[row][col] == player and board[row + 1][col + 1] == "-" and board[row -1][col-1] == "-":
                  total_one += 1
                
                if board[row][col] == player and board[row + 1][col-1] == player and board[row - 1][col + 1] == "-":
                    total_one += 1
            except IndexError:
                # try:
                #   if board[row][col] == player and board[row - 1][col-1] == player and board[row - 2][col-2] == player and board[row - 3][col-3] == player:
                #     return True
                # except IndexError:
                #     pass
                next
    return total_one

def check_three_total(player):
    return (check_three_col(player) + check_three_row(player) + check_three_diag(player)) * 50

def check_two_total(player):
    return (check_two_col(player) + check_two_row(player) + check_two_diag(player)) * 20
    
def check_one_total(player):
    return (check_one_col(player) + check_one_row(player) + check_one_diag(player)) * 7

def check_curr_score():
    return check_three_total("black") + check_two_total("black") + check_one_total("black") - check_two_total("red") - check_three_total("red") - check_one_total("red")

def minimax(player, depth, alpha, beta):
    optimalColumn = -1
    if check_win("O"):
        return (10, None)
    if check_win("X"):
        return (-10, None)
    if depth == 0 or check_tie():
        return (check_curr_score(), None)
    
    if player == "O":
        best = -10000
        for c in range(7):
            if(is_valid_move(c)):
                make_move("O", c)
                val = minimax("X", depth - 1, alpha, beta)[0]
                undo_move(c)
                if val > best:
                    best = val
                    optimalColumn = c
                alpha = max(alpha, best)
                if alpha >= beta:
                    break
        return(best, optimalColumn)
    
    else:
        worst = 10000
        for c in range(7):
            if(is_valid_move(c)):
                make_move("X", c)
                val = minimax("O", depth - 1, alpha, beta)[0]
                undo_move(c)
                beta = min(beta, worst)
                if val < worst:
                    worst = val
                    optimalColumn = c
                if alpha >= beta:
                    break
        return(worst, optimalColumn)
                    
def play():
    player = "X"
    print_board()
    while(check_win("O") == False and check_win("X") == False and check_tie() == False):
        if(player == "X"):
            column = int(input("Enter a column "))
            if(not is_valid_move(column)):
                print("Please enter a valid move")
                play()
            else:
                make_move(player, column)
                player = "O"
        else:
            print("Now the bot will go")
            val = minimax("O", 7, -100, 100) #change this depth to change difficulty.
            make_move(player, val[1])
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
        board = [["-","-","-","-","-","-","-"],["-","-","-","-","-","-","-"],["-","-","-","-","-","-","-"],["-","-","-","-","-","-","-"],["-","-","-","-","-","-","-"],["-","-","-","-","-","-","-"]]
        play()
    else:
        print("Okay, see you later!")

play()