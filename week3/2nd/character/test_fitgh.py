import Fight, Orc, Hero, weapon

def main():
    """The test for fighting"""
    weapon1 = weapon.Weapon("Krik", 15 ,0.6)
    weapon2 = weapon.Weapon("BorMashina", 20, 0.8)
    orcFigther = Orc.Orc("BatGeorgi", 1.2, 120)
    heroFigther = Hero.Hero("Zadushavam", "Zatvorenia")
    orcFigther.equip_weapon(weapon1)
    heroFigther.equip_weapon(weapon2)

    charactersFight = Fight.Fight(orcFigther, heroFigther)
    charactersFight.simulate_fight()

if __name__ == "__main__":
    main()
