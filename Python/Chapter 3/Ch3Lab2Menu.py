#----------------------
#CS110
#Adam Clements
#Taco Menu
#----------------------
#welcome them to the taco shop
print("Welcome to the Taco Shop!")
#ask if they want a taco
taco = input("Would you like a taco? [Y/N] ")
#if yes, ask how many
if taco == "Y":
    numtaco = int(input("How many would you like? "))
else:
    numtaco = 0
#then ask if they want a soft taco
sfttaco = input("Would you like a soft taco? [Y/N] ")
#if yes ask how many
if sfttaco == "Y":
    numsfttaco = int(input("How many would you like? "))
else:
    numsfttaco = 0
#then ask if they want a burrito
burrito = input("Would you like a burrito? [Y/N] ")
#if yes, then ask how many
if burrito == "Y":
    numburrito = int(input("How many would you like? "))
else:
    numburrito = 0
#then ask if they want nachos
nachos = input("Would you like nachos? [Y/N] ")
#ask how mnay nachos they want
if nachos == "Y":
    numnacho = int(input("How many would you like? "))
else:
    numnacho = 0
#then ask if they want to order cinnamon chips
cchips = input("Would you like cinnamon chips? [Y/N] ")
#if yes, how many
if cchips == "Y":
    numcchips = int(input("How many would you like? "))
else:
    numcchips = 0
#ask if they want a drink
drink = input("Would you like a drink? [Y/N] ")
#if yes, ask which drink (RC cola, drpepper, 7up, iced tea)
if drink == "Y":
    drnkcost = .99
    drink = input("Which drink would you like? (RC Cola, Dr. Pepper, 7UP, or Iced Tea) ")
else:
    drink = "No drink"
    drnkcost = 0
#calculate the cost
cost = float(numtaco * .89) + float(numsfttaco * .99) + float(numburrito * 1.89) + float(numnacho * 2.99) + float(numcchips * .99) + drnkcost
#display order and total
print("Thank you for ordering at the Taco Shop! You ordered " + str(numtaco) + " taco(s), " + str(numsfttaco) + " soft taco(s), " + str(numburrito) + " burritto(s), " + str(numnacho) + " nacho(s), " + str(numcchips) + " order(s) of cinnamon chips, and " + drink + " for a total of $" + str(cost) + ".")
