"""
Bagels -a deductive logic game, you must guess a secret 3-digit number based on clues.
The game offers one of the following hints in response to your guess:
“Pico” - correct digit in the wrong place,
“Fermi” - correct digit in the correct place,
“Bagels” if your guess has no correct digits.
You have 10 tries to guess the secret number.
"""
import random


NUM_DIGITS = 3
NUM_GUESSES = 10

introduction = '''Bagels, a deductive logic game.
By AL Sweigart al@inventwithpython.com
I am thinking of a {}-digit number with no repeated digits.
Try to guess what it is. Here are some clues:
When I say:	    That means:
Pico			One digit is correct but in the wrong position.
Fermi			One digit is correct and in the right position.
Bagels			No digit is correct.

For example, if the secret number was 248 and your guess was 842, the clues would be Fermi Pico.'''


def get_secret_num() -> str:
    """Return NUM_DIGITS-digit number with no repeated digits"""
    digits = list('0123456789')
    random.shuffle(digits)
    sec_number = ''.join(digits[:3])
    return sec_number


def exit_():
    print('Thanks for playing!')
    exit()


def guess_number(secret_num):
    for count in range(1, NUM_GUESSES + 1):
        print('Guess #{}'.format(count))
        player_guess = input()
        if player_guess == secret_num:
            print('You got it!')
            break
        elif count == 10:
            print("You ran out of guesses")
            print('The answer was {}.'.format(secret_num))
            break
        else:
            print(get_clues(player_guess, secret_num))


def get_clues(guess, secret_num):
    """Pico			One digit is correct but in the wrong position.
Fermi			One digit is correct and in the right position.
Bagels			No digit is correct."""
    clues = list()
    for i in range(len(guess)):
        if guess[i] == secret_num[i]:
            clues.append('Fermi')
        elif guess[i] in secret_num:
            clues.append('Pico')
    return ' '.join(sorted(clues)) if clues else 'Bagels'


def main():
    while True:
        print(introduction.format(NUM_DIGITS))
        secret_num = get_secret_num()
        print('''I have thought up a number.
 You have {} guesses to get it.'''.format(NUM_GUESSES))
        print('secret_num', secret_num)
        guess_number(secret_num)
        play_again = input('Do you want to play again? (yes or no):> \n')
        if not play_again.lower().startswith('y'):
            exit_()


if __name__ == '__main__':
    main()
