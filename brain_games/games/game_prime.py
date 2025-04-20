from math import sqrt
from random import randint

TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'
MIN_NUMBER_TO_GUESS = 1
MAX_NUMBER_TO_GUESS = 10


def is_prime_number(number):
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


def create_prime_question():
    question = randint(MIN_NUMBER_TO_GUESS, MAX_NUMBER_TO_GUESS)
    correct_answer = 'yes' if is_prime_number(question) else 'no'

    return question, correct_answer