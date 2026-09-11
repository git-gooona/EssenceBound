import random

import data
import enemies

def alive_check(entity):
    if entity.data["health"] > 0:
        return True
    else:
        return False

class Battle:
    def __init__(self, floor, player):
        self.player = player
        self.floor = floor

        self.deck = []
        self.discard = [] # build this system. based off propegating self.player_casted_damage and others with the player_action function.

        self.deck = self.player.data["deck"].copy() # dynamic battle deck
        random.shuffle(self.deck)

        for i in range(player.data["max_hand_size"]):
            player.data["hand"].append(self.deck.pop())

    def battle_start(self):
        self.active_enemies = []
        self.player_casted_cards = []
        self.player_casted_damage = []
        self.player_casted_status_effects = []
        #self.amount_of_enemies = random.randint(1,2) # Future development

        enemy_name = random.choice(self.floor.enemies)
        self.enemy_one = enemies.Enemy(data.enemy_templates[enemy_name])

        self.active_enemies.append(self.enemy_one)

    def turn_start(self):
        for resource, recovery in data.resource_mapping_template.items(): # performs self recovery
            max_resource = f"max_{resource}"
            pending_resource = self.player.data[resource] + self.player.data[recovery]
            self.player.data[resource] = min(pending_resource, self.player.data[max_resource])

        for i in range(self.player.data["max_hand_size"] - len(self.player.data["hand"])): # handles drawing to max hand size
            self.player.data["hand"].append(self.deck.pop())

        for enemy in self.active_enemies: # checks to see who should go first
            if self.player.data["speed"] > enemy.data["speed"]: # for multiple enemies we probably save it as intitiative and index while looping through - initiative1, initiative2, etc
                self.player.data["initiative"] = True
            else:
                self.player.data["initiative"] = False

    def battle(self):
        for enemy in self.active_enemies: # there are updates and actions. where do actions get called? enemy action gets called here, but player actions are unique and dynamic.
            if self.player.data["initiative"]:
                for i in range(len(self.player_casted_damage)):
                    enemy.update_enemy(self.player_casted_damage[i], self.player_casted_status_effects[i], self.player.data)
                if alive_check(enemy) == False:
                    self.active_enemies.remove(enemy)
                self.player.update_player(enemy.enemy_action(), enemy.data) # how are we preventing damage from occuring if the enemy is dead? ideally the instance will dissappear and I wont have to worry about it.
                if alive_check(self.player) == False:
                    pass
                    #gameover here or something
            else:
                self.player.update_player(enemy.enemy_action(), enemy.data)
                if alive_check(self.player) == False:
                    pass
                for i in range(len(self.player_casted_damage)):
                    enemy.update_enemy(self.player_casted_damage[i], self.player_casted_status_effects[i], self.player.data)
                if alive_check(enemy) == False:
                    self.active_enemies.remove(enemy)

    def turn_end(self):
        self.player.data["evading"] = False
        self.player.data["blocking"] = False
        for enemy in self.active_enemies:
            enemy.data["evading"] = False
            enemy.data["blocking"] = False