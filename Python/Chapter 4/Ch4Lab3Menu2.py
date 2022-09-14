#----------------------
#CS110
#Adam Clements
#Taco Menu
#----------------------
#create all the variables in case not used
order = 1
tacocost = 0
sftacocost = 0
burritocost = 0
nachocost = 0
cchipcost = 0
drinkcost = 0
#welcome them to the taco shop
print("Welcome to the Taco Shop! (type 0 to end order)")
#ask what they want
while order != "0":
    order = input("What would you like? (taco, soft taco, burrito, nachos, cinnamon chips, drink) ")
    if order == "taco":
        num = input("How many? ")
        tacocost = float(num) * .89
        print("You ordered " + num + " taco(s)")
    elif order == "soft taco":
        num = input("How many? ")
        sftacocost = float(num) * .99
        print("You ordered " + num + " soft taco(s)")
    elif order == "burrito":
        num = input("How many? ")
        burritocost = float(num) * 1.89
        print("You ordered " + num + " burrito(s)")
    elif order == "nachos":
        num = input("How many? ")
        nachocost = float(num) * 2.99
        print("You ordered " + num + " nacho(s)")
    elif order == "cinnamon chips":
        num = input("How many? ")
        cchipcost = float(num) * .99
        print("You ordered " + num + " cinnamon chip(s)")
    elif order == "drink":
        num = input("What kind? (RC cola, Dr. Pepper, 7UP, or Iced Tea) ")
        drinkcost = .99
        print("You ordered a(n) " + num + " to drink")
    elif order == "0":
        break
    else:
        print("not a menu item")
#calculate the cost
total = (tacocost) + (sftacocost) + (burritocost) + (nachocost) + (cchipcost) + (drinkcost)
#display total
print("Thank you for ordering at the Taco Shop! You ordered for a total of $" + str(total) + ".")
