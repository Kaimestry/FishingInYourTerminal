#game/data/commands.py

from game.fishing import fish
from game.inventory import *
from ui.fishing_dialogue import fishing_dialogue
from ui.terminal import *


def help_command():
    print_help()


def fish_command(state, debug):
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

    print()
    print("=== INVENTORY ===")

    for category, items in state.inventory.items():
        print(f"{category.capitalize()}:")

        if not items:
            print("  (empty)")
        else:
            if isinstance(items, list):
                for item in items:
                    print(f"  {item}")
            else:
                print(f"  {items}")

        print()


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