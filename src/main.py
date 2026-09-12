from cmu_graphics import *

import random
import time

import combat
import data
import enemies
import floor
import media
import player
import scene

def onAppStart(app):
    app.background = "black"
    app.player = player.Player()
    app.floor = None
    app.battle = None

    app.top_left_x, app.top_left_y = data.top_left_xy
    app.top_right_x, app.top_right_y = data.top_right_xy
    app.bottom_left_x, app.bottom_left_y = data.bottom_left_xy
    app.bottom_right_x, app.bottom_right_y = data.bottom_right_xy
    app.midpoint_x, app.midpoint_y = data.midpoint_xy

    app.screen_width = 1920
    app.screen_height = 1080

    app.current_screen = "start"

    for i in range(0,160):
        scene.flames.append({"x": random.randint(0, app.screen_width), "y": random.randint(1180, 2400), "speed": random.randint(3, 5), "color": None, "flame_timer": 0, "direction_bit": 1}) # flame vfx



def start_redrawAll(app):
    drawImage(media.home_room_background_image, app.top_left_x, app.top_left_y)

    drawRect(0, 0, app.screen_width, app.screen_height, fill = gradient("black", "navy"), opacity = scene.title_opacity) # background

    for flame in scene.flames:
        drawRect(flame["x"], flame["y"], 10, 25, fill = flame["color"], opacity = scene.title_opacity) # flame vfx

    drawImage(media.title_background_image, scene.augmented_x, scene.augmented_y, opacity = scene.title_opacity) # title text

def start_onStep(app):
    media.title_screen_soundtrack.play()

    for flame in scene.flames:
        flame["y"] -= flame["speed"]
        flame["flame_timer"] += random.uniform(0.01, 0.15) * flame["direction_bit"] # flame vfx motion
        if flame["flame_timer"] >= 1:
            flame["flame_timer"] = 1
            flame["direction_bit"] *= -1
        elif flame["flame_timer"] <= -1:
            flame["flame_timer"] = -1
            flame["direction_bit"] *= -1
        flame["color"] = scene.get_flame_color(flame["flame_timer"])
        if flame["y"] < -25:
            flame["y"] = random.randint(app.screen_height, 2000)

    if scene.augmented_y <= -20: # title text motion
        scene.direction_bit *= -1
    elif scene.augmented_y >= 30:
        scene.direction_bit *= -1
    scene.augmented_y += (0.6 * scene.direction_bit)

    if scene.title_transitioning and scene.title_opacity > 0:
        scene.title_opacity -= 2.5
    if scene.title_opacity == 0:
        setActiveScreen("main")

def start_onKeyPress(app, key):
    if not scene.title_transitioning:
        scene.title_transitioning = True

def start_onMousePress(app, mouse_x, mouse_y):
    if not scene.title_transitioning:
        scene.title_transitioning = True



def main_redrawAll(app):
    drawImage(media.home_room_background_image, app.top_left_x, app.top_left_y, opacity = scene.augmented_opacity) # main background
    drawImage(media.crypt_icon_image, app.midpoint_x / 4, app.midpoint_y / 4, opacity = scene.main_opacity) # crypt button
    drawImage(media.settings_icon_image, app.bottom_left_x, app.bottom_left_y - 120, opacity = scene.main_opacity) # settings button

def main_onStep(app):
    if scene.main_opacity < 100 and not scene.main_initialized:
        scene.main_opacity += 5
    else:
        scene.main_initialized = True
    if scene.main_transitioning and scene.augmented_opacity > 0: # opacity handler
        scene.augmented_opacity -= 5
        scene.main_opacity -= 5
    if scene.augmented_opacity == 0:
        app.floor = floor.Floor(scene.target_destination)
        scene.main_initialized = False
        scene.main_transitioning = False
        setActiveScreen(scene.scene_mapper[scene.target_destination])

def main_onKeyPress(app, key):
    pass

def main_onMousePress(app, mouse_x, mouse_y):
    if scene.main_opacity == 100:
        if hits_shape(mouse_x, mouse_y, app.midpoint_x / 4, 400, app.midpoint_y / 4, 320): # crypt button
            scene.main_transitioning = True
            scene.target_destination = "crypt"



def floor_redrawAll(app):
    for tile in app.floor.tiles:
        if app.floor.player_position[0] in range(tile["column"] * app.floor.tile_size, (tile["column"] * app.floor.tile_size) + app.floor.tile_size) and app.floor.player_position[1] in range(tile["row"] * app.floor.tile_size, (tile["row"] * app.floor.tile_size) + app.floor.tile_size):
            drawImage(tile["sprite"], app.top_left_x, app.top_left_y, opacity = scene.floor_opacity) # background

    # based off app.floor.current_event # like quest will result in a 40 opacity black film quest dim - shop overlay - boss ui - origin exit
    match app.floor.current_event:
        case "quest":
            drawRect(app.top_left_x, app.top_left_y, app.screen_width, app.screen_height, fill = "black", opacity = 40)
        case "shop":
            drawLabel("Money", app.midpoint_x, app.midpoint_y + (0.25 * app.screen_height), size = 40, fill = "gold", opacity = scene.floor_opacity)
        case "origin":
            drawLabel("Exit", app.midpoint_x, app.midpoint_y + (0.25 * app.screen_height), size = 40, fill = "red", opacity = scene.floor_opacity)


