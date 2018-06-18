import game_items

player_inventory = [game_items.iron_sword, game_items.iron_armour, game_items.iron_shield]      #the items that the player will start with
player_currency = 100                                                                           #the amount of currency that the player will start with

#the following section is entirely optional - it allows you to add or remove keywords for player actions

move_north_keywords = ["north"]

move_south_keywords = ["south"]

move_east_keywords = ["east"]

move_west_keywords = ["west"]

take_inventory_keywords = ["inventory"]

attack_keywords = ["attack"]

equip_keywords = ["equip", "put on"]

consume_keywords = ["consume", "use", "drink"]

observe_keywords = ["observe", "look at", "stats"]

look_around_keywords = ["look around", "search", "stock", "sale", "browse"]

drop_keywords = ["drop"]

pick_up_keywords = ["pick up", "retrieve", "retreive", "take"]

buy_keywords = ["buy", "purchase"]

sell_keywords = ["sell"]

flee_keywords = ["flee", "run away", "retreat"]
