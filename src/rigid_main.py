# *********************************** Point Robot ********************************#
import matplotlib.pyplot as plt
import numpy as np
import queue
import math
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
# Function to generate new points
def new_points(point, clearance, direction):
    if direction == 0:
        point[1] = point[1] - np.sqrt(2)*clearance
    elif direction == 1:
        point[0] = point[0] + np.sqrt(2)*clearance
    elif direction == 2:
        point[1] = point[1] + np.sqrt(2)*clearance
    else:
        point[0] = point[0] - np.sqrt(2)*clearance
    return point
    
# Function to generate new points for the concave polygon
def new_points_pol(point, point0, point1, point3, clearance, direction):
    if direction == 0:
        slope1 = (point1[1] - point[1]) / (point1[0] - point[0])
        a1 = (90 - math.degrees(math.atan(slope1)))/2
        l1 = clearance/math.sin(math.radians(a1))
        x1 = l1*math.sin(math.radians(a1))
        y1 = l1*math.cos(math.radians(a1))       
        point[0] = point[0] - x1 
        point[1] = point[1] - y1 
        #point[1] = point[1] - np.sqrt(2)*clearance
    elif direction == 1:
        point[1] = point[1] - np.sqrt(2)*clearance
    elif direction == 2:
        #slope3 = (point1[1] - point[1]) / (point1[0] - point[0])
        #a3 = 90 - (180 - math.degrees(math.atan(slope3)))
        #l3 = clearance/math.sin(math.radians(a3))
        #x3 = l3*math.sin(math.radians(a3))
        #y3 = l3*math.cos(math.radians(a3))       
        #point[0] = point[0] + x3 
        #point[1] = point[1] - y3
        point[1] = point[1] - np.sqrt(2)*clearance 
    elif direction == 3:
        point[0] = point[0] + np.sqrt(2)*clearance
    elif direction == 4:
        slope4 = (point[1] - point1[1]) / (point[0] - point1[0])
        a4 = math.degrees(math.atan(slope4))
        l4 = clearance/math.sin(math.radians(a4))
        x4 = l4*math.cos(math.radians(a4))
        y4 = l4*math.sin(math.radians(a4))       
        point[0] = point[0] + x4 
        point[1] = point[1] + y4 
    else:
        slope5 = (point[1] - point1[1]) / (point[0] - point1[0])
        a5 = 180 - math.degrees(math.atan(slope5))
        l5 = clearance/math.sin(math.radians(a5))
        x5 = l5*math.cos(math.radians(a5))
        y5 = l5*math.sin(math.radians(a5))       
        point[0] = point[0] - x5 
        point[1] = point[1] + y5 
    return point
# Function to generate new equation of line acc. to new points

def eqn(point1, point2):
    a = point1[1] - point2[1]
    b = point2[0] - point1[0]
    c = point1[1]*b - point1[0]*(-a)
    return a,b,c

# Function to check if the given point lies outside the final map or in the obstacle space
def check_node(node):
    u = 150.  # x-position of the center
    v = 100.  # y-position of the center
    a = 40.  # radius on the x-axis
    b = 20.  # radius on the y-axis
    
    clear_val = 5

    # New points for diamond obstacle
    p1 = new_points([225,15], clear_val, 0)
    p2 = new_points([250,30], clear_val, 1)
    p3 = new_points([225,45], clear_val, 2)
    p4 = new_points([200,30], clear_val, 3)
    
    
    # New lines for diamond obstacle
    
    a1,b1,c1 = eqn(p1,p2)
    a2,b2,c2 = eqn(p2,p3)
    a3,b3,c3 = eqn(p3,p4)
    a4,b4,c4 = eqn(p4,p1)   
    
    # New points for tilted cuboid
    p5 = new_points([95,30], clear_val, 0)
    p6 = new_points([100,38.66], clear_val, 1)
    p7 = new_points([35.05,76.16], clear_val, 2)
    p8 = new_points([30.05,67.5], clear_val, 3)
    
    
    # New lines for tilted cuboid
    
    a5,b5,c5 = eqn(p5,p6)
    a6,b6,c6 = eqn(p6,p7)
    a7,b7,c7 = eqn(p7,p8)
    a8,b8,c8 = eqn(p8,p5)
    
    # New points for concave polygon
    p9 = new_points_pol([20,120], [20,120], [50,150], [100,150],clear_val, 0)
    p10 = new_points_pol([50,150], [20,120], [50,150], [100,150],clear_val, 1)
    p11 = new_points_pol([75,120],[20,120], [50,150], [100,150],clear_val, 2)
    p12 = new_points_pol([100,150], [20,120], [50,150], [100,150],clear_val, 3)
    p13 = new_points_pol([75,185], [20,120], [50,150], [100,150],clear_val,4)
    p14 = new_points_pol([25,185], [20,120], [50,150], [100,150],clear_val, 5)
    
    
    # New lines for concave polygon

    a9,b9,c9 = eqn(p9,p10)
    a10,b10,c10 = eqn(p10,p11)
    a11,b11,c11 = eqn(p11,p12)
    a12,b12,c12 = eqn(p12,p13)
    a13,b13,c13 = eqn(p13,p14)
    a14,b14,c14 = eqn(p14,p9)  
    a15,b15,c15 = eqn(p14,p11)
    
    if node[0] >= 300 or node[0] < 0 or node[1]>= 200 or node[1]< 0:
        print('Sorry the point is out of bounds! Try again.')
        return False
    elif (node[0] - 225) ** 2 + (node[1] - 150) ** 2 < (25+clear_val) ** 2 :
        print('Sorry the point is in the obstacle space! Try again.1')
        return False
    elif ((node[0] - 150) ** 2) / (a+clear_val) ** 2 + ((node[1] - 100) ** 2) / (b+clear_val) ** 2 < 1:
        print('Sorry the point is in the obstacle space! Try again.2')
        return False
    elif (a1*node[0] + b1*node[1]>c1) and (a2*node[0] + b2*node[1]>c2) and (
            a3*node[0] + b3*node[1]>c3) and (a4*node[0] + b4*node[1]>c4):
        print('Sorry the point is in the obstacle space! Try again.3')
        return False
    elif (a5*node[0] + b5*node[1]>c5) and (a6*node[0] + b6*node[1]>c6) and (
            a7*node[0] + b7*node[1]>c7) and (a8*node[0] + b8*node[1]>c8):
        print('Sorry the point is in the obstacle space! Try again. hello')
        return False
    # Dividing concave shape into 2 convex shapes
    elif (a10*node[0] + b10*node[1]>c10) and (a11*node[0] + b11*node[1]>c11) and (a12*node[0] + b12*node[1]>c12) and (a13*node[0] + b13*node[1]<c13):
        print('Sorry the point is in the obstacle space! Try again.4')
        return False
    elif (a10*node[0] + b10*node[1]<c10) and (a14*node[0] + b14*node[1]>c14) and (a9*node[0] + b9*node[1]>c9):
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
    file = open('Nodes.txt', 'r')
    points = file.readlines()
    for point in points:
         pts = point.split(',')
         plt.scatter(int(pts[0]), int(pts[1]), c='b', s=6)
         # plt.pause(0.05)
    file = open('nodePath.txt', 'r')
    points = file.readlines()
    for point in points:
        pts = point.split(',')
        plt.scatter(int(pts[0]), int(pts[1]), c='g', s=5)
    plt.show()


if __name__ == '__main__':
    main()
