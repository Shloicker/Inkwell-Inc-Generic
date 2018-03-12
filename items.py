class item:
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value
    def observe(self):
        return "{}\n-----\n{}\nValue: {} gold\n".format(self.name, self.description, self.value)
    def __str__(self):
        return "{}".format(self.name)