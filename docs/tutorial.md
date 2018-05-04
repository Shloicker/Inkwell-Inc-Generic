# Tutorial

### Contents

1. Getting Started
2. Playing the Game
3. Making a Game
    * Items
    * Enemies
    * The Map
4. Conclusion

### Getting Started

 To use this library it is important to maintain the file structure provided:

    Text Adventure
    |--- setup.py
    |--- src/text_adventure
            |--- player
            |--- items.py
            |--- enemies.py
            |--- map_tiles.py
            |--- world.py

 To install the software use ```setup.py```:

    python setup.py install

 Now you can create your own game from anywhere on your computer using the following files but they must be kept together and should not be renamed:

    My Game
    |--- game.py
    |--- game_items.py
    |--- game_player.py
    |--- game_enemies.py
    |--- game_map.py

 The ```game.py``` file should not be edited in any way but the remaining files can be freely edited. In ```game_items.py``` you can create your items - weapons, armour, shields, consumables and basic items. You will also establish the game's currency here (gold by default). In ```game_player.py``` you will tell the game what the player will start with - you will need to reference the items created in ```game_items.py``` to do this. In ```game_enemies.py``` you will create the various enemies for the game. The ```game_map.py``` file is probably the most complicated - here you need to create each map tile by explicitly expressing their coordinates and by referencing both items and enemies. By default these files contain the resources for a demo game so you can play the game immediately to see how it works if you wish. This also provides an example of how to create your content. You can add to the demo game or if you're feeling confident you can backup and delete everything in the files to start with a blank canvas; there are a few things to consider when doing this, though, which will be explained later.

### Playing the Game

 The recommended python version for this program is 2.7.12. To play the game you need to run ```game.py```:

    python game.py

 When the game first starts you will be greeted by the text for the starting room and given a list of actions:

    #based on the demo game
    You stand at the entrance to a dark and ominous cave. It beckons you as you prepare for the horrors within.

    Choose an action:

    move east
    take inventory
    equip
    observe
    consume
    look around
    pick up
    drop

    Action:

 The list of available actions changes depending on what room you are in and if you are in combat or not. To take an action, type it as it appears here. User input is not case sensitive.

    Action: TakE InVentORY

    Iron Sword
    Iron Armour
    Iron Shield
    100 gold.
    You have 100 HP.

If the action requires additional input, you will be prompted to give it:

    Action: drop

    What do you want to drop?iron sword

    You drop Iron Sword

Note that currency is a special item that must simply be referred to as 'gold' or whatever the name of the in-game currency is - you would not refer to an amount of it:

    Action: pick up

    What do you want to pick up?1000 gold

    There is no such thing.

    Choose an action:

    move north
    take inventory
    equip
    observe
    consume
    look around
    pick up
    drop

    Action: pick up

    What do you want to pick up?gold

    You pick up 1000 Gold.

 The following table shows the meanings of each action:

| Action  | Meaning  |
| :------------ |:---------------:|
| Move East    | Move into the room to the east. |
| Move West      | Move into the room to the west. |
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

 In combat you need to consider the health, damage, armour and block of yourself and the enemy you are facing. Health and damage are self explanatory; armour is resistance to damage and block is the chance to dodge or block an attack.

    Action: observe

    What do you want to observe?giant spider

    Giant Spider
    -----
    A venomous spider as large as a bear.
    Health: 200
    Damage: 25
    Armour: 15
    Block: 15

    Choose an action:

    attack
    flee
    observe

    Action: attack

    You hit Giant Spider with Iron Sword (equipped), dealing 42 damage!
    Giant Spider now has 158 HP.
    Giant Spider hits you for 18 damage!
    You now have 82 HP.

 You can win the game by entering a 'victory room' - a special class of room - although if there is no victory room in the game then there is no win condition. The only way to lose is by dying.

### Making a Game

 To make a game you need to edit ```game_items.py```, ```game_enemies.py```, ```game_player.py``` and ```game_map.py```. These files should not be renamed and need to be in the same directory as ```game.py```. The imports of each file should not be edited either. We will discuss what to do with each file in turn; editing ```game_player.py``` is trivial so we will include this under Items.

#### Items

 The items file contains all of the items that your game will use. The import line at the top should read:

     >>> from text_adventure import item, weapon, shield, armour, healing_consumable, currency

 As indicated by this code, you can make five different types of item as well as an additional special item - currency. An 'item' is a generic item and only has a name, description and value. The value determines how much money the player can buy or sell the item for. The first two arguments are strings and the third is an integer:

    #name, description, value
    >>> gold_necklace = item("Gold Necklace", "A necklace made of gold.", 1000)

 A 'weapon' takes an additional argument, damage, an integer:

    #name, description, value, damage
    >>> iron_sword = weapon("Iron Sword", "A sword made of iron.", 500, 50)

 A 'shield' takes block as an argument, again an integer. This represents the percentage dodge chance that the player will have if they equip the item - keep in mind that the player will have a base dodge chance of 10% if they do not equip a shield.

    #name, description, value, block
    >>> iron_shield = shield("Iron Shield", "A shield made of iron.", 500, 25)

 An 'armour' item takes armour value as an argument, an integer representing the damage reduction that the armour will provide (e.g. an armour item with an armour value of 25 will give a 25% damage reduction).

    #name, description, value, armour value
    >>> iron_armour = armour("Iron Armour", "Armour made of iron.", 1000, 25)

 A healing consumable takes a healing value as an argument, an integer representing the amount of health the player will gain if they consume it. You could make this value negative if you wish.

    #name, description, value, healing value
    >>> healing_potion = healing_consumable("Healing Potion", "A useful healing potion.", 250, 50)

 Finally we have the currency class - __you should make exactly one item of this type__. This will simply determine how currency is referred to in certain contexts, such as when taking inventory, and you should not create instances of it in-game by adding it to the player's starting inventory or to any map tiles. It only requires a name and description:

    #name, description
    >>> gold = currency("Gold", "Valuable gold coins.")

 Note that, while the player will refer to items by their names, when referencing your items in ```game_player.py``` and ```game_map.py```, you will need to refer to them by their python ID, such as 'iron_sword.' Additionally, take caution when creating similar items - creating two items with the same string name will break the game as the player will only be able to refer to one of them.

 Finally, editing ```game_player.py``` is trivial; 'player_inventory' is the list of items that the player will start with and it can be empty. Remember to use the 'game_items' prefix on each item you reference. 'player_currency' is an integer that represents the amount of currency that the player will start with. Do not include your currency item in the player inventory - you are not supposed to create instances of it in-game.

    >>> player_inventory = [game_items.iron_sword, game_items.iron_shield, game_items.iron_armour]
    >>> player_currency = 100

