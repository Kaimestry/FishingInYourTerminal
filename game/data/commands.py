from game.fishing import fish
from ui.terminal import display_catch, clear_terminal, print_help, display_inventory


def help_command():
    print_help()


def fish_command():
    caught_fish = fish()

    if caught_fish is None:
        print("You didn't catch anything...")
    else:
        display_catch(caught_fish)

def inventory_command():
    display_inventory()


def quit_command():
    print("Goodbye!")
    return False


commands = {
    "help": {
        "aliases": [],
        "description": "Show available commands",
        "function": help_command,
    },
    "fish": {
        "aliases": ["f"],
        "description": "Go fishing",
        "function": fish_command,
    },
    "inventory": {
            "aliases": ["inv"],
            "description": "Open inventory",
            "function": inventory_command,
        },
    "quit": {
        "aliases": ["q"],
        "description": "Exit the game",
        "function": quit_command,
    },
}