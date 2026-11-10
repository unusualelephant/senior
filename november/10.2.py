# second example

#  article, noun, verb, preposition, article, and noun.

digits = int(input("Please enter 6 digits 1 - 5: "))

# make 4 arrays

list = [["the","a","one","every","any"],
        ["boy", "girl", "dog", "car", "tree"],
        ["jumped", "skipped", "stepped", "walked", "ran"],
        ["under", "over", "along", "with", "beside"]]



# nouns = ["boy", "girl", "dog", "car", "tree"]

# verbs = ["jumped", "skipped", "stepped", "walked", "ran"]

# preps = ["under", "over", "along", "with", "beside"]














# first example of 10-2

"""

alpha = 0
digit = 0
specs = 0

sentence = str(input("Please enter a sentence: "))
while True:
    for x in sentence:
        if x.isalpha():
            alpha +=1
        if x.isdigit():
            digit += 1
        else:
            specs += 1
    print("Number of Alphabets in the string is:",alpha,"\nNumber of Digits in the string is:",digit,"\nNumber of Special characters in the string is:",specs)
    break 
    
"""









"""

shop = "Web & Computer Programming"
shop = shop.replace("&", "and")
print(shop)
info = shop.split()
print(info[2])

stuff = "testing 123 abc"
print(stuff[8].isdigit())
print(stuff)

"""





"""

with open("november/words.txt", "r") as file:
    lines = file.readlines()
print(lines)
words = [line.strip() for line in lines]
print(words)

alpha_words = [word for word in words if word.isalpha()]
print(alpha_words)

"""









"""

import random

greetings = ["Hello", "Hi", "Welcome", "Greetings", "Hey"]

def greeting(name):
    # num = random.randint(0,4) #len(greetings) + 1
    # print(greetings[num]+ " " + name + "!")
    chosen = random.choice(greetings)
    print(f"{chosen}, {name}!")

name = input("Enter name: ")
greeting(name)

# Function that counts vowels in string
def count_vowel(text):
    vowels = "aeiou"
    count = 0
    for char in text:
        if char.lower() in vowels.lower():
            count += 1
        return count

sentence = input("Enter sentence:")
answer = count_vowel(sentence)
print(f"Vowel count: {answer}")

"""
