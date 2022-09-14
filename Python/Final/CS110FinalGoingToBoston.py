# ------------------------------------
# Adam Clements
# Going to Boston-
#   -4 players are playing a game of "Going to Boston"
#   -make a class Player with name and a list of dice
#   -roll all 3 dice and save the highest roll
#   -roll the 2 lower dice and save the highest roll
#   -roll the last die, and calculate the final score
#   -compare the final scores to see who wins
#   -if 2 players have the same high score, both win
# ------------------------------------
# import random for the dice roll
import random


# make class player
class Player:
    # initialize, make a list of dice, and overload with a name
    def __init__(self, name):
        self.dice = []
        self.name = name
        self.savedDice = []
        self.finalscore = 0

    # make a function for the first roll, which will roll and add 3 dice to the empty list "dice"
    # sort the dice in descending order
    # move the highest dice into a "savedDice" list
    # calculate the score
    # print the score
    def roll1(self):
        for i in range(3):
            die = random.randint(1, 6)
            self.dice.append(die)
        self.dice.sort(reverse=True)
        self.savedDice.append(self.dice[0])
        self.dice = []
        score = 0
        for i in self.savedDice:
            score += i
        print(self.name + " score: " + str(score))

    # make a function for the first roll, which will roll and add 2 dice to the empty list "dice"
    # sort the dice in descending order
    # move the highest dice into a "savedDice" list
    # calculate the score
    # print the score
    def roll2(self):
        for i in range(2):
            die = random.randint(1, 6)
            self.dice.append(die)
        self.dice.sort(reverse=True)
        self.savedDice.append(self.dice[0])
        self.dice = []
        score = 0
        for i in self.savedDice:
            score += i
        print(self.name + " score: " + str(score))

    # roll 1 die, and add it to saved dice (no need to sort for highest die)
    # calculate the final score
    def roll3(self):
        die = random.randint(1, 6)
        self.savedDice.append(die)

        for i in self.savedDice:
            self.finalscore += i
        print(self.name + " final score: " + str(self.finalscore))

    # print the currently saved dice from list "savedDice"
    def __str__(self):
        return self.name + " currently saved dice: " + str(self.savedDice)


# function for round 1 organizes the first roll
def roundone():
    print("Roll 1:")
    p1.roll1()
    p2.roll1()
    p3.roll1()
    p4.roll1()
    print("\n")


# function for round 2 organizes the first roll
def roundtwo():
    print("Roll 2:")
    p1.roll2()
    p2.roll2()
    p3.roll2()
    p4.roll2()
    print("\n")


# function for round 3 organizes the first roll
def roundthree():
    print("Final roll:")
    p1.roll3()
    p2.roll3()
    p3.roll3()
    p4.roll3()
    print("\n")


# function for results calculates the winners
def results():
    # make a list "finalScores"
    finalScores = []
    # append all 4 player's scores
    finalScores.append(p1.finalscore)
    finalScores.append(p2.finalscore)
    finalScores.append(p3.finalscore)
    finalScores.append(p4.finalscore)
    # sort them in descending order
    finalScores.sort(reverse=True)
    # check which player's final scores match the max number in "finalScores" and print them as the winner
    if p1.finalscore == finalScores[0]:
        print(p1.name + " Wins!")

    if p2.finalscore == finalScores[0]:
        print(p2.name + " Wins!")

    if p3.finalscore == finalScores[0]:
        print(p3.name + " Wins!")

    if p4.finalscore == finalScores[0]:
        print(p4.name + " Wins!")


p1 = Player("Bob")
p2 = Player("Rob")
p3 = Player("Knob")
p4 = Player("Dob")

roundone()
roundtwo()
roundthree()
results()
