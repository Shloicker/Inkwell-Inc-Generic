from text_adventure.player import player

class action(object):
    def __init__(self, method, name):
        self.method = method
        self.name = name

    def __str__(self):
        return "{}".format(self.name)

class action_arg(action):
    def __init__(self, method, name, prompt):
        self.prompt = prompt
        super(action_arg, self).__init__(method, name)

MoveNorth = action(player.move_north, "move north")

MoveSouth = action(player.move_south, "move south")

MoveEast = action(player.move_east, "move east")

MoveWest = action(player.move_west, "move west")

TakeInventory = action(player.take_inventory, "take inventory")

Attack = action(player.attack, "attack")

Equip = action_arg(player.equip, "equip", "What do you want to equip?")

Consume = action_arg(player.consume, "consume", "What do you want to consume?")

Observe = action_arg(player.observe, "observe", "What do you want to observe?")

LookAround = action(player.look_around, "look around")

Drop = action_arg(player.drop, "drop", "What do you want to drop?")

PickUp = action_arg(player.pick_up, "pick up", "What do you want to pick up?")

Buy = action_arg(player.buy, "buy", "What do you want to buy?")

Sell = action_arg(player.sell, "sell", "What do you want to sell?")

Flee = action(player.flee, "flee")