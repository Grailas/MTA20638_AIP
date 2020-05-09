import numpy as np
import random
import time
from queue import PriorityQueue
from experimentsNicolai2 import *

#A* - redblobgames.com/pathfinding/a-star/implementation.html

#Sets up a 50x50 grid
g = GridWithWeights(50, 50)

#randomizes the sheep position and fold position
sheep_position = (random.randint(1,48), random.randint(1,48))
fold_position = (random.randint(0,10), random.randint(0,10))
goal_position = (0, 0)
sheep_movement = []
dog_movement = []

self_press = True

def NewGoal():
    global sheep_position, goal_position, fold_position, g
    #Define walls and goal position based on the sheep position.
    if sheep_position[0] == fold_position[0] and sheep_position[1] > fold_position[1]:
        if sheep_position[0] == 0:
            g.walls = [(sheep_position[0], sheep_position[1] - 1), (sheep_position[0] + 1, sheep_position[1])]
            goal_position = (sheep_position[0], sheep_position[1] + 1)
        else:
            g.walls = [(sheep_position[0], sheep_position[1] - 1), (sheep_position[0] + 1, sheep_position[1]), (sheep_position[0] - 1, sheep_position[1])]
            goal_position = (sheep_position[0], sheep_position[1] + 1)

    elif sheep_position[0] > fold_position[0] and sheep_position[1] == fold_position[1]:
        if sheep_position[1] == 0:
            g.walls = [(sheep_position[0] - 1, sheep_position[1]), (sheep_position[0], sheep_position[1] + 1)]
            goal_position = (sheep_position[0] + 1, sheep_position[1])
        else:
            g.walls = [(sheep_position[0] - 1, sheep_position[1]), (sheep_position[0], sheep_position[1] + 1), (sheep_position[0], sheep_position[1] - 1)]
            goal_position = (sheep_position[0] + 1, sheep_position[1])

    elif sheep_position[0] > fold_position[0] and sheep_position[1] > fold_position[1]:
        g.walls = [(sheep_position[0] - 1, sheep_position[1]), (sheep_position[0], sheep_position[1] - 1)]
        goal_position = (sheep_position[0] + 1, sheep_position[1])

    elif sheep_position[0] < fold_position[0] and sheep_position[1] > fold_position[1]:
        g.walls = [(sheep_position[0] + 1, sheep_position[1]), (sheep_position[0], sheep_position[1] - 1)]
        goal_position = (sheep_position[0] + 1, sheep_position[1])

    elif sheep_position[0] > fold_position[0] and sheep_position[1] < fold_position[1]:
        g.walls = [(sheep_position[0] - 1, sheep_position[1]), (sheep_position[0], sheep_position[1] + 1)]
        goal_position = (sheep_position[0] + 1, sheep_position[1])

    if sheep_position[0] < fold_position[0] and sheep_position[1] < fold_position[1]:
        g.walls = [(sheep_position[0] + 1, sheep_position[1]), (sheep_position[0], sheep_position[1] + 1)]
        try:
            goal_position = (sheep_position[0] - 1, sheep_position[1])
        except:
            print('woops')
        else:
            goal_position = (sheep_position[0], sheep_position[1] - 1)

#Function for moving the sheep
def MoveSheep():
    global sheep_position, goal_position, g
    #Removes walls placed to restrict dog movement.
    g.walls.clear()
    if goal_position[0] > sheep_position[0] and goal_position[1] == sheep_position[1]:
        sheep_position = (sheep_position[0] - 1, sheep_position[1])
    elif goal_position[0] == sheep_position[0] and goal_position[1] > sheep_position[1]:
        sheep_position = (sheep_position[0], sheep_position[1] - 1)
    elif goal_position[0] == sheep_position[0] and goal_position[1] < sheep_position[1]:
        sheep_position = (sheep_position[0], sheep_position[1] + 1)
    elif goal_position[0] < sheep_position[0] and goal_position[1] == sheep_position[1]:
        sheep_position = (sheep_position[0] + 1, sheep_position[1])
    
    
print(sheep_position, " ", goal_position, " ", fold_position)
start = (49, 49)
dog_movement.append(start)
sheep_movement.append(sheep_position)

#Runs untill the sheep is within the fold, hopefully.
while sheep_position != fold_position:
    NewGoal()
    goal = goal_position
    #starts pathfinding and prints grid
    came_from, cost_so_far = a_star_search(g, start, goal)
    draw_grid(g, width=3, point_to=came_from, start=start, goal=goal, sheep=sheep_position, fold=fold_position)
    print()
    print(sheep_position)
    MoveSheep()
    print("Sheep position: ", sheep_position)
    print("Fold position: ", fold_position)
    draw_grid(g, width=3, point_to=came_from, start=start, goal=goal, sheep=sheep_position, fold=fold_position)
    print()
    start = goal_position
    draw_grid(g, width=3, number=cost_so_far, start=start, goal=goal)
    print()
    sheep_movement.append(sheep_position)
    dog_movement.append(goal)
    #Waits for keypress, 'y' runs through to the next step, anything else runs untill done.
    if self_press:
        result = input('Y to next step, "N" to run till the end.')
        if result.lower() == 'y':
            continue
        else:
            self_press = False

print("Sheep movement:")
print(sheep_movement)
print()
print("Dog movement")
print(dog_movement)
