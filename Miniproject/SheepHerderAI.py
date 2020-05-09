from queue import PriorityQueue
import copy

# level information
#  legend: _ = open, # = blocked, f = fold, s = sheep, d = dog
level_layout = [
    ['_', '_', '_', '_', '_', '_', '_', '_', '_'],
    ['_', '_', 'f', '_', '_', '_', '_', '_', '_'],
    ['_', '_', '_', '_', '_', '_', '_', '_', '_'],
    ['_', '_', '_', '_', '_', '_', '_', '_', '_'],
    ['_', '_', '_', '_', '_', '_', '_', '_', '_'],
    ['_', '_', 's', '_', '_', '_', '_', '_', '_'],
    ['_', '_', '_', '_', '_', '_', '_', '_', '_'],
    ['_', '_', '_', '_', '_', '_', '_', '_', '_'],
    ['_', '_', '_', '_', '_', '_', '_', 'd', '_'],
    ['_', '_', '_', '_', '_', '_', '_', '_', '_']]

level_graph = []  # 1D list of nodes
level_height = len(level_layout)
level_width = len(level_layout[0])

# entity locations
dog_start = (None, None)
fold = (None, None)
sheep_start = (None, None)

debug = False

# do not change here
number_of_sheep = 0


class Node:
    def __init__(self, x, y, content):
        self.x = x
        self.y = y
        self.content = content
        self.neighbors = []

    def location_to_tuple(self):
        return self.x, self.y

    #  connects this node to neighboring node in given graph
    def connect_neighbors(self, graph):
        if self.content != '#':
            directions = [[0, -1], [1, 0], [0, 1], [-1, -0]]  # up, right, down, left
            if debug:
                print("Finding neighbors for (" + str(self.x) + ", " + str(self.y) + ")...")
            for direction in directions:
                if -1 < self.y + direction[1] < level_height:
                    if -1 < self.x + direction[0] < level_width:
                        neighbor = get_node_from_location_tuple(graph, (self.x + direction[0], self.y + direction[1]))
                        if neighbor.content != '#':
                            self.neighbors.append(neighbor)
                            if debug:
                                print("Neighbor at (" + str(neighbor.x) + ", " + str(neighbor.y) + ")")


# given an empty graph, and a level layout, generates and appends the resulting graph node structure
# https://robertheaton.com/2014/02/09/pythons-pass-by-object-reference-as-explained-by-philip-k-dick/
def generate_level_nodes(graph: list, layout: list):
    for y in range(level_height):
        for x in range(level_width):
            new_node = Node(x, y, level_layout[y][x])
            graph.append(new_node)  # level_graph[-1]

            if layout[y][x] == 'd':
                global dog_start
                dog_start = new_node.location_to_tuple()
                if debug:
                    print("Dog starts at (" + str(new_node.x) + ", " + str(new_node.y) + ")")
            elif layout[y][x] == 's':
                global sheep_start
                global number_of_sheep
                sheep_start = new_node.location_to_tuple()
                number_of_sheep += 1
                if debug:
                    print("Sheep starts at (" + str(new_node.x) + ", " + str(new_node.y) + ")")
            elif layout[y][x] == 'f':
                global fold
                fold = new_node.location_to_tuple()
                if debug:
                    print("Fold is at (" + str(new_node.x) + ", " + str(new_node.y) + ")")


# gets a node from graph at a specific coordinate
def get_node_from_location_tuple(graph, location):
    x, y = location
    i = y * level_width + x
    return graph[i]


# goes through each node in a graph to find their neighbours
def connect_neighbors(graph):
    for y in range(level_height):
        for x in range(level_width):
            get_node_from_location_tuple(graph, (x, y)).connect_neighbors(graph)
            if debug:
                print()
    if debug:
        print("Graph complete.")


# prints the level from graph
def print_nodes(graph):
    for y in range(level_height):
        to_print = ""
        for x in range(level_width):
            to_print += get_node_from_location_tuple(graph, (x, y)).content + " "
        print(to_print)


