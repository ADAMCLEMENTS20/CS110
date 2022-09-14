#------------------------------
#Adam Clements
#CS110
#QB Passer Rating
#------------------------------
#define the function for passer rating
def nflQB(c,a,y,t,i):
    #input all variables into the equation for passer rating
    rating = (25/12)*(((40*c)+(a)+(2*y)+(160*t)-(200*i))/a)
    return rating
#define the "main" function
def main():
    #input all stats for each player in the function, and print the rating
    print("Dak Prescott Passer Rating: " + str(nflQB(356,526,3885,22,8)))
    print("Cam Newton Passer Rating: " + str(nflQB(320,471,3395,24,13)))

#call the main function
main()
