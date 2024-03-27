import os
from itertools import permutations
import random
import math
import random

folder_path = os.path.abspath(os.path.dirname(__file__))
filename = "cities_1.txt"
P = 250
n = 0.8

def read_file(filename):
    path = f"{folder_path}/{filename}"
    return open(path, "r")

def calculate_distance(coor1, coor2):
    return math.sqrt((coor1[0] - coor2[0])**2 + (coor1[1] - coor2[1])**2)

file = read_file(filename)
lines = file.readlines()

x_line = lines[1]
y_line = lines[2]
x = x_line[x_line.find('[') + 1:x_line.find(']')].split(' ')
x = [int(el) for el in x]
y = y_line[y_line.find('[') + 1:y_line.find(']')].split(' ')
y = [int(el) for el in y]

cities = [(x[i], y[i]) for i in range(0, len(x))]
 
permut = list(permutations(cities))

parents = random.sample(permut, P)

distances = []

for parent in parents:
    parent_distances = []
    for index, val in enumerate(parent):
        distance = 0
        if index < len(parent) - 1:
            distance = calculate_distance(val, parent[index+1])
        else:
            distance = calculate_distance(val, parent[0])
        parent_distances.append(distance)
    distances.append(sum(parent_distances))

maxDistance = max(distances)

fitnesses = [(maxDistance - distance) for distance in distances]
total_fitness = sum(fitnesses)

print(total_fitness)

selected_parents = []

while len(selected_parents) < n*P:
    current_sum = 0
    random_value = random.randrange(0, int(total_fitness))
    for index, fitness in enumerate(fitnesses):
        current_sum += fitness
        if current_sum >= random_value:
            selected_parents.append(parents[index])
            break

print(parents[0])
print(len(selected_parents))
