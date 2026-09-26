#fishing.py

import random
from game.data.fish import fish_list

def fish():
    # Stage 1: Determine whether the player catches anything
    luck = roll_luck()

    if luck > 0.75:
        return None

    # Stage 2: Determine rarity
    rarity = roll_rarity()

    # Find fish belonging to that rarity
    possible_fish = [
        fish for fish in fish_list
        if fish["rarity"] == rarity
    ]

    # Pick one fish from that rarity
    caught_fish = random.choice(possible_fish)

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


