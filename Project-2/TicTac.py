# Game Variables
Game = 0
board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
player = 1
mark = 'X'

# Draw board function
def DrawBoard():
    print(" %c | %c | %c " % (board[1], board[2], board[3]))
    print("-----------")
    print(" %c | %c | %c " % (board[4], board[5], board[6]))
    print("-----------")
    print(" %c | %c | %c " % (board[7], board[8], board[9]))
    
# Check to see who's won the game    
def CheckWin():
    if board[1] == board[2] and board[2] == board[3] and board[1] != ' ':
        return 1
    elif board[4] == board[5] and board[5] == board[6] and board[4] != ' ':
        return 1
    elif board[7] == board[8] and board[8] == board[9] and board[7] != ' ':
        return 1
    elif board[1] == board[4] and board[4] == board[7] and board[1] != ' ':
        return 1
    elif board[2] == board[5] and board[5] == board[8] and board[2] != ' ':
        return 1
    elif board[3] == board[6] and board[6] == board[9] and board[3] != ' ':
        return 1
    elif board[1] == board[5] and board[5] == board[9] and board[5] != ' ':
        return 1
    elif board[3] == board[5] and board[5] == board[7] and board[5] != ' ':
        return 1
    elif board[1] != ' ' and board[2] != ' ' and board[3] != ' ' and \
            board[4] != ' ' and board[5] != ' ' and board[6] != ' ' and \
            board[7] != ' ' and board[8] != ' ' and board[9] != ' ':
        return 2
    
print("Tic-Tac-Toe")
print("Player 1 [X] --- Player 2 [O]\n")

while True:
    DrawBoard()

    if player % 2 != 0:
        print("Player 1's chance")
        mark = 'X'
    else:
        print("Player 2's chance")
        mark = 'O'    
        
    while True:
        try:
            choice = int(input("Enter the position between [1-9] where you want to mark: "))
        except ValueError:
            print("Please enter a number between 1-9\n")
        else:
            if(choice < 1 or choice > 9):
                continue
            else:
                break
            
    board[choice] = mark
    player += 1
    Game = CheckWin()
    DrawBoard()

    if Game == 2:
        print("Game Draw")
    elif Game == 1:
        player -= 1
        if player % 2 != 0:
            print("Player 1 Won")
        else:
            print("Player 2 Won")
        break