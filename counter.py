s = input ("Enter a word: ")
c = input ("Enter a character that appears in the word: ") 
counter = 0
for i in range(len(s)):
    if s[i] == c:
        counter = counter + 1
print("The character", c, "appears", counter, "times in", s) 
