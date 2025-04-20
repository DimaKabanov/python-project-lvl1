import prompt


def run_game(task, create_question):
    print('Welcome to the Brain Games!')

    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')

    print(task)

    MAX_ATTEMPTS_COUNT = 3
    spent_attempts_count = 0

    while spent_attempts_count < MAX_ATTEMPTS_COUNT:
        question, correct_answer = create_question()

        print(f'Question: {question}')

        answer = prompt.string('Your answer: ')

        if answer != correct_answer:
            print(f"'{answer}' is wrong answer ;(."
                  f"Correct answer was '{correct_answer}'.")

            print(f"Let's try again, {name}!")
            break

        print('Correct!')
        spent_attempts_count += 1

    if spent_attempts_count == MAX_ATTEMPTS_COUNT:
        print(f'Congratulations, {name}!')