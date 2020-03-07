#*********************************** Point Robot ********************************#
import numpy as np
import queue
import time
import cv2

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
    u=150.     #x-position of the center
    v=100.    #y-position of the center
    a=40.     #radius on the x-axis
    b=20.    #radius on the y-axis

    if node[0] >= 300 or node[0] < 0 or node[1] >= 200 or node[1] < 0:
        print('Sorry the point is out of bounds! Try again.')
        return False
    elif (node[0]-225)**2 + (node[1]-150)**2 <= 25**2:
        print('Sorry the point is in the obstacle space! Try again.')
        return False
    elif ((node[0]-150)**2)/a**2 + ((node[1]-100)**2)/b**2 <= 1:
        print('Sorry the point is in the obstacle space! Try again.')
        return False
    elif (3*node[0]-5*node[1]>=450) and (3*node[0]+5*node[1]<=900) and (3*node[0]-5*node[1]<=600) and (3*node[0]+5*node[1]>=750):
        print('Sorry the point is in the obstacle space! Try again.')
        return False
    elif (1.732*node[0]-node[1]<=134.54) and ( 0.577*node[0]+node[1]<=96.36) and (node[1]+0.577*node[0]>=84.849) and (1.732*node[0] - node[1]>=-15.453):
        print('Sorry the point is in the obstacle space! Try again.')
        return False
    # Dividing concave shape into 2 convex shapes
    elif (node[1]<=185) and (node[1]+1.4*node[0]<=290) and (1.2*node[0]-node[1]<=-30) and (node[1]+1.2*node[0]>=210):
        print('Sorry the point is in the obstacle space! Try again.')
        return False
    elif (node[1]+1.4*node[0]<=220) and (node[0]-node[1]<=-100) and (13*node[0]-node[1]>=140):
        print('Sorry the point is in the obstacle space! Try again.')
        return False
    else:
        return True

def index(position):
    return position[0] + position[1]*300

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

def get_line(x1, y1, x2, y2):
    points = []
    issteep = abs(y2-y1) > abs(x2-x1)
    if issteep:
        x1, y1 = y1, x1
        x2, y2 = y2, x2
    rev = False
    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1
        rev = True
    deltax = x2 - x1
    deltay = abs(y2-y1)
    error = int(deltax / 2)
    y = y1
    ystep = None
    if y1 < y2:
        ystep = 1
    else:
        ystep = -1
    for x in range(x1, x2 + 1):
        if issteep:
            points.append((y, x))
        else:
            points.append((x, y))
        error -= deltay
        if error < 0:
            y += ystep
            error += deltax
    # Reverse the list if the coordinates were reversed
    if rev:
        points.reverse()
    return points
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
    start_time = time.time()
    start = Node(start_point, None, 0, index(start_point))
    goal = start.dijkstra(goal_point)
    open('nodePath.txt', 'w').close()
    generate_path(goal, start_point)
    end_time = time.time()
    print('Time taken to find path: ' + str(end_time - start_time))
    grid = np.ones((201,301,3),dtype=np.uint8)*255
    lines = []
    lines.append(get_line(0,0,300,0))
    lines.append(get_line(0, 0, 0, 200))
    lines.append(get_line(300, 0, 300, 200))
    lines.append(get_line(0, 200, 300, 200))

    lines.append(get_line(200, 30, 225, 45))
    lines.append(get_line(225, 45, 250, 30))
    lines.append(get_line(250, 30, 225, 15))
    lines.append(get_line(225, 15, 200, 30))

    lines.append(get_line(95, 30, 100, 38))
    lines.append(get_line(100, 38, 35, 76))
    lines.append(get_line(35, 76, 30, 67))
    lines.append(get_line(30, 67, 95, 30))

    lines.append(get_line(20, 120, 25, 185))
    lines.append(get_line(25, 185, 75, 185))
    lines.append(get_line(75, 185, 100, 150))
    lines.append(get_line(100, 150, 75, 120))
    lines.append(get_line(75, 120, 50, 150))
    lines.append(get_line(50, 150, 20, 120))

    circle = []
    for i in range(200,250):
        for j in range(125,175):
            if (i - 225)**2 + (j - 150)**2 <= 25**2:
                circle.append([i,j])
    lines.append(circle)

    ellipse = []
    for i in range(110,190):
        for j in range(80,120):
            if (i - 150)**2/40**2 + (j - 100)**2/20**2 <= 1:
                ellipse.append([i,j])
    lines.append(ellipse)

    # node[0]-150)**2)/a**2 + ((node[1]-100)**2)/b**2 <= 1:
    for line in lines:
        for l in line:
            # print(l)
            grid[l[1]][l[0]] = [0, 0, 0]
    file = open('Nodes.txt', 'r')
    points = file.readlines()
    for point in points:
        pts = point.split(',')
        grid[int(pts[1])][int(pts[0])] = [255, 0, 0]
        cv2.imshow('graph',np.flip(grid,0))
        cv2.waitKey(1)
    file = open('nodePath.txt', 'r')
    points = file.readlines()
    for point in points:
        pts = point.split(',')
        grid[int(pts[1])][int(pts[0])] = [0, 255, 0]
        cv2.imshow('Path', np.flip(grid, 0))
        cv2.waitKey(1)
    cv2.waitKey()
    graph_end_time = time.time()
    print('Time taken to animate paths: ' + str(graph_end_time - end_time))
if __name__ == '__main__':
    main()
