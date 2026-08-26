########################################################################
###Archived Problems:
########################################################################
#Up down walking animation as entering room/event
#update stat labels
#Implement Inspect
#Find a way to reduce coding bloat (functions, Lists, etc.) #??? Just dont write bloat in the first place
#left tan box just for info (buffs, debuffs, map, settings, text boxes, active items) consumables
#Source sfx
#Add elements to card dictionary
#
#
#
#
#
#######################################################################
###Archived Plans
#######################################################################
#
##Fire - Damage and Damage overtime, limited card draw and mana management with high costs and discards for higher dps
#Water - Card Draw, regen, and debuffs, limited damage and defense cards # nice
#Earth - Defenses, greed buffs (higher chance for relics, more gold, more cards after combat etc.) # nice
#Air - Mana regen and Mana prep(+x mana next turn), buffs, maybe even dodge % if possible and not broken, combos
#Arcane - All rounder there to fill out any missing parts of a deck
#
#
#bag icon next to map for help items plus descriptions
#160 x 160 for npc icons
#dont take damage when u 1 shot the enemy
#draw cards 1 by 1
#prevent enemy spawn right after opening the map
#only comit hitting sounds after turn end, not spell cast  - make a mini combat phase
#######################################################################
###Archived Discussions
#######################################################################
#
#
#
#
#
#
#
#
# 
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# 
# 
# 
# 
# 
#Squares next to the player are visible('orange') everything else is invisible until next to player? At least that's how I thought we were gonna do it let me know how you were thinking it should be
#
#Enemies are already very common. Look at how many tiles there are. Every floor you are already going to have to face around 10 enemies with no way of healing your health - heal from cards, events(camp, shop, relics), camps should spawn at least spawn twice a floor and should heal a percentage at least make enemies 40% and events 10% and then 50% for nothing ig
#
#
#
#
#
#map enemy spawn fix ###### 12/2/25
#
#SOUNDS - have to cut down sound lengths for more smooth experience
#
#rework map to remove arrows and mouse presses
#make functions usable to optimize code
#for gamescreen to be visible on battle encounter == true so remove cards n shit until battle starts
#
#function to make labels increments. so like Len(str) iterated length for segment int, for each int we make a label and assign it part of the str. base str would be defined at the beginning like x.
#^^For further NPC Dialogue
#
#remove sleeps, make battle screen dissappear on end turn press.
#
#burn cards and dont discard entire hand at turn end
#perhaps drawing out the deck should result in consuming all current mana to replenish it?
#
#
#death animation for enemies with sound and maybe fade away or some kind of vfx
#
#
#
#
# up down up down walk in room animation
#
#Image generation for cards and enemies
######################################################################## CREDITS
#Scott Arc - Monster sfx
#Yodguard - Magic sfx
#Floraphonic - Magic sfx
#
#
########################################################################
from cmu_graphics import *
import random
import time
from pathlib import Path

