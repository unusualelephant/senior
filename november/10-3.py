#word guessing game


artists = ["Monet", "Manet", "Cassatt", "Degas", "Cezanne", "Renoir"]

# randomly select an artist from the list

import random
x = random.choice(artists).lower()
print(x)

while True:
    guess = str(input("Guess letter (you have 6 tries): "))
    ctr = 0
    if guess in x:
        print("You guessed a letter in the word!")
        a = x.replace(guess, "")
        print(a)
        if len(x) == 0:
            print("You guessed the artist! It was " + x + ".")
            break
    else:
        print("Try again.")
        ctr += 1
        if ctr == 6:
            print("Game over!")

