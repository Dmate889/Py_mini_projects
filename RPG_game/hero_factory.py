import classes
import fantasy_names


def hero_creation(list):
    death_knight = classes.DeathKnight(fantasy_names.randomize(), 150, 50, "Death Blade")
    warrior = classes.Warrior(fantasy_names.randomize(), 150, 50, "Brutal Cut")
    mage = classes.Mage(fantasy_names.randomize(), 100, 100, "Fireball")
    list.extend([death_knight, warrior, mage])