###########################################################
###App Start, App variables
###########################################################
def onAppStart(app):

    ###Directories
    BASE_DIR = Path(__file__).resolve().parent
    MEDIA_DIR = BASE_DIR / "Media"
    SOUND_DIR = BASE_DIR / "Audio"

    ###Timers
    app.gameTimer = 0
    app.timer = 0 
    app.questTimer = 0
    
    ###240x360
    app.BIG_Ember = str(MEDIA_DIR / 'EmberFireCard.png')
    app.BIG_FireBreath = str(MEDIA_DIR / 'FireBreathFireCards.png')
    app.BIG_FireBall = str(MEDIA_DIR / 'FireBallFireCard+(1).png')
    app.BIG_MeteorShower = str(MEDIA_DIR / 'MeteorShowerFireCard+(1).png')
    app.BIG_BlazingBeam = str(MEDIA_DIR / 'BlazingBeamFireCard+(1).png')
    
    ###60x90 Cards
    app.Ember = str(MEDIA_DIR / 'EmberFireCard_optimized.png')
    app.FireBreath = str(MEDIA_DIR / 'FireBreathFireCards_optimized.png')
    app.FireBall = str(MEDIA_DIR / 'FireBallFireCard_1_optimized.png')
    app.MeteorShower = str(MEDIA_DIR / 'MeteorShowerFireCard_1_optimized.png')
    app.BlazingBeam = str(MEDIA_DIR / 'BlazingBeamFireCard_1_optimized.png')

    ###NPCs
    app.wizardNPC = str(MEDIA_DIR / 'WizardNPC.png')
    
    ###Monsters
    app.skeleton_Monsters = []
    app.skeleton_Warrior = str(MEDIA_DIR / 'Skeleton_Warrior.png')
    app.skeleton_Archer = str(MEDIA_DIR / 'Skeleton_Archer.png')
    app.skeleton_Monsters.append(app.skeleton_Warrior)
    app.skeleton_Monsters.append(app.skeleton_Archer)
    app.currentMonster = app.skeleton_Monsters[random.randrange(len(app.skeleton_Monsters))] ### add toggling between skeleton_types
    
    ###Monster Actions
    app.action = []
    app.skeleton_Warrior_Actions = ['thrust','slash','guard','shriek']
    app.skeleton_Archer_Actions = ['power_shot','wait','draw','enfeebling_arrow']

    ###Screen Media
    app.yggdrasil = str(MEDIA_DIR / 'Yggdrasil.png')
    app.bigManaIcon = str(MEDIA_DIR / 'bigMana.png')
    app.dungeonCorridorBG = str(MEDIA_DIR / 'Dungeon+Corridor+with+Torches+and+Barrels.png')
    app.mapIcon = str(MEDIA_DIR / 'Map.png')
    app.camp = str(MEDIA_DIR / 'CampPixelArtScreen.png')
    app.tinyMana = str(MEDIA_DIR / 'tinyMana.png')
    
    ###Map Icons
    app.enemyIcon = str(MEDIA_DIR / 'Final_Skull.png')
    app.questIcon = str(MEDIA_DIR / 'Final_Scroll.png')
    app.nextFloorIcon = str(MEDIA_DIR / 'Final_Ladder.png')
    app.questIconAccepted = str(MEDIA_DIR / 'university-school-icons-pixel-art-260nw-2218660645-removebg-preview.png')
    
    app.questIconVisToggle1 = True
    app.questIconToggle = False #accept/decline quest
    app.questIconAcceptedToggle = False #is a vis
    app.questStatus = False #not completed
    app.questX=540
    app.questY=320

    app.enemyX1 = 749
    app.enemyY1 = 169
    app.enemyX2 = 669
    app.enemyY2 = 409
    app.enemyIconVisToggle1 = False
    app.enemyIconVisToggle2 = False
    
    ### Hand, Deck, Discard Variables
    app.Deck = [*([app.Ember] * 4), *([app.FireBreath] * 4), *([app.FireBall] * 4), *([app.MeteorShower] * 4), *([app.BlazingBeam] * 4)]
    app.Hand = []
    app.Discard = []
    app.randomSelect = random.randrange(len(app.Deck))
    app.canDraw = False
    app.currentCards = 0
    app.cardIndex = -1
    app.drawing=False
    
    for i in range(0,5): 
        app.Hand.append(app.Deck[app.randomSelect])
        app.Deck.pop(app.randomSelect)
        app.randomSelect = random.randrange(len(app.Deck))
        app.currentCards += 1

    ###Position Variables
    app.deckX=1200
    app.deckY=140
    
    app.discardX=1200
    app.discardY=240
    
    app.orderX=400
    app.orderY=140
    
    app.handX=600
    app.handY=450
    
    app.UIX=0
    app.UIY=0
    
    app.mX = 200
    app.mY = 200
    
    app.LX1 = 1050
    app.LY1 = 230
    
    app.RW1 = 400
    app.RH1 = 75
    
    app.EX1 = 80
    app.EY1 = 520
    
    app.bw = 60
    app.bh = 90
    app.by = 450
    
    app.bx1=600
    app.bx2=670
    app.bx3=740
    app.bx4=810
    app.bx5=880
    #app.bx6=
    #app.bx7=
    #app.bx8=
    
    app.mapOriginX = 700
    app.mapOriginY = 280
    
    app.pX = app.mapOriginX + 60
    app.pY = app.mapOriginY + 20
    
    
    app.mapTiles = []
    
    app.tPosition = [(app.mapOriginX, app.mapOriginY), (app.mapOriginX, app.mapOriginY-40), (app.mapOriginX, app.mapOriginY-80), (app.mapOriginX+40, app.mapOriginY-80), (app.mapOriginX-40, app.mapOriginY-80), (app.mapOriginX-80, app.mapOriginY-80), (app.mapOriginX+40, app.mapOriginY), (app.mapOriginX-40, app.mapOriginY), (app.mapOriginX-80, app.mapOriginY), (app.mapOriginX-80, app.mapOriginY+40), (app.mapOriginX-80, app.mapOriginY+80), (app.mapOriginX-160, app.mapOriginY+40), (app.mapOriginX-40, app.mapOriginY+120),
    (app.mapOriginX+40, app.mapOriginY+40), (app.mapOriginX-120, app.mapOriginY-80), (app.mapOriginX-80, app.mapOriginY+120), (app.mapOriginX-120, app.mapOriginY+40), (app.mapOriginX-80, app.mapOriginY-160), (app.mapOriginX-40, app.mapOriginY-160), (app.mapOriginX-80, app.mapOriginY-120), (app.mapOriginX+40, app.mapOriginY-120)]
    for (x, y) in app.tPosition:
        tData = {
            'tX':x,
            'tY':y,
            'adjacentPlayer': False,
            'tFill':'grey',
            'miniX':0,
            'miniY':0,
            'onTile': False,
            'hasBeenOnTile': False
        }
        app.mapTiles.append(tData)
    app.mapMinX = min(tData['tX'] for tData in app.mapTiles)
    app.mapMinY = min(tData['tY'] for tData in app.mapTiles)
    
    app.tileSpacing = 40
    for tData in app.mapTiles:
        app.indexX = (tData['tX'] - app.mapMinX) // app.tileSpacing
        app.indexY = (tData['tY'] - app.mapMinY) // app.tileSpacing
        tData['miniX'] = 1000 + app.indexX*40
        tData['miniY'] = -100 + app.indexY*40

    app.offSetX = 1200 - tData['tX']
    app.adjustedValueX = tData['tX'] + app.offSetX
    
    app.offSetY = 70 - tData['tY']
    app.adjustedValueY = tData['tY'] + app.offSetY

    ###Background Toggles
    app.startScreen = True
    app.startToggle = 100

    app.dungeonCorridor = True
    app.forwardMove = True
    app.rightMove = True
    app.leftMove = True
    app.backMove = True
    
    app.forwardLabelX = app.pX
    app.forwardLabelY = app.pY - 40
    
    app.rightLabelX = app.pX + 40
    app.rightLabelY = app.pY
    
    app.leftLabelX = app.pX - 40
    app.leftLabelY = app.pY
    
    app.backLabelX = app.pX
    app.backLabelY = app.pY + 40
    
    ###Card Option Visibility
    app.optionVis = False
    app.oX=0
    app.x = 0
    
    ### Game Element
    app.battleEncounter = False
    app.turnOver = False
    app.turnTimer = 0
    app.flow = False
    app.flowEffect = 0
    app.firstTurn = True
    app.burnCounter = 0
    
    app.MmTF = True

    ### Settings/Config
    app.musicOn = True#
    app.sfxOn = True#
    app.labelConfig = True
    app.barConfig = False

    app.pauseScreen = False#

    app.labelOpacity = 100
    app.barOpacity = 100
    
    ### Player Values
    app.playerHP = 100
    app.currentMana = 12
    app.healthColor = 'lime'
    app.manaColor = 'blue'
    app.maxMana = 12
    app.meter = 0
    app.meterMax = 6
    app.meterToggle = ['black',rgb(100,0,0),rgb(140,0,0),rgb(160,0,0),rgb(180,0,0),rgb(220,0,0),rgb(255,20,20)] #Item to increase meter max blue fire?

    ### Stats
    app.luck = 1
    app.manaMaxIncrease = 0
    app.magicRecovery = 6
    app.turnHeal = 0
    app.damageAMP = 0
    app.damageRED = 0
    app.damageNEG = 0
    app.fireRES = 0
    app.waterRES = 0
    app.earthRES = 0
    app.windRES = 0
    app.thunderRES = 0
    app.poisonRES = 0
    app.bleedRES = 0
    app.demonicRES = 0
    app.holyRES = 0
    
    app.voodooeffect = False
    app.overheal = False
    app.bailout = False
    app.harp = False
    app.compass = False
    app.enhanced_alchemy = False

    ### Enemy Values
    app.enemyHP = 0
    if app.currentMonster == app.skeleton_Warrior:
        app.enemyHP = 60
    elif app.currentMonster == app.skeleton_Archer:
        app.enemyHP = 40
    app.damageCount = 0
    app.playerDamage = 0
    app.enemyReduction = 1
    app.enemyIncrease = 1
    app.burnAdder = 0

    ### Sounds
    #Player
    app.step_Sound = [
    Sound(str(SOUND_DIR / 'footstep1.mp3')),
    Sound(str(SOUND_DIR / 'footstep2.mp3')),
    Sound(str(SOUND_DIR / 'footstep3.mp3')),
    Sound(str(SOUND_DIR / 'footstep4.mp3'))
    ]
    #Spells
    app.burnCard_Sound = Sound(str(SOUND_DIR / 'burnCard.mp3'))
    app.fireBall_Sound = Sound(str(SOUND_DIR / 'fireBall.mp3'))
    app.earthBall_Sound = Sound(str(SOUND_DIR / 'earthBall.mp3'))
    app.meteor_Sound = Sound(str(SOUND_DIR / 'meteor.mp3'))
    app.dragon_Breath_Sound = Sound(str(SOUND_DIR / 'dragon_Breath.mp3'))
    app.blazing_Beam_Sound = Sound(str(SOUND_DIR / 'blazing_Beam.mp3'))
    app.ember_Sound = Sound(str(SOUND_DIR / 'ember.mp3'))
    app.earthQuake_Sound = Sound(str(SOUND_DIR / 'earthQuake.mp3'))
    #Enemies
    app.enemy_Arrow_Sound = Sound(str(SOUND_DIR / 'arrow.mp3'))
    app.enemy_Avoid_Sound = Sound(str(SOUND_DIR / 'evade.mp3'))
    app.enemy_Block_Sound = Sound(str(SOUND_DIR / 'block.mp3'))
    app.enemy_Slash_Sound = Sound(str(SOUND_DIR / 'slash.mp3'))
    #Bosses
    app.bossBattleLoop1_Sound = Sound(str(SOUND_DIR / 'bossBattleLoop1.mp3'))
    app.bossBattleLoop2_Sound = Sound(str(SOUND_DIR / 'bossBattleLoop2.mp3'))
    app.bossIntro2_Sound = Sound(str(SOUND_DIR / 'bossIntro2.mp3'))
    app.evilLaugh_Sound = Sound(str(SOUND_DIR / 'evilLaugh.mp3'))
    #UI
    app.money_Sound = Sound(str(SOUND_DIR / 'money.mp3'))
    app.tinySell_Sound = [
    Sound(str(SOUND_DIR / 'tinySell1.mp3')),
    Sound(str(SOUND_DIR / 'tinySell2.mp3')),
    Sound(str(SOUND_DIR / 'tinySell3.mp3'))
    ]
    app.bigSell_Sound = Sound(str(SOUND_DIR / 'bigSell.mp3'))
    app.purchase_Sound = Sound(str(SOUND_DIR / 'purchase.mp3'))
    app.lightButton = Sound(str(SOUND_DIR / 'lightButton.mp3'))
    app.heavyButton = Sound(str(SOUND_DIR / 'heavyButton.mp3'))
    app.interactButton = Sound(str(SOUND_DIR / 'interactButton.mp3'))
    app.interactButton2 = Sound(str(SOUND_DIR / 'interactButton2.mp3'))
    app.spellScreenOpen_Sound = Sound(str(SOUND_DIR / 'spellScreenOpen.mp3'))
    app.spellScreenPageFlip_Sound = Sound(str(SOUND_DIR / 'spellScreenPageFlip.mp3'))
    #Ambient
    app.dungeonAmbienceLoop_Sound = Sound(str(SOUND_DIR / 'dungeonAmbienceLoop.mp3')) # too loud
    app.cinematicLoop_Sound = Sound(str(SOUND_DIR / 'cinematicLoop.mp3'))
    app.windyAmbienceLoop_Sound = Sound(str(SOUND_DIR / 'windyAmbienceLoop.mp3'))
    app.shopMusicLoop_Sound = Sound(str(SOUND_DIR / 'shopMusicLoop.mp3'))
    app.discovery_Sound = Sound(str(SOUND_DIR / 'discovery.mp3'))
    #NPCs
    app.NPCDissapointed_Sound = Sound(str(SOUND_DIR / 'NPCDissappointed.mp3'))
    app.NPCExclaim_Sound = Sound(str(SOUND_DIR / 'NPCExclaim.mp3'))
    app.NPCExclaim2_Sound = Sound(str(SOUND_DIR / 'NPCExclaim2.mp3'))
    app.NPCGreeting_Sound = Sound(str(SOUND_DIR / 'NPCGreeting.mp3'))
    app.NPCHappy_Sound = Sound(str(SOUND_DIR / 'NPCHappy.mp3'))
    app.NPCSad_Sound = Sound(str(SOUND_DIR / 'NPCSad.mp3'))
    app.NPCShock_Sound = Sound(str(SOUND_DIR / 'NPCShock.mp3'))
    app.youngBird_Sound = Sound(str(SOUND_DIR / 'youngBird.mp3'))
    app.oldBird_Sound = Sound(str(SOUND_DIR / 'oldBird.mp3'))
    #Sfx
    #app.cardDraw_Sound = Sound(str(SOUND_DIR / 'cardDraw.mp3'))
    app.playCard_Sound = Sound(str(SOUND_DIR / 'playCard.mp3'))
    #app.cardShuffle_Sound = Sound(str(SOUND_DIR / 'cardShuffle.mp3'))
    app.doorOpen_Sound = Sound(str(SOUND_DIR / 'doorOpen.mp3'))
    
    ### Artifacts:
    app.Voodoo_IdolPos = False ### When you take damage, they take damage. On kill heal
    app.ArchMagi_StaffPos = False ### Damage amp and magic recovery
    app.Crystal_BallPos = False ### Max mana increase
    app.Branch_Of_YggdrassilPos = False ### Heal at the end of each turn
    app.Sigil_Of_ArcanistPos = False ### authority 
    app.Shattered_CrownPos = False ### extra mana to health
    app.Magic_RobesPos = False ### damage reduction
    app.Cloak_Of_MidnightPos = False ### Chance to negate Damage
    app.Token_Of_Holy_OrderPos = False ### authority
    app.Enchanted_EarringsPos = False ### Magic recovery
    app.Enchanted_RingPos = False ### Magic recovery
    app.Amulet_Of_ProtectionPos = False ### Damage reduction
    app.Wooden_StavePos = False ### shite staff
    app.Rabbits_FootPos = False ### Luck
    app.Dice_Of_DestinyPos = False ### Reroll drops
    app.Pixie_In_A_JarPos = False ### Bailout
    app.Harp_Of_LyraPos = False ### Harp effect and better stave
    app.Pocket_CompassPos = False ### Reveals shop on entrance
    app.Circlet_Of_Clear_ThoughtPos = False ### Max mana
    app.Scarf_Of_EvasionPos = False ### dodge chance
    app.Alchemist_BagPos = False ### increases duration of buff effects
    app.Alchemist_GlovesPos = False ### Increases poison res
    ### need to add more "enchanted" gear and luck stat/gear

    app.Voodoo_Idol = str(MEDIA_DIR / 'Final_Scroll.png') ### When you take damage, they take damage. On kill heal
    app.ArchMagi_Staff = str(MEDIA_DIR / 'Final_Scroll.png') ### Damage amp and magic recovery
    app.Crystal_Ball = str(MEDIA_DIR / 'Final_Scroll.png') ### Max mana increase
    app.Branch_Of_Yggdrassil = str(MEDIA_DIR / 'Final_Scroll.png') ### Heal at the end of each turn
    app.Sigil_Of_Arcanist = str(MEDIA_DIR / 'Final_Scroll.png') ### authority 
    app.Shattered_Crown = str(MEDIA_DIR / 'Final_Scroll.png') ### extra mana to health
    app.Magic_Robes = str(MEDIA_DIR / 'Magic_Robes.png') ### damage reduction
    app.Cloak_Of_Midnight = str(MEDIA_DIR / 'Final_Scroll.png') ### Chance to negate Damage
    app.Token_Of_Holy_Order = str(MEDIA_DIR / 'Final_Scroll.png') ### authority
    app.Enchanted_Earrings = str(MEDIA_DIR / 'Enchanted_Earrings.png') ### Magic recovery
    app.Enchanted_Ring = str(MEDIA_DIR / 'Enchanted_Ring.png') ### Magic recovery
    app.Amulet_Of_Protection = str(MEDIA_DIR / 'Amulet_Of_Protection.png') ### Damage reduction
    app.Wooden_Stave = str(MEDIA_DIR / 'Wooden_Stave.png') ### shite staff
    app.Rabbits_Foot = str(MEDIA_DIR / 'Final_Scroll.png') ### Luck
    app.Dice_Of_Destiny = str(MEDIA_DIR / 'Final_Scroll.png') ### Reroll drops
    app.Pixie_In_A_Jar = str(MEDIA_DIR / 'Final_Scroll.png') ### Bailout
    app.Harp_Of_Lyra = str(MEDIA_DIR / 'Final_Scroll.png') ### Harp effect and better stave
    app.Pocket_Compass = str(MEDIA_DIR / 'Final_Scroll.png') ### Reveals shop on entrance
    app.Circlet_Of_Clear_Thought = str(MEDIA_DIR / 'Final_Scroll.png') ### Max mana
    app.Scarf_Of_Evasion = str(MEDIA_DIR / 'Final_Scroll.png') ### dodge chance
    app.Alchemist_Bag = str(MEDIA_DIR / 'Final_Scroll.png') ### increases duration of buff effects
    app.Alchemist_Gloves = str(MEDIA_DIR / 'Final_Scroll.png') ### Increases poison res

    app.Voodoo_IdolDesc = 'Make your enemies share your pain.\nConsume fallen enemies life force.'#maybe add to some demonic item
    app.ArchMagi_StaffDesc = 'A staff of a legendary archmage,\nsure to amplify your damage.'
    app.Crystal_BallDesc = 'A vessel fit for storing magic,\nwill increase your mana capacity.'
    app.Branch_Of_YggdrassilDesc = 'A branch overflowing with life,\nwill recover your health a\nthe end of each turn.'
    app.Sigil_Of_ArcanistDesc = 'Holds an authority'
    app.Shattered_CrownDesc = 'An ancient crown, its main gem shattered.\nConverts excess mana into health.'
    app.Magic_RobesDesc = 'Robes imbued with firm mana structures.\nAttacks will lose force before reaching you.'
    app.Cloak_Of_MidnightDesc = 'Made of the darkest cloth,\nwith magical stars scattered throughout its form,\nthis robe has a chance to absorb enemy attacks.'
    app.Token_Of_Holy_OrderDesc = 'Holds an authority.'
    app.Enchanted_EarringsDesc = 'Earrings imbued with a magic gathering formation.\nWill increase your mana regeneration.'
    app.Enchanted_RingDesc = 'A ring imbued with a magic gathering formation.\nWill increase your mana regeneration.'
    app.Amulet_Of_ProtectionDesc = 'An amulet imbued with a spell of protection.\nWill negate part of the enemies attack.'
    app.Wooden_StaveDesc = 'A primitive wooden stave.\nMay help you cast spells.'
    app.Rabbits_FootDesc = 'A rabbits foot.'
    app.Dice_Of_DestinyDesc = 'Mystical dice, interweaved with fate.'
    app.Pixie_In_A_JarDesc = 'A pixie trapped in a jar,\ncan be released to help you escape.'
    app.Harp_Of_LyraDesc = 'A spiritual harp that plays itself.\nHearing it floods you with warmth.'
    app.Pocket_CompassDesc = 'A compass imbued with the location of shops.\nReveals shop locations on the map.'
    app.Circlet_Of_Clear_ThoughtDesc = 'A circlet that clears your mind.\nHelps you retain your mana.'
    app.Scarf_Of_EvasionDesc = 'A scarf enchanted by a wind fairy.\nGives you a chance to evade attacks.'
    app.Alchemist_BagDesc = 'An alchemists bag. Enchanted with preservation magic,\nit may increase the potency of potions.'
    app.Alchemist_GlovesDesc = 'An alchemists gloves. Can help prevent\npoison from reaching you.'

    app.drops = { ### not including authorities
        app.Voodoo_Idol : {'damageAMP':0,'VoodooEffect':True,'manaRecovery':0,'manaIncrease':0,'turnHeal':0,'overHeal':False,'damageRED':0,'damageNEG':0,'luckIncrease':0,'reroll':0,'bailout':False,'harp':False,'compass':False,'enhanced_Alchemy':False,'poisonRES':0,'fireRES':0,'windRES':0,'earthRES':0,'thunderRES':0,'waterRES':0,'demonicRES':0,'holyRES':0,'bleedRES':0},
        app.ArchMagi_Staff : {'damageAMP':0.4,'VoodooEffect':False,'manaRecovery':2,'manaIncrease':0,'turnHeal':0,'overHeal':False,'damageRED':0,'damageNEG':0,'luckIncrease':0,'reroll':0,'bailout':False,'harp':False,'compass':False,'enhanced_Alchemy':False,'poisonRES':0,'fireRES':0,'windRES':0,'earthRES':0,'thunderRES':0,'waterRES':0,'demonicRES':0,'holyRES':0,'bleedRES':0},
        app.Crystal_Ball : {'damageAMP':0,'VoodooEffect':False,'manaRecovery':0,'manaIncrease':3,'turnHeal':0,'overHeal':False,'damageRED':0,'damageNEG':0,'luckIncrease':0,'reroll':0,'bailout':False,'harp':False,'compass':False,'enhanced_Alchemy':False,'poisonRES':0,'fireRES':0,'windRES':0,'earthRES':0,'thunderRES':0,'waterRES':0,'demonicRES':0,'holyRES':0},
        app.Branch_Of_Yggdrassil : {'damageAMP':0,'VoodooEffect':False,'manaRecovery':0,'manaIncrease':1,'turnHeal':12,'overHeal':False,'damageRED':0,'damageNEG':0,'luckIncrease':0,'reroll':0,'bailout':False,'harp':False,'compass':False,'enhanced_Alchemy':False,'poisonRES':0,'fireRES':0,'windRES':0,'earthRES':0,'thunderRES':0,'waterRES':0,'demonicRES':0,'holyRES':0,'bleedRES':0},
        app.Shattered_Crown : {'damageAMP':0,'VoodooEffect':False,'manaRecovery':0,'manaIncrease':0,'turnHeal':0,'overHeal':True,'damageRED':0,'damageNEG':0,'luckIncrease':0,'reroll':0,'bailout':False,'harp':False,'compass':False,'enhanced_Alchemy':False,'poisonRES':0,'fireRES':0,'windRES':0,'earthRES':0,'thunderRES':0,'waterRES':0,'demonicRES':0,'holyRES':0,'bleedRES':0},
        app.Magic_Robes : {'damageAMP':0,'VoodooEffect':False,'manaRecovery':0,'manaIncrease':0,'turnHeal':0,'overHeal':False,'damageRED':0.2,'damageNEG':0,'luckIncrease':0,'reroll':0,'bailout':False,'harp':False,'compass':False,'enhanced_Alchemy':False,'poisonRES':0,'fireRES':0,'windRES':0,'earthRES':0,'thunderRES':0,'waterRES':0,'demonicRES':0,'holyRES':0,'bleedRES':0},
        app.Cloak_Of_Midnight : {'damageAMP':0,'VoodooEffect':False,'manaRecovery':0,'manaIncrease':0,'turnHeal':5,'overHeal':False,'damageRED':0,'damageNEG':0.4,'luckIncrease':0,'reroll':0,'bailout':False,'harp':False,'compass':False,'enhanced_Alchemy':False,'poisonRES':0,'fireRES':0,'windRES':0,'earthRES':0,'thunderRES':0,'waterRES':0,'demonicRES':0,'holyRES':0,'bleedRES':0},
        app.Enchanted_Earrings : {'damageAMP':0,'VoodooEffect':False,'manaRecovery':1,'manaIncrease':0,'turnHeal':0,'overHeal':False,'damageRED':0,'damageNEG':0,'luckIncrease':0,'reroll':0,'bailout':False,'harp':False,'compass':False,'enhanced_Alchemy':False,'poisonRES':0,'fireRES':0,'windRES':0,'earthRES':0,'thunderRES':0,'waterRES':0,'demonicRES':0,'holyRES':0,'bleedRES':0},
        app.Enchanted_Ring : {'damageAMP':0,'VoodooEffect':False,'manaRecovery':1,'manaIncrease':0,'turnHeal':0,'overHeal':False,'damageRED':0,'damageNEG':0,'luckIncrease':0,'reroll':0,'bailout':False,'harp':False,'compass':False,'enhanced_Alchemy':False,'poisonRES':0,'fireRES':0,'windRES':0,'earthRES':0,'thunderRES':0,'waterRES':0,'demonicRES':0,'holyRES':0,'bleedRES':0},
        app.Amulet_Of_Protection : {'damageAMP':0,'VoodooEffect':False,'manaRecovery':0,'manaIncrease':0,'turnHeal':0,'overHeal':False,'damageRED':0.2,'damageNEG':0,'luckIncrease':0,'reroll':0,'bailout':False,'harp':False,'compass':False,'enhanced_Alchemy':False,'poisonRES':0,'fireRES':0,'windRES':0,'earthRES':0,'thunderRES':0,'waterRES':0,'demonicRES':0,'holyRES':0,'bleedRES':0},
        app.Wooden_Stave : {'damageAMP':0.2,'VoodooEffect':False,'manaRecovery':0,'manaIncrease':0,'turnHeal':0,'overHeal':False,'damageRED':0,'damageNEG':0,'luckIncrease':0,'reroll':0,'bailout':False,'harp':False,'compass':False,'enhanced_Alchemy':False,'poisonRES':0,'fireRES':0,'windRES':0,'earthRES':0,'thunderRES':0,'waterRES':0,'demonicRES':0,'holyRES':0,'bleedRES':0},
        app.Rabbits_Foot : {'damageAMP':0,'VoodooEffect':False,'manaRecovery':0,'manaIncrease':0,'turnHeal':0,'overHeal':False,'damageRED':0,'damageNEG':0,'luckIncrease':1,'reroll':0,'bailout':False,'harp':False,'compass':False,'enhanced_Alchemy':False,'poisonRES':0,'fireRES':0,'windRES':0,'earthRES':0,'thunderRES':0,'waterRES':0,'demonicRES':0,'holyRES':0,'bleedRES':0},
        app.Dice_Of_Destiny : {'damageAMP':0,'VoodooEffect':False,'manaRecovery':0,'manaIncrease':0,'turnHeal':0,'overHeal':False,'damageRED':0,'damageNEG':0,'luckIncrease':2,'reroll':2,'bailout':False,'harp':False,'compass':False,'enhanced_Alchemy':False,'poisonRES':0,'fireRES':0,'windRES':0,'earthRES':0,'thunderRES':0,'waterRES':0,'demonicRES':0,'holyRES':0,'bleedRES':0},
        app.Pixie_In_A_Jar : {'damageAMP':0,'VoodooEffect':False,'manaRecovery':0,'manaIncrease':0,'turnHeal':0,'overHeal':False,'damageRED':0,'damageNEG':0,'luckIncrease':0,'reroll':0,'bailout':True,'harp':False,'compass':False,'enhanced_Alchemy':False,'poisonRES':0,'fireRES':0,'windRES':0,'earthRES':0,'thunderRES':0,'waterRES':0,'demonicRES':0,'holyRES':0,'bleedRES':0},
        app.Harp_Of_Lyra : {'damageAMP':0.2,'VoodooEffect':False,'manaRecovery':1,'manaIncrease':0,'turnHeal':0,'overHeal':False,'damageRED':0,'damageNEG':0,'luckIncrease':0,'reroll':0,'bailout':False,'harp':True,'compass':False,'enhanced_Alchemy':False,'poisonRES':0,'fireRES':0,'windRES':0,'earthRES':0,'thunderRES':0,'waterRES':0,'demonicRES':0,'holyRES':0,'bleedRES':0},
        app.Pocket_Compass : {'damageAMP':0,'VoodooEffect':False,'manaRecovery':0,'manaIncrease':0,'turnHeal':0,'overHeal':False,'damageRED':0,'damageNEG':0,'luckIncrease':0,'reroll':0,'bailout':False,'harp':False,'compass':True,'enhanced_Alchemy':False,'poisonRES':0,'fireRES':0,'windRES':0,'earthRES':0,'thunderRES':0,'waterRES':0,'demonicRES':0,'holyRES':0,'bleedRES':0},
        app.Circlet_Of_Clear_Thought : {'damageAMP':0,'VoodooEffect':False,'manaRecovery':0,'manaIncrease':1,'turnHeal':0,'overHeal':False,'damageRED':0,'damageNEG':0,'luckIncrease':0,'reroll':0,'bailout':False,'harp':False,'compass':False,'enhanced_Alchemy':False,'poisonRES':0,'fireRES':0,'windRES':0,'earthRES':0,'thunderRES':0,'waterRES':0,'demonicRES':0,'holyRES':0,'bleedRES':0},
        app.Scarf_Of_Evasion : {'damageAMP':0,'VoodooEffect':False,'manaRecovery':0,'manaIncrease':0,'turnHeal':0,'overHeal':False,'damageRED':0,'damageNEG':0.2,'luckIncrease':0,'reroll':0,'bailout':False,'harp':False,'compass':False,'enhanced_Alchemy':False,'poisonRES':0,'fireRES':0,'windRES':0,'earthRES':0,'thunderRES':0,'waterRES':0,'demonicRES':0,'holyRES':0,'bleedRES':0},
        app.Alchemist_Bag : {'damageAMP':0,'VoodooEffect':False,'manaRecovery':0,'manaIncrease':0,'turnHeal':0,'overHeal':False,'damageRED':0,'damageNEG':0,'luckIncrease':0,'reroll':0,'bailout':False,'harp':False,'compass':False,'enhanced_Alchemy':True,'poisonRES':0,'fireRES':0,'windRES':0,'earthRES':0,'thunderRES':0,'waterRES':0,'demonicRES':0,'holyRES':0,'bleedRES':0},
        app.Alchemist_Gloves : {'damageAMP':0,'VoodooEffect':False,'manaRecovery':0,'manaIncrease':0,'turnHeal':0,'overHeal':False,'damageRED':0,'damageNEG':0,'luckIncrease':0,'reroll':0,'bailout':False,'harp':False,'compass':False,'enhanced_Alchemy':False,'poisonRES':0.2,'fireRES':0,'windRES':0,'earthRES':0,'thunderRES':0,'waterRES':0,'demonicRES':0,'holyRES':0,'bleedRES':0},
    }
    app.legendaryDrops = [app.ArchMagi_Staff,app.Shattered_Crown,app.Dice_Of_Destiny] #3
    app.epicDrops = [app.Voodoo_Idol,app.Branch_Of_Yggdrassil,app.Cloak_Of_Midnight,app.Harp_Of_Lyra,app.Crystal_Ball] #5
    app.rareDrops = [app.Magic_Robes,app.Rabbits_Foot,app.Pixie_In_A_Jar,app.Alchemist_Bag,app.Alchemist_Gloves] #5
    app.commonDrops = [app.Amulet_Of_Protection,app.Enchanted_Ring,app.Enchanted_Earrings,
                       app.Wooden_Stave,app.Pocket_Compass,app.Scarf_Of_Evasion,app.Circlet_Of_Clear_Thought] #7
    
    app.rarities = [app.commonDrops,app.rareDrops,app.epicDrops,app.legendaryDrops]

    ### Augment system
    app.item = []
    app.currentItems = []
    app.augmentPulling = False
    app.aug1 = 'None'
    app.aug2 = 'None'
    app.aug3 = 'None'

    for i, aug in enumerate([app.aug1, app.aug2, app.aug3], start=1):
        desc_var = aug + "desc"
        if desc_var in globals():
            setattr(app, f"text{i}", globals()[desc_var])
        else:
            setattr(app, f"text{i}", "Description not found")
    
    ### Visual systems
    app.rain = []
    for i in range(0,30):
        drop = {'x':random.randint(0,1300), 'y':random.randint(600,900), 'speed':random.randint(3,5)}
        app.rain.append(drop)
    app.fireRain = []
    for i in range(0,10):
        drop2 = {'x':random.randint(0,1300), 'y':random.randint(600,900), 'speed':random.randint(3,5)}
        app.fireRain.append(drop2)
    
    ### Label systems
    app.charWidths = {
    'a': 9, 'b': 9.5, 'c': 11.5, 'd': 10, 'e': 7.7, 'f': 10, 'g': 11.7, 'h': 8,
    'i': 5.2, 'j': 7, 'k': 8.5, 'l': 11, 'm': 14.5, 'n': 12, 'o': 8.5, 'p': 15,
    'q': 13, 'r': 8, 's': 9, 't': 10, 'u': 10, 'v': 13, 'w': 12, 'x': 10,
    'y': 9, 'z': 11, 'A': 9, 'B': 9.5, 'C': 11.5, 'D': 10, 'E': 7.5, 'F': 10,
    'G': 11.7, 'H': 8, 'I': 5, 'J': 7, 'K': 8.5, 'L': 11, 'M': 14.5, 'N': 12,
    'O': 8.5, 'P': 15, 'Q': 13, 'R': 8, 'S': 9, 'T': 10, 'U': 10, 'V': 13,
    'W': 12, 'X': 10, 'Y': 9, 'Z': 11, ' ': 15, ',': 2, '.': 2, '!': 2
    }
    
    ### Card Data
    app.cardData = {
    str(MEDIA_DIR / 'EmberFireCard_optimized.png'): {'damage':2, 'effect':'burn', 'effectStack':1, 'manaCost':1,'sound':app.ember_Sound},
    str(MEDIA_DIR / 'FireBreathFireCards_optimized.png'): {'damage':2, 'effect':'burn', 'effectStack':4, 'manaCost':3,'sound':app.dragon_Breath_Sound},
    str(MEDIA_DIR / 'FireBallFireCard_1_optimized.png'): {'damage':4, 'effect':'burn', 'effectStack':4, 'manaCost':5,'sound':app.fireBall_Sound},
    str(MEDIA_DIR / 'MeteorShowerFireCard_1_optimized.png'): {'damage':800, 'effect':'burn', 'effectStack':4, 'manaCost':6,'sound':app.meteor_Sound}, ### immolate would deal damage based on app.currentBurn // another for dealing damage based off how many order cards you have down.
    str(MEDIA_DIR / 'BlazingBeamFireCard_1_optimized.png'): {'damage':6, 'effect':'burn', 'effectStack':1, 'manaCost':4,'sound':app.blazing_Beam_Sound},
    }

    ### Events - crying statue ## zodiac constellations for events
    #Taurus
    #Leo
    #Sagittarius
    #Cancer
    #Aquarius
    #Scorpius
    #Gemini
    #Virgo
    #Libra
    #Capricornus
    #Pisces
    #Aries

    #Constellations?
    #Orion
    
    ### Fire Element
    app.currentBurn = 0
    app.burn = False
    app.orderCount = 0
    app.fireModifier = 0
    
