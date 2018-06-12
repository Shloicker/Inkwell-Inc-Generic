import text_adventure, game_items, game_enemies, game_map
from game_player import player_inventory, player_currency

player = text_adventure.player(player_inventory, player_currency)
room = text_adventure.tile_exists(player.location_x, player.location_y)
print(room.show_room_text())
while player.is_not_dead() and not player.victory:
    room = text_adventure.tile_exists(player.location_x, player.location_y)
    room.victory(player)
    if player.is_not_dead() and not player.victory:
        available_actions = room.available_actions()
        directions = ""
        if text_adventure.MoveNorth in available_actions:
            directions += "^"
        if text_adventure.MoveSouth in available_actions:
            directions += "v"
        if text_adventure.MoveWest in available_actions:
            directions += "<"
        if text_adventure.MoveEast in available_actions:
            directions += ">"
        if directions != "":
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
                        for item in text_adventure.objects_list:
                            if item.name.lower() in action_input:
                                bools_arg.append(True)
                                print("\n" + player.do_action(action, item))
                            else:
                                bools_arg.append(False)
                        if not any(bools_arg):
                            print("\nThere is no such thing.")
                    else:
                        print("\n" + player.do_action(action))
                    break
                bools_strings.append(False)
            if any(bools_strings):
                break
            bools_actions.append(False)
        if not any(bools_actions):
            print("You can't do that.")
