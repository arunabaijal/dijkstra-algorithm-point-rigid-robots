#*********************************** Point Robot ********************************#
import matplotlib.pyplot as plt

# Function to check if the given point lies outside the map or in the obstacle space
def check_node(node):
	global flag
	if node[0] > 200 or node[0]<0 or node[1] > 100 or node[1]<0:
		print('Sorry the point you entered is out of bounds! Try again.')
	elif node[0] >= 90 and node[0] <= 110 and node[1] >= 40 and node[1] <= 60:
		print('Sorry the point you entered is in the obstacle space! Try again.')
	elif (node[0]-160)**2 + (node[1]-50)**2 < 15**2:
		print('Sorry the point you entered is in the obstacle space! Try again.')
	else:
		flag = 1

#Taking start point and goal point from the user
flag = 0
while flag == 0:
	start_point = eval(input('Please enter the start point in this format - (x,y): '))
	check_node(start_point)
	
print('The start point you gave is:', start_point)
print('')

flag = 0
while flag == 0:
	goal_point = eval(input('Please enter the goal point in this format - (x,y): '))
	check_node(goal_point)
	
print('The goal point you gave is:', goal_point)


# Plotting the trial map
plt.axes()
circle = plt.Circle((160, 50), radius=15, fc='y')
square = plt.Rectangle((90, 40), 20, 20, fc='r')
line1 = plt.Line2D((0, 200), (100, 100), lw=2.5)
line2 = plt.Line2D((0, 200), (0, 0), lw=2.5)
line3 = plt.Line2D((0, 0), (0, 100), lw=2.5)
line4 = plt.Line2D((200, 200), (0, 100), lw=2.5)
plt.scatter(start_point[0], start_point[1])
plt.gca().add_line(line1)
plt.gca().add_line(line2)
plt.gca().add_line(line3)
plt.gca().add_line(line4)
plt.gca().add_patch(circle)
plt.gca().add_patch(square)
plt.axis('scaled')
plt.show()


