from cmu_graphics import rgb

import random

import data
import media

# universal attributes
target_destination = None

floor_media = {
    "crypt": {
        "straight_hallway": media.crypt_straight_hallway_images,
        "right_hallway": media.crypt_right_hallway_images,
        "left_hallway": media.crypt_left_hallway_images,
        "two_way_hallway": media.crypt_two_way_hallway_images,
        "three_way_hallway": media.crypt_three_way_hallway_images,
        "event": media.crypt_event_images,
        "shop": media.crypt_shop_images
    }
}

scene_mapper = { # points to the correct screen based off the target destination
    "crypt": "floor"
}

# title flames
flames = []

cyan = (0, 255, 255)
navy = (0, 0, 128)

def get_flame_color(flame_timer):
    r = cyan[0] + ((navy[0] - cyan[0]) * abs(flame_timer))
    g = cyan[1] + ((navy[1] - cyan[1]) * abs(flame_timer))
    b = cyan[2] + ((navy[2] - cyan[2]) * abs(flame_timer))
    color = rgb(r, g, b)

    return color

# title movement
x, y = data.top_left_xy
augmented_x = x + 100
augmented_y = y
direction_bit = 1

# title opacity
title_transitioning = False
title_opacity = 100

# main opacity
main_initialized = False
main_transitioning = False
main_opacity = 0
augmented_opacity = 100

# floor opacity
floor_initialized = False
floor_transitioning = False
floor_opacity = 0

# map opacity
map_initialized = False
map_transitioning = False
map_opacity = 0

# map offset
map_offset_x = 80
map_offset_y = 120