import backend

FILE_PATH = 'Lab2RapidPrototype/KhristianPrototype/music.csv'

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
    numAlbum = input("Enter the number of albums: ")
    active = input("Enter if the artist is active (Yes or No): ")

    backend.add_item(FILE_PATH, [artist, genre, year, album, numAlbum, active])

def edit():
    """Prompt the user to edit an existing item."""
    artist = input("Enter the artist name to edit: ")

    new_artist = input("Enter the new artist name: ")
    new_genre = input("Enter the new genre name: ")
    new_year = input("Enter the new release year: ")
    new_album = input("Enter the new album name: ")
    new_numAlbum = input("Enter the new number of albums: ")
    new_active = input("Enter if the artist is active (Yes or No): ")

    backend.edit_item(FILE_PATH, artist, [new_artist, new_genre, new_year, new_album, new_numAlbum, new_active])