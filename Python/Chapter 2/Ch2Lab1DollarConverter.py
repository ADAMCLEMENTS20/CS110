#-------------------------------------------
#Adam Clements
#Minimum bill converter
#CS110
#-------------------------------------------
#ask for a dollar amount in integer form
dollars = int(input("Enter a dollar amount as an integer (max $100,000):"))
#create variables for all bill denominations and remainder
hundreds = 0
fifties = 0
twenties = 0
tens = 0
fives = 0
ones = 0
remain = 0
#create a max dollar amount
if dollars >= 100000:
    print("error: enter a smaller value")
#create a minimum dollar amount
elif dollars <= 0:
    print("error: enter a value larger than 0")
#check how many times 100 can go into the dollar amount inputted and add to the variable for said bill
hundreds = dollars//100
remain = dollars%100
#check how many times 50 can go into the remaining dollar amount and add to the variable for said bill
fifties = remain//50
remain = remain%50
#check how many times 20 can go into the remaining dollar amount and add to the variable for said bill
twenties = remain//20
remain = remain%20
#check how many times 10 can go into the remaining dollar amount and add to the variable for said bill
tens = remain//10
remain = remain%10
#check how many times 5 can go into the remaining dollar amount and add to the variable for said bill
fives = remain//5
remain = remain%5
#check how many times 1 can go into the remaining dollar amount and add to the variable for said bill
ones = remain
#print the original value and the amount of bills necessary for each value
print ("$" + str(dollars))
print ("One-hundred dollar bills: " + str(hundreds))
print ("Fifty dollar bills: " + str(fifties))
print ("Twenty dollar bills: " + str(twenties))
print ("Ten dollar bills: " + str(tens))
print ("Five dollar bills: " + str(fives))
print ("One dollar bills: " + str(ones))
