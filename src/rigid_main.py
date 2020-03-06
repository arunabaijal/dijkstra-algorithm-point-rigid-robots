# *********************************** Point Robot ********************************#
import matplotlib.pyplot as plt
import numpy as np
import queue
from math import pi


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


def create_graph(xmax=300, ymax=200):
    graph = np.ones((ymax, xmax))
    for i in range(xmax):
        for j in range(ymax):
            if not check_node([i, j]):
                graph[j][i] = 0
    return graph


"""
# Function to check if the given point lies outside the trial map or in the obstacle space
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
"""


# Function to check if the given point lies outside the final map or in the obstacle space
def check_node(node):
    u = 150.  # x-position of the center
    v = 100.  # y-position of the center
    a = 40.  # radius on the x-axis
    b = 20.  # radius on the y-axis

    clearance = 5


    if node[0] + clearance >= 300 or node[0] - clearance < 0 or node[1] + clearance >= 200 or node[1] - clearance < 0:
        print('Sorry the point is out of bounds! Try again.')
        return False
    elif (node[0] - 225) ** 2 + (node[1] - 150) ** 2 < (25 + clearance) ** 2:
        print('Sorry the point is in the obstacle space! Try again.1')
        return False
    elif ((node[0] - 150) ** 2) / (a + clearance) ** 2 + ((node[1] - 100) ** 2) / (b + clearance) ** 2 < 1:
        print('Sorry the point is in the obstacle space! Try again.2')
        return False
    elif (3 * node[0] - 5 * node[1] > 450 + clearance) and (3 * node[0] + 5 * node[1] < 900 - clearance) and (
            3 * node[0] - 5 * node[1] < 600 - clearance) and (3 * node[0] + 5 * node[1] > 750 + clearance):
        print('Sorry the point is in the obstacle space! Try again.3')
        return False
    elif (1.732 * node[0] - node[1] < 134.54 - clearance) and (0.577 * node[0] + node[1] < 96.36 - clearance) and (
            node[1] + 0.577 * node[0] > 84.849 + clearance) and (1.732 * node[0] - node[1] > -15.453 + clearance):
        print('Sorry the point is in the obstacle space! Try again. hello')
        return False
    # Dividing concave shape into 2 convex shapes
    elif (node[1] < 185 - clearance) and (node[1] + 1.4 * node[0] < 290 - clearance) and (1.2 * node[0] - node[1] < -30 - clearance) and (
            node[1] + 1.2 * node[0] > 210 + clearance):
        print('Sorry the point is in the obstacle space! Try again.4')
        return False
    elif (node[1] + 1.4 * node[0] < 220 - clearance) and (node[0] - node[1] < -100 - clearance) and (13 * node[0] - node[1] > 140 + clearance):
        print('Sorry the point is in the obstacle space! Try again.5')
        return False
    else:
        return True


def index(position):
    return position[0] + position[1] * 300


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
    # Taking start point and goal point from the user
    start_point = eval(input('Please enter the start point in this format - [x,y]: '))
    while not check_node(start_point):
        start_point = eval(input('Please enter the start point in this format - [x,y]: '))

    print('The start point you gave is:', start_point)
    print('')

    goal_point = eval(input('Please enter the goal point in this format - [x,y]: '))
    while not check_node(goal_point):
        goal_point = eval(input('Please enter the goal point in this format - [x,y]: '))

    print('The goal point you gave is:', goal_point)

    """
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
    """
    # Plotting the final map

    u = 150.  # x-position of the center
    v = 100.  # y-position of the center
    a = 40.  # radius on the x-axis
    b = 20.  # radius on the y-axis

    fig = plt.figure()
    plt.axes()
    circle = plt.Circle((225, 150), radius=25, fc='y')
    line1 = plt.Line2D((0, 300), (200, 200), lw=2.5)
    line2 = plt.Line2D((0, 300), (0, 0), lw=2.5)
    line3 = plt.Line2D((0, 0), (0, 200), lw=2.5)
    line4 = plt.Line2D((300, 300), (0, 200), lw=2.5)

    # Lines for the diamond
    line5 = plt.Line2D((200, 225), (30, 45), lw=2.5)
    line6 = plt.Line2D((225, 250), (45, 30), lw=2.5)
    line7 = plt.Line2D((250, 225), (30, 15), lw=2.5)
    line8 = plt.Line2D((225, 200), (15, 30), lw=2.5)

    # Lines for the tilted cuboid
    line9 = plt.Line2D((95, 100), (30, 38.66), lw=2.5)
    line10 = plt.Line2D((100, 35.05), (38.66, 76.16), lw=2.5)
    line11 = plt.Line2D((35.05, 30.05), (76.16, 67.5), lw=2.5)
    line12 = plt.Line2D((30.05, 95), (67.5, 30), lw=2.5)

    # Lines for the concave shape
    line13 = plt.Line2D((20, 25), (120, 185), lw=2.5)
    line14 = plt.Line2D((25, 75), (185, 185), lw=2.5)
    line15 = plt.Line2D((75, 100), (185, 150), lw=2.5)
    line16 = plt.Line2D((100, 75), (150, 120), lw=2.5)
    line17 = plt.Line2D((75, 50), (120, 150), lw=2.5)
    line18 = plt.Line2D((50, 20), (150, 120), lw=2.5)

    plt.gca().add_line(line1)
    plt.gca().add_line(line2)
    plt.gca().add_line(line3)
    plt.gca().add_line(line4)
    plt.gca().add_line(line5)
    plt.gca().add_line(line6)
    plt.gca().add_line(line7)
    plt.gca().add_line(line8)
    plt.gca().add_line(line9)
    plt.gca().add_line(line10)
    plt.gca().add_line(line11)
    plt.gca().add_line(line12)
    plt.gca().add_line(line13)
    plt.gca().add_line(line14)
    plt.gca().add_line(line15)
    plt.gca().add_line(line16)
    plt.gca().add_line(line17)
    plt.gca().add_line(line18)
    plt.gca().add_patch(circle)
    plt.axis('scaled')

    t = np.linspace(0, 2 * pi, 100)
    plt.plot(u + a * np.cos(t), v + b * np.sin(t))
    plt.grid(color='lightgray', linestyle='--')

    start = Node(start_point, None, 0, index(start_point))
    goal = start.dijkstra(goal_point)
    open('nodePath.txt', 'w').close()
    generate_path(goal, start_point)

    # Animating the explored nodes
    # file = open('Nodes.txt', 'r')
    # points = file.readlines()
    # for point in points:
    #     pts = point.split(',')
    #     plt.scatter(int(pts[0]), int(pts[1]), c='b', s=6)
    #     # plt.pause(0.05)
    file = open('nodePath.txt', 'r')
    points = file.readlines()
    for point in points:
        pts = point.split(',')
        plt.scatter(int(pts[0]), int(pts[1]), c='g', s=5)
    plt.show()


if __name__ == '__main__':
    main()