# prints the level from graph, including a path
def print_nodes_with_path(graph, path, directions):
    for y in range(level_height):
        to_print = ""
        for x in range(level_width):
            if (x, y) in path:
                if path.index((x, y)) < len(directions):
                    to_print += directions[path.index((x, y))] + " "
                else:
                    to_print += "x "
            else:
                to_print += get_node_from_location_tuple(graph, (x, y)).content + " "
        print(to_print)


# Manhattan distance on a square grid
def heuristic(a: tuple, b: tuple):
    (x1, y1) = a[0], a[1]
    (x2, y2) = b[0], b[1]
    return abs(x1 - x2) + abs(y1 - y2)


# given a graph of locations, a starting point and a goal point, search for an optimal path
def a_star_search(graph, start: tuple, goal: tuple):
    frontier = PriorityQueue()  # queue of prioritized frontier nodes
    frontier.put((0, start))  # put the start location in the queue with priority 0 (no cost)
    came_from = {}  # stores location traversals in a dictionary, using (x, y) tuples as keys
    cost_so_far = {}  # stores path costs in a dictionary, using (x, y) tuples as keys
    came_from[start] = None  # store that we didn't traverse from anywhere to the starting location
    cost_so_far[start] = 0  # store the traversal cost for this path (which is 0 at the start)

    while not frontier.empty():  # as long as there are nodes in the frontier to visit
        current = frontier.get()

        if current[1] == goal:  # if this node is the goal, we're done!
            if debug:
                print("goal found")
            break

        current_node = get_node_from_location_tuple(graph, current[1])

        for next in current_node.neighbors:  # for each neighbor that current node has
            new_cost = cost_so_far[current[1]] + 1  # all costs are currently just 1

            neighbor = next.location_to_tuple()
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:  # if neighbor location not visited
                #  before, or new path to neighbor location has lower cost than when last visited
                cost_so_far[neighbor] = new_cost  # store new cost, using this location as key
                priority = new_cost + heuristic(goal, neighbor)  # use heuristic to prioritize for continuing this path
                new_frontier_element = (priority, neighbor)  # make new frontier element with priority
                frontier.put(new_frontier_element)  # add to frontier
                came_from[neighbor] = current  # store which previous node we came from, using this location as key

    return came_from, cost_so_far  # return the dictionaries containing the paths and costs


#  reads the came_from list and returns the found path and costs
def reconstruct_path(came_from, cost_so_far, start: tuple, goal: tuple):
    path_current = goal  # we start reconstructing from goal
    path = []
    costs = []
    while path_current != start:  # as long as we haven't reached start
        path.append(path_current)  # append the current location to the path
        costs.append(cost_so_far[path_current])  # append the associated cost to this point
        path_current = came_from[path_current][1]  # get the location we came from to reach this point
    path.append(start)  # append the start point to the list
    costs.append(cost_so_far[start])  # append the start cost (should be 0) to the list
    path.reverse()  # flip the order, so it runs from start to goal
    costs.reverse()  # same with costs
    return path, costs


#  given two locations, returns a direction to-from as (x, y) tuple
def locations_to_direction(to_loc: tuple, from_loc: tuple):
    direction = (to_loc[0] - from_loc[0], to_loc[1] - from_loc[1])
    return direction


#  given a direction tuple, returns a char representing the movement direction
def direction_to_char(direction: tuple):
    char_dict = {(0, -1): '^',
                 (1, 0): '>',
                 (0, 1): 'v',
                 (-1, 0): '<'}
    return char_dict[direction]


# given a direction tuple, returns the opposite direction
def reverse_direction(direction: tuple):
    return (-direction[0], -direction[1])


#  given two locations, returns a char representing the movement direction to-from
def locations_to_direction_char(to_loc: tuple, from_loc: tuple):
    return direction_to_char(locations_to_direction(to_loc, from_loc))


#  given a path, returns a list of directions in the form of chars
def path_to_directions(path):
    directions = []
    for i in range(len(path) - 1):
        to_loc, from_loc = path[i + 1], path[i]
        directions.append(locations_to_direction_char(to_loc, from_loc))
    return directions


