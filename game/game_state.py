class GameState:
    def __init__(self):
        self.debug_mode = True
        self.money = 1000

        self.inventory = {
            "rods": ["debug"],
            "baits": {
                "basic": 5,
            },
            "fish": [],
            "tanks": [],
            "food": {},
            "buckets": [
                "basic",
            ],
        }

        self.equipped = {
            "rod": "debug",
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