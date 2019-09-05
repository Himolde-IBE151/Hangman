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

### Exercise: Input a word from the keyboard. Assuming that the user always enters a word with more than two characters, print the second letter of a word. 
The second letter of a word is at position 1, since the index of the first position is 0.
```python
s = input ("Enter a word with more than two characters")
print("The second character in the word you typed is", s[1])
```
### Exercise: Input a word s and the position p of a letter in that word. Print the letter correspondent to the position p in s. 
```python
s = input ("Enter a word with more than two characters")
p = int(input("Enter the position of the letter you want me to print")
print("The character", p, "in the word", s,"is", s[p])
```
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
