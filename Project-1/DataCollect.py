import sqlite3

# Python Variables
game = True
OutcomeID = 3
OutcomeText = ""
required = 0
Choice1 = 0
Choice2 = 0
Choice3 = 0

# Start Database Connection
con = sqlite3.connect("Story.db")
cur = con.cursor()

# Extract Database
cho = (cur.execute("SELECT * FROM choices")).fetchall()
outc = (cur.execute("SELECT * FROM outcomes")).fetchall()

### GAME START ###

# INTRO #
print("You enter a cave there is a small waterway running through\nOn your right you see stairs leading up to another opening\nAlternatively you can go straight ahead and follow the water path.\n\n")

while True:
        
    ## LOOP START
    OutcomeText = outc[OutcomeID - 1][1]
    required = outc[OutcomeID - 1][2]

    # Obtain the ID of possible choices
    Choice1 = outc[OutcomeID - 1][3]
    Choice2 = outc[OutcomeID - 1][4]
    Choice3 = outc[OutcomeID - 1][5]
    Choices = [Choice1, Choice2, Choice3] # Compile in list

    print(OutcomeText + "\n") # Print Outcome Flavour Text

    # Check to see if its a choice or simply the next outcome dialogue
    if required == 1: # It's a choice / List out the options
        rep = 0
        for i in Choices:
            if(i != 0):
                rep += 1
                print(str(rep) + " ~ " + cho[i-1][1])
    else: # Continue to next Outcome
        if OutcomeID == 1 or OutcomeID == 2:
            break
        OutcomeID = Choice1
        continue
        
    # Check Game
    if OutcomeID == 1 or OutcomeID == 2:
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
                #print("NICE! You have chosen " + cho[Choices[option - 1] - 1][1])
                print("\n")
                break
            
    OutcomeID = cho[Choices[option - 1] - 1][2]
    

