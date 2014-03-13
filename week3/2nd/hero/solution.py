class Hero():
    def __init__(self, name, nick, health=100):
        self.name = name
        self.health = health
        self.nickname = nick

    def get_health(self):
        return self.health

    def is_alive(self):
        return self.health != 0

    def take_damage(self, dmg_points):
        if(dmg_points > self.health):
            self.health = 0
        else:
            self.health -= dmg_points

    def known_as(self):
        return self.name + " the " + self.nickname

    def take_healing(self, healing_points):
        if(self.health != 0):
            if(self.health+healing_points > 100):
                self.health = 100
            else:
                self.health += healing_points
            return True
        else:
            return False
