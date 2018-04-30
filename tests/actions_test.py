import text_adventure, pytest, objects, random
from objects import player

def test_move():
    assert (player.do_action(text_adventure.MoveEast)) == "This is a room with loot in it."
    player.move_west()

def test_take_inventory():
    assert (player.do_action(text_adventure.TakeInventory)) == "Iron Sword\nIron Armour\nIron Shield\n100 Gold.\nYou have 100 HP."

def test_attack():
    random.seed(0)
    player.equip(objects.iron_sword)
    player.move_north()
    assert player.do_action(text_adventure.Attack) == "You hit Bandit with Iron Sword (equipped), dealing 37 damage!\nBandit now has 63 HP.\nBandit hits you for 25 damage!\nYou now have 75 HP."
    player.hp = 100
    objects.bandit.hp = 100
    objects.iron_sword.equipped_as_weapon = False
    player.move_south()

def test_equip():
    assert player.do_action(text_adventure.Equip, objects.iron_sword) == "You have equipped Iron Sword (equipped) as weapon."
    assert player.do_action(text_adventure.Equip, objects.iron_shield) == "You have equipped Iron Shield (equipped) as shield."
    assert player.do_action(text_adventure.Equip, objects.iron_armour) == "You have equipped Iron Armour (equipped) as armour."
    assert player.do_action(text_adventure.Equip, objects.steel_sword) == "There is no Steel Sword in your inventory."
    player.inventory.append(objects.steel_sword)
    player.do_action(text_adventure.Equip, objects.steel_sword)
    assert objects.iron_sword.equipped_as_weapon == False
    objects.steel_sword.equipped_as_weapon = False
    player.inventory.remove(objects.steel_sword)
    objects.iron_shield.equipped_as_shield = False
    objects.iron_armour.equipped_as_armour = False

def test_consume():
    player.hp = 50
    player.inventory.append(objects.healing_potion)
    assert player.do_action(text_adventure.Consume, objects.healing_potion) == "You gain 50 health. You now have 100 HP."

def test_observe():
    assert player.do_action(text_adventure.Observe, objects.iron_sword) == "Iron Sword\n-----\nA sword made of iron.\nValue: 500\nDamage: 50"

def test_look_around():
    player.move_east()
    assert player.do_action(text_adventure.LookAround) == "Gold Necklace\n1000 Gold"
    player.move_west()

def test_drop():
    assert player.do_action(text_adventure.Drop, objects.iron_sword) == "You drop Iron Sword"
    player.do_action(text_adventure.PickUp, objects.iron_sword)

def test_pick_up():
    player.do_action(text_adventure.Drop, objects.iron_sword)
    assert player.do_action(text_adventure.PickUp, objects.iron_sword) == "You pick up Iron Sword."

def test_buy():
    player.move_south()
    player.currency_amount = 1000
    assert player.do_action(text_adventure.Buy, objects.steel_sword) == "You have bought Steel Sword for 750 Gold.\nYou now have 250 Gold. The shop now has 1750 Gold."
    player.do_action(text_adventure.Sell, objects.steel_sword)
    player.move_north()

def test_sell():
    player.move_south()
    assert player.do_action(text_adventure.Sell, objects.iron_sword) == "You have sold Iron Sword for 500 Gold.\nYou now have 1500 Gold. The shop now has 500 Gold."
    player.do_action(text_adventure.Buy, objects.iron_sword)
    player.move_north()

def test_flee():
    random.seed(0)
    player.move_north()
    assert player.do_action(text_adventure.Flee) == "Bandit hits you for 25 damage!\nYou now have 75 HP.\nYou are in the starting room."
