import csv

database_file = "music.csv"

#Function to read items from csv file
def read_items():
    with open(database_file, mode="r") as a file:
        reader = csv.Dictreader(file)
        return list(reader)


#Function to write items to the csv file
def write_items():
    with open(database_file, mode="w", newline="") as file:
        fieldnames = ["Name", "Genre", "Debut Year", "Top Album", "Number of Albums", "Active"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(items)


