from cmu_graphics import rgb

import data

# universal attributes
target_destination = None

scene_mapper = { # points to the correct screen based off the target destination
    "main": "main_scene",
    "map": "map_scene",
    "shop": "floor_scene",
    "floor": "floor_scene",
    "crypt": "floor_scene",
    None: None
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

class Scene:
    def __init__(self, opacity):
        self.initialized = False
        self.transitioning = False
        self.opacity = opacity

# map offsets
map_offset_x = 80
map_offset_y = 120

# combat