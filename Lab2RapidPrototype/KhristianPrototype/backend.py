import csv

def read_items(file_path):
    """Reads items from the CSV file and returns them as a list."""
    items = []
    try:
        with open(file_path, mode="r") as file:
            csv_reader = csv.reader(file)
            items = [line for line in csv_reader]
    except FileNotFoundError:
        print(f"File {file_path} not found. Starting with an empty catalog.")
    return items

def add_item(file_path, item):
    """Adds a new item to the CSV file."""
    with open(file_path, mode="a", newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(item)
    print("Item added successfully!")

def edit_item(file_path, artist_name, new_item):
    """Edits an existing item in the CSV file based on the artist name."""
    try:
        updated = False
        items = []
        with open(file_path, mode="r") as file:
            csv_reader = csv.reader(file)
            for line in csv_reader:
                if line and line[0] == artist_name:
                    items.append(new_item)
                    updated = True
                else:
                    items.append(line)
        with open(file_path, mode="w", newline='') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerows(items)
        if updated:
            print("Item updated successfully!")
        else:
            print("Artist not found in the catalog.")
    except FileNotFoundError:
        print(f"File {file_path} not found. No changes were made.")