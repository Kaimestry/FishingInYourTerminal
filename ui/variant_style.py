#ui/variant_style.py

from ui.style import *

def normal_display(fish):
    color = RARITY_COLORS[fish["rarity"]]
    rarity = fish["rarity"].capitalize()

    print("You caught....")
    print()
    print(text_box("t"))
    print()
    print(
        text_box(
            "center",
            text=f"🎣 {color}{fish['name']} - {color}{rarity}{RESET} 🎣"
        )
    )
    print()
    print(text_box("b"))

def baby_display(fish):
    pink = hex_color("#e9b3ff")
    rarity = fish["rarity"]
    rarity_color = RARITY_COLORS[rarity]

    name = small_text(fish["name"])

    print("Your fish panicked and turned into a smaller version of itself")
    print()

    print(text_box("t"))
    print()

    print(
        text_box(
            "center",
            text=f"🍼 {rarity_color}{name}{RESET} 🍼"
        )
    )

    print(
        text_box(
            "center",
            text=        
            f"{small_text('Rarity:')} "
            f"{rarity_color}{small_text(rarity.capitalize())}{RESET}"
            f"{small_text(' - Variant:')} "
            f"{pink}{small_text('Baby')}{RESET}"
        )
    )

    print()

    print(text_box("b"))

BOLD = "\033[1m"
def large_display(fish):
    color = RARITY_COLORS[fish["rarity"]]
    rarity = fish["rarity"].upper()

    print("You caught....")
    print()

    print(text_box("t"))
    print()

    print(
        text_box(
            "center",
            text=f"{BOLD}{color}🎣 {fish['name'].upper()} 🎣{RESET}"
        )
    )
    print()
    print(
        text_box(
            "center",
            text=
            f"{BOLD}RARITY: {color}{rarity} - {RESET}"
            f"{BOLD}VARIETY: LARGE{RESET}"
        )
    )

    print()

    print(text_box("b"))

FIRE_COLORS = [
    hex_color("#FFF200"),
    hex_color("#FFD000"),
    hex_color("#FF9D00"),
    hex_color("#FF5A00"),
    hex_color("#FF1E00"),
]
def burning_display(fish):
    rarity = fish["rarity"]
    rarity_color = RARITY_COLORS[rarity]

    duration = 2
    speed = 0.1

    start = time.time()
    offset = 0

    while time.time() - start < duration:

        animated_name = changing_color(
            f"🔥 {fish['name']} 🔥",
            FIRE_COLORS,
            offset
        )

        animated_variant = changing_color(
            "🔥 Burning 🔥",
            FIRE_COLORS,
            offset
        )

        footer = (
            f"Rarity: "
            f"{rarity_color}{rarity.capitalize()}{RESET}"
            f" - Variant: "
            f"{animated_variant}"
        )

        frame = "\n".join([
            text_box("t"),
            "",
            text_box("center", text=animated_name),
            text_box("center", text=footer),
            "",
            text_box("b"),
        ])

        clear_terminal()
        print(frame)

        time.sleep(speed)
        offset += 1

    print()
            
def uranium_display(fish):
    pass

def shiny_display(fish):
    pass

def shadow_display(fish):
    pass

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