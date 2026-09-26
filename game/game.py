from game.data.commands import commands
from ui.terminal import clear_terminal


def start_game():
    clear_terminal()
    print(
        f'Welcome to Fishing in Terminal!'
    )

    while True:
        print()
        command = input("> ").lower().strip()

        selected_command = None

        for name, data in commands.items():
            if command == name or command in data["aliases"]:
                selected_command = data
                break

        if selected_command is None:
            print("Unknown command. Type 'help' for a list of commands.")
            continue

        clear_terminal()

        result = selected_command["function"]()

        if result is False:
            break