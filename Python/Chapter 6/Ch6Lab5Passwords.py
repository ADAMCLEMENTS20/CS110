# ------------------------------------------------
# Adam Clements
# CS110
# Summary: open the passwords document, read through
#   and change out letters with other symbols, and
#   capitalize each first letter
#-------------------------------------------------
#open the passwords file
f = open("passwords.txt","r")
#create a new passwords file
fnew = open("newPasswords.txt","a")
#read 1 letter
x = f.read(1)
#capitalize the first character
x = x.capitalize()
#write in thet character
fnew.write(str(x))
#start a loop to run until it reaches the end of the file
while x != "":
    #read 1 character
    x = f.read(1)
    #check if that character is "\n"
    if x == "\n":
        #if so, capitalize the next character
        x = f.read(1)
        x = x.capitalize()
        fnew.write("\n")
        fnew.write(x)
    #otherwise, check if the character is a, c, e, t, i, or s
    else:
        if x == "a":
            x = "4"
        elif x == "c":
            x = "("
        elif x == "e":
            x = 3
        elif x == "t":
            x = "7"
        elif x == "i":
            x = "!"
        elif x == "s":
            x = "$"
        #print the new character
        fnew.write(str(x))
#close both files
f.close()
fnew.close()
