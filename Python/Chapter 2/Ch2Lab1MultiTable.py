#-------------------------------------------
#Adam Clements
#Multiplication table 5x5
#CS110
#-------------------------------------------
#create variables for all multiplications in table
#multiples of 1
t11 = 1*1
t21 = 1*2
t31 = 1*3
t41 = 1*4
t51 = 1*5
#multiples of 2
t22 = 2*2
t32 = 2*3
t42 = 2*4
t52 = 2*5
#multiples of 3
t33 = 3*3
t43 = 3*4
t53 = 3*5
#multiples of 4
t44 = 4*4
t54 = 4*5
#multiple of 5
t55 = 5*5
#create header
header =  "|  5x5\t|\t1\t|\t2\t|\t3\t|\t4\t|\t5\t|"
#print header and row 1
print(header)
print("|\t1\t|\t" + str(t11) + "\t\t" + str(t21) + "\t\t" + str(t31) + "\t\t" + str(t41) + "\t\t" + str(t51))
#print row 2
print("|\t2\t|\t" + str(t21) + "\t\t" + str(t22) + "\t\t" + str(t32) + "\t\t" + str(t42) + "\t\t" + str(t52))
#print row 3
print("|\t3\t|\t" + str(t31) + "\t\t" + str(t32) + "\t\t" + str(t33) + "\t\t" + str(t43) + "\t\t" + str(t53))
#print row 4
print("|\t4\t|\t" + str(t41) + "\t\t" + str(t42) + "\t\t" + str(t43) + "\t\t" + str(t44) + "\t\t" + str(t54))
#print row 5
print("|\t5\t|\t" + str(t51) + "\t\t" + str(t52) + "\t\t" + str(t53) + "\t\t" + str(t54) + "\t\t" + str(t55))


