class Entity():
    def __init__(self, name, health):
        self.name = name
        self.max_health = health
        self.health = health
        self.weaponEquiped = None

    def get_health(self):
        return self.health

    def is_alive(self):
        return self.health != 0

    def take_damage(self, dmg_points):
        if(dmg_points > self.health):
            self.health = 0
        else:
            self.health -= dmg_points

    def take_healing(self, healing_points):
        if(self.health != 0):
            if(self.health+healing_points > self.max_health):
                self.health = self.max_health
            else:
                self.health += healing_points
            return True
        else:
            return False

    def has_weapon(self):
        return self.weaponEquiped is not None

    def equip_weapon(self, weapon):
        self.weaponEquiped = weapon

    def attack(self):
        if self.has_weapon():
            return (self.weaponEquiped.damage *
                     self.weaponEquiped.critical_hit())
        else:
            return 0
