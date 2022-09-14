#-------------------------------
#Adam Clements
#Blackjack game:
#   -make a functional blackjack game
#   -use at least 2 classes (Deck and Card)
#   -the computer will be player 2
#   -computer hits on 17 and below
#   -ask the player to hit or stand
#   -compare the final scores and tell who wins
#-------------------------------
#import random for shuffling the deck
import random
#create the deck class
class Deck:
    #create some variables to be used to create the deck
    deck = []
    suit = ["S","D","H","C"]
    rank = ["2","3","4","5","6","7","8","9","T","J","Q","K","A"]
    #__init__ function for the deck, which creates a normal 52 card playing card deck
    def __init__(self):
        #use 2 "for loops" to pair each suit and number
        for s in self.suit:
            for r in self.rank:
                #initialize the card __init__ class to make a card and add it to the deck
                Card(r,s)

#create class "Player" (not required, but very useful)
class Player:
    #give the player a name, and create the player
    def __init__(self,name):
        self.player = str(name)
        self.hand = []
        self.currentVal = 0
    #create a hand for a player
    def newHand(self):
        if len(self.hand) > 0:
            for b in range(len(self.hand)):
                self.hand.remove(self.hand[0])
        for b in range(2):
            self.hand.append(Deck.deck[0])
            deck.deck.remove(deck.deck[0])
            self.addValue(self.getValue(-1))
    #get the value of a single card by separating the characters, and getting the value of the "rank" variable
    def getValue(self,card):
        card = self.hand[card]
        sep = list(card)
        return sep[0]
    #add the value of a card to the player's currentVal variable
    def addValue(self,val):
        addedval = 0
        #check what card type it is, and its value
        if val == "T" or val == "J" or val == "Q" or val == "K":
            addedval = 10
        #check if 11 would make a player bust, and if not, make it worth 11. otherwise, make it 1
        elif val == "A":
            if self.currentVal >= 11:
                addedval = 1
            else:
                addedval = 11
        else:
            addedval = int(val)
        self.currentVal += addedval
    #hit to get a new card
    def hit(self):
        self.hand.append(Deck.deck[0])
        Deck.deck.remove(Deck.deck[0])
        self.addValue(self.getValue(-1))
    #print the hand of each player (with the player's name)
    def __str__(self):
        return self.player + " Hand:" + str(self.hand) + "| Value: " + str(self.currentVal)
#create class card with variables rank and suit
class Card:
    rank = 0
    suit = ""
    #__init__ the class, and overload it with a rank and suit (made in deck __init__ function) and add it to list deck
    def __init__(self,rank,suit):
        self.suit = suit
        self.rank = rank
        c = (str(self.rank)+str(self.suit))
        Deck.deck.append(c)



#make a function to organize a player's turn
def playerTurn():
    hitorstand = "hit"
    #make a loop, so a player can continue hitting, or if there is an error, they can retry typing in a valid phrase
    #also, check for a value over 21
    while hitorstand.lower() == "hit" and p1.currentVal < 21:
        #ask if they would like to hit or stand
        #print out the player's cards
        print(p1)
        print("\nComputer Hand: " + str(com.hand[0]) + ", ?\n")
        #try/except block in case of invalid inputs
        try:
            hitorstand = input("Would you like to hit or stand? (enter 'hit' or 'stand'): ")
        except:
            print("Invalid input, please enter 'hit' or 'stand' ")
            hitorstand = "hit"
        #if "stand" is input, move on to the computer's turn
        if hitorstand.lower() == "stand" or p1.currentVal > 21:
             comTurn()
        #if they hit, add a card, and show the new hand and value
        elif hitorstand.lower() == "hit":
            p1.hit()
        #make sure there are no invalid inputs
        else:
            print("Invalid input, please enter 'hit' or 'stand' ")
            hitorstand = "hit"
    #if the player busts, send it to the computer's turn
    comTurn()

#comTurn function to organize code more
def comTurn():
    #check if the player has busted, and if so, end the game immediately
    if p1.currentVal <= 21:
        #if the computer has less of = to 17 value, they hit
        while com.currentVal <= 17:
            com.hit()
            #check if the computer busted
        if com.currentVal > 21:
            print(com)
            print("You Win! Computer Busted.")
            exit()
        #check if you have a higher score than the computer when done hitting
        if p1.currentVal > com.currentVal:
            print(com)
            print("You Win!")
            exit()
        #check if the computer has a higher score than the player when done hitting
        elif com.currentVal > p1.currentVal:
            print(com)
            print("You Lose.")
            exit()
        #otherwise, the scores are equal, and it is a tie
        else:
            print(com)
            print("Tie!")
            exit()
    else:
        print("Busted! You Lose.")
        exit()

#create the 2 players
p1 = Player("Player")
com = Player("Computer")
#create a deck
deck = Deck()
#shuffle the deck
random.shuffle(Deck.deck)
#give both players a hand
p1.newHand()
com.newHand()
#begin the "playerTurn" (main) function
playerTurn()
