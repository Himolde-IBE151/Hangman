s = input("Type a name with 4 letters or more")
#print first letter of the string
print (s[0])
print (s[1])
print (s[2])
print (s[3])
print("The size of the string is", len(s))

#From now on the user may enter any amount of letters (at least one)

#They know how to ask for the first letter
#Ask if the user entered the first letter of your name
if (s[0] == 'A'):
    print("You wrote the first letter of my name")

#They know how to get the len of a string
#Ask for the len of a string

print("You wrote the last letter of my name")

#They know how to ask for the last letter
#Ask for the last character typed
if (s[len(s)-1] == 'n'):
    print("You wrote the last letter of my name")

#They know how to use logical operators
#Ask if the user entered the first letter of your name
if (s[0] == 'A') and (s[1] == 'n') and (s[2] == 'o') and (s[3] == 'l') and  (s[4] == 'a') and (s[5] == 'n'):
    print("You wrote my name!")
