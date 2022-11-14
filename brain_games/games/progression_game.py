from random import randint, choice


TASK = 'What number is missing in the progression?'
MIN_NUMBER = 1
MAX_NUMBER = 10
LENGTH_PROGRESSION = 10


def get_progression(start, step, length):
    counter = 2
    progression = [start]

    while counter < length:
        next_element = start + ((counter - 1) * step)
        progression.append(next_element)
        counter += 1

    return progression


def create_game():
    start_progression = randint(MIN_NUMBER, MAX_NUMBER)
    step = randint(MIN_NUMBER, MAX_NUMBER)

    progression = get_progression(start_progression, step, LENGTH_PROGRESSION)
    number_to_hide = choice(progression)

    with_hidden_number = map(
        lambda number: '..' if number == number_to_hide else str(number),
        progression
    )

    question = ' '.join(list(with_hidden_number))
    correct_answer = str(number_to_hide)

    return question, correct_answer
