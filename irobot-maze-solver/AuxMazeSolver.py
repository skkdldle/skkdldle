from collections import deque

def createMazeDict(nXCells, nYCells, cellDim):
    mazeDict = {}
    for i in range(nXCells):
        for j in range(nYCells):
            mazeDict[(i,j)] = {"position": (i*cellDim, j*cellDim), "neighbors": [], "visited": False, "cost": 0}
    return mazeDict

nXCells, nYCells, cellDim = 2, 2, 10
mazeDict = createMazeDict(nXCells, nYCells, cellDim)
"""
print(mazeDict)
"""
def addAllNeighbors(mazeDict, nXCells, nYCells):

    for coordinate, info in mazeDict.items():

        (i,j) = coordinate

        if (i-1) >= 0 and (i-1) <= (nXCells - 1) and j >= 0 and j <= (nYCells - 1):

            info["neighbors"].append((i-1,j))

        if i >= 0 and i <= (nXCells - 1) and (j+1) >= 0 and (j+1) <= (nYCells - 1):

            info["neighbors"].append((i,j+1))

        if (i+1) >= 0 and (i+1) <= (nXCells - 1) and j >= 0 and j <= (nYCells - 1):

            info["neighbors"].append((i+1,j))

        if i >= 0 and i <= (nXCells - 1) and (j-1) >= 0 and (j-1) <= (nYCells - 1):

            info["neighbors"].append((i,j-1))

    return mazeDict

"""         
mazeDict = createMazeDict(nXCells, nYCells, cellDim)
mazeDict = addAllNeighbors(mazeDict, nXCells, nYCells)
"""


def getRobotOrientation(heading):
    baseHeading = heading % 360
    cardinalDirection = ""
    if baseHeading >= 315:
        cardinalDirection = "E"
    elif baseHeading >= 225:
        cardinalDirection = "S"
    elif baseHeading >= 135:
        cardinalDirection = "W"
    elif baseHeading >= 45:
        cardinalDirection= "N"
    else:
        cardinalDirection = "E"
    return cardinalDirection
""" 
print(getRobotOrientation(182))
print(getRobotOrientation(88.5))
"""

def getPotentialNeighbors(currentCell, orientation):
    tupList = []
    (i, j) = currentCell
    if orientation == "W":
        tupList.append((i, j-1)) #left
        tupList.append((i-1, j)) #down
        tupList.append((i, j+1)) #right
        tupList.append((i+1, j)) #up
    if orientation == "S":
        tupList.append((i+1, j)) #up
        tupList.append((i, j-1)) #left
        tupList.append((i-1, j)) #down
        tupList.append((i, j+1)) #right
    if orientation == "N":
        tupList.append((i-1, j)) #down
        tupList.append((i, j+1)) #right
        tupList.append((i+1, j)) #up
        tupList.append((i, j-1)) #left
    if orientation == "E":
        tupList.append((i, j+1)) #right
        tupList.append((i+1, j)) #up
        tupList.append((i, j-1)) #left
        tupList.append((i-1, j)) #down  
    return tupList

"""       
print(getPotentialNeighbors((0,0),"E"))
print(getPotentialNeighbors((2,3),"S"))
print(getPotentialNeighbors((4,5),"W"))
"""


def isValidCell(cellIndices, nXCells, nYCells):
    (i, j) = cellIndices
    if i == -1 or j == -1:
        return False
    if nXCells <= i:
        return False
    elif nYCells <= j:
        return False
    else:
        return True
"""
print(isValidCell((-1,0), 2, 2))
"""


def getWallConfiguration(IR0,IR3,IR6,threshold):
    validityList = []
    if IR0 > threshold:
        validityList.append(True)
    else:
        validityList.append(False)
        
    if IR3 > threshold:
        validityList.append(True)
    else:
        validityList.append(False)

    if IR6 > threshold:
        validityList.append(True)
    else:
        validityList.append(False)
    return validityList
"""
print(getWallConfiguration(300, 200, 39, 100))
print(getWallConfiguration(23, 800, 10, 100))
"""

def getNavigableNeighbors(wallsAroundCell, potentialNeighbors, prevCell, nXCells, nYCells):

    x,y = prevCell
    navNeighbors = []
    navNeighbors.append(prevCell)
    for i,j in potentialNeighbors:
        if wallsAroundCell[0] == False:
            if j > y:
                navNeighbors.append((i,j))
        if wallsAroundCell[1] == False:
            if i > x+1:
                navNeighbors.append((i,j))
        if wallsAroundCell[2] == False:
            if j < y:
                navNeighbors.append((i,j))         
    return navNeighbors
