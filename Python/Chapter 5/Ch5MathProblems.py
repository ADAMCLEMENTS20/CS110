#------------------------------
#Adam Clements
#CS110
#Math Practice
#------------------------------
#add necessary inputs
import random
#add necessary variables
realans = 1
signum = 0
#define the make a problem function
def makeProblem():
    #randomize the numbers and sign
    num1 = random.randint(1,9)
    num2 = random.randint(1,9)
    signnum = random.randint(0,2)
    #if the sign is a plus, add the numbers
    if int(signnum) == 1:
        sign = "+"
        realans = num1+num2
    #otherwise, make it multiplication
    else:
        sign = "*"
        realans = num1*num2
    #write out the problem
    print("What is " + str(num1) + sign + str(num2) + "? (type 0 to stop)")
    #return the real answer value
    return realans
def main():
    #assign a necessary variable
    ans = 1
    #loop to keep sending problems when 1 is correctly answered
    while ans != 0:
        looping = True
        #make a problem, and assign its answer to the variable realans
        realans = makeProblem()
        #make a loop to continue until the correct answer is given
        while looping:
            ans = input()
            if int(ans) == realans:
                looping = False
                print("Correct!")
            elif int(ans) == 0:
                looping = False
                ans = 0
                break
            else:
                print("Incorrect, Try again.")

#call the main function
main()
