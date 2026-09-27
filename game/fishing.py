import random

from game.data.fish import fish_list, variant_chances


def fish():

    # *Stage 1: Determine whether the player catches anything*
    luck = roll_luck()

    if luck > 0.75:
        return None

    # *Stage 2: Determine rarity*
    rarity = roll_rarity()

    possible_fish = [
        fish for fish in fish_list
        if fish["rarity"] == rarity
    ]

    caught_fish = random.choice(possible_fish)

    # *Stage 3: Determine variant*
    variant = roll_variant()

    caught_fish = {
        **caught_fish,
        "variant": variant,
    }

    return caught_fish


'''
LUCK
'''


def roll_luck():
    return random.random()


def roll_rarity():

    luck = roll_luck()

    if luck <= 0.60:
        return "common"

    elif luck <= 0.85:
        return "uncommon"

    elif luck <= 0.97:
        return "rare"

    elif luck <= 0.99:
        return "epic"

    else:
        return "legendary"


def roll_variant():

    luck = roll_luck()

    cumulative = 0

    for variant, chance in variant_chances.items():
        cumulative += chance

        if luck <= cumulative:
            return variant