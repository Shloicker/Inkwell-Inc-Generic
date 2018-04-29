# References

This file contains a list of references of actions, for playing the game, and classes, for creating a game. These can also be found in the tutorial.

#### Actions

The following table shows the meanings of each action in the game:

| Action | Meaning |
| :------------ |:---------------:|
| Move East | Move into the room to the east. |
| Move West | Move into the room to the west. |
| Move North | Move into the room to the north. |
| Move South | Move into the room to the south. |
| Take Inventory | Shows your current inventory, including your gold reserves and health. |
| Equip | Equip a weapon, shield or armour item. You need a weapon equipped to attack enemies while armour and shields optionally offer additional protection. You can only equip one of each type of item at a time. |
| Observe | Provides information on an item or enemy. |
| Consume | Consume a consumable item. |
| Look Around | Lists the items that can be found in your current room. |
| Pick Up | Pick up an item from your current room or pick up the gold in the room if there is any.|
| Drop | Drop an item, leaving it in your current room. |
| Buy | Buy an item from the store in your current room. |
| Sell | Sell an item to the store in your current room. |
| Attack | Attack the enemy in your current room. If the enemy survives, they will attack in turn. |
| Flee | Flee from an enemy to a random adjacent room. You will be attacked as you leave the room. |

#### Items

There are six classes (types) of items by default: generic items, weapons, armour, shields, consumables and currency. Remember that you must create **exactly one** instance of the currency class. The various types are shown here with the arguments that they take with the type of input that will be accepted in brackets.

    my_item = item(name (string), description (string), value (integer))

    my_weapon = weapon(name (string), description (string), value (integer), damage(integer))

    my_shield = shield(name (string), description (string), value (integer), block value (integer))

    my_armour_item = armour(name (string), description (string), value (integer), armour value (integer))

    my_consumable = healing_consumable(name (string), description (string), value (integer), healing amount (integer))

    my_currency = currency(name (string), description (string))

#### Enemies

 There is only one type of enemy that you can create:

    my_enemy = enemy(name(string), description (string), health (integer), damage (integer), armour (integer), block (intger))

#### Map

 There are five types of map tile: starting room, victory room, loot room, combat room and shop room. You must create **exactly one** starting room or else create a room with coordinates (0, 0). You should also create at least one victory room if you want the player to be able to win the game. Remember that the y axis is inverted, so a room with coordinates (0, -1) is north of the starting room.

    my_start_room = starting_room(description (string), tile inventory (list of items), tile currency amount (integer))

    my_loot_room = loot_room(x coordinate (integer), y coordinate (integer), description (string), tile inventory (list of items), tile currency amount (integer))

    my_combat_room = combat_room(x coordinate (integer), y coordinate (integer), description enemy alive (string), description enemy dead (string), tile inventory (list of items), tile currency amount (integer), enemy (enemy))

    my_shop_room = shop_room(x coordinate (integer), y coordinate (integer), description (string), shop inventory (list of items), shop currency amount (integer))

    my_victory_room = victory_room(x coordinate (integer), y coordinate (integer), description (string))