# Dijkstra algorithm for point and rigid robots
Dijkstra Algorithm for path planning along obstacles implemented on a Point and Rigid Robot.

## System and library requirements.
 - Python3
 - Numpy
 - Matplotlib
 
## How to Run
### Point Robot
Navigate to folder containing .py files. <br>
Run command `python3 Dijkstra_point.py` <br>
The program will ask for start point, provide input in [x,y] format. For eg: [5,5] <br>
Next program will ask for goal point, provide input in [x,y] format. For eg: [295,195] <br>
If the points provided are in the obstacle space or out of bounds, program will ask you to re-enter points.
<br>
The algorithm takes 5.0372 secs to run for [5,5] and [295,195]. The animation for each node discovered takes too long to run.<br>
To see final image of all explored points and optimal path chosen, comment line 391 (plt.pause(0.000000001)). This takes 20 mins to run.

### Rigid Robot
Navigate to folder containing .py files.<br>
Run command `python3 Dijkstra_rigid.py`<br>
The program will ask for robot radius. Input eg: 2<br>
The program will ask for clearance value. Input eg: 2<br>
The program will ask for start point, provide input in [x,y] format. For eg: [5,5]<br>
Next program will ask for goal point, provide input in [x,y] format. For eg: [295,195]<br>
If the points provided are in the obstacle space or out of bounds, program will ask you to re-enter points.
<br>
The algorithm takes 34.569 secs to run for [5,5] and [295,195]. The animation for each node discovered takes too long to run.<br>
To see final image of all explored points and optimal path chosen, comment line 471 (plt.pause(0.000000001)). This takes 20 mins to run.
