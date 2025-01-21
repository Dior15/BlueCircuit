import csv

def view():
    pass

def edit():
    pass

def add():
    pass

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

