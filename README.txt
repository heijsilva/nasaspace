README

** This program is utilized to map android motion controls to the dolphin emulator.
 * Sensors from the app are mapped to mouse movement, mouse clicks, and keyboard presses,
   which are then mapped in dolphin to emulate Wiimote controls.
 *
**

-- CONTROLS --
1. Movement of phone: Gyroscopic data from phone moves mouse
2. Phone shake: c key
3. D-Pad: Presses numpad on keyboard (be sure to keep Num Lock toggled on or off during setup and gameplay)
4. A button: left mouse click
5. B button: right mouse click
6. + button: d key
7. - button: a key
8. 1 button: w key
9. 2 button: s key
10. ö button: moves mouse to center of screen (ideally pressed when phone is pointed at center of screen to recalibrate cursor)

-Sideways Controls-
11. Full Left tilt: j key
12. Full right tilt: l key
13. Half left tilt: j and k keys
14. Half right tilt: l and k keys
15. Switching to sideways orientation: z key (when pressed, this tells dolphin the wiimote is sideways)

-- SETUP --
1.Resolution
 - Make sure dolphin is running as close to your native desktop resolution as possible, as the recentering is based on your desktop resolution, not dolphin's resolution
 - Pressing the recenter key will not always bring the cursor to the exact center of the screen, so please get comfortable with where it brings it for now.

2. Controls:
 A. Using the mappings above, enter all the standard button controls for A,B,1,2,+,-, and the directional pad (rememeber to keep NumLock either on or off)
 B. Go to the 'Motion Simulation' tab
    - Right click on the "Up" key mapping. 
    - Scroll down to the bottom where "Cursor Y-" is. Highlight whatever is currently in the textbox below and delete it.
    - Select Cursor Y- and hit the "Select" button. 'Cursor Y-' should now appear in the textbox below. Click OK.
    - Do the same for the other controls: Down = Cursor Y+, Left = Cursor X-, and Right = Cursor X+
    - Make sure Relative Input is not checked
 C. Set the X mapping under the 'Shake' section to the c key.
 D. For tilt: 
    - Set Left = j, Right = l, and Modifier = k
 E. Under the 'General and Options' tab, set the Sideways Hold = z key.


-- HOW TO RUN --
1. Make sure Python 3.x is installed on your computer.
2. If you don't already have 'pip' installed, simply double click the file 'get-pip.py' or open command prompt, go to directory containing 'get-pip.py' and run 'python get-pip.py'
  - https://www.liquidweb.com/kb/install-pip-windows/
3. Make sure the library 'pyautogui' is installed. This can be done using 'pip install pyautogui' in the command prompt after you install pip.
4. Run the 'udpServer_wiimote.py' file in the command prompt by double clicking it. If you run into errors, run the command prompt with administrator priviledges and re-run the python file.
  - If successful, you will see 'Server Started' in the window.	
5. Open the app on your android device, enter the ip address of the computer (in command prompt run 'ipconfig' and enter ipv4 address, periods included).
6. click connect, the ip address entered should turn grey, and the mouse should respond to your phone's movement.

*Note: The port '1234' must be open on your computer. This will be true 99% of the time unless you have a specific application, such as this one, using it.
   