#-----------------------
#CS110
#Adam Clements
#Pokemon Pay Calculator
#-----------------------
#ask for a paycode
code = int(input("Please input your paycode: "))
#if their paycode is 1, tell them they are a pokemon trainer and their salary
if code == 1:
    print("Pokemon Trainer: Fixed weekly salary of $1000")
#if their paycode is 2, then ask how many hours they worked in the week
elif code == 2:
    #ask for how many hours they worked
    hours = int(input("How many hours did you work this week? "))
    if hours > 40:
        #figure out how many extra hours they worked
        extra = hours - 40
        #multiply the extra hours by 30 then add 800 for the normal 40 hours worked
        pay1 = int(extra) * 30 + 800
        print("Pokemon Gym Leader: This week you worked " + str(hours) + " hours and made $" + str(pay1))
        #otherwise just multiply their hours by 20
    else:
        pay1 = hours * 20
        print("Pokemon Gym Leader: This week you worked " + str(hours) + " hours and made $" + str(pay1))
elif code == 3:
    #ask how much they sold their pokemon for
    value = float(input('How much did you make from sales this week? '))
    #multiply value of pokemon by .2 and add 500 weekly salary
    pay3 = .2 * value + 500
    print("Pokemon Breeder: You sold $" + str(value) + " worth of Pokemon, and made a total of $" + str(pay3))
elif code == 4:
    #ask how many pokemon they stole
    stolen = int(input("How many pokemon did you steal this week? "))
    #multiply by 500 per pokemon
    pay4 = stolen * 500
    print("Team Rocket: This week you stole " + str(stolen) + " Pokemon, and earned $" + str(pay4))
else:
    print("Invalid paycode")




