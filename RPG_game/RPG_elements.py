import random
import classes
import time


death_knight = classes.DeathKnight("Arthas",100,50,"Death Coil")
warrior = classes.Warrior("Garrosh",100,50,"Bladestorm")
mage = classes.Mage("Jaina",50,100,"Fireball")

hero_list = [death_knight,warrior,mage]

def hero_selection():
    selection = input("Choose your Hero: "
          "\n1. Garrosh"
          "\n2. Jaina"
          "\n3. Arthas\n")

    match selection:
        case "1":
            return classes.Warrior("Garrosh",100,50,"Bladestorm")
        case "2":
            return classes.Mage("Jaina",50,100,"Blizzard")
        case "3":
            return classes.DeathKnight("Arthas",100,50,"Death Coil")



def fight(first_fighter,second_fighter):
    is_running = True
    while is_running:
        print(f"{first_fighter.name} will make their move and attack {second_fighter.name} with a {first_fighter.special}")
        time.sleep(3)
        damage = random.randint(0,first_fighter.dmg)
        print(f"CRITICAL DAMAGE: {damage}" if damage == first_fighter.dmg else f"The damage was {damage}")
        second_fighter.health -= damage
        time.sleep(3)
        if second_fighter.health > 0:
            print(f"{second_fighter.name} HP: {second_fighter.health}")
            time.sleep(3)
        else:
            print(f"{second_fighter.name} died")
            time.sleep(3)
            break

        print(f"{second_fighter.name} composes themselves and attacks back with {second_fighter.special}")
        time.sleep(3)
        damage = random.randint(0, second_fighter.dmg)
        print(f"CRITICAL DAMAGE: {damage}" if damage == second_fighter.dmg else f"The damage was {damage}")
        time.sleep(3)
        first_fighter.health -= damage
        if first_fighter.health > 0:
            print(f"{first_fighter.name} HP: {first_fighter.health}")
            time.sleep(3)
        else:
            print(f"{first_fighter.name} died")
            time.sleep(3)
            break

def hero_activity(command,hero):
    if command == "1":
        print("Your hero will face other heroes in the Arena")
        enemy_hero = random.choice(hero_list)
        while enemy_hero.name == hero.name:
            enemy_hero = random.choice(hero_list)
        fight(hero,enemy_hero)
    elif command == "2":
        print("Your hero goes on a journey..")


