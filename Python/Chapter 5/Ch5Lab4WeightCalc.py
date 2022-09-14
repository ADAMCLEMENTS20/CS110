#------------------------------
#Adam Clements
#CS110
#Weight calculator
#------------------------------
#create necessary variables
kg = "kg"
g = "g"
#define the calcWeight function
def calcWeight(num,unit):
    #check which unit is inputted
    if unit == kg:
        #if kg, then multiply vaiables accordingly
        lbs = num*2.205
        n = num*9.807
        #if g, then multiply accordingly
    elif unit == g:
        lbs = num/453.592
        n = num*0.009807
        #if neither, assign "nan" to the values
    else:
        lbs = "nan"
        n = "nan"
    return lbs,n

#define the main function
def main():
    #turn the touple into 2 variables
    lbs1,n1 = calcWeight(20,kg)
    #print the final output
    print("20kg mass, on earth, is equal to " + str(round(lbs1,1)) + " pounds or " + str(round(n1,1)) + " newtons." )
    lbs2,n2 = calcWeight(1337,g)
    print("1337g mass, on earth, is equal to " + str(round(lbs2,1)) + " pounds or " + str(round(n2,1)) + " newtons." )

#call the main function
main()
