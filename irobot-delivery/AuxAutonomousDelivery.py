import math as m

def getCorrectionAngle(heading):
    correctionAngle= int(heading-90)
    return correctionAngle
"""
print(getCorrectionAngle(135.6))
print(getCorrectionAngle(25))
"""

def getAngleToDestination(current_position,destination):
    arc= m.atan2(destination[0]-current_position[0],destination[1]-current_position[1])
    return int(m.degrees(arc))
"""
currentPosition = (1, 1)
destination = (5, 3)
print(getAngleToDestination(currentPosition, destination))

currentPosition = (5, 5)
destination = (1, 1)
print(getAngleToDestination(currentPosition, destination))
"""
def getMinProxApproachAngle(readings, angles):
    proxs= []
    for reading in readings:
        prox= 4095/(reading+1)
        proxs.append(prox)
    minProx= min(proxs)
    mProxindex= proxs.index(minProx)
    return (minProx, angles[mProxindex])

"""
IR_ANGLES = [-65.3, -38.0, -20.0, -3.0, 14.25, 34.0, 65.3]
readings = [731, 237, 202, 229, 86, 120, 70]
print(getMinProxApproachAngle(readings, IR_ANGLES))

IR_ANGLES = [-65.3, -38.0, -20.0, -3.0, 14.25, 34.0, 65.3]
readings = [4, 347, 440, 408, 205, 53, 27]
print(getMinProxApproachAngle(readings, IR_ANGLES))
"""

def checkPositionArrived(current_position, destination, threshold):
    distance= dist = m.sqrt((destination[0] - current_position[0])**2 + (destination[1] - current_position[1])**2)
    return distance <= threshold

"""
print(checkPositionArrived((97, 99), (100, 100), 5.0))
print(checkPositionArrived((50, 50), (45, 55), 5))
print(checkPositionArrived((72, 84), (72, 89), 5))
"""