###################################################        
#### GAME FUNCTIONS
###################################################

def hitsShape(originX1,originY1,hittingX1,hittingX2,hittingY1,hittingY2):
    if originX1 in range(hittingX1, hittingX2) and originY1 in range(hittingY1, hittingY2):
        return True

def getWordWidth(app,word):
    return sum(app.charWidths.get(c, 10) for c in word)

def playCard(app, cardUrl):
    card = app.cardData.get(cardUrl)
    if card is None:
        return
   
    if app.currentMana >= card['manaCost']:
        app.damageCount -= card['damage']
        app.currentMana -= card['manaCost']
        
        if card['effect'] == 'burn':
            app.burnAdder += card['effectStack']
            if app.burn == True:
                app.damageCount -= card['damage']
                app.burnAdder += card['effectStack']
        if app.flow==True and app.meter == app.meterMax:
            ### draw / special effect / Sound / water could heal on every cast, earth could give shield, wind could give dodge chance, thunder could give mana regen, fire can give burn stacks, arcane could give order stacks -- must interact with flowEffect to be balanced
            app.burnAdder *= 2
            app.flow = False
        app.playCard_Sound.play()
        app.Hand.remove(cardUrl)
        time.sleep(0.8)
        card['sound'].play()

def burnCard(app, cardUrl):
    card = app.cardData.get(cardUrl)
    if card is None:
        return
    
    app.meter+=1
    if app.currentMana < app.maxMana:
        app.currentMana+=1

    app.burnCard_Sound.play()
    app.Hand.remove(cardUrl)

