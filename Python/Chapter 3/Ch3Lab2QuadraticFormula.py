#----------------------------------------
#CS110
#Adam Clements
#Quadratic Formula Calculator
#----------------------------------------
#(-b + (b**2 - 4 ac)**(1/2))/2
#(-b - (b**2 - 4 ac)**(1/2))/2
#ask for a, b, and c
a = input("Input \"a\" ((a)x^2 + bx + c): ")
b = input("Input \"b\" (ax^2 + (b)x + c): ")
c = input("Input \"c\" (ax^2 + bx + (c)): ")
#test the discriminant to make sure it has any real soulutions
real = int(b)**2 - (4*int(a)*int(c))
if int(real) < 0:
    print("No real soulutions")
    #otherwise, run the quadratic formula
else:
    plus = (int(b)*-1 + (int(b)**2 - 4*int(a)*int(c))**(1/2))/2
    minus = (int(b)*-1 - (int(b)**2 - 4*int(a)*int(c))**(1/2))/2
    #check if both solutions are the same number
    if int(minus) == int(plus):
        #print the 1 solution
        print("One real solution:" + str(plus))
    #otherwise, print both solutions
    else:
        print("Two real solutions: " + str(plus) + ", and " + str(minus))
