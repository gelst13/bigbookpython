"""
Birthday Paradox Simulation, by Al Sweigart al@inventwithpython.com
  2. Explore the surprising probabilities of the "Birthday Paradox".
  3. More info at https://en.wikipedia.org/wiki/Birthday_problem
  4. This code is available at https://nostarch.com/big-book-small-python-programming
  5. Tags: short, math, simulation

The Birthday Paradox, also called the Birthday Problem, is the surprisingly
high probability that two people will have the same birthday even in a small
group of people. In a group of 70 people, there’s a 99.9 percent chance of
two people having a matching birthday. But even in a group as small as 23 people,
there’s a 50 percent chance of a matching birthday. This program performs
several probability experiments to determine the percentages for groups of
different sizes. We call these types of experiments, in which we conduct multiple
random trials to understand the likely outcomes, Monte Carlo experiments.
"""

import datetime
import random
import string
from collections import Counter


def readable_dates(days: list) -> list:
    dates = list()
    for day in days:
        dates.append(datetime.date.fromordinal(day).strftime('%b %d'))
    return dates


def generate_birthdays(num_birthdays: int) -> list:
    ordinal_days = list()
    for _ in range(int(num_birthdays)):
        ordinal_days.append(random.choice(range(1, 366)))
    return ordinal_days


def calculate_duplicate_dates(numbers: list) -> list:
    # print(len(set(numbers)))
    freq_counter = Counter(list(map(str, numbers)))
    duplicate_dates = list()
    for data in freq_counter.items():
        if data[1] > 1:
            duplicate_dates.append(int(data[0]))
    return duplicate_dates


def calculate_probability(num_birthdays: int):
    shared_birthday = 0
    total_number_of_experiments = 100_000
    print('Generating {} random birthdays 100_000 times...'.format(num_birthdays))
    input('Press Enter to begin...')
    print('Let\'s run another 100,000 simulations.')
    for experiment_index in range(0, total_number_of_experiments):
        if experiment_index % 10000 == 0:
            print(experiment_index, 'simulations run...')
        dates = generate_birthdays(num_birthdays)
        if len(set(dates)) < len(dates):
            shared_birthday += 1
    print('100,000 simulations run.')
    common_probability = round((shared_birthday / total_number_of_experiments) * 100, 2)
    return shared_birthday, common_probability


def print_result(num_birthdays, shared_birthday, probability):
    result = '''Out of 100,000 simulations of \"$people\" people, there was a
matching birthday in that group \"$times\" times. This means
that \"$people\" people have a \"$chance\" % chance of
having a matching birthday in their group.
That's probably more than you would think!'''
    template = string.Template(result)
    message = template.substitute(people=num_birthdays, times=shared_birthday, chance=probability)
    print(message)


def main():
    print('Birthday Paradox, by Al Sweigart al@inventwithpython.com')
    num_birthdays = input('How many birthdays shall I generate? (Max 100):> \n')
    ordinal_days = generate_birthdays(int(num_birthdays))
    print(f'Here are {len(ordinal_days)} birthdays:')
    print(*readable_dates(ordinal_days), sep=', ')
    duplicate_dates = calculate_duplicate_dates(ordinal_days)
    if duplicate_dates:
        message = 'In this simulation, multiple people have a birthday on {}'
        print(message.format(', '.join(readable_dates(duplicate_dates))))
    else:
        print('there are no matching birthdays.')
    print()
    data = calculate_probability(int(num_birthdays))
    print_result(num_birthdays, data[0], data[1])


if __name__ == '__main__':
    main()
