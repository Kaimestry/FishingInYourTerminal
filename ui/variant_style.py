#ui/variant_style.py

from ui.style import *

'''
TEMPLATE
'''
def animated_variant_display(
    fish,
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

    animate_frame(
        build_frame,
        duration=duration,
        speed=speed
    )

    clear_terminal()
    print(build_frame(0))

'''
STYLING
'''
def normal_display(fish):
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

BABY_COLOR = hex_color("#E9B3FF")


def baby_display(fish):
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

BOLD = "\033[1m"


def large_display(fish):
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

FIRE_COLORS = [
    hex_color("#FF9D00"),
    hex_color("#FF5A00"),
    hex_color("#FF1E00"),
]


def burning_display(fish):
    animated_variant_display(
        fish,
        message="Your fish were caught in a Magma Stream",
        name_text="🔥 Burning {name} 🔥",
        variant_text="🔥 Burning 🔥",
        colors=FIRE_COLORS,
        duration=1.2,
        speed=0.15,
    )

URANIUM_COLORS = [
    hex_color("#7CFF4F"),
    hex_color("#00FF66"),
    hex_color("#00C853"),
    hex_color("#087F23"),
]


def uranium_display(fish):
    animated_variant_display(
        fish,
        message="Your fish might have escaped a Science lab",
        name_text="⚠️ Radioactive {name} ⚠️",
        variant_text="Uranium",
        colors=URANIUM_COLORS,
        duration=1.2,
        speed=0.08,
        uniform=True,
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
def shiny_display(fish):
    animated_variant_display(
        fish,
        message="Your fish might have escaped a Science lab",
        name_text="💫 Shiny {name} 💫",
        variant_text="Shiny",
        colors=SHINY_COLORS,
        duration=2,
        speed=0.05,
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
def shadow_display(fish):
    animated_variant_display(
        fish,
        message="Your fish befriended the dark side",
        name_text="👻 Shadow {name} 👻",
        variant_text="Shadow",
        colors=SHADOW_COLORS,
        duration=2,
        speed=0.05,
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