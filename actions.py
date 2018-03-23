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

MoveSouth = action(player.move_south, "Move South", "s")

MoveEast = action(player.move_east, "Move East", "a")

MoveWest = action(player.move_west, "Move West", "d")

TakeInventory = action(player.take_inventory, "Take Inventory", "i")

Attack = action(player.attack, "Attack", "r")          #not sure

EquipWeapon = action(player.equip_weapon, "Equip Weapon", "e")

ViewEquippedItems = action(player.view_equipped_items, "View Equipped Items", "v")

ObserveItem = action(player.observe_item, "Observe Item", "o")