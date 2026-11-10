grades = [95,100,87,92,95]
grades.append(98)
print(grades)
grades.insert(1,99)
print(grades)
grades.remove(100)
print(grades)


students = ["Sam","Sally","Jim","Joe","Julie","Michael","Mark"]
students.insert(3,"Kim")
print(students)
students.pop(7)
print(students)
students.pop(1)
print(students)
students.remove("Sam")
print(students)
print(students.index("Kim"))
students.sort()
print(students)


friends = []
while True:
    name = input("Enter names of friends: ").title()
    print(friends)
    if name == "End" or name == "":
        break
    elif name not in friends and name not in students:
        friends.append(name)

everyone = (friends + students)
everyone.sort()
everyone.reverse()
print(everyone)






























"""
lang = ["Python", "JavaScript", "Java", "C++", "Perl"]
print(lang)
lang.append("C#")
print(lang)
lang.sort()
lang.reverse()
print(lang)
if "C++" in lang:
    lang.remove("C++")
print(lang)
if "JS" in lang:
    lang.remove("JS")
temp = lang.pop()
print(lang)
print(temp)
ans = lang.pop(1)
print(lang)
lang.insert(2, "SQL")
print(lang)
del lang[0]
print(lang)
del lang 
"""