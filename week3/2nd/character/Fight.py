import random
from time import sleep

class Fight():
    """docstring for Fight"""
    def __init__(self, orc, hero):
        self.orc = orc
        self.hero = hero

    def __attack_turn(self):
        x = random.random() * 100
        if x < 50:
            damage = self.orc.attack()
            self.hero.take_damage(damage)
            print("The orc attacked with {0} power - hero health = {1}\n".format(damage, self.hero.get_health()))
        else:
            damage = self.hero.attack()
            self.orc.take_damage(damage)
            print("The hero attacked with {0} power - orc health = {1}\n - ".format(damage, self.orc.get_health()))

    def simulate_fight(self):
        print("\t--- THE FIGHT TO DEATH BEGINS ---\n\n")
        while self.orc.health > 0 and self.hero.health:
            self.__attack_turn()
            sleep(1)
        if self.orc.health == 0:
            print("The orc is dead\n")
        else:
            print("The hero is dead\n")
