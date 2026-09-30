import os
from ui.display_inventory import *
from ui.style import *
from ui.variant_style import *

def start_ins():
    print(f'🎣 Welcome to {BLUE}Fish In Terminal{RESET} 🎣')
    print()
    print(f"- Start fishing by entering the command {BLUE}fish{RESET}")
    print(f"- To view all availble commands, enter {MAGENTA}help{RESET}")
    pass

def print_help(state, debug):
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
    money = state.money
    text = f"{YELLOW}MONEY - {money:,} (G){RESET}"
    box_len = get_recent_catch_row_length(state) + 2

    #PRINTING
    inv_header(state, box_len, title="INVENTORY", subtitle=text)
    display_recent_caught_fish(state, box_len)
    display_bucket_capacity(state)
    display_equipments(state, box_len)
    inv_footer(state, box_len=box_len, text=f'Use {BLUE}inv!help{RESET} to learn more')

def display_bucket(state, debug):
    box_len = get_bucket_row_length(state) + 2

    text = display_bucket_capacity(state)
    inv_header(
        state,
        box_len,
        title="BUCKET",
        subtitle=text
    )

    if not state.inventory["fish"]:
        print(
            text_box(
                "center",
                width=box_len,
                text=f"{hex_color('#6c6c6c')}There's none in the bucket.{RESET}"
            )
        )        
        print()
        inv_footer(state, box_len=box_len, text=f'Start fishing to fill bucket')
        return

    fish_inventory = state.inventory["fish"]

    for index in range(len(fish_inventory) - 1, -1, -1):
        fish = fish_inventory[index]

        name = inventory_fish_name(fish)
        rarity = fish["rarity"]
        rarity_color = RARITY_COLORS[rarity]
        value = fish["money"]

        print(
            f"{index + 1:>3}. "
            f"{pad_text(name, 30)}"
            f"{rarity_color}{rarity.capitalize():<15}{RESET}"
            f"{YELLOW}{value:>7,} (G){RESET}"
        )
        print()

    inv_footer(state, box_len=box_len, text=f'Use {BLUE}sell_b{RESET} to empty bucket')


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