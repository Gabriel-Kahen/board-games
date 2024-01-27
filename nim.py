board = [[0,0,0,1,0,0,0],[0,0,1,1,1,0,0],[0,1,1,1,1,1,0],[1,1,1,1,1,1,1]]

def print_board():
    curr = ""
    for r in range(4):
        print("\n",r, end = "")
        for c in range(7):
            if(board[r][c] == 0):
                curr = " "
            else:
                curr = "|"
            print("\t" + curr, end ="")
        print()
        
def total():
    count = 0
    for row in range(4):
        for col in range(7):
            if(board[row][col] == 1):
                count+= 1
    return count

def count_in_row(r):
    count = 0
    for c in range(7):
        if(board[r][c] == 1):
            count+= 1
    return count

def is_valid_move(r, amount):
    if(r > 3 or r < 0):
        return False
    if(amount > count_in_row(r) or amount < 1):
        return False
    return True

def make_move(r, amount):
    if(not is_valid_move(r, amount)):
        raise Exception("Not a valid move")
    for c in range(7):
        if amount > 0:
            if(board[r][c] == 1):
                board[r][c] = 0
                amount -= 1
                
def undo_move(r, amount):
    find = -1
    for c in range(7):
        if(board[r][c] == 1):
            find = c
            break
    if(find == -1):
        find = 4 + r
    for i in range(amount):
        board[r][find - 1 - i] = 1

def minimax(player, depth, alpha, beta):
    optimalRow = -1
    optimalAmount = -1
    
    if(total() == 0):
        if(player == "Bot"):
            return (10, None, None)
        return (-10, None, None)
    
    if(depth == 0):
        return (0, None, None)

    if player == "Bot":
        best = -10000
        for row in range(4):
            for amount in range(count_in_row(row)):
                if is_valid_move(row, amount + 1):
                    make_move(row, amount + 1)
                    val = minimax("User", depth - 1, alpha, beta)[0]
                    undo_move(row, amount + 1)
                    if val > best:
                        best = val
                        optimalRow = row
                        optimalAmount = amount + 1
                    alpha = max(alpha, best)
                    if alpha >= beta:
                        break
        return best, optimalRow, optimalAmount

    else:
        worst = 10000
        for row in range(4):
            for amount in range(count_in_row(row)):
                if is_valid_move(row, amount + 1):
                    make_move(row, amount + 1)
                    val = minimax("Bot", depth - 1, alpha, beta)[0]
                    undo_move(row, amount + 1)
                    if val < worst:
                        worst = val
                        optimalRow = row
                        optimalAmount = amount + 1
                    beta = min(beta, worst)
                    if alpha >= beta:
                        break
        return worst, optimalRow, optimalAmount

def play():
    player = "User"
    while(total() > 1):
        print_board()
        if(player == "User"):
            row = int(input("Enter a row "))
            amount = int(input("Enter how many pieces you want to take away "))
            if(not is_valid_move(row, amount)):
                print("Please enter a valid move")
                play(player)
            else:
                make_move(row, amount)
                player = "Bot"
        else:
            print("Now the bot will go")
            val = minimax("Bot", 4, -1000, 1000) #change this depth to change difficulty. A depth of 4 has been unbeatable in my testing. 
            make_move(val[1], val[2])
            print("The bot removed", val[2], "pieces from row", val[1])
            player = "User"
        if(total() == 1):
            if(player == "User"):
                print("You are forced to take the last piece. The Bot Wins!")
                print_board()

            else:
                print_board()
                print("The bot is forced to take the last piece. You Win!")
    again = input("Would you like to play again?\n")
    if("N" not in again.upper()):
        global board
        board = [[0,0,0,1,0,0,0],[0,0,1,1,1,0,0],[0,1,1,1,1,1,0],[1,1,1,1,1,1,1]]
        play()
    else:
        print("Okay, see you later!")

play()