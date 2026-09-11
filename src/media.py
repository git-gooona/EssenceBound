import pathlib

from cmu_graphics import Sound

###
# Media Directories
###

BASE_DIR = pathlib.Path(__file__).resolve().parent.parent / "media"

CARDS_DIR = BASE_DIR / "images" / "cards"
CHARACTERS_DIR = BASE_DIR / "images" / "characters"
ENVIRONMENT_DIR = BASE_DIR / "images" / "environment"
GUI_DIR = BASE_DIR / "images" / "gui"
ITEMS_DIR = BASE_DIR / "images" / "items"
MONSTERS_DIR = BASE_DIR / "images" / "monsters"

BUTTONS_DIR = BASE_DIR / "sounds" / "buttons"
CHIMES_DIR = BASE_DIR / "sounds" / "chimes"
COMBAT_DIR = BASE_DIR / "sounds" / "combat"
DIALOGUE_DIR = BASE_DIR / "sounds" / "dialogue"
MOVEMENT_DIR = BASE_DIR / "sounds" / "movement"
OBJECTS_DIR = BASE_DIR / "sounds" / "objects"
SOUNDTRACKS_DIR = BASE_DIR / "sounds" / "soundtracks"

###
# Defining Media - Images
###

# Cards
blazing_beam_image = str(CARDS_DIR / "fire" / "blazing_beam.png")
ember_image = str(CARDS_DIR / "fire" / "ember.png")
fireball_image = str(CARDS_DIR / "fire" / "fireball.png")
fire_breath_image = str(CARDS_DIR / "fire" / "fire_breath.png")
meteor_shower_image = str(CARDS_DIR / "fire" / "meteor_shower.png")

# Characters
wizard_npc_image = str(CHARACTERS_DIR / "wizard")

# Environments
home_room_background_image = str(ENVIRONMENT_DIR / "main" / "home_room.png")
title_background_image = str(ENVIRONMENT_DIR / "title" / "title.png")
town_background_image = str(ENVIRONMENT_DIR / "town.png")
yggdrasil_background_image = str(ENVIRONMENT_DIR / "yggdrasil.png")

CRYPT_DIR = ENVIRONMENT_DIR / "crypt"
crypt_straight_hallway_images = [str(CRYPT_DIR / "standard_corridor_one.png"),
                                 str(CRYPT_DIR / "standard_corridor_two.png"),
                                 str(CRYPT_DIR / "standard_corridor_three.png"),
                                 str(CRYPT_DIR / "sounds_corridor.png")]

crypt_right_hallway_images = [str(CRYPT_DIR / "right_corridor.png")]

crypt_left_hallway_images = [str(CRYPT_DIR / "left_corridor.png"),
                             str(CRYPT_DIR / "creepy_corridor.png")]

crypt_two_way_hallway_images = [str(CRYPT_DIR / "two_way_corridor.png")]

crypt_three_way_hallway_images = [str(CRYPT_DIR / "three_way_corridor.png")]

crypt_event_images = [str(CRYPT_DIR / "creepy_corridor.png"),
                      str(CRYPT_DIR / "sounds_corridor.png")]

crypt_shop_images = [str(CRYPT_DIR / "shop" / "shop_one"),
                     str(CRYPT_DIR / "shop" / "shop_two")]

# GUI
alchemy_kit_image = str(GUI_DIR / "icons" / "buttons" / "alchemy_kit.png")
astrolabe_image = str(GUI_DIR / "icons" / "buttons" / "astrolabe.png")
compass_image = str(GUI_DIR / "icons" / "buttons" / "compass.png")
crypt_icon_image = str(GUI_DIR / "icons" / "buttons" / "crypt_icon.png")
map_image = str(GUI_DIR / "icons" / "buttons" / "map.png")
settings_icon_image = str(GUI_DIR / "icons" / "buttons" / "settings_icon.png")

pixie_image = str(GUI_DIR / "icons" / "event" / "pixie.png")

big_mana_image = str(GUI_DIR / "icons" / "information" / "big_mana.png")
tiny_mana_image = str(GUI_DIR / "icons" / "information" / "tiny_mana.png")

# map
boss_icon = str(GUI_DIR / "icons" / "map" / "boss.png")
elite_icon = str(GUI_DIR / "icons" / "map" / "skull.png")
ladder_icon = str(GUI_DIR / "icons" / "map" / "ladder.png")
quest_icon = str(GUI_DIR / "icons" / "map" / "quest.png")
shop_icon = str(GUI_DIR / "icons" / "map" / "gold.png")

