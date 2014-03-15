import unittest
import Orc
import Hero
import weapon

class OrcTest(unittest.TestCase):
    """Testing the orc moduleorcTest"""
    def setUp(self):
        self.orcName = "Gosho"
        self.orcHp = 120
        self.orcBerserk_factor = 1.4
        self.orc = Orc.Orc(self.orcName, self.orcBerserk_factor,
                        self.orcHp)

# Testing atributes
    def test_fields_name(self):
        self.assertEqual(self.orcName, self.orc.name)

    def test_fields_Hp(self):
        self.assertEqual(self.orcHp, self.orc.health)

    def test_berserk(self):
        self.orc = Orc.Orc("Orcito", 3, 150)
        self.assertEqual(2, self.orc.berserk_factor)

# Testing methods
    def test_get_health(self):
        self.assertEqual(self.orcHp, self.orc.get_health())

    def test_take_damage(self):
        self.orc.take_damage(20)
        self.orcHp -= 20
        self.assertEqual(self.orcHp, self.orc.health())

    def test_is_alive(self):
        self.assertEqual(True, self.orc.is_alive())
        self.orc.take_damage(self.orcHp)
        self.assertEqual(False, self.orc.is_alive())

    def test_heal(self):
        self.orc.take_damage(self.orcHp)
        self.assertEqual(False, self.orc.take_healing(10))

    def test_take_damage(self):
        self.orc.take_damage(30)
        self.assertEqual(self.orcHp-30, self.orc.get_health())
        self.assertEqual(True, self.orc.take_healing(15))
        self.assertEqual(self.orcHp-15, self.orc.get_health())

class HeroTest(unittest.TestCase):
    """Testing the hero moduleHeroTest"""
    def setUp(self):
        self.heroName = "Gosho"
        self.heroHp = 80
        self.heroNick = "Goshoto"
        self.hero = Hero.Hero(self.heroName, self.heroNick)
        self.hero.take_damage(20)

# Testing atributes
    def test_fields_name(self):
        self.assertEqual(self.heroName, self.hero.name)

    def test_fields_Hp(self):
        self.assertEqual(self.heroHp, self.hero.health)

    def test_fields_nick(self):
        self.assertEqual(self.heroNick, self.hero.nickname)

# Testing methods
    def test_known_as(self):
        self.assertEqual(self.heroName + " the " + self.heroNick,
         self.hero.known_as())

    def test_get_health(self):
        self.assertEqual(self.heroHp, self.hero.get_health())

    def test_take_damage(self):
        self.hero.take_damage(20)
        self.heroHp -= 20
        self.assertEqual(self.heroHp, self.hero.health())

    def test_is_alive(self):
        self.assertEqual(True, self.hero.is_alive())
        self.hero.take_damage(100)
        self.assertEqual(False, self.hero.is_alive())

    def test_heal(self):
        self.hero.take_damage(100)
        self.assertEqual(False, self.hero.take_healing(10))

    def test_take_damage(self):
        self.assertEqual(True, self.hero.take_healing(15))
        self.heroHp += 15
        self.assertEqual(self.heroHp, self.hero.get_health())

class TestWeapons(unittest.TestCase):
    """docstring for ClassName"""
    def test_no_weapon(self):
        self.hero = Hero.Hero("Bat", "Goshoto")
        self.assertEqual(False,
                         self.hero.has_weapon())
        self.assertEqual(0,
                        self.hero.attack())

    def test_has_weapon(self):
        self.weapon = weapon.Weapon("Golemiq", 25, 0.6)
        self.hero = Hero.Hero("Bat", "Goshoto")
        self.hero.equip_weapon(self.weapon)
        self.assertEqual(True,
                        self.hero.has_weapon())
        self.assertEqual(50,
                        self.hero.attack())


if __name__ == "__main__":
    unittest.main()
