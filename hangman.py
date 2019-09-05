# Guess a letter inside a word.
#We have a secret word (a string), the user will type ONLY 1 LETTER and the position where it appears on the secret word. If (s)he succeds the program should print  "Sucess, you won!" otherwise print "You lost!"
#Remember that string's first index is 0
secretWord = "Orangutan"
s = input ("Write a character: ")
p = int(input ("Write the position: "))
if s == secretWord[p]:
    print("You won! \N{grinning face with smiling eyes}")
else:
    print("You lost \N{face with rolling eyes}") 
    #print("\N{grimacing face}")
    #print("😢")
    #https://www.geeksforgeeks.org/python-program-to-print-emojis/
