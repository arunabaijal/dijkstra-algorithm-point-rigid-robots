#*********************************** Point Robot ********************************#
import matplotlib.pyplot as plt

#Taking start point and goal point from the user
start_point = input('Please enter the start point in this format - (x,y): ')
print('The start point you gave is:', start_point)
print('')
goal_point = input('Please enter the goal point in this format - (x,y): ')
print('The goal point you gave is:', goal_point)

# Plotting the trail map
plt.axes()
circle = plt.Circle((160, 50), radius=15, fc='y')
square = plt.Rectangle((90, 40), 20, 20, fc='r')
line1 = plt.Line2D((0, 200), (100, 100), lw=2.5)
line2 = plt.Line2D((0, 200), (0, 0), lw=2.5)
line3 = plt.Line2D((0, 0), (0, 100), lw=2.5)
line4 = plt.Line2D((200, 200), (0, 100), lw=2.5)
plt.gca().add_line(line1)
plt.gca().add_line(line2)
plt.gca().add_line(line3)
plt.gca().add_line(line4)
plt.gca().add_patch(circle)
plt.gca().add_patch(square)
plt.axis('scaled')
plt.show()


