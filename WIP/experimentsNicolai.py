import numpy as np
import random
import time
from queue import PriorityQueue
from experimentsNicolai2 import *


#A* 
'''
class State(object):
    def __init__(self, value, parent, start = 0 , goal = 0):
        self.children = []
        self.parent = parent
        self.value = value
        self.dist = 0
        if parent:
            self.path = parent.path[:]
            self.path.append(value)
            self.start = parent.start
            self.goal = parent.goal
        else:
            self.path = [value]
            self.start = start
            self.goal = goal
        
    def GetDist(self):
        pass
    def CreateChildren(self):
        pass

class State_String(State):
    def __init__(self, value, parent, start = 0, goal = 0):
        super(State_String, self).__init__(value, parent, start, goal)
        self.dist = self.GetDist()

    def GetDist(self):
        if self.value == self.goal:
            return 0
        dist = 0
        for i in range(len(self.goal)):
            letter = self.goal[i]
            dist += abs(i - self.value.index(letter))
        return dist
    
    def CreateChildren(self):
        if not self.children:
            for i in range(len(self.goal)-1):
                val = self.value
                val = val[:i] + val[i+1] + val[i] + val[i+2:]
                child = State_String(val, self)
                self.children.append(child)

class AStar_Solver:
    def __init__(self, start, goal):
        self.path = []
        self.visitedQueue = []
        self.priorityQueue = PriorityQueue()
        self.start = start
        self.goal = goal

    def Solve(self):
        startState = State_String(self.start, 0, self.start, self.goal)
        count = 0
        self.priorityQueue.put((0, count, startState))
        while(not self.path and self.priorityQueue.qsize()):
            closestChild = self.priorityQueue.get()[2]
            closestChild.CreateChildren()
            self.visitedQueue.append(closestChild.value)
            for child in closestChild.children:
                if child.value not in self.visitedQueue:
                    count += 1
                    if not child.dist:
                        self.path = child.path
                        break
                    self.priorityQueue.put((child.dist, count, child))
        if not self.path:
            print("Goal of " + self.goal + " is not possible!")
        return self.path

if __name__ == "__main__":
    start1 = "!HWod eolrll"
    goal1 = "Hello World!"
    print("starting...")
    a = AStar_Solver(start1,goal1)
    a.Solve()
    for i in range(len(a.path)):
        print("%d) " %i + a.path[i])
'''

#Test world space with above A*
'''
def make_playspace():
    #- Initialize world space
    global world_space 
    global goal_space1
    world_space = [
    ['_', '_', '_', '_', '_', '_'],
    ['_', '_', '_', '_', '_', '_'],
    ['_', '_', '_', '_', '_', '_'],
    ['_', '_', '_', '_', '_', '_'],
    ['_', 'g', '_', '_', '_', '_'],
    ['_', '_', '_', '_', '_', '_'],
    ['_', 's', '_', '_', '_', '_'],
    ['_', '_', '_', '_', '_', '_'],
    ['_', '_', '_', '_', '_', '_'],
    ['_', '_', '_', '_', '_', 'd']]

    goal_space1 = [
    ['_', '_', '_', '_', '_', '_'],
    ['_', '_', '_', '_', '_', '_'],
    ['_', '_', '_', '_', '_', '_'],
    ['_', '_', '_', '_', '_', '_'],
    ['_', 'g', '_', '_', '_', '_'],
    ['_', '_', '_', '_', '_', '_'],
    ['_', 's', '_', '_', '_', '_'],
    ['_', 'd', '_', '_', '_', '_'],
    ['_', '_', '_', '_', '_', '_'],
    ['_', '_', '_', '_', '_', '_']]

    
    #- Randomize goal position
    #goal_pos = random.randint(0,9), random.randint(0,5)
    #world_space[goal_pos[0]+1][goal_pos[1]] = 'g'

    #- Place sheep
    #if(goal_pos[0] == 9):
    #    world_space[goal_pos[0]-1][goal_pos[1]] = 's'
    #else:
    #    world_space[goal_pos[0]+1][goal_pos[1]] = 's'

make_playspace()

world_space_test = "_d_______"
goal_space_test = "________d"
a = AStar_Solver(world_space_test,goal_space_test)
a.Solve()
for i in range(len(a.path)):
    print("%d) " %i + a.path[i])
'''

#A* - redblobgames.com/pathfinding/a-star/implementation.html

#Sets up a 10x10 grid
g = GridWithWeights(50, 50)

#randomizes the sheep position and fold position
sheep_position = (random.randint(1,48), random.randint(1,48))
fold_position = (random.randint(0,10), random.randint(0,10))
goal_position = (0, 0)
sheep_movement = []
dog_movement = []

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

#Function for moving the sheep - not working yet(?)
def MoveSheep():
    global sheep_position
    global goal_position
    global g
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
while sheep_position != fold_position:
    NewGoal()
    goal = goal_position
    came_from, cost_so_far = a_star_search(g, start, goal)
    draw_grid(g, width=3, point_to=came_from, start=start, goal=goal, sheep=sheep_position, fold=fold_position)
    print()
    print(sheep_position)
    MoveSheep()
    print("Sheep position: ", sheep_position)
    print("Fold position: ", fold_position)
    #starts pathfinding and prints grid
    #came_from, cost_so_far = a_star_search(g, start, goal)
    draw_grid(g, width=3, point_to=came_from, start=start, goal=goal, sheep=sheep_position, fold=fold_position)
    print()
    start = goal_position
    #draw_grid(g, width=3, number=cost_so_far, start=start, goal=goal)
    #print()
    sheep_movement.append(sheep_position)
    dog_movement.append(goal)

print("Sheep movement:")
print(sheep_movement)
print()
print("Dog movement")
print(dog_movement)
