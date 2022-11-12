from random import randint

TASK = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN_NUMBER_TO_GUESS = 1
MAX_NUMBER_TO_GUESS = 100


def is_even_number(number):
    return number % 2 == 0


def create_game():
    random_number = randint(MIN_NUMBER_TO_GUESS, MAX_NUMBER_TO_GUESS)

    question = random_number
    correct_answer = 'yes' if is_even_number(random_number) else 'no'

    return question, correct_answer
