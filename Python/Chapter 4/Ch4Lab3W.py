#------------------------------------
#Adam Clements
#CS110
#W generator
#------------------------------------
#ask how tall the 'W' should be
n= int(input("how tall? (max:40) "))
#check if the number is less than 40
if n <= 40:
    #find the middle of the W
    mid = int(n//2)
    #loop for number of times 'n' is
    for i in range(n):
    #loop again for number of times 'n' is (make a coordinate grid)
      for j in range(n):
          #print a vertical line of stars on j==0 and j == (n-1) or on the diagonals between the sides
        if j==0 or j==n-1 or ((i+j==(n-1)) and j<=mid) or (i==j and j>mid):
          print("*",end=" ")
          #if it doesnt meet the criteria (spot on coordinate grid) print a space
        else:
          print(end="  ")
      print()
#if the number is larger than 40, give an error message
else:
    print("Please enter a number lower than 40")
