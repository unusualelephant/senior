shops = ["WCP","CISCO","Graphic Design","Automotive","Robotics","Culinary"]
print(shops)
shops[-3] = "IT Hybrid"
print(shops)
print(shops[-4]) # question 4
print(shops[1:4]) # question 5
print(shops[-2])
print(shops[4])
shops[0] = "Web and Computer Programming"
print(shops)

attendance = [16, 15, 16, 12, 14, 16]
print(attendance[2])
final = print(shops[2] + " has " + str(attendance[2]) + " students.")

num = int(input("Enter a number 1-6: "))
while True:
    if num > 6 or num < 1:
        num = int(input("Enter a number 1-6: "))
    else:
        num = num-1
        print(shops[num] + " has " + str(attendance[num]) + " students.")
        
    



"""
    if num == 1:
        print(shops[0] + " has " + str(attendance[0]) + " students.")
    if num == 2:
        print(shops[1] + " has " + str(attendance[1]) + " students.")
    if num == 3:
        print(shops[2] + " has " + str(attendance[2]) + " students.")
    if num == 4:
        print(shops[3] + " has " + str(attendance[3]) + " students.")        
    if num == 5:
        print(shops[4] + " has " + str(attendance[4]) + " students.")
    if num == 6:
        print(shops[5] + " has " + str(attendance[5]) + " students.")
    else:
        print("Try again!")
"""














"""
students = ["David","Tre","Kaden","Jerry","Evan","Cian","Joseph","Cam"]

for x in students:
    print(x)

for i in range(len(students)):
    print(students[i])
"""




"""

students = ["David","Tre","Kaden","Jerry","Evan"]
students[3] = "Hugh"
print(students)
print(len(students))
print(students[-3:-1])

"""











"""
students = ["David", "Tre", "Kaden","Jerry","Evan"]
# print(students)
# print(students[1])
# print(students[-2])
lang = ["HTML", "CSS", "JavaScript", "Python"]
answer = students + lang
# print(answer)
"""



"""
ages = [2,7,12]
versions = [4,27,8]
result = ages + versions
print(result)
r2 = ages[0]+versions[-1]
print(r2)
print(students[0]+ages[-1])
"""
# i did something wrong in the code about lol