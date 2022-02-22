"""Magic Fortune Ball, by Al Sweigart al@inventwithpython.com
Ask a yes/no question about your future. Inspired by the Magic 8 Ball.
View the original code at https://nostarch.com/big-book-small-python-projects
Tags: tiny, beginner, humor"""

import random, time


def slow_space_print(text, interval=0.1):
    """Slowly display text with spaces in between each letter and
    lowercase letter i's."""
    for character in text:
        if character == 'I':
            # I's are displayed in lowercase for style:
            print('i ', end='', flush=True)
        else:
            # All other characters are displayed normally:
            print(character + ' ', end='', flush=True)
        time.sleep(interval)
    print()  # Print two newlines at the end.
    print()


# Prompt for a question.
slow_space_print('MAGIC FORTUNE BALL, BY AL SWEIGART')
time.sleep(0.5)
slow_space_print('ASK ME YOUR YES/NO QUESTIONS.')
input('> ')

# Display a brief reply:
replies = [
    'LET ME THINK ON THIS...',
    'AN INTERESTING QUESTION...',
    'HMMM... ARE YOU SURE YOU WANT TO KNOW..?',
    'DO YOU THINK SOME THINGS ARE BEST LEFT UNKNOWN..?',
    'I MIGHT TELL YOU, BUT YOU MIGHT NOT LIKE THE ANSWER...',
    'YES... NO... MAYBE... I WILL THINK ON IT...',
    'AND WHAT WILL YOU DO WHEN YOU KNOW THE ANSWER? WE SHALL SEE...',
    'I SHALL CONSULT MY VISIONS...',
    'YOU MAY WANT TO SIT DOWN FOR THIS...',
]
slow_space_print(random.choice(replies))

# Dramatic pause:
slow_space_print('.' * random.randint(4, 12), 0.7)

# Give the answer:
slow_space_print('I HAVE AN ANSWER...', 0.2)
time.sleep(1)
answers = [
    'YES, FOR SURE',
    'MY ANSWER IS NO',
    'ASK ME LATER',
    'I AM PROGRAMMED TO SAY YES',
    'THE STARS SAY YES, BUT I SAY NO',
    'I DUNNO MAYBE',
    'FOCUS AND ASK ONCE MORE',
    'DOUBTFUL, VERY DOUBTFUL',
    'AFFIRMATIVE',
    'YES, THOUGH YOU MAY NOT LIKE IT',
    'NO, BUT YOU MAY WISH IT WAS SO',
]
slow_space_print(random.choice(answers), 0.05)
