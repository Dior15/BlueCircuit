import csv

#Function to read items from csv file
with open('Lab2RapidPrototype\music.csv', mode="r") as file:
    csvFile = csv.reader(file)
    for lines in csvFile:
        print(lines)