def floor_onStep(app):
    if scene.floor_opacity < 100 and not scene.floor_initialized: # opacity handler
        scene.floor_opacity += 5
    else:
        scene.floor_initialized = True

    if scene.floor_transitioning and scene.floor_opacity > 0:
        scene.floor_opacity -= 5
    if scene.floor_opacity == 0:
        scene.floor_initialized = False
        scene.floor_transitioning = False
        setActiveScreen("map")

def floor_onKeyPress(app, key):
    if key == "m" and scene.floor_initialized:
        scene.floor_transitioning = True

def floor_onMousePress(app, mouse_x, mouse_y):
    pass



def map_redrawAll(app):
    drawRect(app.top_left_x, app.top_left_y, app.screen_width, app.screen_height, fill = gradient("black", "darkGreen","forestGreen","darkGreen","black",start="top"), opacity = scene.map_opacity) # background

    for tile in app.floor.tiles:
        x = tile["column"] * app.floor.tile_size + scene.map_offset_x
        y = tile["row"] * app.floor.tile_size + scene.map_offset_y
        if not tile["visited"] and tile["icon"] == None:
            drawRect(x, y, app.floor.tile_size, app.floor.tile_size, fill = "grey", border = "silver", opacity = scene.map_opacity) # map tiles
        elif tile["visited"] and tile["icon"] == None:
            drawRect(x, y, app.floor.tile_size, app.floor.tile_size, fill = "orange", border = "silver", opacity = scene.map_opacity) # visited tiles # it looks like tiles can still draw over pre existing ones. do a tile merge system where if they do share the same coordinates, they combined data.
        elif tile["icon"] != None and not tile["visited"]:
            drawRect(x, y, app.floor.tile_size, app.floor.tile_size, fill = "grey", border = "silver", opacity = scene.map_opacity)
            drawImage(tile["icon"], x, y, opacity = scene.map_opacity) # icons
        elif tile["icon"] != None and tile["visited"]:
            drawRect(x, y, app.floor.tile_size, app.floor.tile_size, fill = "pink", border = "silver", opacity = scene.map_opacity)
            drawImage(tile["icon"], x, y, opacity = scene.map_opacity) # icons

    drawRect((app.floor.player_position[0] + (app.floor.tile_size / 2) - (app.floor.player_width / 2)) + scene.map_offset_x, (app.floor.player_position[1] + (app.floor.tile_size / 2) - (app.floor.player_height / 2)) + scene.map_offset_y, app.floor.player_width, app.floor.player_height, fill = "white") # player

def map_onStep(app):
    if scene.map_opacity < 100 and not scene.map_initialized: # opacity handler
        scene.map_opacity += 5
    else:
        scene.map_initialized = True

    if scene.map_transitioning and scene.map_opacity > 0:
        scene.map_opacity -= 5
    if scene.map_opacity == 0:
        scene.map_initialized = False
        scene.map_transitioning = False
        setActiveScreen("floor")

def map_onKeyPress(app, key):
    if key == "m" and scene.map_initialized:
        scene.map_transitioning = True
    if app.battle == None:
        app.floor.player_position = app.floor.move_tile(app.floor.player_position, key)
        app.floor.current_event = app.floor.event_handler(app.floor.player_position)
        app.floor.tile_update(app.floor.player_position)

def map_onMousePress(app, mouse_x, mouse_y):
    pass

def shop_redrawAll(app):
    pass
def shop_onStep(app):
    pass
def shop_onKeyPress(app, key):
    pass
def shop_onMousePress(app, mouse_x, mouse_y):
    pass

def pause_redrawAll(app):
    pass
def pause_onStep(app):
    pass
def pause_onKeyPress(app, key):
    pass
def pause_onMousePress(app, mouse_x, mouse_y):
    pass

def gameover_redrawAll(app):
    pass
def gameover_onStep(app):
    pass
def gameover_onKeyPress(app, key):
    pass
def gameover_onMousePress(app, mouse_x, mouse_y):
    pass

def main():
    runAppWithScreens(initialScreen="start", width = 1920, height = 1080)

def hits_shape(mouse_x, mouse_y, starting_x, width, starting_y, height):
    if mouse_x in range(int(starting_x), int(starting_x) + width) and mouse_y in range(int(starting_y), int(starting_y) + height):
        return True

main()

### planned
# key hold functionality for the map