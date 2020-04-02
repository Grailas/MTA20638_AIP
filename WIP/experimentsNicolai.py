import numpy as np
import random


def make_playspace():
    #- Initialize world space
    global world_space 
    world_space = np.zeros(shape=(10,6))

    #- Randomize goal position
    goal_pos = random.randint(0,9), random.randint(0,5)
    world_space[goal_pos[0], goal_pos[1]] = 1

    #- Place sheep
    if(goal_pos[0] == 9):
        world_space[goal_pos[0] - 1, goal_pos[1]] = 2
    else:
        world_space[goal_pos[0]+1, goal_pos[1]] = 2

make_playspace()

print(world_space)