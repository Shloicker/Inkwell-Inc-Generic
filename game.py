import text_adventure, game_items, game_enemies, game_map, game_player

text_adventure.MoveNorth.strings = game_player.move_north_keywords
text_adventure.MoveEast.strings = game_player.move_east_keywords
text_adventure.MoveWest.strings = game_player.move_west_keywords
text_adventure.MoveSouth.strings = game_player.move_south_keywords
text_adventure.TakeInventory.strings = game_player.take_inventory_keywords
text_adventure.Attack.strings = game_player.attack_keywords
text_adventure.Equip.strings = game_player.equip_keywords
text_adventure.Consume.strings = game_player.consume_keywords
text_adventure.Observe.strings = game_player.observe_keywords
text_adventure.LookAround.strings = game_player.look_around_keywords
text_adventure.Drop.strings = game_player.drop_keywords
text_adventure.PickUp.strings = game_player.pick_up_keywords
text_adventure.Buy.strings = game_player.buy_keywords
text_adventure.Sell.strings = game_player.sell_keywords
text_adventure.Flee.strings = game_player.flee_keywords

help_text = "\nThe interpreter searches for key words in the text that you enter so simply use any of the key words for an action in a sentance and the game will attempt to perform that action. To perform an action on items or enemies, you will need to include the corresponding exact name(s) in the sentance. The input is not case sensitive.\n\nKey Words:\n\nMove North: " + ", ".join(game_player.move_north_keywords) + "\nMove South: " + ", ".join(game_player.move_south_keywords) + "\nMove East: " + ", ".join(game_player.move_east_keywords) + "\nMove West: " + ", ".join(game_player.move_west_keywords) + "\nTake Inventory: " + ", ".join(game_player.take_inventory_keywords) + "\nAttack: " + ", ".join(game_player.attack_keywords) + "\nEquip: " + ", ".join(game_player.equip_keywords) + "\nConsume: " + ", ".join(game_player.consume_keywords) + "\nObserve: " + ", ".join(game_player.observe_keywords) + "\nSearch a Room/Browse a Shop: " + ", ".join(game_player.look_around_keywords) + "\nDrop: " + ", ".join(game_player.drop_keywords) + "\nPick Up: " + ", ".join(game_player.pick_up_keywords) + "\nBuy: " + ", ".join(game_player.buy_keywords) + "\nSell: " + ", ".join(game_player.sell_keywords) + "\nFlee: " + ", ".join(game_player.flee_keywords)

player = text_adventure.player(game_player.player_inventory, game_player.player_currency)
room = text_adventure.tile_exists(player.location_x, player.location_y)
print(room.show_room_text())
while player.is_not_dead() and not player.victory:
    room = text_adventure.tile_exists(player.location_x, player.location_y)
    room.victory(player)
    if player.is_not_dead() and not player.victory:
        available_actions = room.available_actions()
        directions = "\n"
        if text_adventure.MoveNorth in available_actions:
            directions += "^"
        if text_adventure.MoveSouth in available_actions:
            directions += "v"
        if text_adventure.MoveWest in available_actions:
            directions += "<"
        if text_adventure.MoveEast in available_actions:
            directions += ">"
        if directions != "\n":
            print(directions)
        action_input = raw_input("\n").lower()
        bools_actions = []
        for action in available_actions:
            bools_strings = []
            for string in action.strings:
                if string in action_input:
                    bools_strings.append(True)
                    bools_actions.append(True)
                    if type(action) is text_adventure.action_arg:
                        bools_arg = []
                        objects = []
                        for item in text_adventure.objects_list:
                            if item.name.lower() in action_input:
                                bools_arg.append(True)
                                objects.append(item)
                            else:
                                bools_arg.append(False)
                        if not any(bools_arg):
                            print("\nThere is no such thing.")
                        else:
                            new_objects = []
                            for item in objects:
                                new_action_input = action_input
                                for other_item in objects:
                                    if not other_item == item:
                                        if item.name.lower() in other_item.name.lower():
                                            new_action_input = new_action_input.replace(other_item.name.lower(), "")
                                if item.name.lower() in new_action_input:
                                    new_objects.append(item)
                            for item in new_objects:
                                print("\n" + player.do_action(action, item))
                    else:
                        print("\n" + player.do_action(action))
                    break
                bools_strings.append(False)
            if any(bools_strings):
                break
            bools_actions.append(False)
        if not any(bools_actions):
            if "help" in action_input:
                    print(help_text)
            else:
                print("You can't do that.")