# Items
abyssal_scourge_image = str(ITEMS_DIR / "consumables" / "abyssal_scourge.png")
aether_brew_image = str(ITEMS_DIR / "consumables" / "aether_brew.png")
aether_weave_elixir_image = str(ITEMS_DIR / "consumables" / "aether_weave_elixir.png")
berserkers_brew_image = str(ITEMS_DIR / "consumables" / "berserkers_brew.png")
blessing_image = str(ITEMS_DIR / "consumables" / "blessing.png")
blood_key_image = str(ITEMS_DIR / "consumables" / "blood_key.png")
blood_rage_brew_image = str(ITEMS_DIR / "consumables" / "blood_rage_brew.png")
caustic_brew_image = str(ITEMS_DIR / "consumables" / "caustic_brew.png")
cinderblooms_hearth_image = str(ITEMS_DIR / "consumables" / "cinderblooms_hearth.png")
curing_potion_image = str(ITEMS_DIR / "consumables" / "curing_potion.png")
curing_vial_image = str(ITEMS_DIR / "consumables" / "curing_vial.png")
flesh_stitch_elixir_image = str(ITEMS_DIR / "consumables" / "flesh_stitch_elixir.png")
ghoulrot_extract_image = str(ITEMS_DIR / "consumables" / "ghoulrot_extract.png")
health_potion_image = str(ITEMS_DIR / "consumables" / "health_potion.png")
health_vial_image = str(ITEMS_DIR / "consumables" / "health_vial.png")
ironbark_extract_image = str(ITEMS_DIR / "consumables" / "ironbark_extract.png")
ironskin_potion_image = str(ITEMS_DIR / "consumables" / "ironskin_potion.png")
lampfern_extract_image = str(ITEMS_DIR / "consumables" / "lampfern_extract.png")
mana_potion_image = str(ITEMS_DIR / "consumables" / "mana_potion.png")
mana_vial_image = str(ITEMS_DIR / "consumables" / "mana_vial.png")
marrow_kindle_elixir_image = str(ITEMS_DIR / "consumables" / "marrow_kindle_elixir.png")
masterwork_key_image = str(ITEMS_DIR / "consumables" / "masterwork_key.png")
messenger_image = str(ITEMS_DIR / "consumables" / "messenger.png")
mystical_hourglass_image = str(ITEMS_DIR / "consumables" / "mystical_hourglass.png")
phoenix_tears_image = str(ITEMS_DIR / "consumables" / "phoenix_tears.png")
potion_of_fortitude_image = str(ITEMS_DIR / "consumables" / "potion_of_fortitude.png") # gives Fortification status effect
purple_loot_bag_image = str(ITEMS_DIR / "consumables" / "purple_loot_bag.png") # purple lotus extract gives magic regen or damage buff
recovery_vial_image = str(ITEMS_DIR / "consumables" / "recovery_vial.png")
salamanders_essence_image = str(ITEMS_DIR / "consumables" / "salamanders_essence.png")
snowmint_sap_image = str(ITEMS_DIR / "consumables" / "snowmint_sap.png")
stamina_potion_image = str(ITEMS_DIR / "consumables" / "stamina_potion.png")
stamina_vial_image = str(ITEMS_DIR / "consumables" / "stamina_vial.png")
stygian_rust_extract_image = str(ITEMS_DIR / "consumables" / "stygian_rust_extract.png")
venomleaf_extract_image = str(ITEMS_DIR / "consumables" / "venomleaf_extract.png")
vital_brew_image = str(ITEMS_DIR / "consumables" / "vital_brew.png")
winters_chill_extract_image = str(ITEMS_DIR / "consumables" / "winters_chill_extract.png")
wolfsbane_extract_image = str(ITEMS_DIR / "consumables" / "wolfsbane_extract.png")

