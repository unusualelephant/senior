shops = ["CISCO","Graphic Design", "WCP"]
s1,s2,s3 = shops
print(f"The BEST shops at Tech are {s1}, {s2},and {s3}.")

shops2 = ["CISCO","Graphic Design", "WCP"]
s1,s2,s3 = shops2
print(f"The BEST shops at Tech are "+s1,s2,"and",s3,".")





"""
ages = (35, 22, 18, 40, 22, 48)
print(ages)
print(len(ages))
print(len(ages))
print(ages[1])
total = 0
for a in ages:
    print(a)
    total+=a
print(total)
ageList = list(ages)
print(ageList)
ageList.append(77)
ageList.insert(0,22)
print(ageList)
age = 
"""






"""
def changelist(pets):
    ogpet = input("Pet?:").lower()
    pets.append(ogpet)
    newpet = input("New pet?:").lower()
    pets.insert(0,newpet)
    print(pets)
    pets.sort()
    print(pets)
    pets.reverse()
    print(pets)
    last = pets.pop(-1)
    print(last)
    print(pets)
    pets.pop(2)
    print(pets)
    if "snake" in pets:
        pets.remove("snake")
    else:
        print("Snake is not found.")
    


def main(pets):
    pets = ['dog', 'cat', 'rabbit', 'bird', 'hampster', 'snake']
    changelist(pets)
    print(pets)

    bowling = [220, 247, 198, 201, 218]
    print(max(bowling))
    print(min(bowling))

    
    for x in bowling:
        print("Bowling score #",(bowling.index(x)),":",x)

main(pets="elohel")

"""




'''
import random 

ages = [35, 22, 18, 7, 17, 88, 72, 33]

def change(a):
    a.append(47)
    a[0] = 38
    print(a)

change(ages)
print(ages)
answer = random.choice(ages)
print(answer)
answers = random.choices(ages, k=3)
print(answers)
print(min(ages))
print(max(ages))
'''




"""
num = 5

def one(num):

    num = num + 1
    print(num)

one(num)
print(num)

"""