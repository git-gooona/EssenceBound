import random

import combat
import data

class Floor:
    def __init__(self, floor):
        self.floor = floor
        self.current_event = None
        self.enemies = data.floor_templates[floor]["enemies"].copy()
        self.events = data.floor_templates[floor]["events"].copy()
        self.items = data.floor_templates[floor]["items"].copy()
        self.quests = data.floor_templates[floor]["quests"].copy()

        self.rows = 10
        self.columns = 22
        self.total_tiles = (self.rows * self.columns) - random.randint(self.rows * self.columns // 4, self.rows * self.columns // 2)
        self.tile_size = 80
        self.tiles = []
        self.generator_stack = []

        self.player_width = self.tile_size / 4
        self.player_height = self.tile_size / 4

        starting_row = random.randrange(self.rows) # initialize a position to begin generation at
        starting_column = random.randrange(self.columns)
        self.tiles.append({"row": starting_row, "column": starting_column, "type": "origin", "visited": True, "icon": data.map_icons["origin"], "sprite": random.choice(data.floor_templates[floor]["paths"]["straight"])})
        self.player_position = (starting_column * self.tile_size, starting_row * self.tile_size) # coordinates of the player starting position

        row = starting_row
        column = starting_column

        self.possible_directions = [
            (-1, 0), # Left
            (1, 0), # Right
            (0, -1), # Up
            (0, 1)] # Down

        chosen_direction = (0, 0)

        possible_tile_types = {"event": {"weight": 6,"minimum": self.total_tiles // 20,"maximum": self.total_tiles // 10},
                                "shop": {"weight": 2,"minimum": self.total_tiles // self.total_tiles,"maximum": self.total_tiles // 25},
                                "quest": {"weight": 2,"minimum": self.total_tiles // self.total_tiles,"maximum": self.total_tiles // 25},
                                "elite": {"weight": 6,"minimum": self.total_tiles // 15,"maximum": self.total_tiles // 10},
                                "boss": {"weight": 2,"minimum": self.total_tiles // self.total_tiles,"maximum": self.total_tiles // self.total_tiles},
                                "standard": {"weight": 82,"minimum": None,"maximum": None}}

        while len(self.tiles) < self.total_tiles:
            valid_directions = []
            for direction in self.possible_directions: # checks for all valid directions
                test_row = row + direction[0]
                test_column = column + direction[1]

                if test_row >= 0 and test_row < self.rows: # boundry check
                    if test_column >= 0 and test_column < self.columns:

                        if not any(tile["row"] == test_row and tile["column"] == test_column for tile in self.tiles): # already generated tile check
                            valid_directions.append(direction) # populates valid directions

            self.generator_stack.append({"row": row, "column": column, "valid_directions": valid_directions, "previous_direction": chosen_direction}) # populates the generator_stack with all directions

            while not self.generator_stack[-1]["valid_directions"]: # incase there is no valid direction, pop the generator stack while removing the direction what would have resulted in that position
                self.generator_stack[-2]["valid_directions"].remove(self.generator_stack[-1]["previous_direction"])
                self.generator_stack.pop()
                row = self.generator_stack[-1]["row"] # returns the rows and columns to what they were before we got stuck
                column = self.generator_stack[-1]["column"]

            chosen_direction = random.choice(self.generator_stack[-1]["valid_directions"]) # chooses a random valid direction
            row += chosen_direction[0]
            column += chosen_direction[1]
            self.tiles.append({"row": row, "column": column, "type": "standard", "visited": False, "icon": None, "sprite": random.choice(data.floor_templates[floor]["paths"]["straight"])}) # populates self.tiles


        for tile_type, info in possible_tile_types.items(): # adds tile types into the generated tiles
            if tile_type != "standard":
                amount = random.randint(info["minimum"], info["maximum"]) # gets an amount of said tile type to add

                available_tiles = [] # stores tiles that can be changed
                for tile in self.tiles:
                    if tile["type"] == "standard":
                        if tile["row"] != starting_row and tile["column"] != starting_column: # if the tile isnt in the starting area we add it to the list of candidates
                            available_tiles.append(tile)
                for tile in random.sample(available_tiles, amount): # here we change an amount of tiles to the chosen types, which we randomly got earlier
                    tile["type"] = tile_type
                    tile["icon"] = data.map_icons[str(tile_type)]
                    if tile_type == "event":
                        tile["sprite"] = random.choice(data.floor_templates[floor]["events"])
                    elif tile_type == "shop":
                        tile["sprite"] = random.choice(data.floor_templates[floor]["shops"]) # add custom media for these
                    elif tile_type == "quest":
                        tile["sprite"] = random.choice(data.floor_templates[floor]["paths"]["straight"])
                    elif tile_type == "elite":
                        tile["sprite"] = random.choice(data.floor_templates[floor]["paths"]["straight"])
                    elif tile_type == "boss":
                        tile["sprite"] = random.choice(data.floor_templates[floor]["paths"]["straight"])
                    elif tile_type == "standard":
                        tile["sprite"] = random.choice(data.floor_templates[floor]["paths"]["straight"])
                    else:
                        continue # incase of new tile types


    def move_tile(self, player_position, key):
        player_x, player_y = player_position
        valid_directions = []
        for direction in self.possible_directions:
            for tile in self.tiles:
                if (tile["column"] * self.tile_size) == (player_x + (direction[0] * self.tile_size)) and (tile["row"] * self.tile_size) == (player_y + (direction[1] * self.tile_size)):
                    valid_directions.append(direction)

        if key == "a" or key == "left":
            if (-1, 0) in valid_directions:
                return player_x - self.tile_size, player_y
            else:
                return player_x, player_y

        elif key == "d" or key == "right":
            if (1, 0) in valid_directions:
                return player_x + self.tile_size, player_y
            else:
                return player_x, player_y

        elif key == "w" or key == "up":
            if (0, -1) in valid_directions:
                return player_x, player_y - self.tile_size
            else:
                return player_x, player_y

        elif key == "s" or key == "down":
            if (0, 1) in valid_directions:
                return player_x, player_y + self.tile_size
            else:
                return player_x, player_y

        else:
            return player_x, player_y

    def tile_update(self, player_position, player):
        for tile in self.tiles:
            if player_position[0] in range(tile["column"] * self.tile_size, (tile["column"] * self.tile_size) + self.tile_size) and player_position[1] in range(tile["row"] * self.tile_size, (tile["row"] * self.tile_size) + self.tile_size):
                if not tile["visited"]:
                    tile["visited"] = True
                    if  tile["type"] == "standard" and random.random() < 0.1:
                        return combat.Battle(self.floor, player, self.enemies) # initiate combat
                    else:
                        pass

    def event_handler(self, player_position):
        player_x, player_y = player_position
        for tile in self.tiles:
            if (tile["column"] * self.tile_size) == player_x and (tile["row"] * self.tile_size) == player_y:
                if tile["type"] != "event":
                    return tile["type"]
                elif tile["visited"] == False:
                    return random.choice(self.events) # instead of random make it based off the sprite of the tile
                else:
                    return "standard"
