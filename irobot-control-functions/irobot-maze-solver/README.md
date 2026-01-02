# About
'MazeSolver.py' implements different behaviors that enable a robot to explore and exit out of a maze. The robot does not require previous knowledge of the maze, and will identify maze walls until it reaches the cell corresponding to the exit. Note that these walls must be white or a similar color so that the detection sensors operate well.

## Auxiliary Functions
1. createMazeDict()
    - Constructs a dictionary representing a maze grid. Each entry has a tuple of (i, j) as the key, where i and j are the cell's x and y coordinates in the grid. The value associated with each key is another dictionary containing the cell's actual position
in space (position), a list of neighboring cells (neighbors), and another boolean flag to track if the cell has
been visited (visited), a cost that can be used to indicate the distance to the destination (cost).
2. addAllNeighbors()
    - Populates the 'neighbors' field for each cell in a maze grid within the provided mazeDict.
3. getRobotOrientation()
    - Converts a robot's heading, given in degrees, into the nearest cardinal direction ("N", "W", "S", or "E").
4. getPotentialNeighbors()
    - Calculates the indices of the potential neighboring cells relative to a given cell in a grid, based on the robot's current orientation.
5. isValidCell()
    - Determines whether a given cell, identified by its coordinates (cellIndices), falls within the bounds of a specified grid.
6. getWallConfiguration()
    - Assesses the presence of walls around the robot using infrared (IR) sensor readings. Processes each IR sensor reading using the proximity formula 4095/(IRx+1), where IRx is the reading from one of the IR sensors and compares the result to the threshold. If the calculated value is less than or equal to the threshold, it infers the presence of a wall in that direction.
7. getNavigableNeighbors()
    - Determines the accessible neighboring cells of a given cell within a grid, taking into account the presence of walls, the grid's dimensions, and the previously visited cell.
8. updateMazeNeighbors()
    - Updates the neighbor information concerning a specific cell within a maze.
9. getNextMove()
    - Determines the next best move (or cell to navigate to) from the current cell in a maze, based on a cost metric and visitation status.
10. checkCellArrived()
    - Assesses whether a given cell, represented by currentCell, matches the destination cell in a grid-based environment.

## Navigation Functions
1. navigateToNextCell()
    - Orchestrates the movement of a robot toward the next specified cell (nextCell) in a grid based on the robot's current orientation (orientation). Begins by defining the possible offsets for each orientation (North, South, West, East), determining the relative position of the left, front, right, and back cells from the robot's perspective. Identifies which direction the robot needs to move to reach nextCell from its current position (CURR_CELL). After the turn, the robot moves forward by the distance of one cell dimension(CELL_DIM). Finally, the function updates the MAZE_DICT to mark CURR_CELL as visited and updates
PREV_CELL and CURR_CELL to reflect the robot's new position.
2. navigateMaze()
    - Guides a robot through a maze to a designated destination. Within a loop, it performs several key actions:
        - Sensor information retrieval: Gets the robot's current position and IR proximity sensor readings.
        - Destination check: Determines whether the robot has arrived at the destination.
        - Orientation and neighbors: Orientation is calculated, and potential navigable neighbors are identified based on the maze layout and the presence of walls.
        - Maze dictionary update: The maze's data dictionary (MAZE_DICT) is updated with the current navigable neighbors and costs associated with each move.
        - Navigation decision: Calculates the next best move and navigates the robot to the next cell.  
  
This process is repeated until the robot either reaches the destination or encounters a collision. When the robot reaches the exit from the maze, it stops and turns on a spinning green light.

