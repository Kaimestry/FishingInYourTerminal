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


def display_catch(fish):
    color = RARITY_COLORS[fish["rarity"]]

    print(
        f"🎣 You caught "
        f"{color}{fish['name']}{RESET} "
        f"({color}{fish['rarity']}{RESET})! "
        f"🎣"

    )