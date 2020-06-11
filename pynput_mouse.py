import time
from pynput.mouse import Button, Controller

mouse = Controller()
long_delay = 30
middle_delay = 10
short_delay = 5
positions = [
        {'x': 100, 'y': 255},
        {'x': 100, 'y': 285},
        {'x': 100, 'y': 315}
    ]

time.sleep(short_delay)

while True:
    print ('Current position: ' + str(mouse.position))
    
    for point in positions:
        # Set cursor position
        mouse.position = (point['x'], point['y'])
        # Click the left button
        mouse.click(Button.left, 1)
        time.sleep(short_delay)

    # Move cursor position
    mouse.move(900, 100)
    time.sleep(short_delay)
    # Click the right button
    mouse.click(Button.right, 1)
    time.sleep(short_delay)
    # Click the middle button
    mouse.click(Button.middle, 1)
    time.sleep(short_delay)
    # Double click the left button
    mouse.click(Button.left, 2)
    time.sleep(short_delay)
    # Click the left button ten times
    # mouse.click(Button.left, 10)
    # mouse.press(Button.left)
    # mouse.release(Button.left)
    # time.sleep(short_delay)
    # Scroll up two steps
    mouse.scroll(0, 2)
    time.sleep(short_delay)
    # Scroll right five steps
    mouse.scroll(5, 0)
    time.sleep(short_delay)
    # Move cursor position
    mouse.move(-900, -100)
    time.sleep(long_delay)