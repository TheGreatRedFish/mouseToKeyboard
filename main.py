import pyautogui
import keyboard


pyautogui.FAILSAFE = False

isActive = True

mouseSpeedConst = 15
mouseSpeed = mouseSpeedConst
mouseAcceleration = 12

while True:
    #left
    if keyboard.is_pressed('a') and isActive:
        while(keyboard.is_pressed('a')):
            pyautogui.move(mouseSpeed * -1, 0)
            mouseSpeed += mouseAcceleration
        mouseSpeed = mouseSpeedConst
    #right
    elif keyboard.is_pressed('d') and isActive:
        while(keyboard.is_pressed('d')):
            pyautogui.move(mouseSpeed, 0)
            mouseSpeed += mouseAcceleration
        mouseSpeed = mouseSpeedConst
    #up
    elif keyboard.is_pressed('w') and isActive:
        while(keyboard.is_pressed('w')):
            pyautogui.move(0, mouseSpeed * -1)
            mouseSpeed += mouseAcceleration
        mouseSpeed = mouseSpeedConst
    #down
    elif keyboard.is_pressed('s') and isActive:
        while(keyboard.is_pressed('s')):
            pyautogui.move(0, mouseSpeed)
            mouseSpeed += mouseAcceleration
        mouseSpeed = mouseSpeedConst
    #left click
    elif keyboard.is_pressed('e') and isActive:
        pyautogui.click()
    elif keyboard.is_pressed('`'):
        isActive = True
    elif keyboard.is_pressed('\\'):
        isActive = False
