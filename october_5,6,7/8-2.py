def change():
    try:
        my_numbers = [100, 200, 300, 400]
        index = int(input("Enter the index (0-3) to update: "))
        new_num = float(input("Enter the new number value: "))

        my_numbers[index] = new_num

        # print(my_numbers)
    except ValueError:
        print("Input Error: Both the index and value numbers must both be valid.")
    except IndexError:
        print("List Error: The index is outside the list (must be 0, 1, 2, or 3).")
    print("Update successful! New list:",my_numbers)

while True:
    change()







"""

def selective_sum(I):
    total = 0
    for i in I:
        print("Processing item:",i, end="\n")
        try:
            total += float(i)
        except ValueError:
            print("--> Skipped! Not a number.")
            pass
    return total

data_list = ['10', 'fail', 5, 'okay', '25', 1.5]

print(selective_sum(data_list))

"""



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