alchemists_staff_image = str(ITEMS_DIR / "equipment" / "alchemists_staff.png")
amulet_of_festering_image = str(ITEMS_DIR / "equipment" / "amulet_of_festering.png")
amulet_of_protection_image = str(ITEMS_DIR / "equipment" / "amulet_of_protection.png")
ancient_grimoire_image = str(ITEMS_DIR / "equipment" / "ancient_grimoire.png")
boots_of_agility_image = str(ITEMS_DIR / "equipment" / "boots_of_agility.png")
boots_of_hermes_image = str(ITEMS_DIR / "equipment" / "boots_of_hermes.png")
dragoncrested_shield_image = str(ITEMS_DIR / "equipment" / "dragoncrested_shield.png")
dragonscale_armor_image = str(ITEMS_DIR / "equipment" / "dragonscale_armor.png")
dragonscale_shield_image = str(ITEMS_DIR / "equipment" / "dragonscale_shield.png")
elderwood_ring_image = str(ITEMS_DIR / "equipment" / "elderwood_ring.png")
enchanted_earrings_image = str(ITEMS_DIR / "equipment" / "enchanted_earrings.png")
enchanted_ring_image = str(ITEMS_DIR / "equipment" / "enchanted_ring.png")
magic_robes_image = str(ITEMS_DIR / "equipment" / "magic_robes.png")
masterwork_staff_image = str(ITEMS_DIR / "equipment" / "masterwork_staff.png")
necromancers_ring_image = str(ITEMS_DIR / "equipment" / "necromancers_ring.png") #ring of frost, necros staff, etc 
ring_of_fire_image = str(ITEMS_DIR / "equipment" / "ring_of_fire.png")
ring_of_poison_image = str(ITEMS_DIR / "equipment" / "ring_of_poison.png")
runic_belt_image = str(ITEMS_DIR / "equipment" / "runic_belt.png")
samsaras_flame_image = str(ITEMS_DIR / "equipment" / "samsaras_flame.png")
sanguine_amulet_image = str(ITEMS_DIR / "equipment" / "sanguine_amulet.png")
sapphire_ring_image = str(ITEMS_DIR / "equipment" / "sapphire_ring.png")
staff_of_channeling_image = str(ITEMS_DIR / "equipment" / "staff_of_channeling.png")
staff_of_flames_image = str(ITEMS_DIR / "equipment" / "staff_of_flames.png")
staff_of_frost_image = str(ITEMS_DIR / "equipment" / "staff_of_frost.png")
staff_of_growth_image = str(ITEMS_DIR / "equipment" / "staff_of_growth.png")
staff_of_the_arcane_image = str(ITEMS_DIR / "equipment" / "staff_of_the_arcane.png")
staff_of_tides_image = str(ITEMS_DIR / "equipment" / "staff_of_tides.png")
staff_of_wind_image = str(ITEMS_DIR / "equipment" / "staff_of_wind.png")
wooden_stave_image = str(ITEMS_DIR / "equipment" / "wooden_stave.png")

ancient_tablets_image = str(ITEMS_DIR / "loot" / "ancient_tablets.png")

barrowshroom_image = str(ITEMS_DIR / "materials" / "herbs" / "barrowshroom.png")
blighted_flower_image = str(ITEMS_DIR / "materials" / "herbs" / "blighted_flower.png")
bogshroom_image = str(ITEMS_DIR / "materials" / "herbs" / "bogshroom.png")
cinderbloom_image = str(ITEMS_DIR / "materials" / "herbs" / "cinderbloom.png")
cureroot_image = str(ITEMS_DIR / "materials" / "herbs" / "cureroot.png")
firegrass_image = str(ITEMS_DIR / "materials" / "herbs" / "firegrass.png")
frostfern_image = str(ITEMS_DIR / "materials" / "herbs" / "frostfern.png")
ghoulrot_image = str(ITEMS_DIR / "materials" / "herbs" / "ghoulrot.png")
glaciers_tear_image = str(ITEMS_DIR / "materials" / "herbs" / "glaciers_tear.png")
glowberries_image = str(ITEMS_DIR / "materials" / "herbs" / "glowberries.png")
hyacinth_image = str(ITEMS_DIR / "materials" / "herbs" / "hyacinth.png")
ironbark_image = str(ITEMS_DIR / "materials" / "herbs" / "ironbark.png")
lampfern_image = str(ITEMS_DIR / "materials" / "herbs" / "lampfern.png")
mage_thistle_image = str(ITEMS_DIR / "materials" / "herbs" / "mage_thistle.png")
marrowkindle_image = str(ITEMS_DIR / "materials" / "herbs" / "marrowkindle.png")
moonshade_image = str(ITEMS_DIR / "materials" / "herbs" / "moonshade.png")
nightshade_image = str(ITEMS_DIR / "materials" / "herbs" / "nightshade.png")
panacea_image = str(ITEMS_DIR / "materials" / "herbs" / "panacea.png")
pixie_dust_image = str(ITEMS_DIR / "materials" / "herbs" / "pixie_dust.png")
redcap_mushroom_image = str(ITEMS_DIR / "materials" / "herbs" / "redcap_mushroom.png")
rosseta_image = str(ITEMS_DIR / "materials" / "herbs" / "rosseta.png")
sage_image = str(ITEMS_DIR / "materials" / "herbs" / "sage.png")
snowmint_image = str(ITEMS_DIR / "materials" / "herbs" / "snowmint.png")
sunglint_image = str(ITEMS_DIR / "materials" / "herbs" / "sunglint.png")
thalian_berries_image = str(ITEMS_DIR / "materials" / "herbs" / "thalian_berries.png")
venomleaf_image = str(ITEMS_DIR / "materials" / "herbs" / "venomleaf.png")
wolfsbane_image = str(ITEMS_DIR / "materials" / "herbs" / "wolfsbane.png")

