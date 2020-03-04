#*********************************** Point Robot ********************************#
import matplotlib.pyplot as plt
import numpy as np

class Node():
    def __init__(self, start_point, parent, cost2come, index):
        self.current = start_point
        self.parent = parent
        self.cost2come = cost2come
        self.index = index

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

    def bfs(self, goal):
        open('Nodes.txt', 'w').close()  # clearing files
        # open('NodesInfo.txt', 'w').close()
        accepted = dict()
        rejected = dict()
        toBeVisited = dict()
        toBeVisited[self.index] = self
        accepted[self.index] = self
        f = open("Nodes.txt", "a+")
        # f2 = open("NodesInfo.txt", "a+")
        # countMax = 1
        while (len(toBeVisited) != 0):
            # count = 0
            ind = 0
            for key,value in toBeVisited.items():
                ind = key
                break
            visitingNode = toBeVisited.pop(ind)
            node = visitingNode.current
            # print(tuple(node))
            # f2.write(str(visitingNode.index) + ' ' + str(
            # 	0 if visitingNode.parent == None else visitingNode.parent.index) + '\n')
            if visitingNode.index in rejected:  # check if node already visited
                continue
            else:
                toWrite = str(node)
                f.write(toWrite[1:len(toWrite) - 1] + '\n')
                if np.array_equal(node, goal):  # check if goal found
                    f.close()
                    # f2.close()
                    return visitingNode
                # create all possible children
                del accepted[visitingNode.index]
                rejected[visitingNode.index] = visitingNode
                if visitingNode.moveUp():
                    new, up = visitingNode.moveUp()
                    # if not (tuple(new.reshape(1, 9)[0]) in rejected):
                    # 	count += 1
                    new_index  = index(new)
                    new_node = Node(new, visitingNode, visitingNode.cost2come + 1, new_index)
                    if not (new_index in rejected):
                        if new_index in accepted:
                            if accepted[new_index].cost2come > new_node.cost2come:
                                accepted[new_index] = new_node
                                toBeVisited[new_index] = new_node
                        else:
                            accepted[new_index] = new_node
                            toBeVisited[new_index] = new_node
                if visitingNode.moveDown():
                    new, down = visitingNode.moveDown()
                    # if not (tuple(new.reshape(1, 9)[0]) in visited):
                    # 	count += 1
                    new_index = index(new)
                    new_node = Node(new, visitingNode, visitingNode.cost2come + 1, new_index)
                    if not (new_index in rejected):
                        if new_index in accepted:
                            if accepted[new_index].cost2come > new_node.cost2come:
                                accepted[new_index] = new_node
                                toBeVisited[new_index] = new_node
                        else:
                            accepted[new_index] = new_node
                            toBeVisited[new_index] = new_node
                if visitingNode.moveRight():
                    new, right = visitingNode.moveRight()
                    # if not (tuple(new.reshape(1, 9)[0]) in visited):
                    # 	count += 1
                    new_index = index(new)
                    new_node = Node(new, visitingNode, visitingNode.cost2come + 1, new_index)
                    if not (new_index in rejected):
                        if new_index in accepted:
                            if accepted[new_index].cost2come > new_node.cost2come:
                                accepted[new_index] = new_node
                                toBeVisited[new_index] = new_node
                        else:
                            accepted[new_index] = new_node
                            toBeVisited[new_index] = new_node
                if visitingNode.moveLeft():
                    new, left = visitingNode.moveLeft()
                    # if not (tuple(new.reshape(1, 9)[0]) in visited):
                    # 	count += 1
                    new_index = index(new)
                    new_node = Node(new, visitingNode, visitingNode.cost2come + 1, new_index)
                    if not (new_index in rejected):
                        if new_index in accepted:
                            if accepted[new_index].cost2come > new_node.cost2come:
                                accepted[new_index] = new_node
                                toBeVisited[new_index] = new_node
                        else:
                            accepted[new_index] = new_node
                            toBeVisited[new_index] = new_node
                if visitingNode.moveUpRight():
                    new, upRight = visitingNode.moveUpRight()
                    # if not (tuple(new.reshape(1, 9)[0]) in visited):
                    # 	count += 1
                    new_index = index(new)
                    new_node = Node(new, visitingNode, visitingNode.cost2come + np.sqrt(2), new_index)
                    if not (new_index in rejected):
                        if new_index in accepted:
                            if accepted[new_index].cost2come > new_node.cost2come:
                                accepted[new_index] = new_node
                                toBeVisited[new_index] = new_node
                        else:
                            accepted[new_index] = new_node
                            toBeVisited[new_index] = new_node
                if visitingNode.moveDownRight():
                    new, downRight = visitingNode.moveDownRight()
                    # if not (tuple(new.reshape(1, 9)[0]) in visited):
                    # 	count += 1
                    new_index = index(new)
                    new_node = Node(new, visitingNode, visitingNode.cost2come + np.sqrt(2), new_index)
                    if not (new_index in rejected):
                        if new_index in accepted:
                            if accepted[new_index].cost2come > new_node.cost2come:
                                accepted[new_index] = new_node
                                toBeVisited[new_index] = new_node
                        else:
                            accepted[new_index] = new_node
                            toBeVisited[new_index] = new_node
                if visitingNode.moveUpLeft():
                    new, upLeft = visitingNode.moveUpLeft()
                    # if not (tuple(new.reshape(1, 9)[0]) in visited):
                    # 	count += 1
                    new_index = index(new)
                    new_node = Node(new, visitingNode, visitingNode.cost2come + np.sqrt(2), new_index)
                    if not (new_index in rejected):
                        if new_index in accepted:
                            if accepted[new_index].cost2come > new_node.cost2come:
                                accepted[new_index] = new_node
                                toBeVisited[new_index] = new_node
                        else:
                            accepted[new_index] = new_node
                            toBeVisited[new_index] = new_node
                if visitingNode.moveDownLeft():
                    new, downLeft = visitingNode.moveDownLeft()
                    # if not (tuple(new.reshape(1, 9)[0]) in visited):
                    # 	count += 1
                    new_index = index(new)
                    new_node = Node(new, visitingNode, visitingNode.cost2come + np.sqrt(2), new_index)
                    if not (new_index in rejected):
                        if new_index in accepted:
                            if accepted[new_index].cost2come > new_node.cost2come:
                                accepted[new_index] = new_node
                                toBeVisited[new_index] = new_node
                        else:
                            accepted[new_index] = new_node
                            toBeVisited[new_index] = new_node
                # countMax = countMax + count
        f.close()
        # f2.close()
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
        print(node.current)
        node = node.parent
        f.write(toWrite[1:len(toWrite) - 1] + '\n' + content)
        f.close()

    f = open("nodePath.txt", "r+")
    content = f.read()
    f.seek(0, 0)
    print(node.current)
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
    goal = start.bfs(goal_point)
    generate_path(goal, start_point)

    # Animating the explored nodes
    file = open('nodePath.txt', 'r')
    points = file.readlines()
    for point in points:
        pts = point.split(',')
        # print(int(pts[0]), int(pts[1]))
        plt.scatter(int(pts[0]), int(pts[1]), c='g')
        # plt.pause(0.05)
    # for i in range(25):
    # 	new  = up(start_point)
    # 	start_point = new
    # 	plt.scatter(start_point[0], start_point[1])
    # 	plt.pause(0.25)

    plt.show()

if __name__ == '__main__':
    main()