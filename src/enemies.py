import random
import copy

import data

class Enemy:
    def __init__(self, template):
        baseX, baseY = data.baseEnemy
        offsetX, offsetY = template["offset"]

        self.name = template["name"]
        self.sprite = template["sprite"]
        self.centerX = baseX + offsetX
        self.centerY = baseY + offsetY

        self.data = {
            "max_health": template["health"],
            "health": template["health"],
            "speed": template["speed"],
            "skills": copy.deepcopy(template["skills"]),
            "status_effects": []
        }

    def update_enemy(self, damage, statusEffect, attacker): # make a combat handler to handle combat events with speed.
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

        if self.data.get("blocking"):
            damage //= 2

        self.data["health"] -= damage
        self.data["status_effects"].append(statusEffect)

    def enemy_action(self):
        skills = list(self.data["skills"].keys())
        weights = [values["weight"] for values in self.data["skills"].values()]
        chosen_skill_name = random.choices(skills, weights, k=1)[0]
        chosen_skill_data = self.data["skills"][chosen_skill_name]
        if chosen_skill_data.get("evasion"):
            self.data["evading"] = True
        if chosen_skill_data.get("block"):
            self.data["blocking"] = True
        damage = chosen_skill_data.get("damage")
        status_effect = chosen_skill_data.get("status_effect")
        effect_stack = chosen_skill_data.get("effect_stack")

        return damage, status_effect, effect_stack