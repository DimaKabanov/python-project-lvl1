import prompt


def run_game(game):
    print('Welcome to the Brain Games!')

    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}')

    print(game.TASK)

    attempts_count = 3

    while attempts_count:
        question, correct_answer = game.create_game()

        print(f'Question: {question}')

        user_answer = prompt.string('Your answer: ')

        if user_answer == correct_answer:
            print('Correct!')
        else:
            print(f'\'{user_answer}\' is wrong answer ;(.'
                  f'Correct answer was \'{correct_answer}\'.')

            print(f'Let\'s try again, {user_name}!')
            break

        attempts_count -= 1

    if attempts_count == 0:
        print(f'Congratulations, {user_name}!')
