import os
import time

# Game Variables
Game = 0 #[0 = Default, 1 = Win, 2 = Draw]
board = [' ', '1', '2', '3', '4', '5', '6', '7', '8', '9']
player = 1
mark = 'X'

def DrawBoard(type):
    if type == 0:
        for step in range(1, 8, 3):         
            print(" %c | %c | %c " % (board[step], board[step + 1], board[step + 2]))
            if step != 7:
                print("-----------")

        print("\n")
    elif type == 1:
        disp = []
        for step in board:
            if step == 'X':
                disp.append(step)
            elif step == 'O':
                disp.append(step)
            else:
                disp.append(' ')
        for step in range(1, 8, 3):         
            print(" %c | %c | %c " % (disp[step], disp[step + 1], disp[step + 2]))
            if step != 7:
                print("-----------")

        print("\n")
    
    
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
    os.system('cls')
    DrawBoard(0)

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
    os.system('cls')
    DrawBoard(1)
    time.sleep(1)
    if Game == 2:
        print("Game Draw")
    elif Game == 1:
        player -= 1
        if player % 2 != 0:
            print("Player 1 Won")
        else:
            print("Player 2 Won")
        break