def updatePlayerStats(app, itemURL):
    item = app.drops.get(itemURL)
    app.luck += item['luckIncrease']
    app.manaMaxIncrease += item['manaIncrease']
    app.magicRecovery += item['manaRecovery']
    app.turnHeal += item['turnHeal']
    app.damageAMP += item['damageAMP']
    app.damageRED += item['damageRED']
    app.damageNEG += item['damageNEG']
    app.fireRES += item['fireRES']
    app.waterRES += item['waterRES']
    app.earthRES += item['earthRES']
    app.windRES += item['windRES']
    app.thunderRES += item['thunderRES']
    app.poisonRES += item['poisonRES']
    app.bleedRES += item['bleedRES']
    app.demonicRES += item['demonicRES']
    app.holyRES += item['holyRES']

    for key in ['VoodooEffect', 'overHeal', 'bailout', 'harp', 'compass', 'enhanced_Alchemy']:
        if item.get(key):
            setattr(app, key.lower(), True)

def betterLabels(app,text,x,y,lineSpacing,**kwargs):
    lines = text.split('\n')
    for i, line in enumerate(lines):
        drawLabel(line,x,y+i*lineSpacing,**kwargs)

def NPCDialogue(app,string,startX,startY):
   words = string.split(' ')
   x = startX
   spaceLength = app.charWidths[' ']
   pastWordLength = 0
   currentWordLength = 0
   for word in words:
       currentWordLength = getWordWidth(app,word)
       x += (currentWordLength*0.5) + spaceLength + (pastWordLength*0.5)
       drawLabel(word,x,startY,fill='white',font='cinzel',size=16)
       pastWordLength = getWordWidth(app,word)
    
def battleStart(app):
    app.enemyHP = 40
    app.currentMana = app.maxMana
    if app.battleEncounter == True:
        if app.currentMonster == app.skeleton_Warrior:
            app.enemyHP = 60
        elif app.currentMonster == app.skeleton_Archer:
            app.enemyHP = 40

def turnStart(app):
    app.currentMana += 2
    for i in range(0,1):
        card = app.Hand[i]
        cardX = app.handX + i *70
        cardY = app.handY
        drawImage(card, cardX, cardY)

def turnEnd(app):
    if app.currentBurn > 0:
        app.damageCount -= app.currentBurn
        app.currentBurn -= 1

def battleEnd(app):
    app.currentBurn = 0
    app.currentMana = 0
def distance(x0, y0, x1, y1):
    return((x1 - x0)**2 + (y1-y0)**2)**0.5
    
def movePlayer(app, moveX, moveY):
    newX = app.pX + moveX
    newY = app.pY + moveY
    
    validMove = False
    for tData in app.mapTiles:
        tileX = tData['tX'] + 20
        tileY = tData['tY'] + 20
        
        if (tileX - 20 <= newX <= tileX + 20 and tileY - 20 <= newY <= tileY + 20):
            validMove = True
            break
        
    if validMove:
        app.pX = newX
        app.pY = newY
        app.MmTF = False
        
##################################################################
###Start Screen
##################################################################
 