#minerals

carapace_image = str(ITEMS_DIR / "materials" / "monsters" / "carapace.png")
fang_image = str(ITEMS_DIR / "materials" / "monsters" / "fang.png")
horn_image = str(ITEMS_DIR / "materials" / "monsters" / "horn.png")
phoenix_feather_image = str(ITEMS_DIR / "materials" / "monsters" / "phoenix_feather.png")
qingniaos_feather_image = str(ITEMS_DIR / "materials" / "monsters" / "qingniaos_feather.png")
rotsack_image = str(ITEMS_DIR / "materials" / "monsters" / "rotsack.png")
salamanders_tail_image = str(ITEMS_DIR / "materials" / "monsters" / "salamanders_tail.png")
scale_image = str(ITEMS_DIR / "materials" / "monsters" / "scale.png")
wolfpelt_image = str(ITEMS_DIR / "materials" / "monsters" / "wolfpelt.png")

alchemy_kit_quest_image = str(ITEMS_DIR / "quest" / "alchemy_kit_quest.png")
demonic_chalice_image = str(ITEMS_DIR / "quest" / "demonic_chalice.png")
devils_crown_image = str(ITEMS_DIR / "quest" / "devils_crown.png")
devils_sigil_image = str(ITEMS_DIR / "quest" / "devils_sigil.png")
familiar_contract_image = str(ITEMS_DIR / "quest" / "familiar_contract.png")
frozen_chalice_image = str(ITEMS_DIR / "quest" / "frozen_chalice.png")
heart_of_thorns_image = str(ITEMS_DIR / "quest" / "heart_of_thorns.png")
orcish_token_image = str(ITEMS_DIR / "quest" / "orcish_token.png")
orcish_token2_image = str(ITEMS_DIR / "quest" / "orcish_token2.png")
pandoras_box_image = str(ITEMS_DIR / "quest" / "pandoras_box.png")
petrifying_mirror_image = str(ITEMS_DIR / "quest" / "petrifying_mirror.png")
rare_gems_image = str(ITEMS_DIR / "quest" / "rare_gems.png")
rogues_bracers_image = str(ITEMS_DIR / "quest" / "rogues_bracers.png")
spirit_caller_image = str(ITEMS_DIR / "quest" / "spirit_caller.png")
wardens_hammer_image = str(ITEMS_DIR / "quest" / "wardens_hammer.png")
wardens_key_image = str(ITEMS_DIR / "quest" / "wardens_key.png")
werewolf_collar_image = str(ITEMS_DIR / "quest" / "werewolf_collar.png")

# Monsters
skeleton_archer_image = str(MONSTERS_DIR / "crypt" / "skeleton_archer.png")
skeleton_warrior_image = str(MONSTERS_DIR / "crypt" / "skeleton_warrior.png")

###
# Defining Media - Sounds
###

# Buttons
heavy_button_sound = Sound(str(BUTTONS_DIR / "heavy_button.mp3"))
interact_button_sound = Sound(str(BUTTONS_DIR / "interact_button.mp3"))
interact_button2_sound = Sound(str(BUTTONS_DIR / "interact_button2.mp3"))
light_button_sound = Sound(str(BUTTONS_DIR / "light_button.mp3"))
purchase_sound = Sound(str(BUTTONS_DIR / "purchase.mp3"))
sell_sound = Sound(str(BUTTONS_DIR / "sell.mp3"))
spell_screen_open_sound = Sound(str(BUTTONS_DIR / "spellscreen_open.mp3"))
spell_screen_page_flip_sound = Sound(str(BUTTONS_DIR / "spellscreen_pageflip.mp3"))
tiny_sell1_sound = Sound(str(BUTTONS_DIR / "tiny_sell1.mp3"))
tiny_sell2_sound = Sound(str(BUTTONS_DIR / "tiny_sell2.mp3"))
tiny_sell3_sound = Sound(str(BUTTONS_DIR / "tiny_sell3.mp3"))

