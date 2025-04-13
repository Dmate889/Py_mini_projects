import classes
import fantasy_names


def hero_creation(list, level,dmg,health):
    death_knight = classes.DeathKnight(fantasy_names.randomize(), health, dmg, "Death Blade", level)
    warrior = classes.Warrior(fantasy_names.randomize(), health, dmg, "Brutal Cut", level)
    mage = classes.Mage(fantasy_names.randomize(), health, dmg, "Fireball", level)
    list.extend([death_knight, warrior, mage])
