import random



words = ["Monet", "Manet", "Cassatt", "Degas", "Cezanne", "Renoir","Basquiat","Warhol","Kahlo","Van Gogh", "Toulouse-Lautrec","Mondrian","Banksy","Mamet","Rivera","Klee","Kandinsky",]


word = random.choice(words).lower()

print("\nGuess the artist!")


guesses = ''


turns = 12


while turns > 0:

    failed = 0


    for char in word:
        if char in guesses:
            print(char, end=" ")
        else:
            print("_", end=" ")
            failed += 1

    print()


    if failed == 0:
        print("You Win")
        print("Congrats, you guessed the artist! It is", word.title(),"!")
        break


    guess = input("Guess a character: ").lower()


    if len(guess) != 1:
        print("Please enter a single character.")
        continue


    if guess in guesses:
        print("You already guessed that character.")
        continue


    guesses += guess


    if guess not in word:
        turns -= 1
        print("Incorrect!\nYou have",turns,"guesses left.")


        if turns == 0:
            print("Game over!\n The artist was",word.title(),"!")