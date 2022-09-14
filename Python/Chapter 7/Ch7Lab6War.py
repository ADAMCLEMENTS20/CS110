#--------------------------------------
#Adam Clements
#War game
#make a deck of cards, shuffle it, deal it out, draw the top card from each hand, compare the value of the cards, higher value wins, if same value, add a tie
#--------------------------------------
#import random to shuffle
import random
#create necessary variables
deck = []
card_points =['A','K','Q','J','2','3','4','5','6','7','8','9','T']
card_signs =['H','C','D','S']
#create the deck of cards
for points in range(len(card_points)):
    for signs in range (len(card_signs)):
        deck.append(card_points[points]+card_signs[signs])
#shuffle the deck
random.shuffle(deck)
#create the 2 players empty hands
p1 = []
p2 = []
j = False
#split the deck between the 2 players
while len(deck) > 0:
    p1.append(deck[0])
    deck.remove(deck[0])
    p2.append(deck[0])
    deck.remove(deck[0])
#create variables to hold the number of wins
p1wins = 0
p2wins = 0
ties = 0
#while player 2's deck is not empty
while len(p2) != 0:
    #print the cards
    print(p1[0])
    print(p2[0])
    #separate the suit from the value
    p1sep = [char for char in p1[0]]
    p2sep = [char for char in p2[0]]
    p1val = p1sep[0]
    p2val = p2sep[0]
    #if the value is a letter, change it into a value
    if p1val == "A":
        p1val = 14
    elif p1val == "T":
        p1val = 10
    elif p1val == "J":
        p1val = 11
    elif p1val == "Q":
        p1val = 12
    elif p1val == "K":
        p1val = 13
    else:
        p1val = int(p1val)
    if p2val == "A":
        p2val = 14
    elif p2val == "T":
        p2val = 10
    elif p2val == "J":
        p2val = 11
    elif p2val == "Q":
        p2val = 12
    elif p2val == "K":
        p2val = 13
    else:
        p2val = int(p2val)
    #check which value is larger (or if they are equal) then add it to the count
    if p1val > p2val:
        print("Player 1 wins!")
        p1wins +=1
    elif p2val > p1val:
        print("Player 2 wins!")
        p2wins += 1
    else:
        print("Tie!")
        ties += 1
    p1.remove(p1[0])
    p2.remove(p2[0])
#print each number of wins
print("Player 1 Wins: " + str(p1wins))
print("Player 2 Wins: " + str(p2wins))
print("Ties: " + str(ties))
