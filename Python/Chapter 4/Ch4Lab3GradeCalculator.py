#-------------------------
#Adam Clements
#CS110
#Grade calculator
#-------------------------
#create a variable to start the loop
hw = 1
#create variables to edit later
hwgrade = 0
counter = 0
#ask for the 3 test grades, and 1 exam
test1 = input ("Please input your first test grade: ")
test2 = input ("Please input your 2nd test grade: ")
test3 = input ("Please input your 3rd test grade: ")
exam = input("Please input your final exam grade: ")
#begin loop to continue until -1 is entered into the hw input
while hw != -1:
    #ask for the hw grades
    hw = input("Please input your homework grades (1 at a time, then input -1 to stop) ")
    #make sure the hw input doesnt equal -1
    if int(hw) != -1:
        #add hw to running total
        hwgrade += int(hw)
        #increase hw counter by 1
        counter += 1
    else:
        break
#combine all test grades into 1
testgrade = int(test1) + int(test2) + int(test3)
examgrade = exam
#calculate the final total
final = (float(float(testgrade)/.5) + float(float(examgrade)/.25) + float(float(hwgrade / counter)/.25))/14
#print the total
print(final)
