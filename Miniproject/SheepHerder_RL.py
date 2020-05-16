import random
import numpy as np

debug = False
training = True

# level information
level_layout = []
comp_layout = [
    ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
    ['_', 'd', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
    ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
    ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
    ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
    ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
    ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
    ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
    ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
    ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
    ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
    ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
    ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
    ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
    ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
    ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', 'f', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
    ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
    ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
    ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
    ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
    ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
    ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
    ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', 's', '_', '_', '_', '_'],
    ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
    ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
    ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
    ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
    ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
    ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
    ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
    ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
    ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_']]


# starting positions
fold_position = []
dog_position = []
sheep_position = []

level_height = 0
level_width = 0

# entity locations
current_dog_pos = (None, None)
current_fold_pos = (None, None)
current_sheep_pos = (None, None)

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
alpha = 0.1  # learning rate, extent to which Q-values are being updated
gamma = 0.6  # "discount factor", importance given to future rewards
epsilon = 0.1  # chance to try something new during training

# rewards
sheep_closer = 2
sheep_farther = -3
sheep_home = 10
sheep_escape = -10
dog_move = -1
dog_approach = 1

# For plotting metrics
all_epochs = []
all_penalties = []

episodes = 100000


def reset_level():
    global level_layout, fold_position, dog_position, sheep_position, level_height, level_width, current_dog_pos, current_fold_pos, current_sheep_pos, number_of_sheep
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
    if training:
        # Randomize starting positions
        fold_position = [random.randint(1, 30), random.randint(1, 30)]  # TODO: Consider different placement
        dog_position = [random.randint(0, 31), random.randint(0, 31)]
        sheep_position = [random.randint(1, 30), random.randint(1, 30)]
    else:
        # Positions for layout after training starting positions
        fold_position = [15, 15]  
        dog_position = [1, 1]
        sheep_position = [27, 22]

    level_layout[fold_position[1]][fold_position[0]] = 'f'

    while sheep_position[0] == fold_position[0] and sheep_position[1] == fold_position[1]:
        sheep_position = [random.randint(1, 30), random.randint(1, 30)]
    while sheep_position[0] == dog_position[0] and sheep_position[1] == dog_position[1]:
        dog_position = [random.randint(0, 31), random.randint(0, 31)]

    level_layout[sheep_position[1]][sheep_position[0]] = 's'
    level_layout[dog_position[1]][dog_position[0]] = 'd'

    level_height = len(level_layout)
    level_width = len(level_layout[0])

    # entity locations - X,Y format
    current_dog_pos = (dog_position[0], dog_position[1])
    current_fold_pos = (fold_position[0], fold_position[1])
    current_sheep_pos = (sheep_position[0], sheep_position[1])

    number_of_sheep = sum(y.count('s') for y in level_layout)


def update_level_location(position: tuple, new_char):
    global level_layout
    test = level_layout[position[1]][position[0]]
    level_layout[position[1]][position[0]] = new_char


def update_level_locations(positions: list):
    for p in positions:
        if p == current_dog_pos:
            level_layout[p[1]][p[0]] = 'd'
        elif p == current_fold_pos:
            level_layout[p[1]][p[0]] = 'f'
        elif p == current_sheep_pos:
            level_layout[p[1]][p[0]] = 's'
        else:
            level_layout[p[1]][p[0]] = '_'


def find_relative_pos(entity_pos: tuple, in_relation_to_pos: tuple):
    (x1, y1) = entity_pos[0], entity_pos[1]
    (x2, y2) = in_relation_to_pos[0], in_relation_to_pos[1]
    return (x1 - x2, y1 - y2)


# convert a state id (list of 4 trits) into a state number
def state_id_to_state_number(state_id: list):
    state = state_id[0] + state_id[1] * 3 + state_id[2] * 9 + state_id[3] * 27
    return state


# find the current state number
def find_current_state():
    state_id = [0, 0, 0, 0]
    sheep_relative_to_fold = find_relative_pos(current_sheep_pos, current_fold_pos)
    dog_relative_to_sheep = find_relative_pos(current_dog_pos, current_sheep_pos)

    # sheep horizontal
    if sheep_relative_to_fold[0] < 0:  # to the left
        state_id[0] = 0
    elif sheep_relative_to_fold[0] > 0:  # to the right
        state_id[0] = 2
    else:  # correct column
        state_id[0] = 1

    # sheep vertical - signs inverted due to -y being up
    if sheep_relative_to_fold[1] > 0:  # below
        state_id[1] = 0
    elif sheep_relative_to_fold[1] < 0:  # above
        state_id[1] = 2
    else:  # correct row
        state_id[1] = 1

    # dog horizontal
    if dog_relative_to_sheep[0] < 0:  # to the left
        state_id[2] = 0
    elif dog_relative_to_sheep[0] > 0:  # to the right
        state_id[2] = 2
    else:  # correct column
        state_id[2] = 1

    # dog vertical - signs inverted due to -y being up
    if dog_relative_to_sheep[1] > 0:  # below
        state_id[3] = 0
    elif dog_relative_to_sheep[1] < 0:  # above
        state_id[3] = 2
    else:  # correct row
        state_id[3] = 1

    state = state_id_to_state_number(state_id)
    return state


# sample a random action from action space
def sample_action_space():
    action = random.randint(0, 3)
    return action


# Manhattan distance on a square grid
def distance(a: tuple, b: tuple):
    (x1, y1) = a[0], a[1]
    (x2, y2) = b[0], b[1]
    return abs(x1 - x2) + abs(y2 - y1)


# moves the sheep, returning a reward and whether it completed the level. Updates level
def move_sheep(direction: tuple):
    global current_sheep_pos
    reward = 0
    done = False
    old_distance = distance(current_sheep_pos, current_fold_pos)
    old_sheep_pos = current_sheep_pos

    current_sheep_pos = tuple(map(lambda i, j: i + j, current_sheep_pos, direction))  # move sheep

    update_level_locations([old_sheep_pos, current_sheep_pos])

    new_distance = distance(current_sheep_pos, current_fold_pos)
    if old_distance > new_distance:
        reward += sheep_closer

        if current_sheep_pos == current_fold_pos:
            reward += sheep_home
            done = True
            print('Sheep home')
    else:
        reward += sheep_farther

        if not (level_width-1 > current_sheep_pos[0] > 0 and level_height-1 > current_sheep_pos[1] > 0):
            done = True
            reward += sheep_escape
            print('Sheep escaped!')

    return reward, done


# moves the dog, returning a reward and whether it completed the level. Updates level
def move_dog(direction: tuple):
    global current_dog_pos
    reward, done = dog_move, False
    old_distance = distance(current_dog_pos, current_sheep_pos)
    old_dog_pos = current_dog_pos

    new_dog_pos = tuple(map(lambda i, j: i + j, current_dog_pos, direction))
    if level_width > new_dog_pos[0] > -1 and level_height > new_dog_pos[1] > -1:
        current_dog_pos = new_dog_pos  # move dog

    new_distance = distance(current_dog_pos, current_sheep_pos)

    if old_distance > new_distance:
        reward += dog_approach

    update_level_locations([old_dog_pos, current_dog_pos])
    if current_dog_pos == current_fold_pos:
        print('Dog on fold')

    if distance(current_dog_pos, current_sheep_pos) == 1:
        sheep_direction = find_relative_pos(current_dog_pos, current_sheep_pos)
        new_reward, done = move_sheep(sheep_direction)
        reward += new_reward

    return reward, done


# get dog movement direction from action number
def get_move_direction_from_action(action: int):
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]  # 0=up, 1=right, 2=down, 3=left
    return directions[action]


def take_action(action):
    # convert action into a dog movement
    dog_action = get_move_direction_from_action(action)
    # move dog and update level
    reward, done = move_dog(dog_action)
    new_state = find_current_state()
    # return resulting state, reward and whether it solved the level (done)
    return new_state, reward, done


def train_RL():
    print('Training started')
    global q_table, training

    for i in range(1, episodes + 1):
        print('New level')
        reset_level()
        state = find_current_state()

        old_epoch, epochs, penalties, reward = 0, 0, 0, 0
        done = False

        while not done:
            if random.uniform(0, 1) < epsilon:
                action = sample_action_space()  # explore action space
            else:
                action = np.argmax(q_table[state])  # exploit learned values

            next_state, reward, done = take_action(action)

            old_value = q_table[state, action]
            next_max = np.max(q_table[next_state])

            new_value = (1 - alpha) * old_value + alpha * (reward + gamma * next_max)
            q_table[state, action] = new_value

            # if reward == -10:  # TODO: penalty for misdirecting sheep? Consider change
            #     penalties += 1

            state = next_state
            epochs += 1
            if done:
                print(f"Level done at {epochs} epocs.")

            if epochs > 100000:
                print('eh')

        if i % 100 == 0:
            print(f"Episode: {i}")

    print("Training finished.")
    training = False



train_RL()

def print_q_table():
    print("Q_table is as follows:")
    print("\tMov_u\t\t\tMov_r\t\t\tMov_d\t\t\tMod_l")
    print(q_table)

print_q_table()