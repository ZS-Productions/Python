import os
import time

# Game Variables
Game = 0 #[0 = Default, 1 = Win, 2 = Draw]
board = [' ', '1', '2', '3', '4', '5', '6', '7', '8', '9']
player = 1
res = 0

### DEFINE FUNCTIONS ###

# Function to draw the board of the game depending on its type
def DrawBoard(type):
    if type == 0: # Shows numbers for input
        
        # Displays input board 
        for step in range(1, 8, 3):         
            print(" %c | %c | %c " % (board[step], board[step + 1], board[step + 2]))
            if step != 7: # Only print twice
                print("-----------")

        print("\n")
        
    elif type == 1: # Shows clear display
        disp = [] 
        
        # Creates a new list with only X's and O's
        for step in board:
            if step == 'X':
                disp.append(step)
            elif step == 'O':
                disp.append(step)
            else:
                disp.append(' ')
        
        # Display new list
        for step in range(1, 8, 3):         
            print(" %c | %c | %c " % (disp[step], disp[step + 1], disp[step + 2]))
            if step != 7: # Only print twice
                print("-----------")

        print("\n")
    
    
# Check to see who's won the game    
def CheckWin(res):
    
    # If statement for all possible win outcomes
    if(board[1] == board[2] == board[3] and board[1] != '1' or \
       board[4] == board[5] == board[6] and board[4] != '4' or \
       board[7] == board[8] == board[9] and board[7] != '7' or \
       board[1] == board[4] == board[7] and board[1] != '1' or \
       board[2] == board[5] == board[8] and board[2] != '2' or \
       board[3] == board[6] == board[9] and board[3] != '3' or \
       board[1] == board[5] == board[9] and board[5] != '5' or \
       board[3] == board[5] == board[7] and board[5] != '5'):
        return 1 # Win
    
    # Check to see if the entire board is filled and no one has won
    for check in range(1, 10, 1):
        if(board[check] == 'X' or board[check] == 'O'):
            res += 1
    if res == 9: 
        return 2 # Draw
    
### START GAME ###    
print("Tic-Tac-Toe")
print("Player 1 [X] --- Player 2 [O]\n")
time.sleep(3)

# Loop until game finishes
while True:
    os.system('cls') 
    DrawBoard(0)

    # Change player based on turn
    if player % 2 != 0:
        print("Player 1's chance")
        mark = 'X'
    else:
        print("Player 2's chance")
        mark = 'O'    
        
    # Obtain player input and check if valid       
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
                    
    board[choice] = mark # Mark player input space
    player += 1 # Change player
    
    # Obtain game state
    Game = CheckWin(res)
    res = 0
    
    # Show Board State
    os.system('cls')
    DrawBoard(1)
    time.sleep(1)
    
    # Check state of Game
    if Game == 2:
        print("Game Draw")
    elif Game == 1:
        player -= 1
        if player % 2 != 0:
            print("Player 1 Won")
        else:
            print("Player 2 Won")
        break # End Game