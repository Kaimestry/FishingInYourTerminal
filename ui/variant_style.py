#ui/variant_style.py

import random

from game.data.dialogues import *
from ui.style import *
'''
TEMPLATE
'''
def animated_variant_display(
    state,
    fish,
    debug,
    message,
    name_text,
    variant_text,
    colors,
    duration=2,
    speed=0.1,
    uniform=False,
):
    rarity = fish["rarity"]
    rarity_color = RARITY_COLORS[rarity]

    color_function = (
        changing_color_uniform
        if uniform
        else changing_color
    )

    def build_frame(offset):
        animated_name = color_function(
            name_text.format(name=fish["name"]),
            colors,
            offset
        )

        animated_variant = color_function(
            variant_text,
            colors,
            offset
        )

        footer = (
            f"Rarity: "
            f"{rarity_color}{rarity.capitalize()}{RESET}"
            f" - Variant: "
            f"{animated_variant}"
        )

        return "\n".join([
            message,
            "",
            text_box("t"),
            "",
            text_box("center", text=animated_name),
            "",
            text_box("center", text=footer),
            "",
            text_box("b"),
        ]) + "\n"

    if state.debug_mode and debug.skip_animation:
        clear_terminal()
        print(build_frame(0))
        return

    animate_frame(
        build_frame,
        duration=duration,
        speed=speed
    )

    clear_terminal()
    print(build_frame(0))

def gradient_text(text, colors, off_index=1):
    result = []
    color_index = 0

    for char in text:
        if char == " ":
            result.append(char)
            continue

        result.append(
            f"{colors[color_index % len(colors)]}{char}{RESET}"
        )
        color_index += off_index

    return "".join(result)

'''
STYLING
'''
def normal_display(state, fish, debug):
    rarity = fish["rarity"]
    rarity_color = RARITY_COLORS[rarity]

    print("You caught....")
    print()

    print(text_box("t"))
    print()

    print(
        text_box(
            "center",
            text=(
                f"🎣 "
                f"{rarity_color}{fish['name']} - "
                f"{rarity.capitalize()}{RESET}"
                f" 🎣"
            )
        )
    )

    print()
    print(text_box("b"))

def normal_lost_display(state, fish, debug):
    rarity = fish["rarity"]
    rarity_color = RARITY_COLORS[rarity]

    print(
        f"Your "
        f"{fish['name']}"
        f" - ({rarity_color}{rarity.capitalize()}{RESET}) "
        f"escaped..."
    )

BABY_COLOR = hex_color("#E9B3FF")
def baby_display(state, fish, debug):
    rarity = fish["rarity"]
    rarity_color = RARITY_COLORS[rarity]

    name = small_text(fish["name"])

    print(
        "Your fish panicked and turned into a smaller version of itself"
    )
    print()

    print(text_box("t"))
    print()

    print(
        text_box(
            "center",
            text=(
                f"🍼 {small_text('baby')} "
                f"{rarity_color}{name}{RESET} 🍼"
            )
        )
    )

    footer = (
        f"{small_text('Rarity:')} "
        f"{rarity_color}{small_text(rarity.capitalize())}{RESET}"
        f"{small_text(' - Variant:')} "
        f"{BABY_COLOR}{small_text('Baby')}{RESET}"
    )

    print(
        text_box(
            "center",
            text=footer
        )
    )

    print()
    print(text_box("b"))

def baby_lost_display(state, fish, debug):
    rarity = fish["rarity"]
    rarity_color = RARITY_COLORS[rarity]

    print(
        f"Your "
        f"{small_text('baby')} "
        f"{small_text(fish['name'])}"
        f" - ({rarity_color}{small_text(rarity.capitalize())}{RESET}) "
        f"was too small to catch and swam away..."
    )

BOLD = "\033[1m"
def large_display(state, fish, debug):
    rarity = fish["rarity"]
    rarity_color = RARITY_COLORS[rarity]

    print("Your fish is probably bigger than a Whale")
    print()

    print(text_box("t"))
    print()

    print(
        text_box(
            "center",
            text=(
                f"{BOLD}{rarity_color}"
                f"🎣 LARGE {fish['name'].upper()} 🎣"
                f"{RESET}"
            )
        )
    )

    print()

    print(
        text_box(
            "center",
            text=(
                f"{BOLD}RARITY: "
                f"{rarity_color}{rarity.upper()}{RESET}"
                f"{BOLD} - VARIANT: LARGE{RESET}"
            )
        )
    )

    print()
    print(text_box("b"))

def large_lost_display(state, fish, debug):
    rarity = fish["rarity"]
    rarity_color = RARITY_COLORS[rarity]

    print(
        f"Your "
        f"{BOLD}LARGE {fish['name'].upper()}{RESET}"
        f" - ({rarity_color}{rarity.upper()}{RESET}) "
        f"escaped..."
    )

FIRE_COLORS = [
    hex_color("#FFD54A"),  # yellow
    hex_color("#FFB300"),  # golden yellow
    hex_color("#FF9D00"),  # orange
    hex_color("#FF8000"),  # bright orange
    hex_color("#FF5A00"),  # orange-red
    hex_color("#FF3D00"),  # red-orange
    hex_color("#FF1E00"),  # red
    hex_color("#D50000"),  # deep red
]


def burning_display(state, fish, debug):
    message = random.choice(CATCH_DIALOGUES["burning"])

    animated_variant_display(
        state,
        fish,
        debug,
        message=message,
        name_text="🔥 Burning {name} 🔥",
        variant_text="🔥 Burning 🔥",
        colors=FIRE_COLORS,
        duration=1.2,
        speed=0.15,
    )


