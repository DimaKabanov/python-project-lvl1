from brain_games.engine import run_game
from brain_games.games.game_calc import TASK, create_calc_question


def main():
    run_game(TASK, create_calc_question)


if __name__ == "__main__":
    main()