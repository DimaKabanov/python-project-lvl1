from brain_games.engine import run_game
from brain_games.games.game_gcd import TASK, create_gcd_question


def main():
    run_game(TASK, create_gcd_question)


if __name__ == "__main__":
    main()