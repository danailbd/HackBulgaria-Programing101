import random

class Weapon():
    """docstring for Weapon"""
    def __init__(self, type, damage,
                critical_strike_percent):
        self.type = type
        self.damage = damage
        if critical_strike_percent > 1:
            self.critical_strike_percent = 1.0
        elif critical_strike_percent < 0:
            self.critical_strike_percent = 0.0
        else:
            self.critical_strike_percent = critical_strike_percent

    def critical_hit(self):
        return 1 + int(random.uniform(0,1) < self.critical_strike_percent)
