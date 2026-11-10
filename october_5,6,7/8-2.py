while True:
    try:
        def selective_sum():
            mis = ['10','nine','8','seven','6','five']
            for x in mis:
                print(x, end=" ")
    except Exception as e:
        print(e)
    selective_sum()
    break




"""

while True:
    try:
        author = ['Garcia Lorca', 'Vargas Llosa', 'Garcia Marquez', 'Allende', 'Paz']
        print(author)
        num = int(input("Pick an author (1-5): ")) -1
    except IndexError:
        print("Index is outside the list range!")    
    except ValueError:
        print("Integers only.")
    except Exception as e:
        print(e)
    print("Success! The element at index 2 is:", author[num])
    break

"""


"""

while True:
    try:
        age = int(input("Enter age: "))
        if age>120 or age<0:
            raise Exception("Age should be between 0-120.")
        print("You are %d years old in dog years" % (age*7) + ".")
        break # or use return in function
    except ValueError:
        print("Numeric Data Only.")
    except Exception as e:
        print(e)
print("Good Bye.")

"""




"""

try:
    with open ("mynewfile.txt", "rt") as file:
        myinfo = file.read()
        print(myinfo)
except FileNotFoundError:
    print("Could not find file.")
except OSError:
    print("Error reading file.")
except ValueError:
    print("Numeric Data Only.")
except Exception as e:
    print(e)

"""