def start_redrawAll(app):

    drawCircle(app.mX, app.mY, 0.5,opacity=app.startToggle, fill = gradient('white', 'lightBlue', 'blue', start = 'top'))

    drawRect(0,0,350,560, fill = 'tan', border = 'black')
    drawImage(app.dungeonCorridorBG,350,-40)
    drawImage(app.yggdrasil, 0, 0, opacity=app.startToggle)          #BackgroundImage
    
    drawRect(840, 0, 560, 560, fill = gradient ('black', 'black', 'midnightBlue', 'black', 'black', start = 'left'),opacity = app.startToggle)  #RightPanel
    
    drawRect(app.LX1-200, app.LY1-30, app.RW1, app.RH1, fill = 'lightBlue', border = 'silver', opacity = app.startToggle)
    drawRect(app.LX1-100, app.LY1+95, app.RW1-200, app.RH1-30, fill = 'lightBlue', border = 'silver', opacity = app.startToggle)
    
    drawLabel('BEGIN  JOURNEY', app.LX1, app.LY1+5, font = 'cinzel', fill =  'Crimson', border = 'silver', borderWidth = 0.5, bold = True, size = 40, opacity = app.startToggle)
    drawLabel('SETTINGS', app.LX1, app.LY1+115, font = 'cinzel', fill = 'Crimson', border = 'silver', borderWidth = 0.5, size = 30, opacity = app.startToggle)
    
    drawLabel('ESSENCE BOUND',650, 70, font = 'cinzel', fill = 'crimson', border = 'silver', borderWidth = 2, size = 80, opacity = app.startToggle)

    NPCDialogue(app, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 520, 120) # BLYAAAAT
    NPCDialogue(app, 'Greetings, Adventurer!', 520, 250)

def start_onMouseMove(app,mouseX,mouseY):
    app.mX = mouseX
    app.mY = mouseY
    
def start_onMousePress(app,mouseX, mouseY):
    if(hitsShape(app.mX,app.mY,app.LX1-200,app.LX1-200+app.RW1,app.LY1-30,app.LY1-30+app.RH1)==True):
        app.heavyButton.play()
        app.startScreen = False
    if(hitsShape(app.mX, app.mY, app.LX1-100, app.LX1-100+app.RW1-200, app.LY1+95, app.LY1+95+app.RH1-30) == True):
        app.lightButton.play()
        setActiveScreen('settings')

def start_onStep(app):
    if app.startScreen == False:
        app.startToggle -= 2.5
    if app.startToggle == 0:
        setActiveScreen('game')
    app.gameTimer+=1

########################################################################
###Settings Screen
########################################################################

def settings_redrawAll(app):
    drawRect(0, 0, 1300, 560, fill = 'tan')

    drawLabel('Resource UI', 250, 40, font = 'cinzel', fill = 'black', border = 'silver', borderWidth = 0.5, size = 30, bold=True)

    drawRect(160, 80, 180, 40, fill = 'beige', border = None, opacity = app.labelOpacity)
    drawLabel('Labels', 250, 100, font = 'cinzel', fill = 'black', border = 'silver', borderWidth = 0.5, size = 26, bold=True, opacity = app.labelOpacity)

    drawRect(160, 140, 180, 40, fill = 'beige', border = None, opacity = app.barOpacity)
    drawLabel('Bars', 250, 160, font = 'cinzel', fill = 'black', border = 'silver', borderWidth = 0.5, size = 26, bold=True, opacity = app.barOpacity)
    
    drawRect(app.EX1 - 50, app.EY1 - 20, 100, 50, fill = 'lightBlue', border = 'silver')
    drawLabel('EXIT', app.EX1, app.EY1+5, font = 'cinzel', fill = 'Crimson', border = 'silver', borderWidth = 0.5, size = 20, bold=True)

def settings_onMouseMove(app, mouseX, mouseY):
    app.mX = mouseX
    app.mY = mouseY

def settings_onMousePress(app, mouseX, mouseY):
    if(hitsShape(app.mX, app.mY, app.EX1 - 50, app.EX1 - 50 + 100, app.EY1 - 20, app.EY1 + 50)):
        app.lightButton.play()
        setActiveScreen('start')
    if(hitsShape(app.mX, app.mY, 160, 160 + 180, 80, 80 + 40)):
        app.interactButton.play()
        app.labelConfig = not app.labelConfig
        app.barConfig = not app.labelConfig
    if(hitsShape(app.mX, app.mY, 160, 160 + 180, 140, 140 + 40)):
        app.interactButton.play()
        app.barConfig = not app.barConfig
        app.labelConfig = not app.barConfig

def settings_onStep(app):
    if app.labelConfig == True:
        app.labelOpacity = 100
    else:
        app.labelOpacity = 40
    if app.barConfig == True:
        app.barOpacity = 100
    else:
        app.barOpacity = 40
        
#######################################################
###Quest Screen
#######################################################
def quest_onStep(app):
    app.questTimer+=1
def quest_onMousePress(app,mouseX,mouseY):
    if hitsShape(mouseX,mouseY,520,520+60,120+55,120+85) and app.questTimer > 120:
        print('accept')
        app.enemyIconVisToggle1 = True
        app.enemyIconVisToggle2 = True
        app.money_Sound.play()
        app.questIconToggle=True
        setActiveScreen('map')
    elif hitsShape(mouseX,mouseY,520+100,520+160,120+55,120+85) and app.questTimer > 140:
        print('decline')
        app.questIconToggle=False#Sound needed
        setActiveScreen('map')

def quest_redrawAll(app):
    drawImage(app.dungeonCorridorBG, 350, -40)
    drawRect(0, 0, 1400, 600, opacity=40)
    drawImage(app.wizardNPC, 100, 190)
    #NPCDialogue(app, 'Greetings adventurer, I am in dire need of your help.', 520, 120)
    
    # Dialogue setup
    x = 520
    y = 120
    w = 'white'

    # Each tuple: (time threshold, word, x offset, y offset)
    dialogue = [
        (20, 'Hello', 0, 0),
        (25, 'there!', 36, 0),
        (30, "It's", -5, 30),
        (35, 'dangerous', 38, 30),
        (40, 'around', 93, 30),
        (45, 'here,', 133, 30),
        (50, 'could', 168, 30),
        (55, 'you', 200, 30.3),
        (60, 'help', 229, 29.7),
        (65, 'me', 255, 30.5),
        (70, 'clear', 283, 29.8),
        (75, 'this', 312, 29.8),
        (80, 'floor?', 345, 29.8)
    ]

    for t, word, dx, dy in dialogue:
        if app.questTimer > t:
            drawLabel(word, x + dx, y + dy, fill=w, bold=True)
            app.interactButton.play()
    
    # Choices
    if app.questTimer > 120:
        drawLabel('Accept', x+30, y+65, fill='lime', border='lime', size=12)
        app.interactButton2.play()
    if app.questTimer > 140:
        drawLabel('Decline', x+130, y+65, fill='red', border='red', size=12)
        app.interactButton2.play()

#######################################################
###Augment Screen
#######################################################
def aug_redrawAll(app):
    if app.augmentPulling == True:
        drawRect(0,0,1300,560,fill=gradient('black','navy')) # Custom screen # add stars/constellations/spell circles/runes in the background of diff colours.
        x=300
        y=200
        for drop in app.rain:
            drawRect(drop['x'],drop['y'],5,30,fill='lightBlue')
        if app.item[0] == app.commonDrops:
            drawRect(1*x,y,100,100,fill='tan')
            drawImage(app.aug1,1*x,y)
            drawRect(1*x,y,100,100,fill=None,border='darkGrey',borderWidth=3)
        elif app.item[0] == app.rareDrops:
            drawRect(1*x,y,100,100,fill='tan')
            drawImage(app.aug1,1*x,y)
            drawRect(1*x,y,100,100,fill=None,border='blue',borderWidth=3)
        elif app.item[0] == app.epicDrops:
            drawRect(1*x,y,100,100,fill='tan')
            drawImage(app.aug1,1*x,y)
            drawRect(1*x,y,100,100,fill=None,border='purple',borderWidth=3)
        elif app.item[0] == app.legendaryDrops:
            drawRect(1*x,y,100,100,fill='tan')
            drawImage(app.aug1,1*x,y)
            drawRect(1*x,y,100,100,fill=None,border='gold',borderWidth=3)
        if app.item[1] == app.commonDrops:
            drawRect(2*x,y,100,100,fill='tan')
            drawImage(app.aug2,2*x,y)
            drawRect(2*x,y,100,100,fill=None,border='darkGrey',borderWidth=3)
        elif app.item[1] == app.rareDrops:
            drawRect(2*x,y,100,100,fill='tan')
            drawImage(app.aug2,2*x,y)
            drawRect(2*x,y,100,100,fill=None,border='blue',borderWidth=3)
        elif app.item[1] == app.epicDrops:
            drawRect(2*x,y,100,100,fill='tan')
            drawImage(app.aug2,2*x,y)
            drawRect(2*x,y,100,100,fill=None,border='purple',borderWidth=3)
        elif app.item[1] == app.legendaryDrops:
            drawRect(2*x,y,100,100,fill='tan')
            drawImage(app.aug2,2*x,y)
            drawRect(2*x,y,100,100,fill=None,border='gold',borderWidth=3)
        if app.item[2] == app.commonDrops:
            drawRect(3*x,y,100,100,fill='tan')
            drawImage(app.aug3,3*x,y)
            drawRect(3*x,y,100,100,fill=None,border='darkGrey',borderWidth=3)
        elif app.item[2] == app.rareDrops:
            drawRect(3*x,y,100,100,fill='tan')
            drawImage(app.aug3,3*x,y)
            drawRect(3*x,y,100,100,fill=None,border='blue',borderWidth=3)
        elif app.item[2] == app.epicDrops:
            drawRect(3*x,y,100,100,fill='tan')
            drawImage(app.aug3,3*x,y)
            drawRect(3*x,y,100,100,fill=None,border='purple',borderWidth=3)
        elif app.item[2] == app.legendaryDrops:
            drawRect(3*x,y,100,100,fill='tan')
            drawImage(app.aug3,3*x,y)
            drawRect(3*x,y,100,100,fill=None,border='gold',borderWidth=3)
        betterLabels(app,app.text1,1*x-10,y+130,14,fill='lightGray',size=14)
        betterLabels(app,app.text2,2*x-10,y+130,14,fill='lightGray',size=14)
        betterLabels(app,app.text3,3*x-10,y+130,14,fill='lightGray',size=14)
    
def aug_onStep(app):
    for drop in app.rain:
        drop['y'] -= drop['speed']
        if drop['y'] < -61:
            drop['y'] = random.randint(600,900)
            drop['x'] = random.randint(0,1300)

def aug_onMouseMove(app,mouseX,mouseY):
    app.mX = mouseX
    app.mY = mouseY

def aug_onMousePress(app,mouseX,mouseY):
    x=300
    y=200
    if hitsShape(app.mX,app.mY,1*x,1*x+100,y,y+100):
        print('1')
        app.currentItems.append(app.aug1)
        updatePlayerStats(app, app.aug1)
        app.augmentPulling = False
        app.item = []
        app.money_Sound.play()
        setActiveScreen('game') ### add visual stats for items
    if hitsShape(app.mX,app.mY,2*x,2*x+100,y,y+100):
        print('2')
        app.currentItems.append(app.aug2)
        updatePlayerStats(app, app.aug2)
        app.augmentPulling = False
        app.item = []
        app.money_Sound.play()
        setActiveScreen('game')
    if hitsShape(app.mX,app.mY,3*x,3*x+100,y,y+100):
        print('3')
        app.currentItems.append(app.aug3)
        updatePlayerStats(app, app.aug3)
        app.augmentPulling = False
        app.item = []
        app.money_Sound.play()
        setActiveScreen('game')

