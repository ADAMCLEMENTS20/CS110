#----------------------------
#Adam Clements
#Rational Number-
#   make a class of rationalnumber
#   add a function to add
#   add a function to subtract
#   add a function to multiply
#   add a function to divide
#   add a __str__ function to print the result
#----------------------------
#create the class
class RationalNumber:
    #add a variable for numerator and denominator
    num = 0
    den = 0
    #add an __init__ function to create a rational number
    def __init__(self, numerator, denominator):
        self.num = numerator
        self.den = denominator
    #multiply the rational numbers, and return the new numerator and denominator
    def mult(self, rationalln):
        print(str(self.num) + "/" + str(self.den) + " * " + str(rationalln.num) + "/" + str(rationalln.den) + "=")
        return RationalNumber(self.num * rationalln.num, self.den * rationalln.den)
    #divide the rational numbers, and return the new numerator and denominator
    def divide(self, rationalln):
        print("(" + str(self.num) + "/" + str(self.den) + ") / (" + str(rationalln.num) + "/" + str(rationalln.den) + ") =")
        return RationalNumber(self.num * rationalln.den, self.den * rationalln.num)
    #add the rational numbers, and return the new numerator and denominator
    def add(self, rationalln):
        print(str(self.num) + "/" + str(self.den) + " + " + str(rationalln.num) + "/" + str(rationalln.den) + "=")
        return RationalNumber((self.num * rationalln.den + self.den * rationalln.num), (self.den * rationalln.den))
    #subtract the rational numbers, and return the new numerator and denominator
    def subtract(self, rationalln):
        print(str(self.num) + "/" + str(self.den) + " - " + str(rationalln.num) + "/" + str(rationalln.den) + "=")
        return RationalNumber(self.num * rationalln.den - self.den * rationalln.num, self.den * rationalln.den)
    #print the numerator/denominator
    def __str__(self):
        print(str(self.num) + "/" + str(self.den))

#make the first fraction (3/7)
rat1 = RationalNumber(3, 7)
#make the second fraction (4/9)
rat2 = RationalNumber(4, 9)
#print the addition
RationalNumber.__str__(RationalNumber.add(rat1, rat2))
#print the subtraction
RationalNumber.__str__(RationalNumber.subtract(rat1, rat2))
#print the multiplication
RationalNumber.__str__(RationalNumber.mult(rat1, rat2))
#print the division
RationalNumber.__str__(RationalNumber.divide(rat1, rat2))
