from pynput import keyboard
from pynput.mouse import Button, Controller

mouse = Controller()

mouseSpeed = 25

up = False
down = False
left = False
right = False
isActive = -1

print("WASD - to move")
print("e - left click")
print("f - right click")
print("q - quit")
print("Active: " + str(isActive))
def on_press(key):
    global up
    global down
    global left
    global right
    if(isActive == 1):
        try:
            if(key.char == 'w'):
                up = True
            elif(key.char == 's'):
                down = True
            elif(key.char == 'a'):
                left = True
            elif(key.char == 'd'):
                right = True
            elif(key.char == 'e'):
                mouse.press(Button.left)
                mouse.release(Button.left)
            elif(key.char == 'f'):
                mouse.press(Button.right)
                mouse.release(Button.right)

            if(up):
                mouse.move(0, -mouseSpeed)
            if(down):
                mouse.move(0, mouseSpeed)
            if(left):
                mouse.move(-mouseSpeed, 0)
            if(right):
                mouse.move(mouseSpeed, 0)

        except AttributeError:
            pass

def on_release(key):
    global up
    global down
    global left
    global right
    global isActive
    try:
        if(key.char == 'w'):
            up = False
        elif(key.char == 's'):
            down = False
        elif(key.char == 'a'):
            left = False
        elif(key.char == 'd'):
            right = False
        elif(key.char == '`'):
            isActive = isActive*-1
            print("Active: " + str(isActive))

        if key.char == 'q':
            # Stop listener
            return False
    except AttributeError:
        pass
# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

# ...or, in a non-blocking fashion:
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()
