#--------------------------------------
#Adam Clements
#random list calculator
#create a list of random integers of size n, then calculate the average of those values and the standard deviation
#--------------------------------------
#import random to fill the list
import random
#ask how many values should go in the list
num = int(input("Input a number (1-10): "))
#create a variable to count, and the empty list
count = 0
list =[]
#check if it is a valid number
if num <= 0 or num > 10:
    print("Please enter a valid number")
#if it is a valid number, append new random values between 1 and 10, n times
else:
    while count < num:
        x = random.randint(1,10)
        list.append(x)
        count+=1
    #calculate the average
    av = sum(list)/len(list)
    #calculate standard deviation
    #calculate the list - the average
    avlist = [x - av for x in list]
    #square every value
    avlistsq = [x**2 for x in avlist]
    #take the average of that list and the square root
    SD = (sum(avlistsq)/len(avlistsq))**(1/2)
    #print every value
    print(list)
    print("Average:")
    print(av)
    print("Standard Deviation:")
    print(SD)
