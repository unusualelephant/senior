
print("Game Stats program\n")


x = {"Wins":"4", "Losses":"3", "Ties":"12"}

y = {"Wins":"5", "Losses":"2", "Ties":"12"}

z = {"Wins":"6", "Losses":"1", "Ties":"12"}

players = {"Baudelaire":x, "Flaubert":y, "Zola":z}

print("ALL PLAYERS:")

# this is so ugly

for a in players.keys():

    print(a, end="\n")

while True:
    name = input("Enter a player name: ").lower()
    if name == "baudelaire":
        print(players["Baudelaire"])
    elif name == "flaubert":
        print(players["Flaubert"])
    elif name == "zola":
        print(players["Zola"])
    else:
        print("There is no player named "+name.title()+".")
    cont = input("Continue? (y/n): ")
    if cont != "y":
        print("Bye!")
        break
    else:
        True


# this doesn't make sense 



"""
car = {
 "brand": "Chevy",
 "model": "Corvette",
  "year": 1968
}

print(car)
print(car["model"])
car["year"] = "2016"

car["color"]="red"



for a in car.keys():
    print(a, end="\n")

for b in car.values():
    print(b, end="\n")


for x in car.items():
    print(x, end="\n")

"""