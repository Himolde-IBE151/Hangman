# Hangman Game
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
### Exercise: Input a string s with 4 character or more. Print the all characters separated by spaces and in the next line, the size of the string. 
```python
s = input("Type a name with 4 letters or more")
#print first letter of the string
print (s[0] + " " + s[1] + " " + s[2] + " " + s[3])
print("The size of the string is", len(s))
```
### From now on, consider that the user may enter strings with size (larger than 1)

### *(Branching). To know how to ask for a character in the string*.
### Exercise: The user should type a character. If the character entered is the first letter of your name, print "You wrote the first letter of my name"
### Substitute 'X' by the first letter in your name. 
```python
s = input ("Enter the first letter of my name")
if (s[0] == 'X'): 
    print("You wrote the first letter of my name")
```

### To know how to use the length of the string for indexing the last character.
### To know how to ask for a character in the string
### Exercise: Print "You wrote the last letter of my name" if the letter the user typed is the last letter of your name
#They know how to ask for the last letter
#Ask for the last character typed
if (s[len(s)-1] == 'n'):
    print("You wrote the last letter of my name")

#They know how to use logical operators
#Ask if the user entered the first letter of your name
if (s[0] == 'A') and (s[1] == 'n') and (s[2] == 'o') and (s[3] == 'l') and  (s[4] == 'a') and (s[5] == 'n'):
    print("You wrote my name!")


### Exercise: Guess a letter inside a word.
We have fixed a secret word (a string) in your program. For instance 
```python
secretWord = "Orangutan"
```
In this game, the user have to guess one of the letters of a secret word that we have fixed in our program. 
The program inputs from the user **1 character** s and then the **position** p where (s)he guesses the character appears in the secret word (**remember that positions start from 0**). 
If (s)he succeds, the program prints "Success, you won!" otherwise prints "You lost!" 

Try to solve the problem by yourself. Then you can verify your answer [here](./hangman.py)

## 


```python


```
