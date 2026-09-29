import os
from ui.display_inventory import *
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
def display_catch(state, fish, debug):
    variant = fish["variant"]

    display_function = VARIANT_CATCH_DISPLAYS[variant]
    display_function(state, fish, debug)

    print()
    print(f"Fish Value: {YELLOW}{fish['money']:,} (G){RESET}")


def display_lost_fish(state, fish, debug):
    variant = fish["variant"]

    display_function = VARIANT_LOST_DISPLAYS[variant]
    display_function(state, fish, debug)



def display_inventory(state, debug):
    rod = "Basic Fishing Rod"
    bait = "Worm × 12"
    money = 1250

    #PRINTING
    box_len = get_recent_catch_row_length(state) + 2
    inv_header(state, box_len)
    display_recent_caught_fish(state, box_len)
    display_equipments(state, box_len)
    inv_footer(state, box_len)
