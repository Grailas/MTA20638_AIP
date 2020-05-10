import random
import numpy as np

debug = False

# level information
level_layout = []

# starting positions
fold_position = []
dog_position = []
sheep_position = []

level_height = 0
level_width = 0

# entity locations
dog_start = (None, None)
fold = (None, None)
sheep_start = (None, None)

number_of_sheep = 0

# RL parts
sheep_horizontal_dirs = 3
sheep_vertical_dirs = 3
dog_horizontal_dirs = 3
dog_vertical_dirs = 3
dog_actions = 4

observation_space_size = sheep_horizontal_dirs * sheep_vertical_dirs * dog_horizontal_dirs * dog_vertical_dirs

q_table = np.zeros([observation_space_size, dog_actions])

# Hyperparameters
alpha = 0.1 # learning rate, extent to which Q-values are being updated
gamma = 0.6 # "discount factor", importance given to future rewards
epsilon = 0.1 # chance to try something new during training

# For plotting metrics
all_epochs = []
all_penalties = []

episodes = 100000

def reset_level_state():
    global level_layout, fold_position, dog_position, sheep_position, level_height, level_width, dog_start, fold, sheep_start, number_of_sheep
    # level information
    #  legend: _ = open, # = blocked, f = fold, s = sheep, d = dog
    level_layout = [
        ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
         '_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
         '_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
         '_', '_'],
        ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
         '_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
         '_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
         '_', '_'],
        ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
         '_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
         '_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
         '_', '_'],
        ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
         '_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
         '_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
         '_', '_'],
        ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
         '_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
         '_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
         '_', '_'],
        ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
         '_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
         '_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
         '_', '_'],
        ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
         '_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
         '_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
         '_', '_'],
        ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
         '_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
         '_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
         '_', '_'],
        ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
         '_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
         '_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
         '_', '_'],
        ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
         '_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
         '_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
         '_', '_'],
        ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
         '_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
         '_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
         '_', '_'],
        ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
         '_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
         '_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
         '_', '_'],
        ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
         '_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
         '_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
         '_', '_'],
        ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
         '_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
         '_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
         '_', '_'],
        ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
         '_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
         '_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
         '_', '_'],
        ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
         '_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
         '_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
         '_', '_'],
        ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
         '_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
         '_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
         '_', '_'],
        ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
         '_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
         '_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
         '_', '_'],
        ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
         '_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
         '_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
         '_', '_'],
        ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
         '_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
         '_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
         '_', '_'],
        ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
         '_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
         '_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
         '_', '_'],
        ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
         '_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
         '_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
         '_', '_'],
        ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
         '_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
         '_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
         '_', '_'],
        ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
         '_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
         '_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
         '_', '_'],
        ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
         '_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
         '_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
         '_', '_'],
        ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
         '_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
         '_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
         '_', '_'],
        ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
         '_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
         '_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
         '_', '_'],
        ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
         '_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
         '_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
         '_', '_'],
        ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
         '_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
         '_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
         '_', '_'],
        ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
         '_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
         '_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
         '_', '_'],
        ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
         '_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
         '_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
         '_', '_'],
        ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
         '_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
         '_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
         '_', '_']]

    # Randomize starting positions
    fold_position = [random.randint(0, 31), random.randint(0, 31)]  # TODO: Consider different placement
    dog_position = [random.randint(0, 31), random.randint(0, 31)]
    sheep_position = [random.randint(1, 30), random.randint(1, 30)]

    level_layout[fold_position[1]][fold_position[0]] = 'f'

    while sheep_position[0] == fold_position[0] and sheep_position[1] == fold_position[1]:
        sheep_position = [random.randint(1, 30), random.randint(1, 30)]
    while sheep_position[0] == dog_position[0] and sheep_position[1] == dog_position[1]:
        dog_position = [random.randint(0, 31), random.randint(0, 31)]

    level_layout[sheep_position[1]][sheep_position[0]] = 's'
    level_layout[dog_position[1]][dog_position[0]] = 'd'

    level_height = len(level_layout)
    level_width = len(level_layout[0])

    # entity locations
    dog_start = (dog_position[1], dog_position[0])
    fold = (fold_position[1], fold_position[0])
    sheep_start = (sheep_position[1], sheep_position[0])

    number_of_sheep = sum(y.count('s') for y in level_layout)

def find_state():
    state = []
    # TODO: find a way to evaluate the current state
    return state

def sample_action_space():
    action = []
    # TODO: sample an action from action space..?
    return action

def find_relative_pos(entity_pos: tuple, in_relation_to_pos: tuple):
    (x1, y1) = entity_pos[0], entity_pos[1]
    (x2, y2) = in_relation_to_pos[0], in_relation_to_pos[1]
    return (x1 - x2, y1 - y2)

def take_action(action):
    # TODO: convert action into a dog movement
    # TODO: update level
    # TODO: return resulting state, reward and whether it solved the level (done)

def train_RL():
    global q_table

    for i in range(1, episodes+1):
        reset_level_state()
        state = find_state()

        epochs, penalties, reward = 0, 0, 0
        done = False

        while not done:
            if random.uniform(0, 1) < epsilon:
                # TODO: explore action space
                action = sample_action_space()
            else:
                # TODO: exploit learned values
                action = np.argmax(q_table[state])

        next_state, reward, done = take_action(action)

        old_value = q_table[state, action]
        next_max = np.max(q_table[next_state])

        new_value = (1 - alpha) * old_value + alpha * (reward + gamma * next_max)
        q_table[state, action] = new_value

        if reward == -10: #TODO: penalty for misdirecting sheep? Consider change
            penalties += 1

        state = next_state
        epochs += 1

    if i % 100 == 0:
        print(f"Episode: {i}")

    print("Training finished.\n")