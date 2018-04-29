import text_adventure, objects, pytest, random
from objects import player

def test_victory_room():
    player.move_east() 
    player.move_east()
    text_adventure.tile_exists(player.location_x, player.location_y).victory(player) 
    assert player.victory
    player.move_west()
    player.move_west()
    
def test_adjacent_moves():
    assert text_adventure.tile_exists(player.location_x, player.location_y).adjacent_moves() == [text_adventure.MoveEast, text_adventure.MoveWest, text_adventure.MoveNorth, text_adventure.MoveSouth]
    player.move_east()
    assert text_adventure.tile_exists(player.location_x, player.location_y).adjacent_moves() == [text_adventure.MoveEast, text_adventure.MoveWest]
    player.move_west()
    
def test_show_room_text():
    assert text_adventure.tile_exists(player.location_x, player.location_y).show_room_text() == "You are in the starting room."
    player.move_north()
    assert text_adventure.tile_exists(player.location_x, player.location_y).show_room_text() == "This room has a bandit in it."
    text_adventure.tile_exists(player.location_x, player.location_y).enemy.hp = -100
    assert text_adventure.tile_exists(player.location_x, player.location_y).show_room_text() == "This room has a dead bandit in it."
    text_adventure.tile_exists(player.location_x, player.location_y).enemy.hp = 100
    player.move_south()
    
def test_available_actions():
    player.move_east()
    assert text_adventure.tile_exists(player.location_x, player.location_y).available_actions() == [text_adventure.MoveEast, text_adventure.MoveWest, text_adventure.TakeInventory, text_adventure.Equip, text_adventure.Observe, text_adventure.Consume, text_adventure.LookAround, text_adventure.PickUp, text_adventure.Drop]  
    player.move_west()
    player.move_west()
    #assert text_adventure.tile_exists(player.location_x, player.location_y).available_actions() == [text_adventure.Attack, text_adventure.Flee, text_adventure.Observe]
    text_adventure.tile_exists(player.location_x, player.location_y).enemy.hp = -200
    assert text_adventure.tile_exists(player.location_x, player.location_y).available_actions() == [text_adventure.MoveEast, text_adventure.TakeInventory, text_adventure.Equip, text_adventure.Observe, text_adventure.Consume, text_adventure.LookAround, text_adventure.PickUp, text_adventure.Drop]
    text_adventure.tile_exists(player.location_x, player.location_y).enemy.hp = 200
    player.move_east()
    player.move_south()
    assert text_adventure.tile_exists(player.location_x, player.location_y).available_actions() == [text_adventure.MoveNorth, text_adventure.TakeInventory, text_adventure.Equip, text_adventure.Observe, text_adventure.Consume, text_adventure.LookAround, text_adventure.Buy, text_adventure.Sell]  
    player.move_north()
    
def test_view_tile_inventory():
    player.move_east()
    assert text_adventure.tile_exists(player.location_x, player.location_y).view_tile_inventory() == ("Gold Necklace\n1000 Gold")
    player.move_west()
    player.move_south()
    assert text_adventure.tile_exists(player.location_x, player.location_y).view_tile_inventory() == ("Stock:\nSteel Sword\nSteel Armour\nSteel Shield\nThis store has 1000 Gold.")
    player.move_north()
    
def test_pick_up_item():
    player.move_east()
    assert text_adventure.tile_exists(player.location_x, player.location_y).pick_up_item(player, objects.gold) == "You pick up 1000 Gold."
    assert text_adventure.tile_exists(player.location_x, player.location_y).pick_up_item(player, objects.gold_necklace) == "You pick up Gold Necklace."
    player.currency_amount = 100
    text_adventure.tile_exists(player.location_x, player.location_y).drop_item(player, objects.gold_necklace)
    player.move_west()
    
def test_drop_item():
    assert text_adventure.tile_exists(player.location_x, player.location_y).drop_item(player, objects.gold) ==  "Why would you want to do that??"
    assert text_adventure.tile_exists(player.location_x, player.location_y).drop_item(player, objects.iron_sword) ==  "You drop Iron Sword"
    text_adventure.tile_exists(player.location_x, player.location_y).pick_up_item(player, objects.iron_sword)
    
def test_buy_item():
    player.move_south()
    player.currency_amount = 1000
    assert text_adventure.tile_exists(player.location_x, player.location_y).buy_item(player, objects.steel_sword) == "You have bought Steel Sword for 750 Gold.\nYou now have 250 Gold. The shop now has 1750 Gold."
    text_adventure.tile_exists(player.location_x, player.location_y).sell_item(player, objects.steel_sword)
    player.currency_amount = 100
    assert text_adventure.tile_exists(player.location_x, player.location_y).buy_item(player, objects.steel_sword) == "You can't afford that!"
    assert text_adventure.tile_exists(player.location_x, player.location_y).buy_item(player, objects.iron_sword) == "The shop does not have Iron Sword in store."
    text_adventure.tile_exists(player.location_x, player.location_y).shop_currency_amount = 1000
    player.move_north()
    
def test_sell_item():
    player.move_south()
    player.currency_amount = 1000
    text_adventure.tile_exists(player.location_x, player.location_y).buy_item(player, objects.steel_sword)
    assert text_adventure.tile_exists(player.location_x, player.location_y).sell_item(player, objects.steel_sword) == "You have sold Steel Sword for 750 Gold.\nYou now have 1000 Gold. The shop now has 1000 Gold."
    player.currency_amount = 100
    text_adventure.tile_exists(player.location_x, player.location_y).shop_currency_amount = 0
    assert text_adventure.tile_exists(player.location_x, player.location_y).sell_item(player, objects.iron_sword) == "The store can't afford that!"
    assert text_adventure.tile_exists(player.location_x, player.location_y).sell_item(player, objects.steel_armour) == "You have no Steel Armour to sell."
    text_adventure.tile_exists(player.location_x, player.location_y).shop_currency_amount = 1000
    player.move_north()
    
def test_enemy_attack():
    player.move_west()
    random.seed(100)
    assert text_adventure.tile_exists(player.location_x, player.location_y).enemy_attack(player) == "Tough bandit. hits you for 50 damage!\nYou now have 50 HP."
    assert text_adventure.tile_exists(player.location_x, player.location_y).enemy_attack(player) == "You have fallen as Tough bandit. has hit you for 50 damage!"
    player.hp = 100
    random.seed(0)
    assert text_adventure.tile_exists(player.location_x, player.location_y).enemy_attack(player) == "Tough bandit. attacks but misses!"
    player.move_east()
