import csv
students = []
listonnum = -1
def main():
    with open("students.csv", "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerows(students)
    print("1. Add a student\n2. remove a student\n3. print report\n4. exit")
    while True: #Remi was the guide
        chose = int(input("Please enter your choice ===> "))
        if chose == 1:
            add()
        elif chose == 2:
            remove()
        elif chose == 3:
            printer()
        elif chose == 4:
            break
        else:
            print("Please enter a value 1-4")
    wr = open("students.txt", "w")
    for items in students:
        wr.write(str(items) + "\n")
def add(): #Both People Wrote and gave ideas
    global listonnum
    students.append([])
    listonnum += 1
    student = input("Enter a student name: ")
    students[listonnum].append(student)
    for i in range(3):
        student = int(input("Enter Test Score: " + str(i + 1) + ": "))
        students[listonnum].append(student)
def remove(): #75% written by Toby but Remi was the guide
    global listonnum
    for i in students:
        print(i[0], end=" | ")
    remover = int(input("Chose A Item to remove: ")) - 1
    students.pop(remover)
    listonnum -= 1
def printer(): #Both people
    for i in students:
            tot = 0
            num = 0
            for items in i:
                num += 1
                print(str(num)+".", str(items), end=" | ")
                if isinstance(items,int): #Google
                    tot += items
            average = round(tot/3,2)
            print(str(average))
def addfromfile():
    wr = open("students.txt","r")
  #  for line in wr:
  #      students.append()
  #      students.append(wr.readline(line).strip)
if __name__ == "__main__":
    main()

students.close("students.txt")