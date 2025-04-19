
from random import randint

TASK = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even_number(number):
    return number % 2 == 0


def create_even_question():
    question = randint(1, 10)
    correct_answer = 'yes' if is_even_number(question) else 'no'

    return (question, correct_answer)