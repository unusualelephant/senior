import csv


data = []
with open("students.csv","w",newline="") as file:
    wr = csv.writer(file)
    while True:
        student = str(input("Student name: "))
        shop = str(input("Shop class: "))
        year = int(input("Year: "))
        data = student,shop,year
      # add this somehow idk append/??
        for x in data:
            print(x)
        cont = str(input("Continue? (y/n): "))
        if cont == "n":
            False
            break

print("Finished")



#lots wrong plez fix
