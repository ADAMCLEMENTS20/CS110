# --------------------------------------
# Adam Clements
# Taco shop menu - Make a menu using  item classes  for each menu item
# make 1 class for the menu
# make 6 classes for the 6 menu items
# make a __str__ function for each menu item
# add a function to add and order items from the menu
#print the menu, add some items, create an order of 5 items, redisplay the menu
#---------------------------------------
# create the main class
class TacoShopItem:
    # make a list for the
    tacoShopItems = [0, 0, 0, 0, 0, 0]

    # when initiated, initiate all 6 other classes with the number of items inputted
    def __init__(self, numtaco, numstaco, numburrito, numnacho, numcchips, numdrink):
        self.tacos = Taco(numtaco)
        self.softTacos = SoftTaco(numstaco)
        self.burritos = Burrito(numburrito)
        self.nachos = Nachos(numnacho)
        self.cchips = CinnamonChips(numcchips)
        self.drink = Drinks(numdrink)

    # add the number of items made to the current stock
    def addItems(self, numtaco, numstaco, numburrito, numnacho, numcchips, numdrink):
        TacoShopItem.tacoShopItems[0] += numtaco
        TacoShopItem.tacoShopItems[1] += numstaco
        TacoShopItem.tacoShopItems[2] += numburrito
        TacoShopItem.tacoShopItems[3] += numnacho
        TacoShopItem.tacoShopItems[4] += numcchips
        TacoShopItem.tacoShopItems[5] += numdrink

    # subtract the ordered number from the total
    def orderItems(self, numtaco, numstaco, numburrito, numnacho, numcchips, numdrink):
        # make sure there is enough stock
        if numtaco <= TacoShopItem.tacoShopItems[0]:
            TacoShopItem.tacoShopItems[0] -= numtaco
        # if there isnt, say there is not enough stock
        else:
            print("Not enough stock. Only " + str(TacoShopItem.tacoShopItems[0]) + " tacos remaining.")
        if numstaco <= TacoShopItem.tacoShopItems[1]:
            TacoShopItem.tacoShopItems[1] -= numstaco
        else:
            print("Not enough stock. Only " + str(TacoShopItem.tacoShopItems[1]) + " soft tacos remaining.")
        if numburrito <= TacoShopItem.tacoShopItems[2]:
            TacoShopItem.tacoShopItems[2] -= numburrito
        else:
            print("Not enough stock. Only " + str(TacoShopItem.tacoShopItems[2]) + " burritos remaining.")
        if numnacho <= TacoShopItem.tacoShopItems[3]:
            TacoShopItem.tacoShopItems[3] -= numnacho
        else:
            print("Not enough stock. Only " + str(TacoShopItem.tacoShopItems[3]) + " nachos remaining.")
        if numcchips <= TacoShopItem.tacoShopItems[4]:
            TacoShopItem.tacoShopItems[4] -= numcchips
        else:
            print("Not enough stock. Only " + str(TacoShopItem.tacoShopItems[4]) + " cinnamon chips remaining.")
        if numdrink <= TacoShopItem.tacoShopItems[5]:
            TacoShopItem.tacoShopItems[5] -= numdrink
        else:
            print("Not enough stock. Only " + str(TacoShopItem.tacoShopItems[5]) + " drinks remaining.")

    # print out the whole menu using the __str__ methods in the 6 individual classes
    def __str__(self):
        # |  Food  |  D e s c r i p t i o n  o f  f o o d | Cost | Units |
        print("______________________________________________________________________________")
        print("|_________________________Taco Shop Inventory________________________________|")
        print("|______Item______|_____________Description_________________|_Cost__|__Units__|")
        self.tacos.__str__()
        self.softTacos.__str__()
        self.burritos.__str__()
        self.nachos.__str__()
        self.cchips.__str__()
        self.drink.__str__()
        print("\n")


# make a class for each item
class Taco:
    # initialize each item with the original stock
    def __init__(self, amount):
        TacoShopItem.tacoShopItems[0] = amount

    # make a menu "row" for the item
    def __str__(self):
        print("|      Taco      | Beef, lettuce, and cheese in a shell    | $0.89 | " + str(
            TacoShopItem.tacoShopItems[0]) + "\t\t |")


class SoftTaco:
    def __init__(self, amount):
        TacoShopItem.tacoShopItems[1] = amount

    def __str__(self):
        print("|    Soft Taco   | Beef, lettuce, and cheese in a tortilla | $0.99 | " + str(
            TacoShopItem.tacoShopItems[1]) + "\t\t |")


class Burrito:
    def __init__(self, amount):
        TacoShopItem.tacoShopItems[2] = amount

    def __str__(self):
        print("|    Burrito     | Large tortilla with chicken and cheese  | $1.89 | " + str(
            TacoShopItem.tacoShopItems[2]) + "\t\t |")


class Nachos:
    def __init__(self, amount):
        TacoShopItem.tacoShopItems[3] = amount

    def __str__(self):
        print("|     Nachos     | Corn tortilla chips covered in cheese   | $2.99 | " + str(
            TacoShopItem.tacoShopItems[3]) + "\t\t |")


class CinnamonChips:
    def __init__(self, amount):
        TacoShopItem.tacoShopItems[4] = amount

    def __str__(self):
        print("| Cinnamon Chips | Small creamy cinnamon flavored morsels  | $2.99 | " + str(
            TacoShopItem.tacoShopItems[4]) + "\t\t |")


class Drinks:
    def __init__(self, amount):
        TacoShopItem.tacoShopItems[5] = amount

    def __str__(self):
        print("|     Drinks     | RC Cola, Dr. Pepper, 7UP, or tea        | $2.99 | " + str(
            TacoShopItem.tacoShopItems[5]) + "\t\t |")


# initiate the menu with 1 of each item
menu = TacoShopItem(1, 1, 1, 1, 1, 1)
# display the menu
menu.__str__()
# add 5 to each item total
menu.addItems(5, 5, 5, 5, 5, 5)
# display the menu
menu.__str__()
# order 1 soft taco, 3 burritos, and 1 cinnamon chips
menu.orderItems(0, 1, 3, 0, 1, 0)
# display the menu
menu.__str__()
# order too many of an item
menu.orderItems(10, 1, 1, 1, 1, 1)
# display the menu
menu.__str__()