def burning_lost_display(state, fish, debug):
    rarity = fish["rarity"]
    rarity_color = RARITY_COLORS[rarity]

    #name = f"🔥 {FIRE_COLORS[0]}Burning {fish['name']}{RESET}"
    name = gradient_text(
        f"🔥 Burning {fish['name']}",
        FIRE_COLORS,
    )

    print(
        f"Your {name}"
        f" - ({rarity_color}{rarity.capitalize()}{RESET}) "
        f"escaped..."
    )

URANIUM_COLORS = [
    hex_color("#66FF33"),
    hex_color("#00FF66"),
    hex_color("#00E676"),
    hex_color("#00C853"),
    hex_color("#00A83B"),
]


def uranium_display(state, fish, debug):
    message = random.choice(CATCH_DIALOGUES["uranium"])

    animated_variant_display(
        state,
        fish,
        debug,
        message=message,
        name_text="⚠️ Radioactive {name} ⚠️",
        variant_text="Uranium",
        colors=URANIUM_COLORS,
        duration=1.2,
        speed=0.15,
        uniform=False,
    )

def uranium_lost_display(state, fish, debug):
    rarity = fish["rarity"]
    rarity_color = RARITY_COLORS[rarity]

    name = gradient_text(
        f"⚠️ Radioactive {fish['name']}",
        URANIUM_COLORS,
    )

    print(
        f"A {name}"
        f" - ({rarity_color}{rarity.capitalize()}{RESET}) "
        f"had activated its shiniest, distracted you "
        f"and swam away..."
    )

SHINY_COLORS = [
    hex_color("#0000FF"),  
    hex_color("#0080FF"),  
    hex_color("#00FFFF"),  
    hex_color("#00FF80"),  
    hex_color("#00FF00"),  
    hex_color("#66FF00"),  
    hex_color("#BFFF00"),  
    hex_color("#FFFF00"),  
    hex_color("#FFB300"),  
    hex_color("#FF8000"),  
    hex_color("#FF4D00"),  
    hex_color("#FF0000"),  
    hex_color("#FF0080"),
    hex_color("#FF00FF"),  
    hex_color("#BF00FF"),  
    hex_color("#8000FF"),  
    hex_color("#4D00FF"),  
]
def shiny_display(state, fish, debug):
    message = random.choice(CATCH_DIALOGUES["shiny"])

    animated_variant_display(
        state,
        fish,
        debug,
        message=message,
        name_text="💫 Shiny {name} 💫",
        variant_text="Shiny",
        colors=SHINY_COLORS,
        duration=2,
        speed=0.05,
    )
    
def shiny_lost_display(state, fish, debug):
    rarity = fish["rarity"]
    rarity_color = RARITY_COLORS[rarity]

    name = gradient_text(
        f"💫 Shiny {fish['name']}",
        SHINY_COLORS,
    )

    print(
        f"Your {name}"
        f" - ({rarity_color}{rarity.capitalize()}{RESET}) "
        f"escaped into the darkness..."
    )

SHADOW_COLORS = [ 
    hex_color("#050505"), 
    hex_color("#0A0A0A"), 
    hex_color("#101010"), 
    hex_color("#181818"), 
    hex_color("#181818"), 
    hex_color("#101010"), 
    hex_color("#0A0A0A"), 
]
def shadow_display(state, fish, debug):
    message = random.choice(CATCH_DIALOGUES["shadow"])

    animated_variant_display(
        state,
        fish,
        debug,
        message=message,
        name_text="👻 Shadow {name} 👻",
        variant_text="Shadow",
        colors=SHADOW_COLORS,
        duration=2,
        speed=0.05,
    )

def shadow_lost_display(state, fish, debug):
    rarity = fish["rarity"]
    rarity_color = RARITY_COLORS[rarity]

    name = gradient_text(
        f"👻 Shadow {fish['name']}",
        SHADOW_COLORS,
    )

    print(
        f"Your {name}"
        f" - ({rarity_color}{rarity.capitalize()}{RESET}) "
        f"escaped into the darkness..."
    )

'''
font mapping
'''
SMALL_ALPHABET = {
    "a": "ᵃ",
    "b": "ᵇ",
    "c": "ᶜ",
    "d": "ᵈ",
    "e": "ᵉ",
    "f": "ᶠ",
    "g": "ᵍ",
    "h": "ʰ",
    "i": "ⁱ",
    "j": "ʲ",
    "k": "ᵏ",
    "l": "ˡ",
    "m": "ᵐ",
    "n": "ⁿ",
    "o": "ᵒ",
    "p": "ᵖ",
    "q": "q",
    "r": "ʳ",
    "s": "ˢ",
    "t": "ᵗ",
    "u": "ᵘ",
    "v": "ᵛ",
    "w": "ʷ",
    "x": "ˣ",
    "y": "ʸ",
    "z": "ᶻ",
}

def small_text(text):
    return "".join(
        SMALL_ALPHABET.get(char.lower(), char)
        for char in text
    )

VARIANT_CATCH_DISPLAYS = {
    "normal": normal_display,
    "baby": baby_display,
    "large": large_display,
    "burning": burning_display,
    "uranium": uranium_display,
    "shiny": shiny_display,
    "shadow": shadow_display,
}

VARIANT_LOST_DISPLAYS = {
    "normal": normal_lost_display,
    "baby": baby_lost_display,
    "large": large_lost_display,
    "burning": burning_lost_display,
    "uranium": uranium_lost_display,
    "shiny": shiny_lost_display,
    "shadow": shadow_lost_display,
}