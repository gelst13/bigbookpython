"""Rainbow, by Al Sweigart al@inventwithpython.com
Shows a simple rainbow animation. Press Ctrl-C to stop.
View the original code at https://nostarch.com/big-book-small-python-projects
Tags: tiny, artistic, bext, beginner, scrolling"""

import time, sys

try:
    import bext
except ImportError:
    print('This program requires the bext module, which you')
    print('can install by following the instructions at')
    print('https://pypi.org/project/Bext/')
    sys.exit()

print('Rainbow, by Al Sweigart al@inventwithpython.com')
print('Press Ctrl-C to stop.')
time.sleep(3)

indent = 0  # How many spaces to indent.
indent_increasing = True  # Whether the indentation is increasing or not.

try:
    while True:  # Main program loop.
        print(' ' * indent, end='')
        bext.fg('red')
        print('##', end='')
        bext.fg('yellow')
        print('##', end='')
        bext.fg('green')
        print('##', end='')
        bext.fg('blue')
        print('##', end='')
        bext.fg('cyan')
        print('##', end='')
        bext.fg('purple')
        print('##')

        if indent_increasing:
            # Increase the number of spaces:
            indent = indent + 1
            if indent == 60:  # TODO: Change this to 10 or 30.
                # Change direction:
                indent_increasing = False
        else:
            # Decreasing the number of spaces:
            indent = indent - 1
            if indent == 0:
                # Change direction:
                indent_increasing = True

        time.sleep(0.02)  # Add a slight pause.
except KeyboardInterrupt:
    sys.exit()  # When Ctrl-C is pressed, end program.
