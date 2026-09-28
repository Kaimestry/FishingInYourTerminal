#game/data/commands.py

from game.fishing import fish
from ui.fishing_dialogue import fishing_dialogue
from ui.terminal import *


def help_command():
    print_help()


def fish_command(state, debug):
    fishing_dialogue(state, debug)
    
    caught_fish = fish(state)

    if caught_fish["caught"]:
        state.fish_caught += 1

        variant = caught_fish["variant"]
        state.variant_caught[variant] += 1

        display_catch(state, caught_fish, debug)
    else:
        display_lost_fish(state, caught_fish, debug)

def inventory_command(state):
    display_inventory(state)


def quit_command(state):
    print("Goodbye!")
    return False

def demo_command(state, debug):
    debug_command(state, debug)

def debug_command(state, debug):
    print("=== DEBUG STATS ===")
    print(f"Fish caught: {state.fish_caught}")
    print()

    print("Variants:")
    for variant, amount in state.variant_caught.items():
        print(f"  {variant.capitalize()}: {amount}")


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
    "debug": {
        "aliases": ["d"],
        "description": "Execute most recent tested function",
        "function": demo_command,
    },
}