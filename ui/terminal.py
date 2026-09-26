import os
from ui.style import RARITY_COLORS, RESET, YELLOW, text_box

def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")


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
    color = RARITY_COLORS[fish["rarity"]]
    rarity = fish["rarity"].capitalize()

    print("You caught....")
    print(
        f"🎣 "
        f"{color}{fish['name']}{RESET} "
        f"- {color}{rarity}{RESET} "
        f"🎣"
    )

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

    print("                                          ")
    print("  RECENT CATCHES                          ")
    print("  ──────────────────────────────────────  ")

    for fish in recent_fish:
        print(
            f"  🎣 {fish['name']:<20} "
            f"{fish['rarity'].capitalize():<12} "
        )

    print()
    print(f"  ROD - 🎣 {rod}")
    print()
    print(f"  BAIT - 🪱  {bait}")
    print()

    print(text_box("s", box_length))
    print(text_box("text", box_length, "inv!fish → View all fish"))
    print(text_box("text", box_length, "inv!rod → View all rods"))
    print(text_box("text", box_length, "inv!bait → View all baits"))
    print(text_box("b", box_length))
