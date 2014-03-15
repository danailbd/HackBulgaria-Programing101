import Entity

class Orc(Entity.Entity):
    """docstring for Orc"Entity.Entity"""
    def __init__(self, name, berserk_factor, health):
        super().__init__(name, health)
        if berserk_factor > 2:
            self.berserk_factor = 2
        elif berserk_factor < 1:
            self.berserk_factor = 1
        else:
            self.berserk_factor = berserk_factor

    def attack(self):
        return Entity.Entity.attack(self) * self.berserk_factor
