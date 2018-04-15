import text_adventure, game_items, game_enemies, game_map

player = text_adventure.player([game_items.iron_sword, game_items.iron_armour, game_items.iron_shield], 100)
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
        for action in available_actions:
            if action_input == action.name:
                if type(action) is text_adventure.action_arg:
                    action_arg_input = raw_input("\n" + action.prompt).lower()
                    if text_adventure.object_exists(action_arg_input):
                        print("\n" + player.do_action(action, text_adventure.object_exists(action_arg_input)))
                    else:
                        print("\nThere is no such thing.")
                    break
                print("\n" + player.do_action(action))
                break