#######################################################
###Map Screen
#######################################################
def map_redrawAll(app):
    o=60
    drawRect(0,0,1300,560,fill=gradient('black','darkGreen','forestGreen','darkGreen','black',start='top'))
    for tData in app.mapTiles:
        drawRect(tData['tX'], tData['tY'], 40, 40, fill = tData['tFill'], border = 'black', opacity = o)
    
    drawCircle(app.pX,app.pY,5,fill='white',opacity=o+40)#player
    drawImage(app.mapIcon, 10, 500, width = 60, height = 50)
    
    if app.battleEncounter == False:### arrows are made here
        if app.dungeonCorridor == True:
            if app.forwardMove == True:
               drawRect(app.forwardLabelX-10, app.forwardLabelY-10, 20, 20, fill = 'lightGreen', border = 'darkGreen', borderWidth = 2, opacity = 70)
               drawLabel('\u21e7', app.forwardLabelX, app.forwardLabelY, fill = 'darkGreen', size = 16, bold = True, font = 'symbols')
            
            if app.rightMove == True:
               drawRect(app.rightLabelX-10, app.rightLabelY-10, 20, 20, fill = 'lightGreen', border = 'darkGreen', borderWidth = 2, opacity = 70)
               drawLabel('\u21e8', app.rightLabelX, app.rightLabelY, fill = 'darkGreen', size = 16, bold = True, font = 'symbols')
            
            if app.leftMove == True:
               drawRect(app.leftLabelX-10, app.leftLabelY-10, 20, 20, fill = 'lightGreen', border = 'darkGreen', borderWidth = 2, opacity = 70)
               drawLabel('\u21e6', app.leftLabelX, app.leftLabelY, fill = 'darkGreen', size = 16, bold = True, font = 'symbols')
            
            if app.backMove == True:
               drawRect(app.backLabelX-10, app.backLabelY-10, 20, 20, fill = 'lightGreen', border = 'darkGreen', borderWidth = 2, opacity = 70)
               drawLabel('\u21e9', app.backLabelX, app.backLabelY, fill = 'darkGreen', size = 16, bold = True, font = 'symbols')
               
            ### Map Special Tiles 28x28
            drawImage(app.nextFloorIcon,666,127)
            if app.enemyIconVisToggle1 == True:
                drawImage(app.enemyIcon,app.enemyX1,app.enemyY1,visible=app.enemyIconVisToggle1)
            if app.enemyIconVisToggle2 == True:
                drawImage(app.enemyIcon,app.enemyX2,app.enemyY2,visible=app.enemyIconVisToggle2)
            if app.questIconAcceptedToggle == True:
                drawImage(app.questIconAccepted,app.questX+6,app.questY+7,visible=app.questIconAcceptedToggle)
            else:
                drawImage(app.questIcon,app.questX+6,app.questY+8,visible=app.questIconVisToggle1)
            #drawImage() #Shop
            
def map_onStep(app):
    app.questTimer = 0
    for tData in app.mapTiles:
        tCenterX = tData['tX']+20
        tCenterY = tData['tY']+20
        if hitsShape(app.pX, app.pY, tCenterX, tCenterX+5, tCenterY, tCenterY+5):
            tData['tFill'] = 'purple'
            tData['onTile'] = True#
            tData['hasBeenOnTile'] = True
        

        if hitsShape(tCenterX, tCenterY, app.forwardLabelX-5, app.forwardLabelX+5, app.forwardLabelY, app.forwardLabelY+10):
            tData['tFill'] = 'orange'
            tData['adjacentPlayer'] = True
        elif tData['tFill'] != 'orange':
            tData['adjacentPlayer'] = False
            tData['tFill'] = 'grey'
        if hitsShape(tCenterX, tCenterY, app.rightLabelX, app.rightLabelX+10, app.rightLabelY-5, app.rightLabelY+5):
            tData['tFill'] = 'orange'
            tData['adjacentPlayer'] = True
        elif tData['tFill'] != 'orange':
            tData['adjacentPlayer'] = False
            tData['tFill'] = 'grey'
        if hitsShape(tCenterX, tCenterY, app.leftLabelX, app.leftLabelX+10, app.leftLabelY-5, app.leftLabelY+5): ### player hit leftoff for map events
            tData['tFill'] = 'orange'
            tData['adjacentPlayer'] = True
        elif tData['tFill'] != 'orange':
            tData['adjacentPlayer'] = False
            tData['tFill'] = 'grey'
        if hitsShape(tCenterX, tCenterY, app.backLabelX-5, app.backLabelX+5, app.backLabelY, app.backLabelY+10):
            tData['tFill'] = 'orange'
            tData['adjacentPlayer'] = True
        elif tData['tFill'] != 'orange':
            tData['adjacentPlayer'] = False
            tData['tFill'] = 'grey'

        if (
    not hitsShape(tCenterX, tCenterY, app.forwardLabelX-5, app.forwardLabelX+5, app.forwardLabelY, app.forwardLabelY+10)
    and not hitsShape(tCenterX, tCenterY, app.rightLabelX, app.rightLabelX+10, app.rightLabelY-5, app.rightLabelY+5)
    and not hitsShape(tCenterX, tCenterY, app.leftLabelX, app.leftLabelX+10, app.leftLabelY-5, app.leftLabelY+5)
    and not hitsShape(tCenterX, tCenterY, app.backLabelX-5, app.backLabelX+5, app.backLabelY, app.backLabelY+10)
    and tData['tFill'] != 'lightGreen'
            ):
            tData['tFill'] = 'grey'

        if app.MmTF == False and app.battleEncounter == False:
            if random.randint(0,4) == 0:
                app.battleEncounter = True
                if app.currentMonster == app.skeleton_Warrior:
                    app.enemyHP = 60
                elif app.currentMonster == app.skeleton_Archer:
                    app.enemyHP = 40
            else:
                app.MmTF = True

        if tData['hasBeenOnTile'] == True and tData['tFill'] != 'purple' and tData['tFill'] != 'orange':
            tData['tFill'] = 'lightGreen'
    app.forwardLabelX = app.pX
    app.forwardLabelY = app.pY - 40
    
    app.rightLabelX = app.pX + 40
    app.rightLabelY = app.pY
    
    app.leftLabelX = app.pX - 40
    app.leftLabelY = app.pY
    
    app.backLabelX = app.pX
    app.backLabelY = app.pY + 40      
    
    ###Map Toggles
    if app.questIconToggle == False:
        app.questIconVisToggle1 = True
    else:
        app.questIconVisToggle1 = False
        app.questIconAcceptedToggle = True
    if hitsShape(app.pX,app.pY,app.questX,app.questX+40,app.questY,app.questY+40) and app.questIconAcceptedToggle == False:
        setActiveScreen('quest')
    elif hitsShape(app.pX,app.pY,app.questX,app.questX+40,app.questY,app.questY+40) and app.questIconAcceptedToggle == True:
        if app.enemyIconVisToggle1 == False and app.enemyIconVisToggle2 == False:
            print('quest complete')
            app.questStatus = True
    if hitsShape(app.pX,app.pY,app.enemyX1,app.enemyX1+40,app.enemyY1,app.enemyY1+40) and app.enemyIconVisToggle1 == True:
        app.currentMonster = app.skeleton_Warrior
        app.battleEncounter = True
        app.enemyIconVisToggle1 = False
        setActiveScreen('game')
    if hitsShape(app.pX,app.pY,app.enemyX2,app.enemyX2+40,app.enemyY2,app.enemyY2+40) and app.enemyIconVisToggle2 == True:
        app.currentMonster = app.skeleton_Warrior
        app.battleEncounter = True
        app.enemyIconVisToggle2 = False
        setActiveScreen('game')
    
def map_onKeyPress(app, key):
    if app.battleEncounter == False: 
        if key == 'up' and app.forwardMove == True:
            app.interactButton.play()
            movePlayer(app, 0, -40)
            app.MmTF = False
        elif key == 'down' and app.backMove == True:
            app.interactButton.play()
            movePlayer(app, 0, 40)
            app.MmTF = False
        elif key == 'left' and app.leftMove == True:
            app.interactButton.play()
            movePlayer(app, -40, 0)
            app.MmTF = False
        elif key == 'right' and app.rightMove == True:
            app.interactButton.play()
            movePlayer(app, 40, 0)
            app.MmTF = False
        
    if key == 'm':
        app.interactButton.play()
        setActiveScreen('game')
            
            
def map_onMousePress(app, mouseX, mouseY):
    for tData in app.mapTiles:
        if hitsShape(mouseX, mouseY,tData['tX'],tData['tX']+40, tData['tY'], tData['tY']+40) and tData['tFill'] == 'orange' and app.MmTF == True and app.battleEncounter == False:
            app.pX = tData['tX']+20 #????? Marked
            app.pY = tData['tY']+20
            app.MmTF = False
        elif hitsShape(mouseX, mouseY, 10, 70, 500, 550):
            setActiveScreen('game')


#######################################################
###Camp Screen
#######################################################

def camp_redrawAll(app):
    drawImage(app.camp, 250, -300)

         
#######################################################
###Game Screen
#######################################################

