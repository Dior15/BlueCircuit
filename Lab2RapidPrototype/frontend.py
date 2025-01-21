from csv import writer

def view():
    pass

def edit():
    pass

def add():
    
    items = []
    
    items.append(input("Enter Artist Name: "))
    items.append(input("Enter Genre: "))
    items.append(input("Debut Year: "))
    items.append(input("Enter Album: "))
    items.append(input("Enter Number of Albums: "))
    active = input("Are they still active? (Y/N): ")

    if active == "Y":
        items.append(True)
    else: 
        items.append(False)

    
    with open('Lab2RapidPrototype\music.csv', mode="a") as file:
        writer_object = writer(file)
        writer_object.writerow(items)
        file.close() 


def printIntro():
    print("Welcome to your music catalog. Here you can view, add and edit items")

def checkOptions(option):
    if option == 1:
        view()
    elif option == 2:
        add()
    elif option == 3:
        edit()
    else:
        print("Option entered is not valid. Please try again.")
        menu()

def menu():
    print("Menu:")
    print("1. View catalog")
    print("2. Add a new song")
    print("3. Edit or delete an existing song")
    option = int(input("Which option would you like to select: "))
    checkOptions(option)

def main():
    printIntro()
    menu()

main()

