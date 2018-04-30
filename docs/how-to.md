# Making a Simple Game

 This guide will take you through a specific example of creating a text game with this library. It is recommended to read the tutorial file before this one. First we will copy the appropriate files into a new directory:

    Basic Game
    |--- game.py
    |--- game_items.py
    |--- game_enemies.py
    |--- game_player.py
    |--- game_map.py

 We can delete the existing code, **with the exception of the import lines**, from the latter four files as we will be creating a game from scratch. We want to create a game with three rooms - the starting room, a boss room and a victory room whereby the player must face the boss to win the game. We will need to create a set of items for the player to use in the fight, an enemy for the player to face and the three rooms. We will also need to specify the player's inventory, which will contain these three items, and their currency amount, which will be zero for this game.
 We start with `game_items.py`, then. We should create a weapon, shield and armour item for the player to use. We also want the enemy in the game to drop a trophy of some sort, so we will create that here:

    >>> iron_sword = weapon("Iron Sword", "A sword made of iron.", 500, 50)
    >>> iron_armour = armour("Iron Armour", "Armour made of iron.", 1500, 25)
    >>> iron_shield = shield("Iron Shield", "A shield made of iron.", 500, 25)
    >>> ancient_amulet = item("Ancient Amulet", "An ancient amulet with curious engravings.", 5000)

 Our sword is worth 500 Gold and does 50 damage, our armour is worth 1500 Gold and provides 25% resistance and our shield is worth 500 Gold and provides a 25% block chance. To specify the player's inventory and currency amount, we edit the `game_player.py` file. To reference the items that we have just created, we will need to prefix them with `game_items`:

    >>> player_inventory = [game_items.iron_sword, game_items.iron_shield, game_items.iron_armour]
    >>> player_currency = 0

 The `game_enemies.py` file will contain just one enemy:

    >>> undead_warrior = enemy("Undead Warrior", "A ancient warrior raised from the dead.", 100, 45, 20, 20)

 Our warrior has 100 HP, deals 45 damage, has 20% resistance to damage and has a 20% chance to block an attack. Finally, we need to construct the map:

    >>> start_room = starting_room("You prepare to face the warrior.", [], 0)
    >>> warrior_room = combat_room(1, 0, "An undead warrior moves to attack you!", "The undead warrior lays where he fell.", [game_items.ancient_amulet], 1000, game_enemies.undead_warrior)
    >>> end_room = victory_room(2, 0, "You have faced your enemy and leave victorious!")

 Our starting room has no loot in it but we still need to specify the tile's contents and its currency amount so we enter an empty list and 0 for the latter two arguments, respectively. The combat room with our warrior in it is east of the starting room. To create the effect of the warrior dropping his amulet when killed, we simply add it to the tile inventory, remembering to add the `game_items` prefix. We also specify that 1000 Gold is to be found in the room. Finally, we want our enemy to be the enemy we created in the `game_enemies.py` file so we enter him as the final argument, remembering the `game_enemies` prefix. The victory room is east of the combat room and otherwise we merely need to specify the text that will be displayed when the player enters it.

 This code will yield us a fully functional if rudimentary game.