#### Enemies

 The ```game_enemies.py``` file contains the enemies that will be encountered in your game. Its import line should again by kept intact and reads:

    from text_adventure import enemy

 There is only one type of enemy that you can create, but it takes no less than six arguments:

    #name, description, hp, damage, armour, block
    >>> bandit = enemy("Bandit", "A scary bandit.", 100, 50, 25, 25)

 Similarly to in the case of armour and shield items, the armour value determines their resistance to damage and the block value determines their chance to dodge or block an attack. Note that enemies do not carry items but you can give the impression that they have dropped items when killed by adding such items to their tile - this will be discussed in the following section. Also at this stage in development it is not recommended to include more than one instance of the same enemy in game as this may lead to oddities with the code - you should also avoid creating two enemies with the same string name as with items.

#### The Map

 Creating your map is a bit more complicated than the other components of the game. You must edit the ```game_map.py``` file; once again the import lines must be kept intact and should read:

    >>>from text_adventure import map_tile, starting_room, loot_room, shop_room, combat_room, victory_room
    >>>import game_items, game_enemies

 When creating map tiles you will need to give their coordinates explicitly as arguments so it may help to sketch your map before writing this file rather than trying to maintain a mental image of it. Naturally you should not create two rooms that have the same coordinates. Also note that the y axis is inverted so a room with coordinates (0, 1) will be south of a room with coordinates (0, 0) rather than north of it. Additionally, keep in mind that the player will be able to travel between any two rooms that are adjacent to one another. The first type of room, then, is the loot room, which serves as your basic room. The player can pick up and drop items and currency here. It takes 5 arguments:

    #x, y, description, tile inventory, tile currency amount
    >>> chest_room = loot_room(1, 0, "This room has an open chest in it.", [game_items.gold_necklace], 1000)

 The first two arguments are integers and represent the tile's x coordinate and y coordinate respectively. The third is a string and is the description for the room - this is the text that the player will see every time they enter the room. The fourth is a list of items, which can of course be empty. Remember to prefix each item with 'game_items' as shown. The fifth argument is an integer representing the amount of currency that can be found in the room.

  The starting room is a special loot room but the coordinates are forced to be (0, 0). This is the room that the player will start in and you should __create exactly one room of this type__, or else create a room with coordinates (0, 0). It takes the same arguments as the loot room but with the coordinates omitted:

    #description, tile inventory, tile currency amount
    >>> start_room = starting_room("You begin your journey.", [], 0)

 The shop room takes similar arguments to a loot room but, instead of being able to pick up and drop items, the player can only buy and sell items from the vendor.

    #x, y, description, shop inventory, shop currency amount
    merchant_room = shop_room(0, -1, "This room has a merchant in it.", [game_items.steel_sword, game_items.steel_shield], 1000)

 The shop currency amount determines how much the store can pay for items - the player would not be able to sell an item worth more than 1000 gold here unless they bought something first.

 The combat room is another special loot room that has an enemy in it. It takes seven arguments:

    #x, y, enemy alive description, enemy dead description, tile inventory, tile currency amount, enemy
    bandit_room = combat_room(0, -1, "This room has a bandit in it!", "This room has a dead bandit in it.", [game_items.iron_sword], 100, game_enemies.bandit)

 You must give two descriptions for this room type as the description will change depending on if the enemy is alive or not. The 'enemy' argument is the enemy you want to be in the room - you will need to reference your ```game_enemies.py``` file for this as shown. At this stage it is not recommended to use the same enemy in different rooms as this could lead to confusions in the code. Also note that you cannot have more than one enemy in a room although there is no reason why you could not get creative and create a 'fake' group of enemies as a single enemy in the enemies file - a 'a mob of bandits,' for example. If the player kills the enemy in the room, it will behave as a normal loot room; they can only pick up and drop items once the enemy has been killed so you can easily create the impression that the enemy has dropped the items left in the room.

 The final room type is the victory room - this room will cause the player to win when they enter it and thus end the game. It is recommended to create at least one room of this type as the player will not be able to end the game other than by dying otherwise. It does not require an inventory or tile currency amount:

    #x, y, description
    end_room = victory_room(1, 0, "Victory is yours!")

Finally, take caution when adding items to your map - having duplicates of items can lead to oddities due to current limitations in the code. While having duplicates of generic items and consumables is absolutely fine, duplicates of weapons, shields and armour will create bugs related to equipping.

#### Conclusion

 With that you should have a fully functional game! You will most likely make mistakes so be prepared to encounter error messages when first running the game and to fix elements of your game accordingly.
