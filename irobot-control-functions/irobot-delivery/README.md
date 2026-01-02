# About
'AutonomousDelivery.py' enables a robot to simulate an autonomous delivery while avoiding obstacles. 

## Auxiliary Functions
1. getMinProxApproachAngle()
    - Determines the minimum proximity and corresponding approach angle to an obstacle based on sensor readings.
2. getCorrectionAngle()
    - Calculates the angle required for the robot to orient itself with the vertical axis by rotating to the right.
3. getAngleToDestination()
    - Calculates the angle required for the robot to face the destination assuming it is currently oriented along the vertical axis, i.e. it has a heading of 90 degrees.
4. checkPositionArrived()
    - Checks if the robot has reached the destination by calculating the distance between the current position and the destination and checking whether that is below the input threshold.

## Navigation Functions
1. realignRobot()
    - Adjusts the robot's orientation to ensure it is accurately directed towards its destination. Once the alignment is complete, the robot is ready to proceed towards the destination.
2. moveTowardGoal()
    - Directs the robot towards its target destination. Assumes that the robot is initially oriented to face the destination, requiring it to move forward. If the robot detects an obstacle within a predefined proximity of 20.0, it stops advancing and reorients the robot to have its central axis parallel to the obstacle. Once realigned, the robot switches modes, invoking the logic outlined in the followObstacle() function to navigate around the obstruction.
3. followObstacle(robot)
    - Navigates around an obstacle without colliding with it. If the proximity reading from this sensor falls
below 20.0 units, the robot pivots slightly (by 3 degrees) away from the obstacle to create a safer clearance before proceeding forward. When the proximity calculated based on the IR measurement of SENSOR2CHECK becomes larger than 100.00, the robot has successfully navigated past the obstacle. The function switches to the realignRobot() mode to reorient the robot towards its destination. 
4. makeDelivery(robot)
    - Operating within a loop, the function continuously checks for collision and performs the following key actions:
        - Arrival check: Evaluates whether the robot has reached its destination and takes appropriate actions if the destination is reached.
        - Realignment: the robot undergoes realignment when necessary to ensure it's on the correct path to the destination.
        - Moving towards goal: The robot advances towards the destination, accounting for any obstacles encountered.
        - Obstacle navigation: Upon detecting obstacles, the robot follows a procedure to bypass them and continue its path.  
  
When the robot reaches its destination, it stops and all modes are ceased. It turns on a spinning green light to show that it has reached the destination.

