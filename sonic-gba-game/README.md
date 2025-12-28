# Building and running the code
Ensure you have the [mGBA Emmulator](https://mgba.io/downloads.html) downloaded.  
  
Open [Docker Desktop](https://www.docker.com/products/docker-desktop/).  
  
Open a docker terminal and cd to the folder containing the gba files. Run the following script based on your OS:  
  
**macOS and Linux**  
$ ./cs2110docker-gba.sh  
  
**Windows**  
$ cs2110docker-gba  
  
To build your code and run the emulator, run:  
$ make mgba

# How to play
This game is inspired by the scene in Sonic 3 where Robotnik dances through lasers. You are playing as Robotnik. You are surrounded by red lasers and will lose if you touch them. To win, bring Robotnik to the Master Emerald at the bottom right of the screen.    
  
Press Start/Enter to play.  
  
Use arrow keys to move Robotnik around.  

	Right = Right Arrow  
	Left = Left Arrow  
	Up = Up Arrow  
	Down = Down Arrow  

Pressing Select/Backspace at any point during the game will restart the game to the title screen.

If you win or lose, pressing Select/Backspace will restart the game to the title screen.

To avoid tearing, if you touch the borders of the timer, Robotnik's position will reset to the beginning.
