








sen = str(input("Write a sentence:"))
lctr = 0
numctr = 0
ectr = 0

if sen.isalpha() == True:
    lctr += 1
elif sen.isdigit() == True:
    numctr += 1
else:
    ectr += 1
    print("Letters or Numbers only.")


# this doesnt work rightnow









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