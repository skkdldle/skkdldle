# About
These control systems use the Python-based iRobot® Create® 3 SDK module, which enables programming the robot to collect input from its buttons, bumper, and IR sensors in order to produce sounds, lighting effects, and navigate its environment.

# Installing Pip and IRobot SDKs
### Mac/Linux  
Open the Terminal application and enter the following commands line by line:  
```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3 get-pip.py
rm get-pip.py
pip3 install requests
```
If the last command above doesn't work, you can also try 
```
pip install requests
```
### Windows  
Open the Command Prompt application and enter the following commands line by line:  
```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
del get-pip.py
pip install requests
```
### IRobot SDKs
Refer to the [irobot-edu-python-sdk](https://github.com/iRobotEducation/irobot-edu-python-sdk) repo for information on installation and Bluetooth functionality.

# Control Systems
iRobot Maze Solver  
iRobot Delivery  
iRobot Collision Handling  
iRobot Button Input & Audio Output
