class item:
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value
    def __str__(self):
        return "{}\n{}\nValue: {} gold\n".format(self.name, self.description, self.value)