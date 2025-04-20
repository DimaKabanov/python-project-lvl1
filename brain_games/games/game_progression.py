from random import choice, randint

TASK = 'What number is missing in the progression?'
MIN_NUMBER_TO_PROGRESSION = 5
MAX_NUMBER_TO_PROGRESSION = 10
MIN_NUMBER_TO_DIFFERENCE = 1
MAX_NUMBER_TO_DIFFERENCE = 5


def get_progression(start, difference, count):
    return [start + difference * i for i in range(count)]


def create_progression_question():
    difference = randint(MIN_NUMBER_TO_DIFFERENCE, MAX_NUMBER_TO_DIFFERENCE)
    progression = get_progression(
        MAX_NUMBER_TO_PROGRESSION,
        difference,
        MAX_NUMBER_TO_PROGRESSION
    )

    random_progression_item = choice(progression)
    progression_with_hidden_item = map(
        lambda item: '..' if item == random_progression_item else str(item),
        progression
    )

    question = ' '.join(list(progression_with_hidden_item))
    correct_answer = str(random_progression_item)

    return question, correct_answer