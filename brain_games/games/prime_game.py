from math import sqrt
from random import randint


TASK = 'Answer "yes" if number is prime. Otherwise answer "no"'
MIN_NUMBER_TO_GUESS = 1
MAX_NUMBER_TO_GUESS = 20


def is_prime(number):
    if number <= 2:
        return True

    if number % 2 == 0:
        return False

    divider = 3
    sqrt_number = sqrt(number)

    while divider <= sqrt_number:
        if number % divider:
            divider += 2
        else:
            return False

    return True


def create_game():
    random_number = randint(MIN_NUMBER_TO_GUESS, MAX_NUMBER_TO_GUESS)

    question = f'{random_number}'
    correct_answer = 'yes' if is_prime(random_number) else 'no'

    return question, correct_answer
