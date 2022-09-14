#---------------------------------
#Adam Clements
#Roster class
#   make a roster class and a student class
#   in the roster class, define subject, number, name, and professor of the class
#   make a function to add a student
#   make a function to remove a student
#   make a __str__ function to print the roster
#--------------------------------
#create the roster class
class Roster:
    #when initiated, ask for class details
    def __init__(self,subject,number,name,professor):
        self.sub = subject
        self.num = number
        self.name = name
        self.prof = professor
        self.students = Student.students
    #make a function to add a student
    def addStudent(self,firstname,lastname,site):
        self.Firstname = firstname
        self.Lastname = lastname
        self.site = site
        Student.__init__(Student,self.Firstname,self.Lastname,self.site)
    #make a function to remove a student
    def removeStudent(self,firstname,lastname,site):
        #call which student to remove
        student = (firstname + " " + lastname + " " + site + "")
        #search through the roster for the student, and remove them if they exist
        for i in Student.students:
            if i == student:
                Student.students.remove(student)
            else:
                print("Student does not exist")
    #make a __str__ function to print the whole roster and class details
    def __str__(self):
        print(self.sub + " " + self.num + ": " + self.name + "\nProfessor: " + self.prof + "\nRoster:\n First Last Site")
        for a in range(len(Student.students)):
            print(" " + Student.students[a])
#make a student class
class Student:
    #make a list of all students
    students = []
    #make a function to add a student to the list of students
    def __init__(self,firstname,lastname,site):
        newstudent = (firstname + " " + lastname + " " + site + "")
        self.students.append(newstudent)

#make a class for CS110 with professor being Dr. Dostert
r = Roster("CS","110","Intro to Computer Science","Dr. Dostert")
#add 4 students
r.addStudent("Ben","Neb","GSSM")
r.addStudent("Liz","Zil","LTC")
r.addStudent("Rad","Dar","Liberty")
r.addStudent("Van","Nav","Mayo")
#print the roster
r.__str__()
#remove 1 student
r.removeStudent("Ben","Neb","GSSM")
#print new roster
r.__str__()
#add a new student who was not previously removed
r.addStudent("Sam","Mas","GSSM")
#print the new roster
r.__str__()
