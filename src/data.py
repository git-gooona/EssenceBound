import media

music = True
sound_effects = True
label_format = True
bar_format = False
paused = False

###
# Tempaltes - Cards
###

card_data = {
    "blazing_beam":{"damage":6, "effect": "burn", "effect_stack": 2, "cost": 4, "resource": "mana", "sprite": media.blazing_beam_image, "sound": media.blazing_beam_sound},
    "ember":{"damage":2, "effect": "burn", "effect_stack": 2, "cost": 2, "resource": "mana", "sprite": media.ember_image, "sound": media.ember_sound},
    "fireball":{"damage":4, "effect": "burn", "effect_stack": 4, "cost": 5, "resource": "mana", "sprite": media.fireball_image, "sound": media.fireball_sound},
    "fire_breath":{"damage":2, "effect": "burn", "effect_stack": 4, "cost": 3, "resource": "mana", "sprite": media.fire_breath_image, "sound": media.fire_breath_sound},
    "meteor_shower":{"damage":12, "effect": "burn", "effect_stack": 4, "cost": 8, "resource": "mana", "sprite": media.meteor_shower_image, "sound": media.meteor_shower_sound}
}

###
# Templates - Resources
###

resource_mapping_template = {
    "health": "health_recovery",
    "mana": "mana_recovery",
    "stamina": "stamina_recovery"
}

###
# Templates - Locations
###

crypt_template = {
    "name": "Crypt",
    "enemies": ["skeleton_archer", "skeleton_warrior"],
    "items": ["health_vial", "mana_vial", "stamina_vial", "ancient_tablets"],
    "quests": ["crypt_quest"],
    "paths": {"straight": media.crypt_straight_hallway_images, "right": media.crypt_right_hallway_images, "left": media.crypt_left_hallway_images, "two": media.crypt_two_way_hallway_images, "three": media.crypt_three_way_hallway_images},
    "events": media.crypt_event_images,
    "shops": media.crypt_shop_images,
    "gradient": ('black','darkGreen','forestGreen','darkGreen','black')
}

floor_templates = {
    "crypt": crypt_template
}

###
# Templates - Enemies
###

enemy_templates = {

"skeleton_archer": {
    "name": "Skeleton Archer",
    "sprite": media.skeleton_archer_image,
    "offset": (0, 0),
    "health": 100,
    "speed": 8,
    "skills": {
        "shoot": {
            "damage": 12,
            "weight": 0.8
            },
        "evade": {
            "evasion": 0.4,
            "weight": 0.2
            }
    }
},

"skeleton_warrior": {
    "name": "Skeleton Warrior",
    "sprite": media.skeleton_warrior_image,
    "offset": (0, 0),
    "health": 120,
    "speed": 6,
    "skills": {
        "slash": {
            "damage": 8,
            "weight": 0.8
            },
        "block": {
            "block": True,
            "weight": 0.2
            }
    }
}
}

###
# Templates - Items
###

###
# Templates - Quests
###

quests = {
    "crypt_quest": {
        "name": "Clear the Crypt",
        "description": "Defeat the Skeletons in the crypt and retrieve the Ancient Tablets.",
        "requirements": {
            "current_floor_elites": 0
        },
        "reward": {
            "experience": 100,
            "unlock": "Guild"
        }
    },
}

###
# Quest System
###

current_quests = {} # append quest dict with quest name as key and progress as value, check if requirements are met, if so, give reward and remove from current_quests

###
# Deck
###

starting_deck_template = ["blazing_beam", "ember", "fireball", "fire_breath", "meteor_shower"] * 4

###
# Maps
###

###
# Map Icons
###

map_icons = {
    "origin": media.ladder_icon,
    "event": None,
    "shop": media.shop_icon,
    "quest": media.quest_icon,
    "elite": media.elite_icon,
    "boss": media.boss_icon,
    "standard": None
}

###
# Foundational Coordinates
###

top_left_xy = 0, 0
top_right_xy = 1920, 0

bottom_left_xy = 0, 1080
bottom_right_xy = 1920, 1080

midpoint_xy = 960, 540