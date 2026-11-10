#word guessing game
import random

artists = ["Monet", "Manet", "Cassatt", "Degas", "Cezanne", "Renoir"]

# randomly select an artist from the list


x = random.choice(artists).lower()
print(x)
ctr = 0
guesses = '' 

while ctr < 5:
    strike = 0
    guess = str(input("Guess any letter :) (you have 6 tries!): "))
    for y in x:
        if guess in x:
            print(guess,end=" ")
        else:
            print("__", end=" ")
            strike += 1
    if strike == 0:
        print("You win! The artist was",x.title(),"!")
        break

    guesses += x
    print(guesses)

print("You ran out of guesses!\nThe artist was",x.title(),"!")
