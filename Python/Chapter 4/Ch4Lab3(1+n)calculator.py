#-------------------------
#Adam Clements
#CS110
#(1+n) Calculator
#-------------------------
#n + n-1 + n-2 + n-3 + n-4 + n-5....
#ask for the integer
n = int(input("Input an integer: "))
#begin loop that runs for n times (n being the input)
for k in range(1, n+1):
    #run this equation n times
    a = k*(k+1)/2
#print the final result once the loop ends
print(a)
