from queue import PriorityQueue

level_layout = [
    ['_', '_', '_', '_', '_', '_'],
    ['_', '_', 'g', '_', '_', '_'],
    ['_', '_', '_', '_', '_', '_'],
    ['_', '_', '_', '_', '_', '_'],
    ['_', '_', '_', '_', '_', '_'],
    ['_', '_', 's', '_', '_', '_'],
    ['_', '_', '_', '_', '_', '_'],
    ['_', '_', '_', '_', '_', '_'],
    ['_', '_', '_', '_', 'd', '_'],
    ['_', '_', '_', '_', '_', '_']]


class Node:
    def __init__(self, x, y, content):
        self.x = x
        self.y = y
        self.content = content
        self.neighbors = []

    def location_to_tuple(self):
        return self.x, self.y


level_graph = []  # 1D list of nodes
level_height = len(level_layout)
level_width = len(level_layout[0])


dog_start = (None, None)
goal = (None, None)


def generate_level_nodes():
    for y in range(level_height):
        # level_graph.append([])
        for x in range(level_width):
            new_node = Node(x, y, level_layout[y][x])
            level_graph.append(new_node) # level_graph[-1]

            if level_layout[y][x] == 'd':
                global dog_start
                dog_start = new_node.location_to_tuple()
                print("Dog starts at (" + str(new_node.x) + ", " + str(new_node.y) + ")")
            elif level_layout[y][x] == 'g':
                global goal
                goal = new_node.location_to_tuple()
                print("Goal is at (" + str(new_node.x) + ", " + str(new_node.y) + ")")



def get_node_from_location_tuple(location):  # shortcut for getting a node from graph at a specific coordinate
    x, y = location
    i = y * level_width + x
    return level_graph[i]


def neighbors(node: Node):  # finds neighbors for the node
    directions = [[0, -1], [1, 0], [0, 1], [-1, -0]]  # up, right, down, left
    result = []
    print("Finding neighbors for (" + str(node.x) + ", " + str(node.y) + ")...")
    for direction in directions:
        if -1 < node.y + direction[1] < level_height:
            if -1 < node.x + direction[0] < level_width:
                neighbor = get_node_from_location_tuple((node.x + direction[0], node.y + direction[1]))
                node.neighbors.append(neighbor)
                print("Neighbor at (" + str(neighbor.x) + ", " + str(neighbor.y) + ")")


def connect_neighbors():  # goes through each node to find their neighbours
    for y in range(level_height):
        for x in range(level_width):
            neighbors(get_node_from_location_tuple((x, y)))
            print()
    print("Graph complete.")


def print_level():
    for y in range(level_height):
        to_print = ""
        for x in range(level_width):
            to_print += level_layout[y][x] + " "
        print(to_print)


def print_nodes():
    for y in range(level_height):
        to_print = ""
        for x in range(level_width):
            to_print += get_node_from_location_tuple((x, y)).content + " "
        print(to_print)


generate_level_nodes()
connect_neighbors()
print_nodes()


# Manhattan distance on a square grid
def heuristic(a: tuple, b: tuple):
    (x1, y1) = a[0], a[1]
    (x2, y2) = b[0], b[1]
    return abs(x1 - x2) + abs(y1 - y2)


def a_star_search(graph, start: tuple, goal: tuple):
    frontier = PriorityQueue()  #queue of prioritized frontier nodes
    frontier.put((0, start))  # put the start location in the queue with priority 0 (no cost)
    came_from = {}  # stores location traversals in a dictionary, using (x, y) tuples as keys
    cost_so_far = {}  # stores path costs in a dictionary, using (x, y) tuples as keys
    came_from[start] = None  # store that we didn't traverse from anywhere to the starting location
    cost_so_far[start] = 0  # store the traversal cost for this path (which is 0 at the start)

    while not frontier.empty():  # as long as there are nodes in the frontier to visit
        current = frontier.get()

        if current[1] == goal:  # if this node is the goal, we're done!
            print("goal found")
            break

        current_node = get_node_from_location_tuple(current[1])

        for next in current_node.neighbors:  # for each neighbor that current node has
            new_cost = cost_so_far[current[1]] + 1  # all costs are currently just 1

            neighbor = next.location_to_tuple()
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:  # if the neighbor location hasn't been visited
                #  before, or this new path to the neighbor location has a lower cost than when it was last visited
                cost_so_far[neighbor] = new_cost  # store the new cost, using this location as key
                priority = new_cost + heuristic(goal, neighbor)  # uses the heuristic to prioritize for continuing this path
                new_frontier_element = (priority, neighbor)
                frontier.put(new_frontier_element)  # add this location to the frontier with the given priority
                came_from[neighbor] = current  # store which previous node we came from, using this node as key

    return came_from, cost_so_far  # return the dictionaries containing the paths and costs


came_from, cost_so_far = a_star_search(level_graph, dog_start, goal )
print(came_from)
print(cost_so_far)