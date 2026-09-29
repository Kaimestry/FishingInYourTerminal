from game.data.baits import BAITS
from game.data.rods import RODS
from game.fishing import get_bait
from ui.style import *
from ui.variant_style import *

NAME_WIDTH = 30
RARITY_WIDTH = 15
MIN_BOX_LEN = 40


def inv_header(state, box_len):
    money = state.money

    print(text_box("t", box_len))

    print(text_box("text", box_len, "INVENTORY"))
    print(text_box(
        "text",
        box_len,
        f"{YELLOW}MONEY - {money:,} (G){RESET}"
    ))

    print(text_box("s", box_len))


def inventory_fish_name(fish):
    name = fish["name"]
    variant = fish["variant"]

    if variant == "normal":
        return name

    if variant == "baby":
        return small_text(f"Baby {name}")

    if variant == "large":
        return BOLD + f"Large {name}" + RESET

    if variant == "burning":
        return gradient_text(
            f"Burning {name}",
            FIRE_COLORS,
        )

    if variant == "uranium":
        return gradient_text(
            f"Radioactive {name}",
            URANIUM_COLORS,
        )

    if variant == "shiny":
        return gradient_text(
            f"Shiny {name}",
            SHINY_COLORS,
        )

    if variant == "shadow":
        return gradient_text(
            f"Shadow {name}",
            SHADOW_COLORS,
        )


def get_recent_catch_row_length(state):
    recent_fish = state.inventory["fish"][-5:]

    if not recent_fish:
        return MIN_BOX_LEN

    return max(
        NAME_WIDTH
        + RARITY_WIDTH
        + len(f"{fish['money']:,} (G)")
        for fish in recent_fish
    )


def display_recent_caught_fish(state, box_len):
    print()
    print("RECENT CATCHES")
    print(line(box_len + 2, character="─"))
    print()

    if not state.inventory["fish"]:
        print(f"{hex_color("#6c6c6c")}There's none in the inventory.{RESET}")
        print()
        return

    recent_fish = state.inventory["fish"][-5:][::-1]

    for fish in recent_fish:
        name = inventory_fish_name(fish)
        rarity = fish["rarity"]
        rarity_color = RARITY_COLORS[rarity]
        value = fish["money"]

        print(
            f"{pad_text(name, 30)}"
            f"{rarity_color}{rarity.capitalize():<15}{RESET}"
            f"{YELLOW}{value:>7,} (G){RESET}"
        )
        print()

def display_item(item_data):
    label = item_data["label"]
    style = item_data["style"]

    if style == "shiny":
        return gradient_text(label, SHINY_COLORS)
    if style == "burning":
        return gradient_text(label, FIRE_COLORS)
    if style == "shadow":
        return gradient_text(label, SHADOW_COLORS)
    if style == "debug":
        return gradient_text(label, SHADOW_COLORS)

    return label

def display_equipments(state, box_len):
    print(line(box_len + 2, character="─"))
    print()
    rod_data = RODS[state.equipped["rod"]]
    bait_data = get_bait(state)

    rod = display_item(rod_data)
    bait = display_item(bait_data) if bait_data else " "

    print(f"  ROD  - {rod}")
    print()
    print(f"  BAIT - {bait}")
    print()

def inv_footer(state, box_len):
    print(text_box("s", box_len))
    print(text_box("text", box_len, f"Use {BLUE}inv!help{RESET} to learn more"))
    print(text_box("b", box_len))