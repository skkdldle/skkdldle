from irobot_edu_sdk.backend.bluetooth import Bluetooth
from irobot_edu_sdk.robots import event, hand_over, Color, Robot, Root, Create3
from irobot_edu_sdk.music import Note

# robot is the instance of the robot that will allow us to call
# its methods and to define events with the @event decorator.
robot = Create3(Bluetooth("SOPHIA")) 

# LEFT BUTTON
@event(robot.when_touched, [True, False])  # User buttons: [(.), (..)]
async def when_left_button_touched(robot):
    global button_pressed
    button_pressed= True
    await robot.set_wheel_speeds(0, 0)
    await robot.set_lights_rgb(255,0,0)


# RIGHT BUTTON
@event(robot.when_touched, [False, True])  # User buttons: [(.), (..)]
async def when_right_button_touched(robot):
    global button_pressed
    button_pressed= True
    while button_pressed== True:
        await robot.set_wheel_speeds(0, 0)
        await robot.set_lights_rgb(255,0,0)

# EITHER BUMPER
@event(robot.when_bumped, [True, True])  # [left, right]
async def when_either_bumped(robot):
    global bumper_pressed
    bumper_pressed= True
    while bumper_pressed== True:
        await robot.set_wheel_speeds(0, 0)
        await robot.set_lights_rgb(255,0,0)

@event(robot.when_play)
async def avoidCollision(robot):
    await robot.set_wheel_speeds(8, 8)
    global button_pressed
    button_pressed= False
    bumper_pressed= False
    while button_pressed == False and bumper_pressed== False:
        readings = (await robot.get_ir_proximity()).sensors
        centerIR= readings[3]
        global PROX
        PROX= 4095/(centerIR +1)
        if PROX <= 5.0:
            await robot.set_wheel_speeds(0, 0)
            await robot.set_lights_rgb(255,0,0)
            await robot.play_note(Note.D7, 1)
            break
        elif PROX <= 30.0:
            await robot.set_wheel_speeds(1, 1)
            await robot.set_lights(Robot.LIGHT_BLINK,Color(255, 80, 0))
            await robot.play_note(Note.D6, 0.1)
        elif PROX <= 100.0:
            await robot.set_wheel_speeds(4, 4)
            await robot.set_lights(Robot.LIGHT_BLINK,Color(255,215,0))
            await robot.play_note(Note.D5, 0.1)
        elif PROX > 100.0:
            await robot.set_lights(Robot.LIGHT_BLINK,Color(0,255,0))


# start the robot
robot.play()
