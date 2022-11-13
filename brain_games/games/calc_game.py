from random import randint, choice
from operator import mul, add, sub

TASK = 'What is the result of the expression?'
MIN_NUMBER_TO_EXPRESSION = 1
MAX_NUMBER_TO_EXPRESSION = 10


def get_operation():
    operation_list = [('*', mul), ('+', add), ('-', sub)]
    return choice(operation_list)


def create_game():
    left_operand = randint(MIN_NUMBER_TO_EXPRESSION, MAX_NUMBER_TO_EXPRESSION)
    right_operand = randint(MIN_NUMBER_TO_EXPRESSION, MAX_NUMBER_TO_EXPRESSION)

    operation_as_str, calc_operator = get_operation()

    question = f'{left_operand} {operation_as_str} {right_operand}'
    correct_answer = str(calc_operator(left_operand, right_operand))

    return question, correct_answer
