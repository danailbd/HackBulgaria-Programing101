import Entity

class Hero(Entity.Entity):
    """docstring for Hero"Entity.Entity"""
    def __init__(self, name, nickname, health=100):
        super().__init__(name, health)
        self.nickname = nickname

    def known_as(self):
        return self.name + " the " + self.nickname
