import time
from pynput.keyboard import Key, Controller

keyboard = Controller()
long_delay = 30
middle_delay = 10
short_delay = 5

# Press and release space
# keyboard.press(Key.space)
# keyboard.release(Key.space)
# time.sleep(short_delay)

# Type a lower case A; this will work even if no key on the
# physical keyboard is labelled 'A'
# keyboard.press('a')
# keyboard.release('a')
# time.sleep(short_delay)

# Type two upper case As
# keyboard.press('A')
# keyboard.release('A')
# with keyboard.pressed(Key.shift):
#     keyboard.press('a')
#     keyboard.release('a')
# time.sleep(short_delay)    

# Type 'text' using the shortcut type method
while True:
    keyboard.type('NSLog(@"testing");\n')
    time.sleep(middle_delay)