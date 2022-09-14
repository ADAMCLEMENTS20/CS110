#-------------------------------------------
#Adam Clements
#Info card
#CS110
#-------------------------------------------
#ask for Name, Age, Sex, Occupation, Street address number, street address name, city, state, zipcode, and Phone number
name = input("What is your full name? ")
age =  input("How old are you? ")
sex = input("What is your gender? ")
job = input("What is your occupation? ")
SAName = input("What is the name of your street? ")
SANum = input("What is your street address number? ")
city = input("What city do you live in? ")
state = input("What state do you live in?")
zip = input("What is your zipcode? ")
PN = input("What is your phone number? ")
#put the information into strings in order
l1 = str("| Name: " + name )
l2 = str("| Sex: " + sex)
l3 = str("| Age: " + age)
l4 = str("| Occupation: " + job)
l5 = str("| Address: " + SANum + " " + SAName)
l6 = str("|          " + city + ", " + state + " " + zip)
l7 = str("| Phone number: " + PN)
#add a variable for easy separation lines
l0 = ("|-------------------------------------")
#print the information into a card
print (l0)
print (l1)
print (l0)
print (l2)
print (l0)
print (l3)
print (l0)
print (l4)
print (l0)
print (l5)
print (l6)
print (l0)
print (l7)
