#game/data/rods.py
RODS = {
    "beginner": {
        "label": "Beginner Rod 🎣",
        "style": None,

        "luck": {
            "catch": 0.00,
            "money": 0.00,
        },

        "rarity": {
            "common": 0.75,
            "uncommon": 0.20,
            "rare": 0.05,
            "epic": 0.00,
            "legendary": 0.00,
        },

        "variants": {
            "normal": 0.95,
            "baby": 0.025,
            "large": 0.012,
            "burning": 0.007,
            "uranium": 0.004,
            "shiny": 0.0015,
            "shadow": 0.0005,
        },
    },


    "advanced": {
        "label": "Advance Rod 🎣",
        "style": None,

        "luck": {
            "catch": 0.50,
            "money": 0.01,
        },

        "rarity": {
            "common": 0.65,
            "uncommon": 0.13,
            "rare": 0.12,
            "epic": 0.10,
            "legendary": 0.05,
        },

        "variants": {
            "normal": 0.95,
            "baby": 0.025,
            "large": 0.012,
            "burning": 0.007,
            "uranium": 0.004,
            "shiny": 0.0015,
            "shadow": 0.0005,
        },
    },

    "debug": {
        "label": "Debug Rod 🎣",
        "style": "debug",

        "luck": {
            "catch": 0.8,
            "money": 0.01,
        },

        "rarity": {
            "common": 0.00,
            "uncommon": 0.00,
            "rare": 0.50,
            "epic": 0.30,
            "legendary": 0.20,
        },

        "variants": {
            "normal": 0.00,
            "baby": 0.00,
            "large": 0.00,
            "burning": 0.0,
            "uranium": 0.5,
            "shiny": 0.3,
            "shadow": 0.2,
        },
    },
}