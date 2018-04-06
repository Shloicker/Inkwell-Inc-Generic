#to use this file you need to creat a folder in teh same place as theis file and within that folder save an excel file as a .txt file
_world = {}
starting_location = (0, 0)
def load_world():
    with open('resources/world.txt', 'r') as m:
        rows = m.read()
    for y in range(len(rows)):
        colloums = rows[y].split('\t')
        for x in range(len(rows.split('\t'))):
            tile_name = colloums[x].replace('\n' , '')
            if tile_name == 'starting_room':
                starting_location = (x, y)
    _world[(x, y)] = None if tile_name == '' else getattr(__import__(maptilesv2), tile_name)(x, y)