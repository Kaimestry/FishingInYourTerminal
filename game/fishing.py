import random

from game.data.fish import fish_list
from game.data.rods import RODS
from game.data.baits import BAITS
from game.data.prices import RARITY_PRICES, VARIANT_PRICE_BONUS


def fish(state):

    # Stage 1: Determine whether the player catches anything
    caught = roll_catch(state)

    # Stage 2: Determine rarity
    rarity = roll_rarity(state)

    # Stage 3: Determine variant
    variant = roll_variant(state)

    # Stage 4: Determine money
    money = roll_money(state, rarity, variant)

    possible_fish = [
        fish for fish in fish_list
        if fish["rarity"] == rarity
    ]

    caught_fish = random.choice(possible_fish)

    return {
        **caught_fish,
        "variant": variant,
        "money": money,
        "caught": caught,
    }

def get_bait(state):
    bait_id = state.equipped["bait"]

    if bait_id is None:
        return None

    return BAITS[bait_id]

def get_luck(state, luck_type):
    rod = RODS[state.equipped["rod"]]
    bait = get_bait(state)

    rod_luck = rod["luck"][luck_type]
    bait_luck = bait["luck"][luck_type] if bait else 0

    return rod_luck + bait_luck

def roll_catch(state):
    rod = state.equipped["rod"]
    bait = get_bait(state)

    rod_catch = RODS[rod]["luck"]["catch"]
    bait_catch = bait["luck"]["catch"] if bait else 0

    total = rod_catch + bait_catch

    roll = random.random()

    return roll <= total


def roll_rarity(state):
    rod = RODS[state.equipped["rod"]]["rarity"]
    bait = get_bait(state)

    roll = random.random()
    cumulative = 0

    for rarity in rod:
        rod_chance = rod[rarity]
        bait_chance = bait["rarity"][rarity] if bait else 0

        total = rod_chance + bait_chance
        cumulative += total

        if roll <= cumulative:
            return rarity


def roll_variant(state):
    rod = RODS[state.equipped["rod"]]["variants"]
    bait = get_bait(state)

    roll = random.random()
    cumulative = 0

    for variant in rod:
        rod_chance = rod[variant]
        bait_chance = bait["variants"][variant] if bait else 0

        total = rod_chance + bait_chance
        cumulative += total

        if roll <= cumulative:
            return variant


def roll_money(state, rarity, variant):
    money_luck = get_luck(state, "money")

    minimum, maximum = RARITY_PRICES[rarity]

    base_price = random.randint(minimum, maximum)

    variant_bonus = VARIANT_PRICE_BONUS[variant]

    final_price = base_price
    final_price *= 1 + variant_bonus
    final_price *= 1 + money_luck

    return round(final_price)