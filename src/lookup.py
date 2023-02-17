items = {
    # ---- Weapons ----
    "Stick": {
        "Name": "Stick",
        "Description": "A pointy stick, not the greatest weapon of all time",
        "Category": "weapon",
        "Attack": 1
    },

    # ---- Armor ----
    "Fabric": {
        "Name": "Fabric",
        "Description": "Thin fabric cloth, poor protection against any weapon",
        "Category": "armor",
        "Defense": 1
    },

    # ---- Misc. ----
    "Apple": {
        "Name": "Apple",
        "Description": "An apple a day keeps the eldritch horrors away",
        "Category": "consumable",
        "Health": 2
    }
}

# Lvl up formula: (Last Level + Next Level) * 20 * Current Skill Multiplier
levelInfo = {
    0: {
        "level": 0,
        "requiredExp": 0,
        "health": 20,
        "skillMultiplier": 1
    },
    1: {
        "level": 1,
        "requiredExp": 63,
        "health": 22,
        "skillMultiplier": 1.05
    },
    2: {
        "level": 2,
        "requiredExp": 173,
        "health": 25,
        "skillMultiplier": 1.1
    },
    3: {
        "level": 3,
        "requiredExp": 334,
        "health": 29,
        "skillMultiplier": 1.15
    },
    4: {
        "level": 4,
        "requiredExp": 550,
        "health": 34,
        "skillMultiplier": 1.2
    },
    5: {
        "level": 5,
        "requiredExp": 825,
        "health": 40,
        "skillMultiplier": 1.25
    },
    6: {
        "level": 6,
        "requiredExp": 1163,
        "health": 47,
        "skillMultiplier": 1.3
    },
    7: {
        "level": 7,
        "requiredExp": 1568,
        "health": 55,
        "skillMultiplier": 1.35
    },
    8: {
        "level": 8,
        "requiredExp": 2044,
        "health": 64,
        "skillMultiplier": 1.4
    },
    9: {
        "level": 9,
        "requiredExp": 2595,
        "health": 74,
        "skillMultiplier": 1.45
    },
    10: {
        "level": 10,
        "requiredExp": 3225,
        "health": 85,
        "skillMultiplier": 1.5
    },
    11: {
        "level": 11,
        "requiredExp": 3938,
        "health": 97,
        "skillMultiplier": 1.55
    },
    12: {
        "level": 12,
        "requiredExp": 4738,
        "health": 110,
        "skillMultiplier": 1.6
    },
    13: {
        "level": 13,
        "requiredExp": 5629,
        "health": 124,
        "skillMultiplier": 1.65
    },
    14: {
        "level": 14,
        "requiredExp": 6615,
        "health": 139,
        "skillMultiplier": 1.7
    },
    15: {
        "level": 15,
        "requiredExp": 7700,
        "health": 155,
        "skillMultiplier": 1.75
    },
    16: {
        "level": 16,
        "requiredExp": 8888,
        "health": 172,
        "skillMultiplier": 1.8
    },
    17: {
        "level": 17,
        "requiredExp": 10183,
        "health": 190,
        "skillMultiplier": 1.85
    },
    18: {
        "level": 18,
        "requiredExp": 11589,
        "health": 209,
        "skillMultiplier": 1.9
    },
    19: {
        "level": 19,
        "requiredExp": 13110,
        "health": 229,
        "skillMultiplier": 1.95
    },
    20: {
        "level": 20,
        "requiredExp": 14750,
        "health": 250,
        "skillMultiplier": 2
    }
}