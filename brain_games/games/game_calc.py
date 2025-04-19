from operator import add, mul, sub
from random import choice, randint

TASK = 'What is the result of the expression?'
MIN_NUMBER_TO_EXPRESSION = 1
MAX_NUMBER_TO_EXPRESSION = 10


def get_operation():
    operations = [('+', add), ('-', sub), ('*', mul)]
    return choice(operations)


def create_calc_question():
    left_operand = randint(MIN_NUMBER_TO_EXPRESSION, MAX_NUMBER_TO_EXPRESSION)
    right_operand = randint(MIN_NUMBER_TO_EXPRESSION, MAX_NUMBER_TO_EXPRESSION)

    operation_as_string, operation = get_operation()

    question = f'{left_operand} {operation_as_string} {right_operand}'
    correct_answer = str(operation(left_operand, right_operand))

    return question, correct_answer