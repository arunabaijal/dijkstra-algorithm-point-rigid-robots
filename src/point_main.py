#*********************************** Point Robot ********************************#
import matplotlib.pyplot as plt
import numpy as np
import queue

class Node():
    def __init__(self, start_point, parent, cost2come, ind):
        self.current = start_point
        self.parent = parent
        self.cost2come = cost2come
        self.index = ind

    def moveDown(self):
        new_position = [self.current[0], self.current[1] - 1]
        if check_node(new_position):
            return new_position, 'down'
        else:
            return False

    def moveUp(self):
        new_position = [self.current[0], self.current[1] + 1]
        if not check_node(new_position):
            return False
        else:
            return new_position, 'up'

    def moveRight(self):
        new_position = [self.current[0] + 1, self.current[1]]
        if not check_node(new_position):
            return False
        else:
            return new_position, 'right'

    def moveLeft(self):
        new_position = [self.current[0] - 1, self.current[1]]
        if not check_node(new_position):
            return False
        else:
            return new_position, 'left'

    def moveDownRight(self):
        new_position = [self.current[0] + 1, self.current[1] - 1]
        if check_node(new_position):
            return new_position, 'down right'
        else:
            return False

    def moveDownLeft(self):
        new_position = [self.current[0] - 1, self.current[1] - 1]
        if not check_node(new_position):
            return False
        else:
            return new_position, 'down left'

    def moveUpRight(self):
        new_position = [self.current[0] + 1, self.current[1] + 1]
        if not check_node(new_position):
            return False
        else:
            return new_position, 'up right'

    def moveUpLeft(self):
        new_position = [self.current[0] - 1, self.current[1] + 1]
        if not check_node(new_position):
            return False
        else:
            return new_position, 'up left'

    def dijkstra(self, goal):
        open('Nodes.txt', 'w').close()  # clearing files
        accepted = dict()
        visited = dict()
        toBeVisited = queue.Queue()
        toBeVisited.put(self)
        accepted[self.index] = self
        f = open("Nodes.txt", "a+")
        while not toBeVisited.empty():
            visitingNode = toBeVisited.get()
            node = visitingNode.current
            if visitingNode.index in visited:  # check if node already visited
                continue
            else:
                toWrite = str(node)
                f.write(toWrite[1:len(toWrite) - 1] + '\n')
                if np.array_equal(node, goal):  # check if goal found
                    f.close()
                    return visitingNode
                # create all possible children
                if visitingNode.moveUp():
                    new, up = visitingNode.moveUp()
                    new_index = index(new)
                    new_node = Node(new, visitingNode, visitingNode.cost2come + 1, new_index)
                    if new_index not in visited:
                        if new_index in accepted:
                            if accepted[new_index].cost2come > new_node.cost2come:
                                accepted[new_index] = new_node
                                toBeVisited.put(new_node)
                        else:
                            accepted[new_index] = new_node
                            toBeVisited.put(new_node)
                if visitingNode.moveDown():
                    new, down = visitingNode.moveDown()
                    new_index = index(new)
                    new_node = Node(new, visitingNode, visitingNode.cost2come + 1, new_index)
                    if new_index not in visited:
                        if new_index in accepted:
                            if accepted[new_index].cost2come > new_node.cost2come:
                                accepted[new_index] = new_node
                                toBeVisited.put(new_node)
                        else:
                            accepted[new_index] = new_node
                            toBeVisited.put(new_node)
                if visitingNode.moveRight():
                    new, right = visitingNode.moveRight()
                    new_index = index(new)
                    new_node = Node(new, visitingNode, visitingNode.cost2come + 1, new_index)
                    if new_index not in visited:
                        if new_index in accepted:
                            if accepted[new_index].cost2come > new_node.cost2come:
                                accepted[new_index] = new_node
                                toBeVisited.put(new_node)
                        else:
                            accepted[new_index] = new_node
                            toBeVisited.put(new_node)
                if visitingNode.moveLeft():
                    new, left = visitingNode.moveLeft()
                    new_index = index(new)
                    new_node = Node(new, visitingNode, visitingNode.cost2come + 1, new_index)
                    if new_index not in visited:
                        if new_index in accepted:
                            if accepted[new_index].cost2come > new_node.cost2come:
                                accepted[new_index] = new_node
                                toBeVisited.put(new_node)
                        else:
                            accepted[new_index] = new_node
                            toBeVisited.put(new_node)
                if visitingNode.moveUpRight():
                    new, upRight = visitingNode.moveUpRight()
                    new_index = index(new)
                    new_node = Node(new, visitingNode, visitingNode.cost2come + np.sqrt(2), new_index)
                    if new_index not in visited:
                        if new_index in accepted:
                            print(accepted[new_index].cost2come, new_node.cost2come)
                            if accepted[new_index].cost2come > new_node.cost2come:
                                accepted[new_index] = new_node
                                toBeVisited.put(new_node)
                        else:
                            accepted[new_index] = new_node
                            toBeVisited.put(new_node)
                if visitingNode.moveDownRight():
                    new, downRight = visitingNode.moveDownRight()
                    new_index = index(new)
                    new_node = Node(new, visitingNode, visitingNode.cost2come + np.sqrt(2), new_index)
                    if new_index not in visited:
                        if new_index in accepted:
                            if accepted[new_index].cost2come > new_node.cost2come:
                                accepted[new_index] = new_node
                                toBeVisited.put(new_node)
                        else:
                            accepted[new_index] = new_node
                            toBeVisited.put(new_node)
                if visitingNode.moveUpLeft():
                    new, upLeft = visitingNode.moveUpLeft()
                    new_index = index(new)
                    new_node = Node(new, visitingNode, visitingNode.cost2come + np.sqrt(2), new_index)
                    if new_index not in visited:
                        if new_index in accepted:
                            if accepted[new_index].cost2come > new_node.cost2come:
                                accepted[new_index] = new_node
                                toBeVisited.put(new_node)
                        else:
                            accepted[new_index] = new_node
                            toBeVisited.put(new_node)
                if visitingNode.moveDownLeft():
                    new, downLeft = visitingNode.moveDownLeft()
                    new_index = index(new)
                    new_node = Node(new, visitingNode, visitingNode.cost2come + np.sqrt(2), new_index)
                    if new_index not in visited:
                        if new_index in accepted:
                            if accepted[new_index].cost2come > new_node.cost2come:
                                accepted[new_index] = new_node
                                toBeVisited.put(new_node)
                        else:
                            accepted[new_index] = new_node
                            toBeVisited.put(new_node)
                del accepted[visitingNode.index]
                visited[visitingNode.index] = visitingNode
        f.close()
        return False

