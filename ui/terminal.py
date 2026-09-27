import os
from ui.style import RARITY_COLORS, RESET, YELLOW, BLUE, text_box
from ui.variant_style import *


def print_help():
    from game.data.commands import commands

    print("Available commands:")
    print("--------------------------------")

    for command, data in commands.items():
        aliases = data["aliases"]

        if aliases:
            command_text = f"{command} / {' / '.join(aliases)}"
        else:
            command_text = command

        print(f"{command_text:<20} {data['description']}")

'''
COMMAND DISPLAY
'''

def display_catch(fish):
    variant = fish["variant"]

    if variant == "normal":
        normal_display(fish)

    elif variant == "baby":
        baby_display(fish)

    elif variant == "large":
        large_display(fish)

    elif variant == "burning":
        burning_display(fish)

    elif variant == "uranium":
        uranium_display(fish)

    elif variant == "shiny":
        shiny_display(fish)

    elif variant == "shadow":
        shadow_display(fish)
        
def display_inventory():
    recent_fish = [
        {"name": "Salmon", "rarity": "common"},
        {"name": "Mackerel", "rarity": "common"},
        {"name": "Swordfish", "rarity": "rare"},
        {"name": "Cod", "rarity": "common"},
        {"name": "Tuna", "rarity": "common"},
        {"name": "Great White Shark", "rarity": "legendary"},
    ]

    rod = "Basic Fishing Rod"
    bait = "Worm × 12"
    money = 1250

    #PRINTING
    box_length = 40
    print(text_box("t", box_length))
    print(text_box("text", box_length, "INVENTORY"))
    print(text_box("text", box_length, f"{YELLOW}MONEY - {money:,} (G){RESET}"))
    print(text_box("s", box_length))

    print()
    print("  RECENT CATCHES                          ")
    print("  ──────────────────────────────────────  ")

    for fish in recent_fish:
        color = RARITY_COLORS[fish["rarity"]]

        print(
            f"  🎣 {color}{fish['name']:<25} {fish['rarity'].capitalize():<12}{RESET}"
            )

    print()
    print("  ──────────────────────────────────────  ")
    print(f"  ROD - 🎣 {rod}")
    print(f"  BAIT - 🪱  {bait}")
    print()

    print(text_box("s", box_length))
    print(text_box("text", box_length, f"{BLUE}inv!fish{RESET} → View all fish"))
    print(text_box("text", box_length, f"{BLUE}inv!rod{RESET} → View all rods"))
    print(text_box("text", box_length, f"{BLUE}inv!bait{RESET} → View all baits"))
    print(text_box("b", box_length))
