import frontend

def print_intro():
    """Print the introduction message."""
    print("Welcome to your music catalog. Here you can view, add, and edit items.")

def check_options(option):
    """Check and execute menu options."""
    if option == 1:
        frontend.view()
    elif option == 2:
        frontend.add()
    elif option == 3:
        frontend.edit()
    else:
        print("Invalid option. Please try again.")

def menu():
    """Display the menu and get user input."""
    print("\nMenu:")
    print("1. View catalog")
    print("2. Add a new item")
    print("3. Edit or delete an existing item")
    try:
        option = int(input("Which option would you like to select: "))
        check_options(option)
    except ValueError:
        print("Invalid input. Please enter a number.")

def main():
    """Main function to run the application."""
    print_intro()
    while True:
        menu()

if __name__ == "__main__":
    main()