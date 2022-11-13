from random import randint

TASK = 'Find the greatest common divisor of given numbers.'
MIN_NUMBER = 1
MAX_NUMBER = 100


def find_gcd(first_number, second_number):
    first = first_number
    second = second_number

    while second:
        first, second = second, first % second

    return first


def create_game():
    first_number = randint(MIN_NUMBER, MAX_NUMBER)
    second_number = randint(MIN_NUMBER, MAX_NUMBER)

    question = f'{first_number} {second_number}'
    correct_answer = str(find_gcd(first_number, second_number))

    return question, correct_answer
