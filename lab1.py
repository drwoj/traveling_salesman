import os

folderPath = os.getcwd()
filename = "cities_1.txt"

def readFile(filename):
    path = f"{folderPath}/{filename}"
    return open(path, "r")

file = readFile(filename)
print(file.read())