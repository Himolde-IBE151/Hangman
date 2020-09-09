# Preparation for the Hangman Game I
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

### Exercise: 
**Input a string s from the keyboard. Assuming that the user always enters a string with more than two characters, print the second letter of s.**
The second letter of s is at position 1, since the index of the first position is 0.
<details>
  
```python
s = input ("Enter a word with more than two characters ")
print("The second character in the word you typed is", s[1])
```

</details>
  
### Exercise: 
**Input a string s and the position p of a letter in s. Print the letter that corresponds to the position p in s.**

<details>

```python
s = input ("Enter a word with more than two characters ")
p = int(input("Enter the position of the letter you want me to print "))
print("The character at position", p, "in the word", s, "is", s[p])
```
</details>

### Exercise:
**Input a string s with 4 character or more. Print all the characters separated by spaces and in the next line, the size of the string.**
<details>

```python
s = input("Type a name with 4 letters or more")
print (s[0] + " " + s[1] + " " + s[2] + " " + s[3])
print("The size of the string is", len(s))
```

</details>

### From now on, consider that the user may enter strings with any size (larger than 1)

*Branching. Objective: To know how to ask for a character in the string*.
### Exercise: 
**The user should type a character. If the character entered is the first letter of your name, print "You wrote the first letter of my name"**
*In the next code, replace 'X' by the first letter in your name.*
<details>

```python
s = input ("Enter the first letter of my name")
if (s[0] == 'X'): 
    print("You wrote the first letter of my name")
```

</details>

*Objective: To know how to use logical operators*
### Exercise: 
**Input a string s. Compare every letter in your name with the same number of characters in s. If the string s starts with your name, print "Your string starts with my name!".**
*In the next code replace Name with your name. You may need more comparissons*

<details>

```python
if (s[0] == 'A') and (s[1] == 'n') and (s[2] == 'a'):
    print("Your string starts with my name!")
```

</details>

### Exercise:(Game) 
**Guess a letter inside a word.**
We have fixed a secret word (a string) in your program. For instance 
<details>
  
```python
secretWord = "Orangutan"
```

</details>
