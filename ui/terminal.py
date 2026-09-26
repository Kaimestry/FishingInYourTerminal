import os
RESET = "\033[0m"

RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"

RARITY_COLORS = {
    "common": WHITE,
    "uncommon": GREEN,
    "rare": BLUE,
    "epic": MAGENTA,
    "legendary": YELLOW,
}

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

    print("╔══════════════════════════════════════════╗")
    print("║                INVENTORY                 ║")
    print("╠══════════════════════════════════════════╣")

    print("║                                          ║")
    print("║  RECENT CATCHES                          ║")
    print("║  ──────────────────────────────────────  ║")

    for fish in recent_fish:
        print(
            f"║  🎣 {fish['name']:<20} "
            f"{fish['rarity'].capitalize():<12} ║"
        )

    print("║                                          ║")
    print("║  ROD                                     ║")
    print("║  ──────────────────────────────────────  ║")
    print(f"║  🎣 {rod:<36} ║")

    print("║                                          ║")
    print("║  BAIT                                    ║")
    print("║  ──────────────────────────────────────  ║")
    print(f"║  🪱 {bait:<36} ║")

    print("║                                          ║")
    print("║  MONEY                                   ║")
    print("║  ──────────────────────────────────────  ║")
    print(f"║  💰 {money:,} G{'':<31}║")

    print("║                                          ║")
    print("╠══════════════════════════════════════════╣")
    print("║ inv!fish → View all fish                 ║")
    print("║ inv!rod  → View all rods                 ║")
    print("║ inv!bait → View all bait                 ║")
    print("╚══════════════════════════════════════════╝")