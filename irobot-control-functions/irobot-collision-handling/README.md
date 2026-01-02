# About
'CollisionWarning.py' implements different behaviors depending on the robot's proximity to a wall. 
  
'RobotPong.py' simulates the mechanics of the Pong game, in which it moves in a straight line, and upon detecting a boundary using its infrared sensors, it bounces back at the reflected angle.

## CollisionWarning
1. Connect to the robot using Bluetooth via its identifier.  
   - _Note: The script may already be set to a specific identifier. Change this name to connect to another robot._
2. Fail-safe robot behaviors:
   - If either button is pressed, the robot stops and turns on a solid red light.
   - If either bumper is pressed, the robot stops and turns on a solid red light.
3. To calculate the proximity of the robot from the wall, the formula 𝑝𝑟𝑜𝑥𝑖𝑚𝑖𝑡𝑦 = 4095/(𝑖𝑟_𝑟𝑒𝑎𝑑𝑖𝑛𝑔 + 1) is used. If the proximity is...
   - 5.0 units or less: robot stops and sets its ring light to solid red. It plays a sharp, higher-pitch note (D7) for 1 second.
   - 30.0 units or less: robot slows to a maximum speed of 1 cm/s and sets its ring light to blink in orange. It beeps at a moderate pitch note (D6) for a duration of 0.1 seconds per beep.
   - 100.0 units or less: robot moves at a moderate speed of 4 cm/s and sets its ring light to blink
in yellow. It beeps a lower pitch note (D5) for a duration of 0.1 seconds per beep.
   - More than 100.0 units: Proceeds at a fast pace with a maximum speed of 8 cm/s and sets its
ring light to blink in green. No sound is produced in this range.

## RobotPong
1. Connect to the robot using Bluetooth via its identifier.  
   - _Note: The script may already be set to a specific identifier. Change this name to connect to another robot._
2. Fail-safe robot behaviors:
   - If either button is pressed, the robot stops and turns on a solid red light.
   - If either bumper is pressed, the robot stops and turns on a solid red light.
3. Functionality:
   - The ring light is set to the spinning mode in the color cyan.
   - The robot moves in a straight direction with a speed of 15 cm/s.
   - Continuously collecting all the infrared sensor readings, the proximity is calculated based on the same equation used for the 'CollisionWarning.py' system. Upon detecting a wall within 20.0 units of distance of any of the sensors, the robot...
      - Stops momentarily
      - Reflects off the wall based on the closest angle of approach.
      - Changes the light to magenta if it was previously cyan and vice versa.
4. This behavior continues until the collision flag is set to True due to a button press or bumper collision.

### getApproachAngle function  
Determines the closest angle of approach by finding the maximum sensor reading, which corresponds to the closest boundary. The closest approach angle corresponds to the IR sensor angle with the maximum sensor reading.

### Finding the reflection angle
If the closest angle of approach is on the right side, the robot rotates to the right by the reflection angle, which is calculated as: 𝑟𝑒𝑓𝑙𝑒𝑐𝑡𝑖𝑜𝑛𝐴𝑛𝑔𝑙𝑒 = 180 − 2 ∗ 𝑎𝑝𝑝𝑟𝑜𝑎𝑐ℎ𝐴𝑛𝑔𝑙𝑒  
  
If the closest angle of approach is on the left side, the robot should rotate to the left by the reflection angle, which is calculated as: 𝑟𝑒𝑓𝑙𝑒𝑐𝑡𝑖𝑜𝑛𝐴𝑛𝑔𝑙𝑒 = 180 + 2 ∗ 𝑎𝑝𝑝𝑟𝑜𝑎𝑐ℎ𝐴𝑛𝑔𝑙e


