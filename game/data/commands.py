#game/data/commands.py

from game.fishing import fish
from game.inventory import *
from ui.fishing_dialogue import fishing_dialogue
from ui.terminal import *


def help_command(state, debug):
    print_help(state, debug)


def fish_command(state, debug):
    if is_bucket_full(state):
        print(f"Your bucket is full now! Enter {BLUE}sell_bucket{RESET} to empty it!")
        return

    fishing_dialogue(state, debug)
    clear_terminal()

    caught_fish = fish(state)

    if caught_fish["caught"]:
        state.fish_caught += 1

        variant = caught_fish["variant"]
        state.variant_caught[variant] += 1

        add_caught_fish(state, caught_fish)

        display_catch(state, caught_fish, debug)

    else:
        display_lost_fish(state, caught_fish, debug)

def inventory_command(state, debug):
    display_inventory(state, debug)

def view_bucket(state, debug):
    display_bucket(state, debug)

def sell_bucket(state, debug):
    display_sellbucket_result(state)
    sell_all_fish(state)

    


def quit_command(state):
    print("Goodbye!")
    return False

def demo_command(state, debug):
    debug_command(state, debug)



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
    "bucket": {
        "aliases": ["b"],
        "description": "View fish in bucket",
        "function": view_bucket,
    },
    "sell_bucket": {
            "aliases": ["sell_b"],
            "description": "Sell all fish in equipped bucket",
            "function": sell_bucket,
        },
    "quit": {
        "aliases": ["q"],
        "description": "Exit the game",
        "function": quit_command,
    },
    "debug": {
        "aliases": ["d"],
        "description": "Execute most recent tested function",
        "function": demo_command,
    },
}