# Chimes
discovery_sound = Sound(str(CHIMES_DIR / "discovery.mp3"))
money_found_sound = Sound(str(CHIMES_DIR / "money_found.mp3"))
quest_complete_sound1 = Sound(str(CHIMES_DIR / "quest_complete1.mp3"))
quest_complete_sound2 = Sound(str(CHIMES_DIR / "quest_complete2.mp3"))

# Combat
play_card_sound = Sound(str(COMBAT_DIR / "play_card.mp3"))

arrow1_sound = Sound(str(COMBAT_DIR / "enemy" / "crypt" / "skeleton_archer" / "arrow1.mp3"))
evade_sound = Sound(str(COMBAT_DIR / "enemy" / "crypt" / "skeleton_archer" / "evade.mp3"))

block_sound = Sound(str(COMBAT_DIR / "enemy" / "crypt" / "skeleton_warrior" / "block.mp3"))
slash1_sound = Sound(str(COMBAT_DIR / "enemy" / "crypt" / "skeleton_warrior" / "slash1.mp3"))

blazing_beam_sound = Sound(str(COMBAT_DIR / "player" / "fire" / "blazing_beam.mp3"))
burn_card_sound = Sound(str(COMBAT_DIR / "player" / "fire" / "burn_card.mp3"))
fire_breath_sound = Sound(str(COMBAT_DIR / "player" / "fire" / "fire_breath.mp3"))
ember_sound = Sound(str(COMBAT_DIR / "player" / "fire" / "ember.mp3"))
erupt_sound = Sound(str(COMBAT_DIR / "player" / "fire" / "erupt.mp3"))
fireball_sound = Sound(str(COMBAT_DIR / "player" / "fire" / "fireball.mp3"))
meteor_shower_sound = Sound(str(COMBAT_DIR / "player" / "fire" / "meteor_shower.mp3"))

# Dialogue
evil_laugh_sound = Sound(str(DIALOGUE_DIR / "evil_laugh.mp3"))
npc_dissappointed_sound = Sound(str(DIALOGUE_DIR / "npc_dissappointed.mp3"))
npc_exclaim1_sound = Sound(str(DIALOGUE_DIR / "npc_exclaim1.mp3"))
npc_exclaim2_sound = Sound(str(DIALOGUE_DIR / "npc_exclaim2.mp3"))
npc_greeting_sound = Sound(str(DIALOGUE_DIR / "npc_greeting.mp3")) # add more variation of these sounds
npc_happy_sound = Sound(str(DIALOGUE_DIR / "npc_happy.mp3"))
npc_sad_sound = Sound(str(DIALOGUE_DIR / "npc_sad.mp3"))
npc_shocked_sound = Sound(str(DIALOGUE_DIR / "npc_shocked.mp3"))
old_bird_sound = Sound(str(DIALOGUE_DIR / "old_bird.mp3"))
young_bird_sound = Sound(str(DIALOGUE_DIR / "young_bird.mp3"))

# Movement
footstep1_sound = Sound(str(MOVEMENT_DIR / "footstep1.mp3"))
footstep2_sound = Sound(str(MOVEMENT_DIR / "footstep2.mp3"))
footstep3_sound = Sound(str(MOVEMENT_DIR / "footstep3.mp3"))
footstep4_sound = Sound(str(MOVEMENT_DIR / "footstep4.mp3"))
travel_sound = Sound(str(MOVEMENT_DIR / "travel.mp3"))

# Objects
door_open_sound = Sound(str(OBJECTS_DIR / "door_open.mp3"))

# Soundtracks - All Loop - gotta give boss opening scene which you gotta click outa so we can loop bossintro
boss_intro_soundtrack = Sound(str(SOUNDTRACKS_DIR / "boss_intro.mp3"))
boss_phase1_soundtrack = Sound(str(SOUNDTRACKS_DIR / "boss_phase1.mp3"))
boss_phase2_soundtrack = Sound(str(SOUNDTRACKS_DIR / "boss_phase2.mp3"))

camp_soundtrack = Sound(str(SOUNDTRACKS_DIR / "camp.mp3"))
dungeon_soundtrack = Sound(str(SOUNDTRACKS_DIR / "dungeon.mp3"))
shop_soundtrack = Sound(str(SOUNDTRACKS_DIR / "shop.mp3"))
title_screen_soundtrack = Sound(str(SOUNDTRACKS_DIR / "title_screen.mp3"))