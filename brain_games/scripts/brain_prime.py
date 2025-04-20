from brain_games.engine import run_game
from brain_games.games.game_prime import TASK, create_prime_question


def main():
    run_game(TASK, create_prime_question)


if __name__ == "__main__":
    main()