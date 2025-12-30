from irobot_edu_sdk.backend.bluetooth import Bluetooth
from irobot_edu_sdk.robots import event, hand_over, Color, Robot, Root, Create3
from irobot_edu_sdk.music import Note

import math as m

# robot is the instance of the robot that will allow us to call
# its methods and to define events with the @event decorator.
robot = Create3(Bluetooth("XJ-9"))

color= "cyan"
# LEFT BUTTON
@event(robot.when_touched, [True, False])  # User buttons: [(.), (..)]
async def when_left_button_touched(robot):
    global collision
    collision= True
    while collision == True:
        await robot.set_wheel_speeds(0, 0)
        await robot.set_lights_rgb(255,0,0)


# RIGHT BUTTON
@event(robot.when_touched, [False, True])  # User buttons: [(.), (..)]
async def when_right_button_touched(robot):
    global collision
    collision= True
    while collision == True:
        await robot.set_wheel_speeds(0, 0)
        await robot.set_lights_rgb(255,0,0)


# EITHER BUMPER
@event(robot.when_bumped, [True, True])  # [left, right]
async def when_either_bumped(robot):
    global collision
    collision= True
    while collision == True:
        await robot.set_wheel_speeds(0, 0)
        await robot.set_lights_rgb(255,0,0)


@event(robot.when_play)
async def robotPong(robot):
    await robot.set_lights(Robot.LIGHT_SPIN,Color(0,100,100))
    await robot.set_wheel_speeds(15, 15)
    global collision, PROX, color
    collision= False
    while collision == False:
        angles = [-65.3, -38.0, -20.0, -3.0, 14.25, 34.0, 65.3]
        readings = (await robot.get_ir_proximity()).sensors
        for i in range(len(readings)):
            reading= readings[i]
            PROX= 4095/(reading +1)
            if PROX <= 20.0:
                if color == "cyan":
                    await robot.set_lights(Robot.LIGHT_SPIN, Color(255, 0, 255))
                    await robot.set_wheel_speeds(0, 0)
                    color= "magenta"
                elif color == "magenta":
                    await robot.set_lights(Robot.LIGHT_SPIN,Color(0,100,100))
                    await robot.set_wheel_speeds(0, 0)
                    color= "cyan"
                approachAngle= getApproachAngle(readings, angles)
                rightSide= angles[4:8]
                if approachAngle in rightSide:
                    reflectAngle= 180- (2*approachAngle)
                    await robot.turn_right(reflectAngle)
                    await robot.set_wheel_speeds(15, 15)
                else:
                    reflectAngle= 180+ (2*approachAngle)
                    await robot.turn_left(reflectAngle)
                    await robot.set_wheel_speeds(15, 15)
            

def getApproachAngle(readings, angles):
    maxReading= max(readings)
    for i in range(len(readings)):
        if readings[i]== maxReading:
            approachAngle= angles[i]
    return approachAngle
    
# ask for desired
robot.play()
