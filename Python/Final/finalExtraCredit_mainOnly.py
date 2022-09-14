# Your classes should go here
#  Do NOT use any pre-built packages to perform the below operations, each should
#   be coded using regular mathematics operation (+,-,*,/), no numpy or math functions other
#   than math.nan

A = Matrix2x2(1,2,3,4)
B = Matrix2x2(4,3,2,1)

print('Addition: A+B')
print(A,"+\n",B,"=\n",A+B,sep="")
input(),print('Subtraction: A-B')
print(A,"-\n",B,"=\n",A-B,sep="")
input(),print('Multiplication: A*B')
print(A,"*\n",B,"=\n",A*B,sep="")
input(),print('Multiplication: B*A')
print(B,"*\n",A,"=\n",B*A,sep="")
input(),print('Powers: A^3 ')
print(A,"^3","\n=\n",A**3,sep="")
input(),print('Inverse: A^-1 ')
print(A,"^-1","\n=\n",A**(-1),sep="")
input(),print('Inverse with powers: A^-3  = (A^-1)^3')
print(A,"^-3","\n=\n",A**(-3),sep="")
