
from random import randint

TASK = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN_NUMBER_TO_GUESS = 1
MAX_NUMBER_TO_GUESS = 10


def is_even_number(number):
    return number % 2 == 0


def create_even_question():
    question = randint(MIN_NUMBER_TO_GUESS, MAX_NUMBER_TO_GUESS)
    correct_answer = 'yes' if is_even_number(question) else 'no'

    return question, correct_answer