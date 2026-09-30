class GameState:
    def __init__(self):
        self.debug_mode = True
        self.money = 1000

        self.inventory = {
            "rods": ["debug, advanced"],
            "baits": {
                "basic": 5,
            },
            "fish": [
                    {'name': 'Minnow', 'rarity': 'common', 'variant': 'burning', 'money': 36, 'origin': 'caught'},
                    {'name': 'Cod', 'rarity': 'common', 'variant': 'baby', 'money': 25, 'origin': 'caught'},
                    {'name': 'Bluefish', 'rarity': 'uncommon', 'variant': 'normal', 'money': 95, 'origin': 'caught'},
                    {'name': 'Whitefish', 'rarity': 'common', 'variant': 'normal', 'money': 15, 'origin': 'caught'},
                    {'name': 'Guppy', 'rarity': 'common', 'variant': 'normal', 'money': 22, 'origin': 'caught'},
                    {'name': 'Zander', 'rarity': 'uncommon', 'variant': 'normal', 'money': 78, 'origin': 'caught'},
                    {'name': 'Giant Sea Bass', 'rarity': 'epic', 'variant': 'normal', 'money': 496, 'origin': 'caught'},
                    {'name': 'Salmon', 'rarity': 'common', 'variant': 'normal', 'money': 29, 'origin': 'caught'},
                    {'name': 'Mullet', 'rarity': 'common', 'variant': 'normal', 'money': 24, 'origin': 'caught'},
                    {'name': 'Smelt', 'rarity': 'common', 'variant': 'normal', 'money': 10, 'origin': 'caught'},
                    ],
            "tanks": [],
            "food": {},
            "buckets": [
                "basic",
            ],
        }

        self.equipped = {
            "rod": "advanced",
            "bait": None,
            "bucket": "basic",
        }

        self.fish_caught = 0
        self.variant_caught = {
            "normal": 0,
            "baby": 0,
            "large": 0,
            "burning": 0,
            "uranium": 0,
            "shiny": 0,
            "shadow": 0,
        }


class DebugState:
    def __init__(self):
        self.skip_animation = True
        self.cooldown_speed = 0
        self.skip_dialogue = True