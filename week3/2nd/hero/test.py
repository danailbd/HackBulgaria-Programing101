import unittest
import solution

class HeroTest(unittest.TestCase):
    """Testing the hero moduleHeroTest"""
    def setUp(self):
        self.heroName = "Gosho"
        self.heroHp = 80
        self.heroNick = "Goshoto"
        self.hero = solution.Hero(self.heroName, self.heroNick, self.heroHp)

# Testing atributes
    def test_fields_name(self):
        self.assertEquals(self.heroName, self.hero.name)

    def test_fields_Hp(self):
        self.assertEquals(self.heroHp, self.hero.health)

    def test_fields_nick(self):
        self.assertEquals(self.heroNick, self.hero.nickname)

# Testing methods
    def test_known_as(self):
        self.assertEquals(self.heroName + " the " + self.heroNick,
         self.hero.known_as())

    def test_get_health(self):
        self.assertEquals(self.heroHp, self.hero.get_health())

    def test_take_damage(self):
        self.hero.take_damage(20)
        self.heroHp -= 20
        self.assertEquals(self.heroHp, self.hero.health())

    def test_is_alive(self):
        self.assertEquals(True, self.hero.is_alive())
        self.hero.take_damage(100)
        self.assertEquals(False, self.hero.is_alive())

    def test_heal(self):
        self.hero.take_damage(100)
        self.assertEquals(False, self.hero.take_healing(10))

    def test_take_damage(self):
        self.hero.take_healing(15)
        self.heroHp += 15
        self.assertEquals(self.heroHp, self.hero.get_health())

if __name__ == "__main__":
    unittest.main()
