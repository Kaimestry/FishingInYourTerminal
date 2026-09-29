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



import os
import re
import time
import sys

ANSI_PATTERN = re.compile(r"\033\[[0-9;]*m")


def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")

def text_box(box_type, width=40, text=""):
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

    elif box_type == "center":
        visible_text = ANSI_PATTERN.sub("", text)
        padding = width - len(visible_text)

        left = padding // 2
        right = padding - left

        return (" " * left) + text + (" " * right)

def line(length, character="-"):
    return character * length

'''
COLOR
'''
def hex_color(hex_code):
    hex_code = hex_code.lstrip("#")

    r = int(hex_code[0:2], 16)
    g = int(hex_code[2:4], 16)
    b = int(hex_code[4:6], 16)

    return f"\033[38;2;{r};{g};{b}m"

def changing_color(text, colors, offset):
    colored = ""

    for i, char in enumerate(text):
        color = colors[(i + offset) % len(colors)]
        colored += f"{color}{char}"

    return f"{colored}{RESET}"

def changing_color_uniform(text, colors, offset):
    color = colors[offset % len(colors)]
    return f"{color}{text}{RESET}"

def changing_color_text(
    text,
    colors,
    duration=3,
    speed=0.1,
    width=40
):
    start = time.time()
    offset = 0

    while time.time() - start < duration:

        # Entire text gets the same color
        colored = changing_color_uniform(
            text,
            colors,
            offset
        )

        # Center it
        visible_length = len(text)
        padding = width - visible_length
        left = padding // 2
        right = padding - left

        centered_text = (
            " " * left
            + colored
            + " " * right
        )

        print(
            f"\r{centered_text}",
            end="",
            flush=True
        )

        time.sleep(speed)
        offset += 1

    print()
    
def animate_frame(
    frame_function,
    duration=1.5,
    speed=0.1
):
    start = time.time()
    offset = 0

    # Build the first frame
    frame = frame_function(offset)

    # Figure out how many terminal lines it occupies
    frame_height = frame.count("\n") + 1

    while time.time() - start < duration:

        # Build current frame
        frame = frame_function(offset)

        # Print it
        print(frame, end="")

        time.sleep(speed)

        # Move cursor back to the top of the frame
        print(f"\033[{frame_height}A", end="")

        offset += 1


def pad_text(text, width):
    visible_length = len(ANSI_PATTERN.sub("", text))
    return text + " " * max(0, width - visible_length)