from irobot_edu_sdk.backend.bluetooth import Bluetooth
from irobot_edu_sdk.robots import event, hand_over, Color, Robot, Root, Create3
from irobot_edu_sdk.music import Note

# robot is the instance of the robot that will allow us to call
# its methods and to define events with the @event decorator.
robot = Create3(Bluetooth("SOPHIA"))

CORRECT_CODE = "341124"
USER_CODE= ""

# LEFT BUTTON
@event(robot.when_touched, [True, False])  # User buttons: [(.), (..)]
async def when_left_button_touched(robot):
    global USER_CODE
    USER_CODE += "1"
    await robot.play_note(Note.C5, 0.5)
    await checkUserCode(robot)


# RIGHT BUTTON
@event(robot.when_touched, [False, True])  # User buttons: [(.), (..)]
async def when_right_button_touched(robot):
    global USER_CODE
    USER_CODE += "2"
    await robot.play_note(Note.D5, 0.5)
    await checkUserCode(robot)


# LEFT BUMP
@event(robot.when_bumped, [True, False])  # [left, right]
async def when_left_bumped(robot):
    global USER_CODE
    USER_CODE += "3"
    await robot.play_note(Note.E5, 0.5)
    await checkUserCode(robot)

# RIGHT BUMP
@event(robot.when_bumped, [False, True]) # [left, right]
async def when_right_bumped(robot):
    global USER_CODE
    USER_CODE += "4"
    await robot.play_note(Note.F5, 0.5)
    await checkUserCode(robot)

async def checkUserCode(robot):
    global USER_CODE, CORRECT_CODE
    if len(USER_CODE) == len(CORRECT_CODE):
        if USER_CODE == CORRECT_CODE:
            await robot.set_wheel_speeds(20, -20)
            await robot.set_lights_rgb(100, 50, 250)
            await robot.play_note(293, 0.3)
            await robot.play_note(329, 0.3)
            await robot.play_note(392, 0.3)
            await robot.play_note(329, 0.3)
            await robot.play_note(246, 0.5)
            await robot.play_note(123, 0.4)
            await robot.play_note(110, 0.4)
            await robot.play_note(293, 0.3)
            await robot.play_note(329, 0.3)
            await robot.play_note(392, 0.3)
            await robot.play_note(329, 0.3)
            await robot.play_note(220, 0.5)
            await robot.play_note(220, 0.4)
            await robot.play_note(196, 0.3)
            await robot.play_note(392, 0.3)
            await robot.play_note(784, 0.3)
        else:
            USER_CODE= ""
            await robot.set_lights_rgb(255, 0, 0)
            await robot.play_note(78, 0.5)
            await robot.play_note(90, 0.5)
            await robot.play_note(110, 0.5)
        


@event(robot.when_play)
async def play(robot):
    pass
    


robot.play()
