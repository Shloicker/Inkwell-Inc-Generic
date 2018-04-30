from text_adventure import map_tile, starting_room, loot_room, shop_room, combat_room, victory_room
import game_items, game_enemies

starting_room = starting_room("You stand at the entrance to a dark and ominous cave. It beckons you as you prepare for the horrors within.", [], 0)
cave_corridor_1 = loot_room(1, 0, "You step into the darkness. The light from outside quickly dissipates but there is a faint orange light further into the cave.", [], 0)
giant_spider_room = combat_room(2, 0, "You find yourself in an opening lit by torches of everlasting fire. The floor and walls are covered in cobwebs... suddenly, a huge and gruesome Giant Spider decends from above and lands in front of you!", "The dead spider lies where it fell.", [game_items.spider_poison], 100, game_enemies.giant_spider)
merchant_room = shop_room(2, -1, "Miraculously, a daring entrepreneur has set up shop in the dungeon! He asks if you are to be his first customer.", [game_items.steel_sword, game_items.steel_armour, game_items.steel_shield, game_items.healing_potion], 1000)
chest_room = loot_room(2, 1, "You enter room that has a large, unlocked and centrally located chest in it.", [game_items.gold_necklace, game_items.silver_ring], 1000)
cave_corridor_2 = loot_room(3, 0, "You walk into a long and dark passage.", [], 0)
skeleton_room = combat_room(4, 0, "You enter another opening - as you do, a collection of bones on the floor begins to move and rise into the air. Within seconds, they have formed into an undead Skeleton! It picks up a rusted sword from the floor and moves towards you.", "Curiously, a smoking pile of dust in all that remains of the raised entity.", [game_items.rusted_sword], 0, game_enemies.skeleton)
victory_room = victory_room(5, 0, "Having defeated the horrors of the dungeon, you can walk away proud and unharmed!")
