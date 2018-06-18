from text_adventure.player import player

class action(object):
    def __init__(self, method):
        self.method = method
        self.strings = []

    def __str__(self):
        return self.strings[0]

class action_arg(action):
    pass

MoveNorth = action(player.move_north)

MoveSouth = action(player.move_south)

MoveEast = action(player.move_east)

MoveWest = action(player.move_west)

TakeInventory = action(player.take_inventory)

Attack = action(player.attack)

Equip = action_arg(player.equip)

Consume = action_arg(player.consume)

Observe = action_arg(player.observe)

LookAround = action(player.look_around)

Drop = action_arg(player.drop)

PickUp = action_arg(player.pick_up)

Buy = action_arg(player.buy)

Sell = action_arg(player.sell)

Flee = action(player.flee)