"""       
print(getNavigableNeighbors([True, True, False], [(1,2),(2,1),(1,0),(0,1)], (0,1), 2, 2))
"""

def updateMazeNeighbors(mazeDict, currentCell, navNeighbors):
    for (i,j) in mazeDict[currentCell]["neighbors"]:
        if (i,j) not in navNeighbors:
            mazeDict[currentCell]["neighbors"].remove((i,j))
    mazeDict[currentCell]["neighbors"] = navNeighbors

    return mazeDict


def getNextCell(mazeDict, currentCell):
    minCost = 100000
    minCell = ()
    visited = []
    for (i,j) in mazeDict[currentCell]["neighbors"]:
        if mazeDict[(i,j)]["visited"] == False:
            visited.append((i,j))
            if mazeDict[(i,j)]["cost"] < minCost:
                minCost = mazeDict[(i,j)]["cost"]
                minCell = (i,j)
    if visited == []:
        if mazeDict[(i,j)]["cost"] < minCost:
                minCost = mazeDict[(i,j)]["cost"]
                minCell = (i,j)
            
    return minCell
"""
mazeDict = {(0, 0): {'position': (0, 0),'neighbors': [(0, 1)], 'visited': True, 'cost': 0},
            (0, 1): {'position': (0, 1),'neighbors': [(0, 0), (1, 1)], 'visited': True, 'cost': 1},
            (1, 0): {'position': (1, 0), 'neighbors': [(1, 1)], 'visited': False, 'cost': 3},
            (1, 1): {'position': (1, 1), 'neighbors': [(1, 0), (0, 1)], 'visited': False, 'cost': 2}}
currentCell = (0,1)
print(getNextCell(mazeDict, currentCell))

mazeDict = {(0, 0): {'position': (0, 0),'neighbors': [(0, 1)], 'visited': True, 'cost': 0},
            (0, 1): {'position': (0, 1),'neighbors': [(0, 0), (1, 1)], 'visited': False, 'cost': 1},
            (1, 0): {'position': (1, 0), 'neighbors': [(1, 1)], 'visited': False, 'cost': 3},
            (1, 1): {'position': (1, 1), 'neighbors': [(1, 0), (0, 1)], 'visited': True, 'cost': 2}}
currentCell = (1,1)
print(getNextCell(mazeDict, currentCell))
"""


def checkCellArrived(currentCell, destination):
    i, j = currentCell
    x, y = destination
    if i == x and j == y:
        return True
    else:
        return False
"""
print(checkCellArrived((4,3), (4,3)))
print(checkCellArrived((6,7), (7,6)))
"""



"""
The following implementation of the Flood Fill algorithm is
tailored for maze navigation. It updates the movement cost for
each maze cell as the robot learns about its environment. As
the robot moves and discovers navigable adjacent cells, it
gains new information, leading to frequent updates in the
maze's data structure. This structure tracks the layout and
traversal costs. With each step and discovery, the algorithm
recalculates the cost to reach the destination, adapting to
newly uncovered paths. This iterative process of moving,
observing, and recalculating continues until the robot reaches
its destination, ensuring an optimal path based on the robot's
current knowledge of the maze.
"""
def updateMazeCost(mazeDict, start, goal):
    for (i,j) in mazeDict.keys():
        mazeDict[(i,j)]["flooded"] = False
    queue = deque([goal])
    mazeDict[goal]['cost'] = 0
    mazeDict[goal]['flooded'] = True
    while queue:
        current = queue.popleft()
        current_cost = mazeDict[current]['cost']
        for neighbor in mazeDict[current]['neighbors']:
            if not mazeDict[neighbor]['flooded']:
                mazeDict[neighbor]['flooded'] = True
                mazeDict[neighbor]['cost'] = current_cost + 1
                queue.append(neighbor)
    return mazeDict

"""
This function prints the information from the dictionary as
a grid and can help you troubleshoot your implementation.
"""
def printMazeGrid(mazeDict, nXCells, nYCells, attribute):
    for y in range(nYCells - 1, -1, -1):
        row = '| '
        for x in range(nXCells):
            cell_value = mazeDict[(x, y)][attribute]
            row += '{} | '.format(cell_value)
        print(row[:-1])
