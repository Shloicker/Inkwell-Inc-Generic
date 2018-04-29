import text_adventure

iron_sword = text_adventure.weapon("Iron Sword", "A sword made of iron.", 500, 50)
iron_armour = text_adventure.armour("Iron Armour", "A suit of armour made of iron.", 750, 25)
iron_shield = text_adventure.shield("Iron Shield", "A shield made of iron.", 500, 25)
steel_sword = text_adventure.weapon("Steel Sword", "A sword made of iron.", 750, 60)
steel_armour = text_adventure.armour("Steel Armour", "A suit of armour made of steel.", 1500, 35)
steel_shield = text_adventure.shield("Steel Shield", "A shield made of steel.", 750, 35)
gold_necklace = text_adventure.item("Gold Necklace", "A necklace made of gold.", 1000)
healing_potion = text_adventure.healing_consumable("Healing Potion", "A useful healing potion.", 250, 50)
gold = text_adventure.currency("Gold", "Shiny gold.")

bandit = text_adventure.enemy("Bandit", "A fearsome bandit.", 100, 25, 25, 25)
tough_bandit = text_adventure.enemy("Tough bandit.", "A more fearsome bandit.", 200, 50, 50, 50)

starting_room = text_adventure.starting_room("You are in the starting room.", [], 0)
a_loot_room = text_adventure.loot_room(1, 0, "This is a room with loot in it.", [gold_necklace], 1000)
a_combat_room_bandit = text_adventure.combat_room(0, -1, "This room has a bandit in it.", "This room has a dead bandit in it.", [healing_potion], 100, bandit)
a_combat_room_tough_bandit = text_adventure.combat_room(-1, 0, "This room has a tough bandit in it.", "This room has a dead tough bandit in it.", [healing_potion], 100, tough_bandit)
a_shop_room = text_adventure.shop_room(0, 1, "This is a shop room.", [steel_sword, steel_armour, steel_shield], 1000)

player = text_adventure.player([iron_sword, iron_armour, iron_shield], 100)