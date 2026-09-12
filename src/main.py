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

    app.title_scene = scene.Scene(100)
    app.main_scene = scene.Scene(0)
    app.floor_scene = scene.Scene(0)
    app.map_scene = scene.Scene(0)
    app.shop_scene = scene.Scene(0)
    app.inventory_scene = scene.Scene(0)

    app.hud_scene = scene.Scene(100) # needs fading mechanics
    app.combat_scene = scene.Scene(0)
    app.cards_scene = scene.Scene(0)

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
    drawRect(0, 0, app.screen_width, app.screen_height, fill = gradient("black", "navy"), opacity = app.title_scene.opacity) # background

    for flame in scene.flames:
        drawRect(flame["x"], flame["y"], 10, 25, fill = flame["color"], opacity = app.title_scene.opacity) # flame vfx

    drawImage(media.title_background_image, scene.augmented_x, scene.augmented_y, opacity = app.title_scene.opacity) # title text

def start_onStep(app):
    #media.title_screen_soundtrack.play()

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

    transition(app, "title", scene.scene_mapper[scene.target_destination])

def start_onKeyPress(app, key):
    if not app.title_scene.transitioning:
        scene.target_destination = "main"
        app.title_scene.transitioning = True

def start_onMousePress(app, mouse_x, mouse_y):
    if not app.title_scene.transitioning:
        scene.target_destination = "main"
        app.title_scene.transitioning = True



def main_redrawAll(app):
    drawImage(media.home_room_background_image, app.top_left_x, app.top_left_y, opacity = app.main_scene.opacity) # main background
    drawImage(media.crypt_icon_image, app.midpoint_x / 4, app.midpoint_y / 4, opacity = app.main_scene.opacity) # crypt button
    drawImage(media.settings_icon_image, app.bottom_left_x, app.bottom_left_y - 120, opacity = app.main_scene.opacity) # settings button

def main_onStep(app):
    transition(app, "main", scene.scene_mapper[scene.target_destination])

def main_onKeyPress(app, key):
    pass

def main_onMousePress(app, mouse_x, mouse_y):
    if app.main_scene.opacity == 100:
        if hits_shape(mouse_x, mouse_y, app.midpoint_x / 4, 400, app.midpoint_y / 4, 320): # crypt button
            scene.target_destination = "crypt"
            app.main_scene.transitioning = True
            app.floor = floor.Floor(scene.target_destination)



def floor_redrawAll(app):
    for tile in app.floor.tiles:
        if app.floor.player_position[0] in range(tile["column"] * app.floor.tile_size, (tile["column"] * app.floor.tile_size) + app.floor.tile_size) and app.floor.player_position[1] in range(tile["row"] * app.floor.tile_size, (tile["row"] * app.floor.tile_size) + app.floor.tile_size):
            drawImage(tile["sprite"], app.top_left_x, app.top_left_y, opacity = app.floor_scene.opacity) # background

    # based off app.floor.current_event # like quest will result in a 40 opacity black film quest dim - shop overlay - boss ui - origin exit
    match app.floor.current_event:
        case "quest":
            drawRect(app.top_left_x, app.top_left_y, app.screen_width, app.screen_height, fill = "black", opacity = 40)
        case "shop":
            drawLabel("Money", app.top_left_x + 100, app.top_left_y + 120, size = 40, fill = "gold", opacity = app.floor_scene.opacity)
        case "origin":
            drawLabel("Exit", app.midpoint_x, app.midpoint_y + (0.25 * app.screen_height), size = 40, fill = "red", opacity = app.floor_scene.opacity)

    # hud ui
    drawRect(app.top_left_x, app.top_left_y, 400, 240, fill = "sienna", opacity = 50) # hud background - # add config for size and for labels/bars

    drawLabel(app.player.data["health"], app.top_left_x + 80, app.top_left_y + 70, size = 50, fill = "red", opacity = app.hud_scene.opacity)
    drawLabel(app.player.data["mana"], app.top_left_x + 200, app.top_left_y + 70, size = 50, fill = "blue", opacity = app.hud_scene.opacity)
    drawLabel(app.player.data["stamina"], app.top_left_x + 320, app.top_left_y + 70, size = 50, fill = "gold", opacity = app.hud_scene.opacity)

    drawLabel(app.player.data["health_recovery"], app.top_left_x + 80, app.top_left_y + 170, size = 50, fill = "hotPink", opacity = app.hud_scene.opacity)
    drawLabel(app.player.data["mana_recovery"], app.top_left_x + 200, app.top_left_y + 170, size = 50, fill = "cyan", opacity = app.hud_scene.opacity)
    drawLabel(app.player.data["stamina_recovery"], app.top_left_x + 320, app.top_left_y + 170, size = 50, fill = "yellow", opacity = app.hud_scene.opacity)

    # combat ui and enemies
    if app.battle != None:
        for i, enemy in enumerate(app.battle.active_enemies):
            drawRect(i * 200 + 750, app.midpoint_y - 350, (enemy.data["health"] * 4) + 1, 40, fill = 'crimson', border = 'black', borderWidth = 2, opacity = app.combat_scene.opacity) # how to decide the coordinates of enemies? lets do based off list index
            drawImage(enemy.sprite, ((i * 200) + 750) + enemy.data["offset"][0], (app.midpoint_y - 150) + enemy.data["offset"][1], opacity = app.combat_scene.opacity)

    # cards ui
    for i, card in enumerate(app.player.data["hand"]):
        drawImage(data.card_data[card]["sprite"], (app.midpoint_x / 2) + (i * 80), app.bottom_left_y - 200, opacity = app.cards_scene.opacity)

