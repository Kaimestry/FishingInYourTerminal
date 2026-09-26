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

import re

ANSI_PATTERN = re.compile(r"\033\[[0-9;]*m")


def text_box(box_type, width, text=""):
    if box_type == "t":
        return "╔" + "═" * width + "╗"

    elif box_type == "b":
        return "╚" + "═" * width + "╝"

    elif box_type == "s":
        return "╠" + "═" * width + "╣"

    elif box_type == "text":
        visible_text = ANSI_PATTERN.sub("", text)
        padding = width - len(visible_text)

        left = padding // 2
        right = padding - left

        return "║" + (" " * left) + text + (" " * right) + "║"