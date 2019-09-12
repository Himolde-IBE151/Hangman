import random
random.seed()
def get_words():
    words = ["dogs", "elephant", "pencil", "mouse", "jazzist", "dancer", 
    "accident", "building", "orchid", "bamboo", "hangman", "orangutan", 
    "gorilla", "mountain", "pineapple", "window", "hurricane", "folder", 
    "border", "literature", "throne", "computer", "binary", "number", "galaxies"]
    n =  random.randint(0,len(words)-1)
    return words[n]