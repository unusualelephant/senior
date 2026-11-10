

while True:
    a = str(input("Enter a sentence: "))
    if a.isalpha()== True or a.isdigit() == True:
        print(a)            
        break
    
    else:
        print("Letters or Numbers only.")
        True








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