def floor_onStep(app):
    transition(app, "floor", scene.scene_mapper[scene.target_destination])

    if app.battle != None:
        app.combat_scene.opacity = 100
    else:
        app.combat_scene.opacity = 0

def floor_onKeyPress(app, key):
    if key == "m" and app.floor_scene.initialized:
        scene.target_destination = "map"
        app.floor_scene.transitioning = True

def floor_onMousePress(app, mouse_x, mouse_y):
    pass



def map_redrawAll(app):
    drawRect(app.top_left_x, app.top_left_y, app.screen_width, app.screen_height, fill = gradient("black", "darkGreen","forestGreen","darkGreen","black",start="top"), opacity = app.map_scene.opacity) # background

    for tile in app.floor.tiles:
        x = tile["column"] * app.floor.tile_size + scene.map_offset_x
        y = tile["row"] * app.floor.tile_size + scene.map_offset_y
        if not tile["visited"] and tile["icon"] == None:
            drawRect(x, y, app.floor.tile_size, app.floor.tile_size, fill = "grey", border = "silver", opacity = app.map_scene.opacity) # map tiles
        elif tile["visited"] and tile["icon"] == None:
            drawRect(x, y, app.floor.tile_size, app.floor.tile_size, fill = "orange", border = "silver", opacity = app.map_scene.opacity) # visited tiles # it looks like tiles can still draw over pre existing ones. do a tile merge system where if they do share the same coordinates, they combined data.
        elif tile["icon"] != None and not tile["visited"]:
            drawRect(x, y, app.floor.tile_size, app.floor.tile_size, fill = "grey", border = "silver", opacity = app.map_scene.opacity)
            drawImage(tile["icon"], x, y, opacity = app.map_scene.opacity) # icons
        elif tile["icon"] != None and tile["visited"]:
            drawRect(x, y, app.floor.tile_size, app.floor.tile_size, fill = "pink", border = "silver", opacity = app.map_scene.opacity)
            drawImage(tile["icon"], x, y, opacity = app.map_scene.opacity) # icons

    drawRect((app.floor.player_position[0] + (app.floor.tile_size / 2) - (app.floor.player_width / 2)) + scene.map_offset_x, (app.floor.player_position[1] + (app.floor.tile_size / 2) - (app.floor.player_height / 2)) + scene.map_offset_y, app.floor.player_width, app.floor.player_height, fill = "white", opacity = app.map_scene.opacity) # player

def map_onStep(app):
    transition(app, "map", scene.scene_mapper[scene.target_destination])

def map_onKeyPress(app, key):
    if key == "m" and app.map_scene.initialized:
        scene.target_destination = "floor"
        app.map_scene.transitioning = True
    if app.battle == None:
        app.floor.player_position = app.floor.move_tile(app.floor.player_position, key)
        app.floor.current_event = app.floor.event_handler(app.floor.player_position)
        app.battle = app.floor.tile_update(app.floor.player_position, app.player)

def map_onMousePress(app, mouse_x, mouse_y):
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

def transition(app, current_location, target_location):
    if target_location != None:
        current = getattr(app, current_location + "_scene")
        target = getattr(app, target_location)

        if not current.initialized and not current.transitioning: # initialize current
            current.opacity += 5
        if current.opacity == 100:
            current.initialized = True

        if current.transitioning and current.opacity > 0: # transitioning off current
            current.opacity -= 5
        elif current.transitioning:
            current.transitioning = False
            current.initialized = False
            screen = target_location.replace("_scene", "")
            setActiveScreen(screen)

        if not current.transitioning and current.opacity == 0:
            if not target.initialized and not target.transitioning: # initialize target
                target.opacity += 5
            if target.opacity == 100:
                target.initialized = True

def draw_hud_ui(app):
    pass

def draw_combat_ui(app):
    pass

def draw_player_ui(app):
    pass

def draw_shop_ui(app):
    pass

main()

### planned
# key hold functionality for the map