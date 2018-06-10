import text_adventure, game_items, game_enemies, game_map
from game_player import player_inventory, player_currency

player = text_adventure.player(player_inventory, player_currency)
room = text_adventure.tile_exists(player.location_x, player.location_y)
print(room.show_room_text())
while player.is_not_dead() and not player.victory:
    room = text_adventure.tile_exists(player.location_x, player.location_y)
    room.victory(player)
    if player.is_not_dead() and not player.victory:
        print("\nChoose an action:\n")
        available_actions = room.available_actions()
        for action in available_actions:
            print(action)
        action_input = raw_input("\nAction: ").lower()
        bools_actions = []
        for action in available_actions:
            if action.name in action_input:
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
                    break
                print("\n" + player.do_action(action))
                break
            else:
                bools_actions.append(False)
        if not any(bools_actions):
            print("You can't do that.")