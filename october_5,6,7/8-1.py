# second

def quest():

    while True:

        try:
            a = round(float(input("Please enter your first number: ")),1)
            b = round(float(input("Please enter your second number: ")),1)
            print(str(a),"divided by",str(b),"equals",str(a/b))
            break
        
        except ZeroDivisionError:
            print("You cannot divide by zero!")

        except ValueError:
            print("Both values must be valid numbers.")

        except Exception as d:
            print(d)
            print("Unknown error.")

quest()






# first

"""

while True:
    try:
        n = int(input("Enter a number (n): "))
        a = n + n*11 + n*111
        print(str(n),"+",str(n*11),"+",str(n*111),"=",str(a))

    except ValueError:
        print("Please enter a valid number.")

"""





#exception handling

"""

try:
    age = int(input("How old are you? "))
    if age < 0 or age > 120:
        raise Exception("Number must be between 0 and 120.")
    print("You are",age,"years old.")
except ValueError:
    print("Numeric Data Only.")
except Exception as e:
    print(e)
    print("Numeric Data Only.")

"""