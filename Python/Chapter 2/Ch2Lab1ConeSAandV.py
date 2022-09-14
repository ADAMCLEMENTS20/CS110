#-------------------------------------------
#Adam Clements
#Surface area and volume of a cone calculator
#CS110
#-------------------------------------------
#SA = 3.1415r^2 + 3.1415rl
#V = 3.1415r^2(h/3)
#ask for the height and radius of a cone
h = float(input("Type the height of your cone: "))
r = float(input("Type the radius of the base of your cone: "))
#calculate the slant of the cone
l = float(((h**2)+(r**2))**(1/2))
#run the formula for surface area using inputted variables and slant
SA = 3.1415*(r**2) + 3.1415*(r*l)
#run formula for volume using inputted variables
V = 3.1415*(r**2)*(h/3)
#print volume and surface area
print("Volume: " + str(V))
print("Surface Area: " + str(SA))
