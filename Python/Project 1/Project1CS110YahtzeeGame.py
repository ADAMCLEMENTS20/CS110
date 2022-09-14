# ---------------------------------------------------------------------------------------------------------------------------------
# Project #1
# Adam Clements
# Summary: Make a "dice" game

# -use random to roll 4 different dice
# -find out whether any dice match
# -ask if they want to hold any dice, and which ones
# -roll again, only the dice not held
# -check which dice match
# -ask if they want to hold any dice, and which ones
# -roll again, and calculate the score
# -loop the whole game again, and add the scores
# ----------------------------------------------------------------------------------------------------------------------------------
# import the necessary "random" import
import random
# make a variable for the game to loop twice
game = 0
run = 0
# make a variable to hold the score
score1 = 0
score2 = 0
# make a variable to make a loop for holding dice
hloop = True
# set the values of the dice as random numbers between 1 and 6
dice1 = random.randint(1,6)
dice2 = random.randint(1,6)
dice3 = random.randint(1,6)
dice4 = random.randint(1,6)
isHeld1 = False
isHeld2 = False
isHeld3 = False
isHeld4 = False
#run the loop for round 1
while game < 2:
    # print the 4 dice values
    print("Dice values: " + str(dice1) + " " + str(dice2) + " " + str(dice3) + " " + str(dice4))
    while hloop:
        # ask if the player wants to hold or unhold any dice
        hold = input("Which dice would you like to hold/unhold? (if none, type -1): ")
        # check if the player has asked to hold any dice
        if int(hold) == 1 and isHeld1 == False:
            isHeld1 = True
        elif int(hold) == 2 and isHeld2 == False:
            isHeld2 = True
        elif int(hold) == 3 and isHeld3 == False:
            isHeld3 = True
        elif int(hold) == 4 and isHeld4 == False:
            isHeld4 = True
        elif int(hold) == 1 and isHeld1 == True:
            isHeld1 = False
        elif int(hold) == 2 and isHeld2 == True:
            isHeld2 = False
        elif int(hold) == 3 and isHeld3 == True:
            isHeld3 = False
        elif int(hold) == 4 and isHeld4 == True:
            isHeld4 = False
        elif int(hold) == -1:
            hloop = False
        else:
            print("Please enter a valid die number or -1")
    hloop = True
    #roll the un-held dice
    if not isHeld1:
        dice1 = random.randint(1,6)
    if not isHeld2:
        dice2 = random.randint(1,6)
    if not isHeld3:
        dice3 = random.randint(1,6)
    if not isHeld4:
        dice4 = random.randint(1,6)
    game += 1
#print final dice values for round 1
print ("Dice Values: " + str(dice1) + " " + str(dice2) + " " + str(dice3) + " " + str(dice4))
#figure out which dice match, and the score associated
if dice1 == dice2 == dice3 == dice4:
    score1 = 50
elif dice1 == dice2 == dice3 or dice1 == dice2 == dice4 or dice1 == dice3 == dice4 or dice2 == dice3 == dice4:
    score1 = 35
elif dice1 != dice2 and dice1 != dice3 and dice1 != dice4 and dice2 != dice3 and dice2 != dice4 and dice3 != dice4:
    score1 = dice1 + dice2 + dice3 + dice4
else:
    score1 = dice1 + dice2 + dice3 + dice4 + 10
#print score for round 1
print ("Round 1 Total: " + str(score1))
#set the loop counter back to 0
game = 0
#unhold all dice, and roll all the dice again
isHeld1 = False
isHeld2 = False
isHeld3 = False
isHeld4 = False
dice1 = random.randint(1,6)
dice2 = random.randint(1,6)
dice3 = random.randint(1,6)
dice4 = random.randint(1,6)
#run the round 2 loop
while game < 2:
    # print the 4 dice values
    print("Dice values: " + str(dice1) + " " + str(dice2) + " " + str(dice3) + " " + str(dice4))
    while hloop:
        # ask if the player wants to hold or unhold any dice
        hold = input("Which dice would you like to hold/unhold? (if none, type -1): ")
        # check if the player has asked to hold any dice
        if int(hold) == 1 and isHeld1 == False:
            isHeld1 = True
        elif int(hold) == 2 and isHeld2 == False:
            isHeld2 = True
        elif int(hold) == 3 and isHeld3 == False:
            isHeld3 = True
        elif int(hold) == 4 and isHeld4 == False:
            isHeld4 = True
        elif int(hold) == 1 and isHeld1 == True:
            isHeld1 = False
        elif int(hold) == 2 and isHeld2 == True:
            isHeld2 = False
        elif int(hold) == 3 and isHeld3 == True:
            isHeld3 = False
        elif int(hold) == 4 and isHeld4 == True:
            isHeld4 = False
        elif int(hold) == -1:
            hloop = False
        else:
            print("Please enter a valid die number or -1")
    hloop = True
    #roll the un-held dice
    if not isHeld1:
        dice1 = random.randint(1,6)
    if not isHeld2:
        dice2 = random.randint(1,6)
    if not isHeld3:
        dice3 = random.randint(1,6)
    if not isHeld4:
        dice4 = random.randint(1,6)
    game += 1
#print final dice values for round 2
print ("Dice Values: " + str(dice1) + " " + str(dice2) + " " + str(dice3) + " " + str(dice4))
#figure out which dice match, and the score
if dice1 == dice2 == dice3 == dice4:
    score2 = 50
elif dice1 == dice2 == dice3 or dice1 == dice2 == dice4 or dice1 == dice3 == dice4 or dice2 == dice3 == dice4:
    score2 = 35
elif dice1 != dice2 and dice1 != dice3 and dice1 != dice4 and dice2 != dice3 and dice2 != dice4 and dice3 != dice4:
    score2 = dice1 + dice2 + dice3 + dice4
else:
    score2 = dice1 + dice2 + dice3 + dice4 + 10
#print score for round 2
print ("Round 2 Total: " + str(score2))
#print the final score
print("Final Score: " + str(score1 + score2))
