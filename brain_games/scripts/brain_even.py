from brain_games.engine import run_game
from brain_games.games.game_even import TASK, create_even_question


def main():
    run_game(TASK, create_even_question)


if __name__ == "__main__":
    main()