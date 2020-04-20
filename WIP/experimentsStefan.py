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


level_nodes = []
level_height = len(level_layout)
level_width = len(level_layout[0])


def generate_level_nodes():
    for y in range(level_height):
        level_nodes.append([])
        for x in range(level_width):
            new_node = Node(x, y, level_layout[y][x])
            level_nodes[-1].append(new_node)


def get_node(x, y):
    return level_nodes[y][x]


def neighbors(node: Node):
    directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]  # up, right, down, left
    result = []
    print("Finding neighbors for (" + str(node.x) + ", " + str(node.y) + ")...")
    for direction in directions:
        if -1 < node.y + direction[0] < level_height:
            if -1 < node.x + direction[1] < level_width:
                neighbor = level_nodes[node.y + direction[0]][node.x + direction[1]]
                node.neighbors.append(neighbor)
                print("Neighbor at (" + str(neighbor.x) + ", " + str(neighbor.y) + ")")


def connect_neighbors():
    for y in range(level_height):
        for x in range(level_width):
            neighbors(get_node(x, y))
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
            to_print += get_node(x, y).content + " "
        print(to_print)


generate_level_nodes()
connect_neighbors()
print_nodes()


# Manhattan distance on a square grid
def heuristic(a, b):
    (x1, y1) = a
    (x2, y2) = b
    return abs(x1 - x2) + abs(y1 - y2)