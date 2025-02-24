import backend

FILE_PATH = 'Lab2RapidPrototype/KhristianPrototype/music.csv'

def print_intro():
    """Print the introduction message."""
    print("Welcome to your music catalog. Here you can view, add, and edit items.")

def check_options(option):
    """Check and execute menu options."""
    if option == 1:
        view()
    elif option == 2:
        add()
    elif option == 3:
        edit()
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

def view():
    """View all items in the catalog."""
    items = backend.read_items(FILE_PATH)
    if items:
        print("\nCurrent Music Catalog:")
        for item in items:
            print(item)
    else:
        print("\nThe catalog is empty.")

def add():
    """Prompt the user to add a new item."""
    artist = input("Enter the artist name: ")
    genre = input("Enter the genre name: ")
    year = input("Enter the release year: ")
    album = input("Enter the album name: ")
    num_album = input("Enter the number of albums: ")
    active = input("Enter if the artist is active (Yes or No): ")

    backend.add_item(FILE_PATH, [artist, genre, year, album, num_album, active])

def edit():
    """Prompt the user to edit an existing item."""
    artist = input("Enter the artist name to edit: ")

    new_artist = input("Enter the new artist name: ")
    new_genre = input("Enter the new genre name: ")
    new_year = input("Enter the new release year: ")
    new_album = input("Enter the new album name: ")
    new_num_album = input("Enter the new number of albums: ")
    new_active = input("Enter if the artist is active (Yes or No): ")

    backend.edit_item(FILE_PATH, artist, [new_artist, new_genre, new_year, new_album, new_num_album, new_active])