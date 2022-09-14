#------------------------------------------
#Adam Clements
#Grade calculator-
#   -calculate the average of a student
#   -12 hw assignments (out of 12 points) (25%)
#   -3 exams (25%)
#   -1 final (50%)
#-----------------------------------------
#open grades.txt as readable
g = open('grades.txt','r')
#run a loop to keep reading lines
while True:
    #make some variables
    hw = []
    exams = []
    hwOverall = 0
    examsOverall = 0
    #try to readline
    try:
        name = g.readline().strip()
    except ValueError:
        g.close()
        exit()
    #try to read 12 lines for the hw assignments (all multiplied by 10) except a valueError will end the code (becuase it hit the end of the code)
    for a in range(12):
        try:
            hw.append(int(g.readline().strip())*10)
        except ValueError:
            g.close()
            exit()
    #try to read 3 lines for the exams, except a valueError will end the code (becuase it hit the end of the code)
    for a in range(3):
        try:
            exams.append(int(g.readline().strip()))
        except ValueError:
            g.close()
            exit()
    #try to read 1 last line for the exam, execpt if it gives a valueError, it will exit
    try:
        final = int(g.readline().strip())
    except ValueError:
        g.close()
        exit()
    #sort and take out the lowest hw grade
    hw.sort()
    hw.pop(0)
    #sort the exams
    exams.sort()
    #check if the final is a higher score than the lowest exam
    if final > exams[0]:
        exams[0] = final
    #calculate the hw average
    for a in hw:
        hwOverall += a
    hwOverall = hwOverall/11
    #calculate the exam average
    for a in exams:
        examsOverall += a
    examsOverall = examsOverall/3

    #calculate the overall average
    avg = (hwOverall*.25) + (examsOverall*.25) + (final*.5)

    #print the result
    print(name + ": " + str(round(avg,2)))