# given a sheep's path to a fold, returns a herding point for moving it the next step
def get_herding_point(path):
    next_dir = locations_to_direction(path[1], path[0])
    rev_dir = reverse_direction(next_dir)
    if debug:
        print(str(next_dir) + " " + str(rev_dir))
    # add starting location together with the reverse direction
    herding_point = tuple(map(lambda i, j: i + j, path[0], rev_dir))

    return herding_point


def get_dog_level_layout(original_level, sheep_location, herding_point):
    dog_level_layout = copy.deepcopy(original_level)  # really stupid, but other options pass references and break map
    directions = [[0, -1], [1, 0], [0, 1], [-1, -0]]  # up, right, down, left

    # check locations around sheep
    for direction in directions:
        # ensure we are within the map
        if -1 < sheep_location[1] + direction[1] < level_height:
            if -1 < sheep_location[0] + direction[0] < level_width:
                neighbor_location = tuple(map(lambda i, j: i + j, sheep_location, direction))
                if neighbor_location != herding_point:
                    dog_level_layout[neighbor_location[1]][neighbor_location[0]] = '#'

    return dog_level_layout


# returns updated graph, and new locations for dog and sheep
def get_updated_scene(graph: list, dog_path: list, sheep_path: list):
    # clear old animal positions
    # dog
    get_node_from_location_tuple(graph, dog_path[0]).content = '_'
    get_node_from_location_tuple(graph, dog_path[-1]).content = 'd'
    # sheep
    get_node_from_location_tuple(graph, sheep_path[0]).content = '_'
    sheep_target_node = get_node_from_location_tuple(graph, sheep_path[1])
    if sheep_target_node.content != 'g':
        sheep_target_node.content = 's'
    else:
        global number_of_sheep
        number_of_sheep -= 1

    return graph, dog_path[-1], sheep_path[1]


def run_sheepherder():
    #  setup
    print("Setting up scene")
    global level_graph
    generate_level_nodes(level_graph, level_layout)
    connect_neighbors(level_graph)
    print_nodes(level_graph)

    sheep_location = sheep_start
    dog_location = dog_start

    auto_continue = False

    while number_of_sheep > 0:

        if not auto_continue:
            result = input('Press Enter for next step, or type "N" to run till the end.')
            print(result)
            if result.lower() == "n":
                auto_continue = True

        sheep_came_from, sheep_cost_so_far = a_star_search(level_graph, sheep_location, fold)
        sheep_path, sheep_costs = reconstruct_path(sheep_came_from, sheep_cost_so_far, sheep_location, fold)
        sheep_directions = path_to_directions(sheep_path)
        print("Sheep path")
        print_nodes_with_path(level_graph, sheep_path, sheep_directions)
        print("Sheep path locations:", sheep_path)
        print("Sheep path costs:", sheep_costs)
        print("Sheep path directions:", sheep_directions)

        if not auto_continue:
            result = input('Press Enter for next step, or type "N" to run till the end.')
            print(result)
            if result.lower() == "n":
                auto_continue = True

        herding_point = get_herding_point(sheep_path)

        # dog information
        dog_level_layout = get_dog_level_layout(level_layout, sheep_location, herding_point)
        dog_graph = []  # 1D list of nodes
        generate_level_nodes(dog_graph, dog_level_layout)
        connect_neighbors(dog_graph)

        dog_came_from, dog_cost_so_far = a_star_search(dog_graph, dog_location, herding_point)
        dog_path, dog_costs = reconstruct_path(dog_came_from, dog_cost_so_far, dog_location, herding_point)

        dog_directions = path_to_directions(dog_path)

        print("Dog path")
        print_nodes_with_path(level_graph, dog_path, dog_directions)
        print("Dog path locations:", dog_path)
        print("Dog path costs:", dog_costs)
        print("Dog path directions:", dog_directions)

        if not auto_continue:
            result = input('Press Enter for next step, or type "N" to run till the end.')
            print(result)
            if result.lower() == "n":
                auto_continue = True

        print("Updating graph")
        level_graph, dog_location, sheep_location = get_updated_scene(level_graph, dog_path, sheep_path)
        print_nodes(level_graph)


run_sheepherder()
