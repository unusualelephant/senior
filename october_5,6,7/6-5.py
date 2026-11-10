def command():
    com = input(str("The Wizard Inventory Program\n\nCOMMAND MENU\nshow - Show all items\ngrab - Grab an item\nedit - Edit an item\ndrop - Drop an item\nexit - Exit program\nCommand:"))
    return com

def show():
    for item in items:
        print(str(items.index(item)+1) + ". " + item)

def grab():
    gitem = str(input("Name:")).lower()
    items.append(gitem)
    print(gitem,"was added.")
    show()
    command()

def edit():
    # prompt user to edit an item
    print("EDIT")
    drop()
    uname = str(input("Updated name: "))
    items.append(uname)
    show()


def drop():
    number = int(input("Number: ")) - 1
    items.pop(number)
    show()

# only four items at a time 
# functions for every if statement

items = ["wooden staff", "wizard hat", "cloth shoes"]
while True:
    com = input(str("The Wizard Inventory Program\n\nCOMMAND MENU\nshow - Show all items\ngrab - Grab an item\nedit - Edit an item\ndrop - Drop an item\nexit - Exit program\nCommand:"))
    if len(items) < 4:
        if com == "show":
            show()
        elif com == "grab":
            grab()        
        elif com == "edit":
            edit()
        elif com == "drop":
            drop()
        else:
            print("You quit.")
            False
            break
        
    








