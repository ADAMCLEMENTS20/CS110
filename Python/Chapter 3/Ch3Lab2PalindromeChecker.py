#----------------------
#CS110
#Adam Clements
#Palindrome checker
#----------------------
#ask for the number
n = int(input("input a 5 digit number: "))
#add a variable for the reversed number
r = 0
#reverse the number by moving 1 digit
lastDigit = n%10
r = r*10 + lastDigit
ne = n//10
#move the second number to the back
lastDigit = ne%10
r = r*10 + lastDigit
ne = ne//10
#move the third number
lastDigit = ne%10
r = r*10 + lastDigit
ne = ne//10
#move the fourth number
lastDigit = ne%10
r = r*10 + lastDigit
ne = ne//10
#move the last number
lastDigit = ne%10
r = r*10 + lastDigit
ne = ne//10
#check if the reversed number is the same as the original
if n == r:
    print("Your number is a palindrome")
else:
    print("Your number is not a palindrome")
