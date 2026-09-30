#game/game.py

from game.data.commands import commands
from ui.terminal import clear_terminal, start_ins


def start_game(state, debug):
    clear_terminal()
    start_ins()

    while True:
        print()
        command = input("> ").lower().strip() or "fish"

        selected_command = None

        for name, data in commands.items():
            if command == name or command in data["aliases"]:
                selected_command = data
                break

        if selected_command is None:
            print("Unknown command. Type 'help' for a list of commands.")
            continue

        clear_terminal()

        result = selected_command["function"](state, debug)

        if result is False:
            break