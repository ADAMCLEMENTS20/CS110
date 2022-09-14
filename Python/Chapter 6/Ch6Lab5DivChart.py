# ------------------------------------------------
# Adam Clements
# CS110
# Summary: calculate all of the numbers in a division
#   chart for 1/8, 1/4, 1/2, 0, 2, 4, and 8.
#-------------------------------------------------
#import fractions to make the final product look nicer
from fractions import Fraction
#open/create a file
f = open("divPowerTwo.txt",'a')
#set necessary variables
t = .125
s = .125
#write out the header
f.write("\t/\t|\t1/8\t\t1/4\t\t1/2\t\t0\t\t2\t\t4\t\t8\n------------------------------------------------------------------\n")
#run a loop until it has multiplied all of the values out
while s != 16:
    #set a vallue for t (top) (.125 = 1/8)
    t = .125
    #calculate the chart value
    a = s/t
    #double t
    t *= 2
    b = s/t
    t *= 2
    c = s/t
    t = 0
    #try to run the code (divide by zero)
    try:
        d = str(format(round((s/t),2),'.2f'))
    #if there is a zero divide error, set d's value to "NaN"
    except ZeroDivisionError:
        d = "NaN"
    #continue as normal
    t = 2
    e = s/t
    t *= 2
    g = s/t
    t *= 2
    h = s/t
    #print 1 line
    f.write("\t" + str(Fraction(s)) + "\t|\t" + str(format(round(a,2),'.2f')) + "\t" + str(format(round(b,2),'.2f')) + "\t" + str(format(round(c,2),'.2f')) + "\t" + d + "\t\t" + str(format(round(e,2),'.2f')) + "\t" + str(format(round(g,2),'.2f')) + "\t" + str(format(round(h,2),'.2f')) + "\n")
    s *= 2
#close the file
f.close()
