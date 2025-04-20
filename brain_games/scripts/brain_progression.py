from brain_games.engine import run_game
from brain_games.games.game_progression import TASK, create_progression_question


def main():
    run_game(TASK, create_progression_question)


if __name__ == "__main__":
    main()