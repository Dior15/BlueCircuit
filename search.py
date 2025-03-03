import tmdbsimple as tmdb
import json

# Set your API key here
tmdb.API_KEY = ''
tmdb.REQUESTS_TIMEOUT = 1

def main():
    print("Welcome to MovieFlix!\n__________________________________________________\nAre you searching for a movie, tv show or person?")
    while(True):
        print("1. Movie\n2. TV Show\n3. Person\n4. Exit\n__________________________________________________")
        choice = input("Enter your choice: ")
        if choice == "1":
            movieSearch()
            print("__________________________________________________")
        elif choice == "2":
            tvSearch()
            print("__________________________________________________")

        elif choice == "3":
            personSearch()
            print("__________________________________________________")

        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
            print("__________________________________________________")

def movieSearch():
    # Ask the user for a search query
    query = input("Enter a movie to search for: ")

    # Initialize the search
    search = tmdb.Search()
    response = search.movie(query=query)

    # Check if there are any results
    if search.results:
        print("\nSearch Results:")
        for s in search.results:
            # Using get() for release_date in case it is missing
            print(f"Title: {s['title']} | ID: {s['id']} | Release Date: {s.get('release_date', 'N/A')} | Popularity: {s['popularity']}")
    else:
        print("No results found for your search.")

def tvSearch():
    # Ask the user for a search query
    query = input("Enter a TV show to search for: ")

    # Initialize the search
    search = tmdb.Search()
    response = search.tv(query=query)

    # Check if there are any results
    if search.results:
        print("\nSearch Results:")
        for s in search.results:
            # Using get() for first_air_date in case it is missing
            print(f"Title: {s['name']} | ID: {s['id']} | First Air Date: {s.get('first_air_date', 'N/A')} | Popularity: {s['popularity']}")
    else:
        print("No results found for your search.")

def personSearch():
    # Ask the user for a search query
    query = input("Enter a person to search for: ")

    # Initialize the search
    search = tmdb.Search()
    response = search.person(query=query)

    # Check if there are any results
    if search.results:
        print("\nSearch Results:")
        for s in search.results:
            # Using get() for known_for in case it is missing
            # print(f"Name: {s['name']} | ID: {s['id']} | Known For: {s.get('known_for', 'N/A')} | Popularity: {s['popularity']}")
            print(f"Name: {s['name']} | ID: {s['id']} | Popularity: {s['popularity']}")
    else:
        print("No results found for your search.")

if __name__ == "__main__":
    main()