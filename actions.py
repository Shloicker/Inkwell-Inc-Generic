from player import player

class action(object):
    def __init__(self, method, name, hotkey, **kwargs):
        self.method = method
        self.name = name
        self.hotkey = hotkey
        self.kwargs = kwargs

    def __str__(self):
        return "{}: {}".format(self.hotkey, self.name)

MoveNorth = action(player.move_north, "Move North", "w")
# class MoveNorth(action):
#     def __init__(self):
#         super(MoveNorth, self).__init__(method=player.move_north, name="Move North", hotkey="w")

MoveSouth = action(player.move_south, "Move South", "s")
# class MoveSouth(action):
#     def __init__(self):
#         super(MoveSouth, self).__init__(method=player.move_south, name="Move South", hotkey="s")

MoveEast = action(player.move_east, "Move East", "a")
# class MoveEast(action):
#     def __init__(self):
#         super(MoveEast, self).__init__(method=player.move_east, name="Move East", hotkey="a")

MoveWest = action(player.move_west, "Move West", "d")
# class MoveWest(action):
#     def __init__(self):
#         super(MoveWest, self).__init__(method=player.move_west, name="Move West", hotkey="d")

TakeInventory = action(player.take_inventory, "Take Inventory", "i")
# class TakeInventory(action):
#     def __init__(self):
#         super(TakeInventory, self).__init__(player.take_inventory, "Take Inventory", "i")

Attack = action(player.attack, "Attack", "r")
# class Attack(action):
#     def __init__(self, enemy):
#         super(Attack, self).__init__(method=player.attack, name="Attack", hotkey="r")

Equip = action(player.equip, "Equip", "e")
# class EquipWeapon(action):
#     def __init__(self):
#         super(EquipWeapon, self).__init__(method=player.equip_weapon, name="Equip Weapon", hotkey="e")

ViewEquippedItems = action(player.view_equipped_items, "View Equipped Items", "v")
# class ViewEquippedItems(action):
#     def __init__(self):
#         super(ViewEquippedItems, self).__init__(method=player.view_equipped_items, name="View Equipped Items", hotkey="v")

Observe = action(player.observe, "Observe", "o")
# class Observe(action):
#     def __init__(self, subject):
#         super(Observe, self).__init__(method=player.observe, name="Observe", hotkey="o", subject=subject)

LookAround = action(player.look_around, "Look for Loot", "p")

Drop = action(player.drop, "Drop", "j")

PickUp = action(player.pick_up, "Pick Up", "l")

Buy = action(player.buy, "Buy", "n")

Sell = action(player.sell, "Sell", "m")

Flee = action(player.flee, "Flee", "f")