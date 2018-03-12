class item(object):
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value
    def observe(self):
        return "{}\n-----\n{}\nValue: {} gold\n".format(self.name, self.description, self.value)
    def __str__(self):
        return "{}".format(self.name)

class weapon(item):
    def __init__(self, name, description, value, damage):
        self.damage = damage
        super(weapon, self).__init__(name, description, value)
    def observe(self):
        return "{}\n-----\n{}\nValue: {} gold\nDamage: {}\n".format(self.name, self.description, self.value, self.damage)