from game.game import start_game
from game.game_state import *


def main():
    state = GameState()
    debug = DebugState()
    start_game(state, debug)


if __name__ == "__main__":
    main()