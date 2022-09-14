# ------------------------------------------------
# Adam Clements
# CS110
# Summary: read all x values, and get the average
#   of those values, then do the same with the y's.
#   Then, run the distance formula for each set of
#   values, and see which is the max and the min.
#-------------------------------------------------

# open the coordinates file
f = open("coordinates.txt","r")
# create necessary variables
x = 0
ma = 0
mi = 999999
xval = 0
yval = 0
countx = 0
county = 0
#start a loop which reads each coordinate until it hits the last line
while x != "":
    #read the first line and set it to x value
    x = f.readline()
    #check if the file has reached the end
    if x == "":
        break
    else:
    #if there is a value, then add it to the runnung total, and add 1 to the count of values
        xval += float(x)
        countx += 1
    #read every other line and set it as a y value
    y = f.readline()
    #check if it has reached the end of the file
    if y == "":
        break
    else:
    #add the y value to the running total
        yval += float(y)
        county += 1
    #run the distance formula
    d = (((float(y)+0)**2 + (float(x)+0)**2)**(1/2))
    #check if the distance is a maximum or a minimum
    if d > ma:
        ma = d
    elif d < mi:
        mi = d
#calculate the average
avgx = xval/countx
avgy = yval/county
#print the values
print("Average X: " + str(round(avgx,2)))
print("Average Y: " + str(round(avgy,2)))
print("Maximum: " + str(round(ma,2)))
print("Minimum: " + str(round(mi,2)))
#close the file
f.close()
