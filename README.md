# Preparation for the Hangman Game
In this assignment you will implement the **Hangman game**. 
We need to practice some concepts from last class that will be needed to implement the game. 
Let's start!

## Strings 
A string is a sequence of characters. The character at position 0 of the string s is s[0]. The next character (at position 1) of the string s is s[1], and so on.. 
```python
s = "Molde"
print(s[0])
print(s[1])
print(s[2])
print(s[3])
print(s[4])
```
The position **must be an integer**.

### Exercise: Input a string s from the keyboard. Assuming that the user always enters a string with more than two characters, print the second letter of s. 
The second letter of s is at position 1, since the index of the first position is 0.
```python
s = input ("Enter a word with more than two characters ")
print("The second character in the word you typed is", s[1])
```
### Exercise: Input a string s and the position p of a letter in s. Print the letter that corresponds to the position p in s. 
```python
s = input ("Enter a word with more than two characters ")
p = int(input("Enter the position of the letter you want me to print ")
print("The character at position", p, "in the word", s, "is", s[p])
```
### Exercise: Input a string s with 4 character or more. Print all the characters separated by spaces and in the next line, the size of the string. 
```python
s = input("Type a name with 4 letters or more")
print (s[0] + " " + s[1] + " " + s[2] + " " + s[3])
print("The size of the string is", len(s))
```
### From now on, consider that the user may enter strings with any size (larger than 1)

*Branching. Objective: To know how to ask for a character in the string*.
### Exercise: The user should type a character. If the character entered is the first letter of your name, print "You wrote the first letter of my name"
*In the next code, replace 'X' by the first letter in your name.*
```python
s = input ("Enter the first letter of my name")
if (s[0] == 'X'): 
    print("You wrote the first letter of my name")
```
*Objective: To know how to use the length of the string to index the last character in s. To be able to take decisions according to the character in a position in the string*
### Exercise: Save your name in the variable s. Input a letter l. If the letter entered is the last character in s, print "You wrote the last letter of my name".
*In the next code, replace "My Name" by your name.*
```python
# write the commands missing here
s = "My Name"
if (s[len(s)-1] == l):
    print("You wrote the last letter of my name")
```

*Objective: To know how to use logical operators*
### Exercise: Input a string s. Compare every letter in your name with the same number of characters in s. If the string s starts with your name, print "Your string starts with my name!". 
*In the next code replace Name with your name. You may need more comparissons*
```python
if (s[0] == 'N') and (s[1] == 'a') and (s[2] == 'm') and (s[3] == 'e'):
    print("Your string starts with my name!")
```

### Exercise:(Game) Guess a letter inside a word.
We have fixed a secret word (a string) in your program. For instance 
```python
secretWord = "Orangutan"
```
In this game, the user have to guess one of the letters of a secret word that we have fixed in our program. 
The program inputs from the user **1 character** s and then the **position** p where (s)he guesses the character appears in the secret word (**remember that positions start from 0**). 
If (s)he succeds, the program prints "Success, you won!" otherwise prints "You lost!" 

**Try to solve the problem by yourself.** Then you can verify your answer [here](./hangman.py)

### Exercise: Given a secretWord (a string), print 3 '_' for every character in the secret word (preparation for the Hangman game). For instance, if the secretWord is "Sky" the program should print:
```
___ ___ ___
```
(3 '_' for every character)

Hint: use a for loop, like in 
```python
for i in range(10):
```
### Exercise: Input a string s. Print all the characters in s separated by 3 spaces. 
Hint: use a for loop

### Exercise: Verify if a character appears in a word. Input a word s and a character c. If the character appears in the word, print("Found it!"). Otherwise, print(Not found")
Hint: use a for loop and search for c character by character in s

### Exercise: Input a string s and a character c. Print how many times c appears in s. 
**Try to solve the problem by yourself.** Then you can verify your answer [here](./counter.py)
