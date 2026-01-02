# About
This is a system that allows users to input a predefined code sequence via touch buttons and bumpers on the robot called 'CodeBreaker.py'  

1. Connect to the robot using Bluetooth via its identifier.  
   - _Note: The script may already be set to a specific identifier. Change this name to connect to another robot._
2. Event-driven mechanisms:
   - (●) button press: appends "1" to the passcode, and plays the note C5.
   - (●●) touch press: appends "2" to the user passcode, and plays the note D5.
   - Left bumper press: appends "3" to the user passcode, and plays the note E5.
   - Right bumper press: appends "4" to the user passcode, and plays the note F5.
  
For example, if the code is "31424" the user should press the left bumper, followed by the (●) button, the right
bumper, the (●●) button, and finally the right bumper again for the passcode to unlock the robot.  

If the user's input via the buttons and sensors matches the predefined code, your robot plays a celebratory tune and dances around in celebration, changing the lighting patterns to indicate the robot is unlocked.  
  
If the user's input length matches the predefined passcode's length, but the sequences don't match, then a “sad” tune plays and the lighting changes, indicating that the user did not get the passcode right.
