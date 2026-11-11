numbers = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6:36, 7:49 , 8:64, 9:81, 10:100, 11:121, 12:144, 13:169, 14:196, 15:225}

for a in numbers.items():
    print(a, end="\n")



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



"""

animals = {"bird":"Flappy","dog":"Sadie",
"cat":"Fluffy","tiger":"Stripes","snake":"Sammy"}
animals["bunny"]="Hoppy"
animals["snake"]="Sally"
print(animals)

name=animals.get("cat")
name2=animals["cat"]
print(name,name2)

name=animals.get("lizard") #return None if not exist
print(name)

name=animals.get["lizard","Does not exist"] #crash if not exist
print(name)

del animals["snake"]
print(animals)

"""



"""

animals = {"dog":"Sadie", "cat":"Fluffy","tiger":"Stripes","snake":"Sammy"}

print(animals)

print("I have a cat named", animals["cat"])

print(animals.keys())

for a in animals.keys():
    print("I have a",a,"named",animals[a])

for b in animals.values():
    print(b)

for a,b in animals.items():
    print(a,b)

animals["dog"] = "Cookie"
for a in animals.keys():
    print("I have a",a,"named",animals[a])

if "bird" in animals.keys():
    animals["bird"] = "Cheapers"
    print("Your bird's name was successfully changed")
else:
    print("You do not have a bird")

"""