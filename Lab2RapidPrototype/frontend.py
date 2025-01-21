import csv

def printIntro():
    print("Welcome to your music catalog. Here you can view, add and edit items")

def menu():
    print("Menu:")
    print("1. View catalog")
    print("2. Add a new song")
    print("3. Edit or delete an existing song")

def readfile(file):
    with open('music.csv', mode='r') as file:
        f = csv.reader(file)
        for lines in f:
            print(lines)

def writefile(file):
    pass

readfile("music.csv")
