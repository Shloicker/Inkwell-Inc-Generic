_world = {}

def tile_exists(x, y):
    return _world.get((x, y))

_objects = {}

def object_exists(name):
    return _objects.get(name)

objects_list = []

world_currency = ""