def game_redrawAll(app):
    
    #Dungeon Corridor
    if app.dungeonCorridor == True:
        drawImage(app.dungeonCorridorBG,350,-40)
    
    #Visual Effects
    if app.flow == True:
        for drop2 in app.fireRain:
            drawRect(drop2['x'],drop2['y'],5,30,fill='orange',opacity=40)
    
    #Mini Map - Why not draw this in the map screen? - big map should be on Map screen every square that is visible for player (adjacent squares) could be used as a mini map, no?
    
    #drawRect(app.mapOriginX,app.mapOriginY,40,40,fill='grey',border='black',opacity=o)#Origin
    #drawRect(app.mapOriginX,app.mapOriginY-40,40,40,fill='grey',border='black',opacity=o)#up1
    #drawRect(app.mapOriginX,app.mapOriginY-40-40,40,40,fill='grey',border='black',opacity=o)#up2
    #drawRect(app.mapOriginX+40,app.mapOriginY-40-40,40,40,fill='grey',border='black',opacity=o)#up2 right1
    #drawRect(app.mapOriginX-40,app.mapOriginY-40-40,40,40,fill='grey',border='black',opacity=o)#up2 left1
    #drawRect(app.mapOriginX-40-40,app.mapOriginY-40-40,40,40,fill='grey',border='black',opacity=o)#up2 left2
    #drawRect(app.mapOriginX+40,app.mapOriginY,40,40,fill='grey',border='black',opacity=o)#right1
    #drawRect(app.mapOriginX-40,app.mapOriginY,40,40,fill='grey',border='black',opacity=o)#left1
    #drawRect(app.mapOriginX-40-40,app.mapOriginY,40,40,fill='grey',border='black',opacity=o)#left2
    
    
    
    o=60
    
    
    drawRect(1110, 0, 200, 150, fill = 'slateGrey', border = 'silver', opacity = 80)
    for tData in app.mapTiles:
        tileX = tData['tX'] + 20
        tileY = tData['tY'] + 20
        dist = distance(app.pX, app.pY, tileX, tileY)
        if dist <= 50:
            offsetX = 1210 - app.pX
            offsetY = 70 - app.pY
            screenX = tData['tX'] + offsetX
            screenY = tData['tY'] + offsetY
            drawRect(screenX , screenY, 40, 40, fill = tData['tFill'], border = 'black', opacity = o)
    
    drawCircle(1210,70,5,fill='white',opacity=o+40)#player
    #Monster
    basepointX, basepointY, = 540, 100
    if app.battleEncounter == True: # gotta add proper tutorial explanations, then i can remove labels like estimated damage or at least add a setting for it.
        if app.enemyHP > 0:
            drawImage(app.currentMonster,basepointX, basepointY)
            if app.labelConfig == True:
                drawLabel(app.enemyHP,basepointX+100,basepointY,fill='crimson',bold=False,size=40,opacity=100, border='silver', borderWidth = 0.5, font = 'cinzel')
                drawLabel('Estimated Damage',basepointX+340,basepointY,fill='gold',size=20,opacity=100, border='silver', borderWidth = 0.5, font = 'cinzel')
                drawLabel(int(app.damageCount*(1+app.damageAMP)*app.enemyReduction*(1+app.flowEffect)),basepointX+330,basepointY+40,fill='gold',size=20,opacity=100, border='silver', borderWidth = 0.5, font = 'cinzel') # boss bars?
                drawLabel('+',basepointX+350,basepointY+40,fill='gold',size=20,opacity=100, border='silver', borderWidth = 0.5, font = 'cinzel')
                drawLabel(str(app.currentBurn),basepointX+370,basepointY+40,fill='gold',size=20,opacity=100, border='silver', borderWidth = 0.5, font = 'cinzel')
            elif app.barConfig == True:
                drawRect(basepointX+60, basepointY-40, (app.enemyHP * 4) + 1, 20, fill = 'crimson', border = 'black', borderWidth = 2)
                drawRect(basepointX+120, basepointY-40, ((int(app.damageCount*(1+app.damageAMP)*app.enemyReduction*(1+app.flowEffect))*-1) * 4) + 1, 20, fill = 'gold', border = 'black', borderWidth = 2)
                drawRect(basepointX+120, basepointY+20, (app.currentBurn * 4) + 1, 20, fill = 'orange', border = 'black', borderWidth = 2)# fix damage bars
            
    ### Draw and Discard Piles
     #Not sure we need these to be visible - Somewhere in a corner there should be a button to check what is in deck, and discard pile should have an outline imo
#    drawRect(app.deckX-10,app.deckY-10,80,210,fill=None,border='black')
    
#    drawRect(app.deckX,app.deckY,60,90)
    
#    drawRect(app.discardX,app.discardY,60,90)
    
    ### Order Zone
#    drawRect(app.orderX-10,app.orderY-10,80,110,fill=None,border='black')
    
#    drawRect(app.orderX,app.orderY,60,90)
    
    ### Hand
    #drawRect(app.handX-10,app.handY-10,80,110,fill=None,border='black')
    
    #drawRect(app.handX,app.handY,60,90)
    
    ##### The Draw
    #if app.currentCards >= 0:# Only one drawn? - Gameplay wise if you run out of cards you end your turn and wait for next
        #for i in range(len(app.Hand)):
            #for (ix,iy) in app.Hand:
                #print(len(app.Hand))
                #drawImage(app.Hand[app.cardIndex],ix,iy)
                #drawImage(app.Hand[app.cardIndex],app.handX+((app.currentCards-1)*60),app.handY)
                #.add? Cuz -??? drawImage doesnt fucking WORKKKKKKKKKK
        for i in range(len(app.Hand)):
            card = app.Hand[i]
            cardX = app.handX + i *70
            cardY = app.handY
            drawImage(card, cardX, cardY)
        
        # Card Options Buttons
        drawRect(app.oX,app.by - 40,app.bw, 20, fill = None, border = 'silver', visible = app.optionVis)
        drawLabel('CAST', app.oX + 30, app.by - 30, size = 15, fill = 'crimson', border = 'silver', font = 'monospace', visible = app.optionVis)
        
        drawRect(app.oX, app.by - 20, app.bw, 20, fill = None, border = 'silver', visible = app.optionVis)
        drawLabel('BURN', app.oX + 30, app.by - 10, size = 15, fill = 'crimson', border = 'silver', font = 'monospace', visible = app.optionVis)

        #Meter
        drawCircle(428,494,40,fill=app.meterToggle[app.meter])

        drawRect(500, 450, 60, 90) ## discard pile
        #Label with amount maybe later on
        
        drawRect(980, 450, 60, 90) ## deck pile
        drawLabel(len(app.Deck),1080,500, fill='tan', border = 'silver', borderWidth = 0.5, font = 'cinzel',bold=True,size=30)

        #End turn button
        drawRect(1150, 475, 100, 55, fill = 'silver', border = 'black', borderWidth = 10, opacity = 50)
        drawLabel('END', 1200, 500, fill = 'tan', border = 'silver', borderWidth = 0.5, font = 'cinzel', size=30, bold = True)
            
    ### Side Bar UI
    drawRect(app.UIX,app.UIY,350,560,fill=gradient('burlyWood','tan'),border='black')
    
    drawRect(app.UIX+40,app.UIY+60,60,60,fill=None,border='black')
    drawRect(app.UIX+110,app.UIY+60,60,60,fill=None,border='black')
    drawRect(app.UIX+180,app.UIY+60,60,60,fill=None,border='black')
    drawRect(app.UIX+250,app.UIY+60,60,60,fill=None,border='black')
    
    drawRect(app.UIX+40,app.UIY+130,60,60,fill=None,border='black')
    drawRect(app.UIX+110,app.UIY+130,60,60,fill=None,border='black')
    drawRect(app.UIX+180,app.UIY+130,60,60,fill=None,border='black')
    drawRect(app.UIX+250,app.UIY+130,60,60,fill=None,border='black')
    
    drawLabel('INTERFACE', 180, 30,  fill='crimson', border = 'black', borderWidth = 1, font = 'cinzel',bold=True, size=30)
    
    drawImage(app.mapIcon, 10, 500, width = 60, height = 50)
    
    #UI BARS

    if app.labelConfig == True:
        drawLabel(app.playerHP,402,47,fill=app.healthColor, border='silver', borderWidth = 0.5, font = 'cinzel', size=30, bold = True)
    if app.barConfig == True:
        drawRect(350, 32, (app.playerHP * 2) + 1, 20, fill = app.healthColor, border = 'black', borderWidth = 2)

    if app.labelConfig == True:
        drawLabel(app.currentMana,402,83,fill=app.manaColor, border='silver', borderWidth = 0.5, font = 'cinzel', size=20, bold = True)
        drawLabel(app.magicRecovery,432,77,fill='cyan')
    if app.barConfig == True:
        drawRect(350, 62, (app.currentMana * 16) + 9, 20, fill = app.manaColor, border = 'black', borderWidth = 2)
        
        #if (len(app.Hand) > 0 and hitsShape(app.mX,app.mY,app.oX,app.oX+app.bw,app.by - 20 , app.by)):
        #    drawImage(app.Hand[app.x], 300, 100, width = 240, height = 360)
        #    drawRect(540, 70, 300, 420, fill = 'slateGrey', border = 'black', opacity = 70)
