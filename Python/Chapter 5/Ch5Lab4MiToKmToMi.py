#------------------------------
#Adam Clements
#CS110
#Mile to Km conerter
#------------------------------
#import necessary impoert (random)
import random
#define the mileToKm function(overloaded with 1 variable)
def mileToKm(num1):
    #multiply by conversion factor
    Kilometers = num1*1.609
    return Kilometers
#define the kmToMile function
def kmToMile(num2):
    #divide by conversion factor
    Miles = num2/1.609
    return Miles

def main():
    rand1 = random.randint(5,15)
    print("1 mile is " + str(mileToKm(1)) + " km.")
    print("1 km is " + str(kmToMile(1)) + " miles")
    print("Random test number: " + str(rand1))
    print("Inverse test: " + str(mileToKm(kmToMile(rand1))))

main()






