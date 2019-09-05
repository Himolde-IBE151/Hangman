# Hangman Game
In this assignment you will implement the **Hangman game**. 
We need to practice some concepts from last class that will be needed to implement the game. 
Let's start!

## Guess a letter inside a word.
We have fixed a secret word (a string).
The user will guess **1 letter** that appears in the secret word and then the **position** where it appears on the secret word (**positions start from 0**). 
If (s)he succeds, the program prints "Success, you won!" otherwise prints "You lost!" 

#Remember that string's first index is 0
hangman.py
```python
secretWord = "Orangutan"
s = input ("Write a character: ")
p = int(input ("Write the position: "))
if s == secretWord[p]:
    print("You won! \N{grinning face with smiling eyes}")
else:
    print("You lost \N{face with rolling eyes}") 
```
## 


```python


```