def game_onStep(app):
    ### Game Elements
    if app.burnCounter == 3:
        app.burn = True #if app.burn == true toggle vfx
        app.burnCounter = 0
    
    if app.battleEncounter == False:
        app.dungeonAmbienceLoop_Sound.play(loop=True)

    ### Quest
    app.questTimer = 0
    
    ### Value meters/bars

    if app.playerHP > 75:
        app.healthColor = 'limeGreen'
    elif app.playerHP > 50:
        app.healthColor = 'gold'
    elif app.playerHP > 25:
        app.healthColor = 'orange'
    else:
        app.healthColor = 'red'

    ### Battle Start
    
    if app.battleEncounter == True:
        if app.enemyHP <= 0:
            app.battleEncounter = False
            app.currentMana = 9
            app.firstTurn=True
            app.Deck = [*([app.Ember] * 4), *([app.FireBreath] * 4), *([app.FireBall] * 4), *([app.MeteorShower] * 4), *([app.BlazingBeam] * 4)]
            app.Hand = []
            app.canDraw = True
            app.burn = 0
            app.currentMonster = app.skeleton_Monsters[random.randrange(len(app.skeleton_Monsters))] # maybe set current to None if it chooses elsewhere?
            ### BATTLE END ############################################################
            app.burnAdder = 0
            app.currentBurn = 0
            if app.augmentPulling == False:
                if random.randint(0,3) == 3:
                    for i in range (0,3):
                        dictate1 = 1.5*app.luck*random.randint(0,3)
                        if dictate1 >= 0 and dictate1 < 6:
                            dictate2 = 0
                        elif dictate1 >= 6 and dictate1 < 10:
                            dictate2 = 1
                        elif dictate1 >= 10 and dictate1 < 16:
                            dictate2 = 2
                        elif dictate1 >= 16:
                            if random.randint(0,1) == 1:
                                dictate2 = 3
                            else:
                                dictate2 = 2
                        app.item.append(app.rarities[dictate2])
                    app.augmentPulling = True #in attempt to make loop only iterate once
                    x = app.item[0]
                    app.aug1 = x[random.randint(0,len(x)-1)]
                    y = app.item[1]
                    app.aug2 = y[random.randint(0,len(y)-1)]
                    z = app.item[2]
                    app.aug3 = z[random.randint(0,len(z)-1)]
                    setActiveScreen('aug')
    # Deck Refresh
    if len(app.Deck) == 0: # was 1
        app.Deck = [*([app.Ember] * 4), *([app.FireBreath] * 4), *([app.FireBall] * 4), *([app.MeteorShower] * 4), *([app.BlazingBeam] * 4)]
    # Turn Element
    if app.turnOver == True:
        app.turnTimer +=1
        time.sleep(0.03)
        ### Damage recieved before 80 ticks
    if app.turnTimer > 10:
        app.enemyHP+=int(app.damageCount*(1+app.damageAMP)*app.enemyReduction*(1+app.flowEffect)) # enemy takes damage at start of their turn
        if app.currentBurn > 0 and app.firstTurn == False:
            app.enemyHP -= app.currentBurn ### burn damage
        if app.currentBurn <= 1:
            app.currentBurn = 0
        app.currentBurn -= int(app.currentBurn/2)
        if app.currentMonster == app.skeleton_Warrior and app.enemyHP > 0:
            app.action.append((app.skeleton_Warrior_Actions[random.randrange(len(app.skeleton_Warrior_Actions))]))
            print(app.action)
            if app.action[0] == 'slash':
                app.enemy_Slash_Sound.play()
                time.sleep(0.03)
                app.playerDamage+=17
                app.action.pop(0)
            elif app.action[0] == 'thrust':
                app.playerDamage+=33
                app.action.pop(0)
            elif app.action[0] == 'guard':
                app.enemy_Block_Sound.play()
                app.enemyReduction = 0
                app.action.pop(0)
            elif app.action[0] == 'shriek':
                app.currentMana -= 1
                app.action.pop(0)
            if app.playerHP - (app.playerDamage*(1-app.damageRED)) < 0:
                app.playerHP = 0
                app.damageRED = 1
            app.playerHP -= int(app.playerDamage*(1-app.damageRED))
            app.playerDamage = 0
        elif app.currentMonster == app.skeleton_Archer and app.enemyHP > 0:
            app.action.append((app.skeleton_Archer_Actions[random.randrange(len(app.skeleton_Archer_Actions))]))
            print(app.action)
            if app.action[0] == 'power_shot':
                app.enemy_Arrow_Sound.play()
                time.sleep(0.03)
                app.playerDamage+=33*app.enemyIncrease
                app.enemyIncrease = 1
                app.action.pop(0)
            elif app.action[0] == 'enfeebling_arrow':
                app.enemy_Arrow_Sound.play()
                time.sleep(0.03)
                app.playerDamage+=24*app.enemyIncrease
                app.enemyIncrease = 1
                app.action.pop(0)
            elif app.action[0] == 'wait':
                app.enemyIncrease = 1
                app.action.pop(0)
            elif app.action[0] == 'draw':
                app.enemyIncrease = 2
                app.action.pop(0)
            if app.playerHP - (app.playerDamage*(1-app.damageRED)) < 0:
                app.playerHP = 0
                app.damageRED = 1
            app.playerHP -= int(app.playerDamage*(1-app.damageRED))
            app.playerDamage = 0
        time.sleep(0.1)
        ### Item Effects Pre Turn:
        
        ###
        app.damageCount = 0
        app.currentBurn += app.burnAdder
        app.burnAdder = 0
        for i in range(0,app.magicRecovery):
            if app.currentMana < app.maxMana:
                app.currentMana+=1
        app.firstTurn=False
        app.playerHP += app.turnHeal
        app.flowEffect = 0
        app.flow = False
        app.turnOver = False### Turn END ############################################################
        app.canDraw = True
        app.enemyReduction=1
        
        ### Item Effects Post Turn:
        
        ###
        app.turnTimer -= 10

    ### Removing duplicate items
    for itemC in app.currentItems:
        for drop in app.rarities:
            if itemC in drop:
                drop.remove(itemC)
    ##### left off here # need to shift X coord???? deck refresh
    for i in range(0,5):
        if len(app.Hand) < 5 and app.canDraw==True:
            if len(app.Deck) == 0:
                app.Deck = [*([app.Ember] * 4), *([app.FireBreath] * 4), *([app.FireBall] * 4), *([app.MeteorShower] * 4), *([app.BlazingBeam] * 4)]
                app.randomSelect = random.randrange(len(app.Deck))
                app.Hand.append(app.Deck[app.randomSelect])
                app.Deck.pop(app.randomSelect)
                app.currentCards += 1
            elif len(app.Deck) > 0:
                app.randomSelect = random.randrange(len(app.Deck))
                app.Hand.append(app.Deck[app.randomSelect])
                app.Deck.pop(app.randomSelect)
                app.currentCards += 1
    app.canDraw=False
    
     ### Initial Draw
    if len(app.Deck) > 1 and app.canDraw==True:
        app.Hand.append(app.Deck[app.randomSelect])
        app.Deck.pop(app.randomSelect)
        app.randomSelect = random.randrange(len(app.Deck))
        app.currentCards += 1
        app.canDraw=False
    
    if app.drawing == True: ### Single Draw
        app.Hand.append(app.Deck[app.randomSelect])
        app.Deck.pop(app.randomSelect)
        app.randomSelect = random.randrange(len(app.Deck))
        app.currentCards += 1
        app.drawing=False
    ###Tile Checker while in game    
    for tData in app.mapTiles:
        tCenterX = tData['tX']+20
        tCenterY = tData['tY']+20
        
        if hitsShape(app.pX, app.pY, tCenterX, tCenterX+5, tCenterY, tCenterY+5):
            tData['tFill'] = 'purple'
            tData['onTile'] = True
            
        if hitsShape(tCenterX, tCenterY, app.forwardLabelX-5, app.forwardLabelX+5, app.forwardLabelY, app.forwardLabelY+10):
            tData['tFill'] = 'orange'
            tData['adjacentPlayer'] = True
        if hitsShape(tCenterX, tCenterY, app.rightLabelX, app.rightLabelX+10, app.rightLabelY-5, app.rightLabelY+5):
            tData['tFill'] = 'orange'
            tData['adjacentPlayer'] = True
        if hitsShape(tCenterX, tCenterY, app.leftLabelX, app.leftLabelX+10, app.leftLabelY-5, app.leftLabelY+5):
            tData['tFill'] = 'orange'
            tData['adjacentPlayer'] = True
        if hitsShape(tCenterX, tCenterY, app.backLabelX-5, app.backLabelX+5, app.backLabelY, app.backLabelY+10):
            tData['tFill'] = 'orange'   
            tData['adjacentPlayer'] = True
        
        else:
            tData['adjacentPlayer'] = False
        
    # Visual Effects
    if app.flow == True:
        for drop2 in app.fireRain:
            drop2['y'] -= drop2['speed']
            if drop2['y'] < -61:
                drop2['y'] = random.randint(600,900)
                drop2['x'] = random.randint(0,1300)

def game_onKeyPress(app,key):
    if app.battleEncounter == False:
        if key == 'm':
            app.interactButton.play()
            setActiveScreen('map')
    
def game_onMouseMove(app, mouseX, mouseY):
    app.mX = mouseX
    app.mY = mouseY
    
def game_onMousePress(app,mouseX,mouseY):

    if hitsShape(mouseX,mouseY,378,378+80,454,454+80)==True:
        print('Meter Toggle Clicked')
        app.heavyButton.play()
        for i in range (app.meter):
            app.flowEffect+=0.1
        app.flow = True
        app.meter = 0
    
    if hitsShape(mouseX,mouseY,1150,1150+100,475,475+55)==True:
        if app.battleEncounter == True:
            app.turnOver = True
            app.interactButton.play()
    if hitsShape(mouseX, mouseY, 10, 70, 500, 550):
        setActiveScreen('map')
    if len(app.Hand) > 0:
        if hitsShape(mouseX,mouseY,app.bx1,app.bx1+app.bw,app.by,app.by+app.bh):
            if app.optionVis and app.x == 0:
                app.optionVis = False
            else:
                app.x = 0
                app.optionVis = True
                app.oX = app.bx1
                app.interactButton2.play()
        if hitsShape(mouseX,mouseY,app.bx2,app.bx2+app.bw,app.by,app.by+app.bh):
            if app.optionVis and app.x == 1:
                app.optionVis = False
            else:
                app.x = 1
                app.optionVis = True
                app.oX = app.bx2
                app.interactButton2.play()
        if hitsShape(mouseX,mouseY,app.bx3,app.bx3+app.bw,app.by,app.by+app.bh):
            if app.optionVis and app.x == 2:
                app.optionVis = False
            else:
                app.x = 2
                app.optionVis = True
                app.oX = app.bx3
                app.interactButton2.play()
        if hitsShape(mouseX,mouseY,app.bx4,app.bx4+app.bw,app.by,app.by+app.bh):
            if app.optionVis and app.x == 3:
                app.optionVis = False
            else:
                app.x = 3
                app.optionVis = True
                app.oX = app.bx4
                app.interactButton2.play()
        if hitsShape(mouseX,mouseY,app.bx5,app.bx5+app.bw,app.by,app.by+app.bh):
            if app.optionVis and app.x == 4:
                app.optionVis = False
            else:
                app.x = 4
                app.optionVis = True
                app.oX = app.bx5
                app.interactButton2.play()
    
        
    if app.optionVis == True:
        if hitsShape(mouseX,mouseY,app.oX, app.oX+app.bw, app.by - 40, app.by - 20) == True:
            if len(app.Hand) > app.x:
                app.optionVis = False
                playCard(app, app.Hand[app.x])
        elif hitsShape(mouseX,mouseY,app.oX,app.oX+app.bw,app.by - 20,app.by) == True:
            if len(app.Hand) > app.x and app.meter < app.meterMax:
                app.optionVis = False
                burnCard(app, app.Hand[app.x])
                    #if app.Hand[app.x] == 'cmu://697547/39095094/EmberFireCard_optimized.png':
                    #    app.damageCount -= 2
                    #    app.currentBurn += 1
                    #    app.currentMana -= 2
                    #    if app.burn == True:
                    #       app.damageCount -= 2
                    #       app.currentBurn += 1
                    #       app.burn = False
                    #    app.Hand.remove(app.Hand[app.x])
                    #elif app.Hand[app.x] == 'cmu://697547/39095168/FireBallFireCard_1_optimized.png':
                    #    app.damageCount -= 4
                    #    app.currentBurn += 4
                    #    app.currentMana -= 5
                    #    if app.burn == True:
                    #       app.damageCount -= 4
                    #       app.currentBurn += 4
                    #       app.burn = False
                    #    app.Hand.remove(app.Hand[app.x])
                    #elif app.Hand[app.x] == 'cmu://697547/39095111/FireBreathFireCards_optimized.png':
                    #    app.damageCount -= 2
                    #    app.currentBurn += 2
                    #    app.currentMana -= 3
                    #    app.fireModifier += 1
                    #    if app.burn == True:
                    #       app.damageCount -= 2
                    #       app.currentBurn += 2
                    #       app.fireModifier += 1
                    #       app.burn = False
                    #    app.Hand.remove(app.Hand[app.x])
                    #elif app.Hand[app.x] == 'cmu://697547/39095139/MeteorShowerFireCard_1_optimized.png':
                    #    app.damageCount -= (16+2*app.orderCount)
                    #    app.currentBurn += 4+2*app.orderCount
                    #    app.currentMana -= 9
                    #    if app.burn == True:
                    #       app.damageCount -= (16+2*app.orderCount)
                    #       app.currentBurn += 4+2*app.orderCount
                    #       app.burn = False
                    #    app.Hand.remove(app.Hand[app.x])
                    #elif app.Hand[app.x] == 'cmu://697547/39095120/BlazingBeamFireCard_1_optimized.png':
                    #    app.damageCount -= 6
                    #    app.currentBurn += 1
                    #    app.currentMana -= 4
                    #    if app.burn == True:
                    #       app.damageCount -= 6
                    #       app.currentBurn += 1
                    #       app.burn = False
                    #    app.Hand.remove(app.Hand[app.x])
        elif hitsShape(mouseX,mouseY,app.oX,app.oX+app.bw,app.by - 20 , app.by): 
            if len(app.Hand) > app.x:
                app.optionVis = False
                if app.Hand[app.x] == app.Ember:
                   app.currentCard = app.Hand[app.x]
                elif app.Hand[app.x] == app.FireBall:
                    app.currentCard = app.Hand[app.x]
                elif app.Hand[app.x] == app.FireBreath:
                    # if len(custom_string) > 0: draw image(custom_string)
                    app.currentCard = app.Hand[app.x]
                elif app.Hand[app.x] == app.MeteorShower:
                    app.currentCard = app.Hand[app.x]
                elif app.Hand[app.x] == app.BlazingBeam:
                    app.currentCard = app.Hand[app.x]   
                    
#############################################################
###Main
#############################################################
                
def main():
    runAppWithScreens(initialScreen='start', width = 1300, height = 560)
main()




