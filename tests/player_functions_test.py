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
    assert (player.observe(objects.iron_sword)) == ("Iron Sword\n-----\nA sword made of iron.\nValue: 500\nDamage: 50\n")
    assert (player.observe(objects.bandit)) == ("Bandit\n-----\nA fearsome bandit.\nHealth: 100\nDamage: 25\nArmour: 25\nBlock: 25")
    player.move_south()

def test_consume():
    assert (player.consume(objects.bandit)) == "Bandit cannot be consumed."
    assert (player.consume(objects.healing_potion)) == "There is no Healing Potion in your inventory."
    player.inventory.append(objects.healing_potion)
    player.hp = 60
    assert (player.consume(objects.healing_potion)) == "You gain 40 health. You now have 100 HP." and player.inventory == [objects.iron_sword, objects.iron_armour, objects.iron_shield]
    assert (player.consume(objects.iron_sword)) == "Iron Sword cannot be consumed."
