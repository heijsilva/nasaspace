import socket
import pyautogui
from datetime import datetime
from pyautogui import position
from pyautogui import size

from os import system
from time import sleep

from windows_directInput import PressKey, ReleaseKey, MouseMoveRelative, left_click, left_release, right_click, right_release

screenSize = size()

###################### CHANGE HERE #########################

## CHANGE HERE IF USING ALTERNATIVE SCREEN RESOLUTION IN DOLPHIN ##
HORIZONTAL_RESOLUTION = screenSize[0] #1920  <- 1080p hardcoded
VERTICAL_RESOLUTION = screenSize[1]   #1080  <- 1080p hardcoded

#############################################################

xCenter = HORIZONTAL_RESOLUTION/2
yCenter = VERTICAL_RESOLUTION/2




#Scan Codes
wKey = 0x11 #one
aKey = 0x1E #minus
sKey = 0x1F #two
dKey = 0x20 #plus
space = 0x39
zKey = 0x2C
xKey = 0x2D
cKey = 0x2E #shake
enterKey = 0x1C
upKey = 0x48 #d_up
downKey = 0x50 #d_down
leftKey = 0x4B #d_left
rightKey = 0x4D #d_right

jKey = 0x24 #left tilt
kKey = 0x25 #tilt modifier
lKey = 0x26 #right tilt

key = 0x0B # zero key placeholder

## Move Mouse ##
def mousey(xAxis, zAxis):
    #mouse movement
    if zAxis < -0:
        MouseMoveRelative(int(zAxis*20)*-1,0)   #change sensitivity
    elif zAxis > 0:
        MouseMoveRelative(int(zAxis*20)*-1,0)
        
    if xAxis < 0:
        MouseMoveRelative(0,int(xAxis*20)*-1)
    elif xAxis > 0:
        MouseMoveRelative(0,int(xAxis*20)*-1)

## Center Mouse ##
def recenter():
    global xCenter
    global yCenter
    
    pos = position()
    x = 0
    y = 0

    if pos[0] > xCenter:
        x = xCenter - pos[0]
    elif pos[0] < xCenter:
        x = xCenter - pos[0]

    if pos[1] < yCenter:
        y = yCenter - pos[1]
    elif pos[1] > yCenter:
        y = yCenter - pos[1]
    
    MouseMoveRelative( int(x) , int(y) )

## MAIN CODE ##
if __name__ == "__main__":
    
    #IPv4 UDP Socekt
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind( (socket.gethostname(), 1234) )

    print("\tServer Started!\n")

    ## Define runtime variables ##
    l = "not pressed"
    r = "not pressed"
    
    while True:
        message, address = s.recvfrom(1024)
        #print(address)
        #print(f"Connection from {address} has been established at {datetime.now()}!")
        
        messageList = message.decode("utf-8").split(",")

        #Message variables
        xAccel = float(messageList[0])
        yAccel = float(messageList[1])
        zAccel = float(messageList[2])
        reCenter = messageList[3]
        buttonA = messageList[4]
        buttonB = messageList[5]
        buttonPlus = messageList[6]
        buttonMinus = messageList[7]
        button1 = messageList[8] 
        button2 = messageList[9]
        buttonUp = messageList[10]
        buttonDown = messageList[11]
        buttonLeft = messageList[12]
        buttonRight = messageList[13]
        xGyro = float(messageList[14])
        yGyro = float(messageList[15])
        zGyro = float(messageList[16])


        # Toggle Orientation #
        if zAccel <= 4:
            PressKey(zKey) #toggles sideways remote
        else:
            ReleaseKey(zKey)

        #Move mouse
        mousey(xGyro, zGyro)

        # Mouse Click (A and B buttons) #
        if buttonA == "D" and l != "pressed":
            left_click()
            l = "pressed"

        elif buttonA != "D" and l == "pressed":
            left_release()
            l ="not pressed"

        if buttonB == "D" and r!= "pressed":
            right_click()
            r = "pressed"

        elif buttonB != "D" and r == "pressed":
            right_release()
            r ="not pressed"
    
        #recenter
        if reCenter == "-":
            recenter()
   
        #key press
        if buttonPlus == "D":
            PressKey(dKey)
        elif buttonPlus != "D":
            ReleaseKey(dKey)

        if buttonMinus == "D":
            PressKey(aKey)
        elif buttonPlus != "D":
            ReleaseKey(aKey)

        if button1 == "D":
            PressKey(wKey)
        elif button1 != "D":
            ReleaseKey(wKey)

        if button2 == "D":
            PressKey(sKey)
        elif button2 != "D":
            ReleaseKey(sKey)

        if buttonUp == "D":
            PressKey(upKey)
        elif buttonUp != "D":
            ReleaseKey(upKey)

        if buttonDown == "D":
            PressKey(downKey)
        elif buttonDown != "D":
            ReleaseKey(downKey)

        if buttonLeft == "D":
            PressKey(leftKey)
        elif buttonLeft != "D":
            ReleaseKey(leftKey)

        if buttonRight == "D":
            PressKey(rightKey)
        elif buttonRight != "D":
            ReleaseKey(rightKey)

        if zGyro > 8.5:
            PressKey(cKey)
        elif zGyro < 8.5:
            ReleaseKey(cKey)


        #accelerometer tilting (marioKart, etc)
        
        ReleaseKey(jKey)
        ReleaseKey(lKey)
        ReleaseKey(kKey)
        if yAccel > 2:
            PressKey(lKey)
        if yAccel < -2:
            PressKey(jKey)
        if (yAccel > 2 and yAccel <7) or (yAccel >-7 and yAccel <-2):
            PressKey(kKey)
    
