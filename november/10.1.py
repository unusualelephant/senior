

while True:
    email = str(input("Email address: "))
    if "@" or "." not in email:
        print("Try Again.")
        True
    else:
        break
print("User name:",email)
        
# doesn't work lol
    






"""

city = str(input("City: ")).title()
city.strip()
if "St" in city:
    city = city.replace("St", "Saint")

while True:
    state = str(input("State: ")).upper()
    if len(state) != 2:
        print("State must be in 2-letter abbreviation.")
        True
    else:
        break

while True:
    zipcode = str(input("Zip Code: "))
    if len(zipcode) != 5:
        print("Zip code must be 5 digits long.")
        True
    else:
        break


print(city,state,zipcode)

"""










"""


sentence = str(input("Please enter a sentence: "))

number = int(input("Please enter a number: ")) - 1

print(len(sentence))
sentence = sentence.split()
print(number)

if number > len(sentence):
    print("Error. Out of bounds.")
else:
    print("Your returned string is:", sentence[number],".")

"""







# i made it work!









# all below are example with mrs v 



"""

shops = ["WCP", "CISCO", "Robotics"]
print(shops)
print(shops[0])
answer = "?".join(shops)
print(answer)
print(answer[4:7])

data = "Tre, Accounting,34,St. Louis"
info = data.split(",") #splits spaces if no
print(info[3])
name = "Remi Winter Schrader"
final = name.split()
print(final)

"""



"""
a = 14.934
b = 5.48123
student = “Mike”
friend = “Stephanie”
"""







"""

teacher = "Mrs. Venturella"
print(teacher[5:9])
print(teacher[5: ])
print(teacher[5::2])
print(teacher[-4:-1])

if "," in teacher:
    print("Yes")
else: 
    print("No")

for letter in teacher:
    print(letter)

"""




"""


print("WCP"*10)

longstring = '''This is an interesting
                way 
            to 
        do 
    things\nThoughts?'''
print(longstring)


# \ is continuation 
print \
(5+5*3+2)

print(ord("A"))

print \
(ord("a"))


print(chr(65))
print(chr(97))


"""