#------------------------------------------
# Adam Clements
# CS110
# Student class:
#   Create a class called student, which takes 5 inputs (first name, last name, site, year, and gpa)
#   add 3 functions to: Change Grade, Change GPA, and print out info in format:
#   Name:
#   Site:
#   Year:
#   GPA:
#------------------------------------------------
#create the class
class Student:
    #make the initialization class to take the 5 inputs, and set them to variables
    def __init__(self, FirstName, LastName, Site, Year, GPA):
        self.name = (FirstName + " " + LastName)
        self.site = Site
        self.year = Year
        self.gpa = GPA

    #print the info in a nice format
    def __str__(self):
        print("Name: " + self.name + "\nSite: " + self.site + "\nYear: " + self.year + "\nGPA: " + str(self.gpa) + "\n")
    #make a change year function to change the year to any grade level depending on input
    def changeYear(self):
        loop = True
        print("1. Freshman")
        print("2. Sophomore")
        print("3. Junior")
        print("4. Senior")

        while loop:
            yr = int(input("Choose which grade: "))
            if yr == 1:
                self.year = "FR"
                loop = False
            elif yr == 2:
                self.year = "SO"
                loop = False
            elif yr == 3:
                self.year = "JR"
                loop = False
            elif yr == 4:
                self.year = "SR"
                loop = False
            else:
                print("invalid year")
                loop = True
    def changeGPA(self, gpa):
        self.gpa = gpa

#initialize the 2 students
Student1 = Student("Ben", "Neb", "GSSM", "SO", 3.23)
Student2 = Student("Deb", "Bed", "Liberty", "JR", 2.55)
#print out the 2 student's information
Student1.__str__()
Student2.__str__()
