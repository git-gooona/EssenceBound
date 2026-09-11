import random

import data

class Player:
    def __init__(self):
        self.data = {
            "max_health": 100,
            "health": 100,
            "health_recovery": 0,
            "max_mana": 100,
            "mana": 100,
            "mana_recovery": 6,
            "max_stamina": 100,
            "stamina": 100,
            "stamina_recovery": 8,
            "damage_amplification": 0,
            "damage_reduction": 0,
            "speed": 10,
            "status_effects": [],
            "deck": data.starting_deck_template.copy(),
            "hand": [],
            "max_hand_size": 5
        }

        # add item effects here

    def update_player(self, damage, status_effect, effect_stack, attacker):
        chance = random.randint(1,10)

        if self.data.get("evading"):
            if self.data["speed"] > attacker.data["speed"]:
                if chance <= 8:
                    damage = 0
            elif self.data["speed"] == attacker.data["speed"]:
                if chance <= 5:
                    damage = 0
            else:
                if chance <= 2:
                    damage = 0

        if self.data.get("blocking") == True:
            if self.data["blocking"] == True:
                damage //= 2

        self.data["health"] -= damage * (1 - self.data["damage_reduction"])
        for i in range(effect_stack):
            self.data["status_effects"].append(status_effect)

    def player_action(self, card_name):
        card_data = data.card_data[card_name]
        actionable = False

        resource = card_data["resource"]
        if self.data[resource] >= card_data["cost"]:
            self.data[resource] -= card_data["cost"]
            actionable = True

        if actionable == True:
            self.data["hand"].remove(card_name)
            damage_output = card_data["damage"] * (1 + self.data["damage_amplification"])
            status_effect_output = [card_data["effect"] for i in range(card_data["effect_stack"])]
            actionable = False
            return damage_output, status_effect_output, card_name
        else:
            return 0, None