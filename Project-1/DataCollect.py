import sqlite3, os, time, sys

# Python Variables
OutcomeID = 3
OutcomeText = ""
required = 0

# Start Database Connection
con = sqlite3.connect("Story.db")
cur = con.cursor()

# Extract Database
cho = (cur.execute("SELECT * FROM choices")).fetchall()
outc = (cur.execute("SELECT * FROM outcomes")).fetchall()

### GAME START ###
print("\nThe Adventure Game - Designed by ZS Productions\n")
print("Game will be starting in...")
for i in range(3, 0, -1):
    print (i, end="\r")
    time.sleep(1)
    

os.system('cls')
# INTRO #
print("You enter a cave there is a small waterway running through\nOn your right you see stairs leading up to another opening\nAlternatively you can go straight ahead and follow the water path.\n\n")
nxt = input("Press enter to continue...")

while True:
    os.system('cls')
    ## LOOP START
    OutcomeText = outc[OutcomeID - 1][1]
    required = outc[OutcomeID - 1][2]
    # Obtain the ID of possible choices
    Choices = [outc[OutcomeID - 1][3], outc[OutcomeID - 1][4], outc[OutcomeID - 1][5]] # Compile in array

    print(OutcomeText + "\n") # Print Outcome Flavour Text

    # Check to see if its a choice or simply the next outcome dialogue
    if required == 1: # The user needs to make a choice         
        
        # List out the available choices
        for x, item in enumerate(Choices):
            if(item != 0):
                rep = x + 1
                print(str(rep) + " ~ " + cho[item-1][1])
               
    else: # Continue to next Outcome
        if OutcomeID == 1 or OutcomeID == 2:
            break
        OutcomeID = outc[OutcomeID - 1][3]
        nxt = input("Press enter to continue...")
        continue

    # Obtain user choice input, must be within the constraints    
    while True:
        try:    
            option = int(input("Make your Choice: "))
        except ValueError:
            print("Please enter a number between 1 and " + str(rep))
            continue
        else:    
            if(option < 1 or option > rep):
                print("Please enter a number between 1 and " + str(rep))
                continue
            else:
                print()
                break
            
    OutcomeID = cho[Choices[option - 1] - 1][2]
    
# Close database connection
con.close()
    