def create_graph(xmax = 200, ymax = 100):
    graph = np.ones((ymax, xmax))
    for i in range(xmax):
        for j in range(ymax):
            if not check_node([i,j]):
                graph[j][i] = 0
    return graph


# Function to check if the given point lies outside the map or in the obstacle space
def check_node(node):
    if node[0] >= 200 or node[0] < 0 or node[1] >= 100 or node[1] < 0:
        # print('Sorry the point you entered is out of bounds! Try again.')
        return False
    elif 90 <= node[0] <= 110 and 40 <= node[1] <= 60:
        # print('Sorry the point you entered is in the obstacle space! Try again.')
        return False
    elif (node[0]-160)**2 + (node[1]-50)**2 < 15**2:
        # print('Sorry the point you entered is in the obstacle space! Try again.')
        return False
    else:
        return True


def index(position):
    return position[0] + position[1]*200

def generate_path(node, root):
    while (not np.array_equal(node.current, root)):
        f = open("nodePath.txt", "r+")
        content = f.read()
        f.seek(0, 0)
        toWrite = str(node.current)
        node = node.parent
        f.write(toWrite[1:len(toWrite) - 1] + '\n' + content)
        f.close()

    f = open("nodePath.txt", "r+")
    content = f.read()
    f.seek(0, 0)
    toWrite = str(node.current)
    f.write(toWrite[1:len(toWrite) - 1] + '\n' + content)
    f.close()

# Functions for the action space - Up, Down, Left, Right, Up-Right, Down-Right, Up-left, Down-left

def main():
    #Taking start point and goal point from the user
    start_point = eval(input('Please enter the start point in this format - [x,y]: '))
    while not check_node(start_point):
        start_point = eval(input('Please enter the start point in this format - [x,y]: '))

    print('The start point you gave is:', start_point)
    print('')

    goal_point = eval(input('Please enter the goal point in this format - [x,y]: '))
    while not check_node(goal_point):
        goal_point = eval(input('Please enter the goal point in this format - [x,y]: '))

    print('The goal point you gave is:', goal_point)


    # Plotting the trial map
    fig = plt.figure()
    plt.axes()
    circle = plt.Circle((160, 50), radius=15, fc='y')
    square = plt.Rectangle((90, 40), 20, 20, fc='r')
    line1 = plt.Line2D((0, 200), (100, 100), lw=2.5)
    line2 = plt.Line2D((0, 200), (0, 0), lw=2.5)
    line3 = plt.Line2D((0, 0), (0, 100), lw=2.5)
    line4 = plt.Line2D((200, 200), (0, 100), lw=2.5)
    plt.scatter(start_point[0], start_point[1])
    plt.scatter(goal_point[0], goal_point[1])

    plt.gca().add_line(line1)
    plt.gca().add_line(line2)
    plt.gca().add_line(line3)
    plt.gca().add_line(line4)
    plt.gca().add_patch(circle)
    plt.gca().add_patch(square)
    plt.axis('scaled')

    start = Node(start_point, None, 0, index(start_point))
    goal = start.dijkstra(goal_point)
    open('nodePath.txt', 'w').close()
    generate_path(goal, start_point)

    # Animating the explored nodes
    file = open('Nodes.txt', 'r')
    points = file.readlines()
    for point in points:
        pts = point.split(',')
        plt.scatter(int(pts[0]), int(pts[1]), c='b')
        # plt.pause(0.05)
    file = open('nodePath.txt', 'r')
    points = file.readlines()
    for point in points:
        pts = point.split(',')
        plt.scatter(int(pts[0]), int(pts[1]), c='g')

    plt.show()

if __name__ == '__main__':
    main()