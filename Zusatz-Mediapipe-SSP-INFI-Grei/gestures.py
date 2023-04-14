from xml.etree.ElementTree import PI


WRIST = 0 # https://google.github.io/mediapipe/solutions/hands.html
THUMB_CMC = 1 # link oben beschreibt was wo ist
THUMB_MCP = 2
THUMB_IP = 3
THUMB_TIP = 4
INDEX_FINGER_MCP = 5
INDEX_FINGER_PIP = 6
INDEX_FINGER_DIP = 7
INDEX_FINGER_TIP = 8
MIDDLE_FINGER_MCP = 9
MIDDLE_FINGER_PIP = 10
MIDDLE_FINGER_DIP = 11
MIDDLE_FINGER_TIP = 12
RING_FINGER_MCP = 13
RING_FINGER_PIP = 14
RING_FINGER_DIP = 15
RING_FINGER_TIP = 16
PINKY_MCP = 17
PINKY_PIP = 18
PINKY_DIP = 19
PINKY_TIP = 20

# Anleitung wie die Gesten ausschauen müssen, um erkannt zu werden, finden Sie im Ordner Symbolbilder_Anleitung

#Papier
def papier(points):
    return points[MIDDLE_FINGER_TIP].y < points[WRIST].y and points[MIDDLE_FINGER_PIP].y < points[RING_FINGER_DIP].y

#Stein
def stein(points):
    return points[MIDDLE_FINGER_TIP].y > points[MIDDLE_FINGER_MCP].y and points[PINKY_MCP].y < points[PINKY_TIP].y and \
    points[RING_FINGER_MCP].y < points[RING_FINGER_TIP].y

#Schere
def schere(points): 
    return points[RING_FINGER_TIP].y < points[RING_FINGER_MCP].y and points[PINKY_TIP].y < points[PINKY_MCP].y