import pytest, text_adventure, objects
from objects import player

def test_inventory():
    assert (player.take_inventory()) == ("Iron Sword\nIron Armour\nIron Shield\n100 Gold.\nYou have 100 HP.")

def test_is_not_dead():
    assert (player.is_not_dead())

def test_move():
    assert player.move_east() == "This is a room with loot in it."
    player.move_west()

def test_observe():
    player.move_north()
    assert (player.observe(objects.iron_sword)) == ("Iron Sword\n-----\nA sword made of iron.\nValue: 500\nDamage: 50")
    assert (player.observe(objects.bandit)) == ("Bandit\n-----\nA fearsome bandit.\nHealth: 100\nDamage: 25\nArmour: 25\nBlock: 25")
    player.move_south()

def test_equip():
    assert (player.equip(objects.bandit)) == ("Bandit cannot be equipped.")
    assert (player.equip(objects.healing_potion)) == ("There is no Healing Potion in your inventory.")
    assert (player.equip(objects.iron_sword)) == ("You have equipped Iron Sword (equipped) as weapon.")
    assert (player.equip(objects.iron_armour)) == ("You have equipped Iron Armour (equipped) as armour.")
    assert (player.equip(objects.iron_shield)) == ("You have equipped Iron Shield (equipped) as shield.")
    objects.iron_sword.equipped_as_weapon = False
    objects.iron_armour.equipped_as_armour = False
    objects.iron_shield.equipped_as_shield = False

def test_gold():
    assert (player.equip(objects.gold)) == ("Gold cannot be equipped.")

def test_buy():
    player.move_south()
    player.currency_amount = 1000
    assert player.buy(objects.steel_shield) == "You have bought Steel Shield for 750 Gold.\nYou now have 250 Gold. The shop now has 1750 Gold."
    player.sell(objects.steel_shield)
    player.move_north()
    player.currency_amount = 100

def test_sell():
    player.move_south()
    player.inventory.append(objects.gold_necklace)
    text_adventure.tile_exists(player.location_x, player.location_y).shop_currency_amount = 1500
    assert (player.sell(objects.gold_necklace)) ==  "You have sold Gold Necklace for 1000 Gold.\nYou now have 1100 Gold. The shop now has 500 Gold."
    player.buy(objects.gold_necklace)
    text_adventure.tile_exists(player.location_x, player.location_y).shop_currency_amount = 1000
    player.inventory.remove(objects.gold_necklace)
    player.move_north()

def test_drop():
    player.inventory.append(objects.gold_necklace)
    assert player.drop(objects.gold_necklace) == "You drop Gold Necklace"
    text_adventure.tile_exists(player.location_x, player.location_y).tile_inventory.remove(objects.gold_necklace)

def test_pickup():
    player.move_east()
    assert player.pick_up(objects.gold_necklace) == "You pick up Gold Necklace."
    player.drop(objects.gold_necklace)
    player.move_west()

def test_attack_noweapon():
    player.move_north()
    assert (player.attack()) == "You need a weapon first!"

# def test_attack_weapon():
#     # player.equip(objects.iron_sword)
#     # assert (player.attack()) ==  ""
#     pass
#
# def test_flee():
#     # assert (player.flee()) == world.tile_exists(self.location_x, self.location_y).enemy_attack(self) + "\n" + self.do_action(moves[r])
#     pass
