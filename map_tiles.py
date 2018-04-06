import items, enemies, player, random
class maptile:
    def __init__(self, x, y):
        self.x = x 
        self.y = y
    def room_text(self):
        raise NotImplementedError()
    def modify_player(self, player):
        raise NotImplementedError()
        
class Starting_room(maptile):
    def room_text(self):
        return
    def modify_player(self, player):
        pass
    
class loot_room(maptile):
    def __init__(self, x, y, items):
        self.item = []
        super().__init__(x, y)
    def room_text(self):
        return
    def modify_player(self, player, item, n):
        self.player.append(items[n-1])
        self.remove(items[n-1])
        
class Combat_room(maptile):
    def __init__(self, x, y, enemy):
        self.enemy = enemy 
        super().__init__(x, y)
    def modify_player(self, player, combat):
        pass
    class combat():
        def attack(self, item, enemy):
            enemy.hp = enemy.hp - random.randint(0, 1) * wepon.dmg
        def block(self, item, enemy, player, random):
            player.hp = player.hp - max(0, random.randint(0, 1) * enemy.dmg - item.block)
        def player_death(self, player):
            if player. hp <= 0:
                print ()
        def enemy_death(self, enemy):
            if enemy.hp <= 0:
                print ()
