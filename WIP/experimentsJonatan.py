# A data structure, that organises the items based on priority
from queue import PriorityQueue

# Base class to store imparitive stuff for A*
class State(object):
    # The start, goal, and solver is used to set a manual start state, if we do not have a parent for initial start state
    def __init__(self, value, parent, start = 0, goal = 0):
        # Children is a list of neighboring possibilities
        self.children = []
        # Current parent
        self.parent = parent
        self.value = value 
        # Not going to be set here, it is just a placeholder
        self.dist = 0
        # Check if the parent is plugged in
        if parent:
            # [:] copy parent list into our list
            self.path = parent.path[:]
            # We store our own value into the path = building on it self to keep track
            self.path.append(value)
            # Store start state
            self.start = parent.start
            # Store goal state
            self.goal = parent.goal
        #If there is no parent, we run the else statement 
        else:
            # We start a path, that is a list of objects -> start with current value
            self.path = [value]
            self.start = start 
            self.goal = goal
    
    # The two empty statement are being defined in the class below
    def GetDist(self):
        pass
    
    def CreateChildren(self):
        pass


class State_String(State):
    def __init__(self, value, parent, start = 0, goal = 0):
        # Constructor -> initialise base class = State class
        super(State_String, self).__init__(value, parent, start, goal)
        # Overwrite distance variable
        self.dist = self.GetDist()

    # Use getDist for measuring distance to the goal
    def GetDist(self):
        if self.value == self.goal:
            return 0
        dist = 0
        for i in range(len(self.goal)):
            letter = self.goal[i]
            dist += abs(i - self.value.index(letter))
        return dist
    
    # Sex function -> create children
    def CreateChildren(self):
        # If there is no children, then we create some
        if not self.children:
            for i in range(len(self.goal)-1):
                val = self.value
                val = val[:i] + val[i+1] + val[i] + val[i+2:]
                child = State_String(val, self)
                self.children.append(child)

class AStar_Solver:
    def __init__(self, start, goal):
        # Store the solution from getting from start to goal
        self.path = []
        # Keeps track of all visited children
        self.visitedQueue = []
        self.priorityQueue = PriorityQueue()
        self.start = start 
        self.goal = goal

    def Solve(self):
        startState = State_String(self.start, 0, self.start, self.goal)
        # Used to create IDs for children
        count = 0
        # Adds whatever we toss in - we pass in a tupple = 0 (priority number), count () and startState (contain all our states)
        self.priorityQueue.put((0, count, startState))
        # While the path is empty and the priorityQueue has a size, we continue through the loop
        while(not self.path and self.priorityQueue.qsize()):
            # We access the startState, and creates a child for it
            closestChild = self.priorityQueue.get()[2]
            closestChild.CreateChildren()
            # We then add this child to the visitedQueue -> keeps track of visited children
            self.visitedQueue.append(closestChild.value)
            # We go through each child created for this state
            for child in closestChild.children:
                # If the child has not been visited, we boos up the count by 1
                if child.value not in self.visitedQueue:
                    count += 1
                    # if childs distance is at 0 and do not exist
                    if not child.dist:
                        # we have our solution, so we set our path to the childs path
                        self.path = child.path
                        break
                    self.priorityQueue.put((child.dist, count, child))
        # The priorityQueue broke, and there is an error
        if not self.path:
            print("Goal of " + self.goal + " is not possible!")
        return self.path
# ========================================================
# Main -> calls everything into existence
# We check if we are in the main file
if __name__ == "__main__":
    # We then set the start and goal state
    start1 = "ecbda"
    goal1 = "dabce"
    # Indicator that program is running
    print("starting...")
    # Initialize the solver
    a = AStar_Solver(start1, goal1)
    # Calls main function to solve the problem
    a.Solve()
    # Output the results
    for i in range(len(a.path)):
        print("%d) " %i + a.path[i])