
from random import randint

TASK = 'Find the greatest common divisor of given numbers.'
MIN_NUMBER_TO_GCD = 1
MAX_NUMBER_TO_GCD = 10


def find_gcd(first_number, second_number):
    first = first_number
    second = second_number

    while second:
        first, second = second, first % second

    return first


def create_gcd_question():
    first_number = randint(MIN_NUMBER_TO_GCD, MAX_NUMBER_TO_GCD)
    second_number = randint(MIN_NUMBER_TO_GCD, MAX_NUMBER_TO_GCD)

    question = f'{first_number} {second_number}'
    correct_answer = str(find_gcd(first_number, second_number))

    return question, correct_answer