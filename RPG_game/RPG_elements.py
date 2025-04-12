import random
import classes
import time


death_knight = classes.DeathKnight("Inquisitor",100,50,"Death Blade")
warrior = classes.Warrior("Ashtronor",100,50,"Brutal Cut")
mage = classes.Mage("Phoenix",50,100,"Fireball")

hero_list = [death_knight,warrior,mage]

def hero_selection():
    selection = input("Choose your Hero: "
          "\n1. Warrior"
          "\n2. Mage"
          "\n3. Death Knight\n")

    match selection:
        case "1":
            return classes.Warrior("Ashtronor",100,50,"Brutal Cut")
        case "2":
            return classes.Mage("Phoenix",50,100,"Fireball")
        case "3":
            return classes.DeathKnight("Inquisitor",100,50,"Death Blade")


def fight(first_fighter,second_fighter):
    is_running = True
    while is_running:
        print(f"{first_fighter.name} will make their move and attack {second_fighter.name} with {first_fighter.special}")
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
            second_fighter.health = 50 if second_fighter.classtype == "Mage" else 100
            break

        print(f"{second_fighter.name} composes themselves and strikes back with {second_fighter.special}")
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
        if hero.health <= 0:
            print("Your hero died in the last fight, please select another hero")
        else:
            enemy_hero = random.choice(hero_list)
            while enemy_hero.name == hero.name:
                enemy_hero = random.choice(hero_list)
            print(f"Your hero will face {enemy_hero.name} ({enemy_hero.classtype}) in the Arena")
            fight(hero,enemy_hero)
    elif command == "2":
        print("Your hero goes on a journey..")
    elif command == "3":
        get_hero_data(hero)

def get_hero_data(hero):
    user_input = input("\n1. Your hero"
                      "\n2.Enemy heroes\n")
    if user_input == "1":
        if hero.health > 0:
            print(f"Hero: {hero.name}\n"
                  f"Class: {hero.classtype}\n"
                  f"Health: {hero.health}\n"
                  f"Basic attack: {hero.special}\n")
        elif hero.health <= 0:
            print("Your hero died in the last fight, please select another hero")
        else:
            print("You don't have a hero selected yet.")
    else:
        for hero in hero_list:
            print(f"\nHero: {hero.name}\n"
                  f"Class: {hero.classtype}\n"
                  f"Health: {hero.health}\n"
                  f"Basic attack: {hero.special}\n")

def main_menu():
    is_running = True
    while is_running:
        print("=======================================")
        print("Welcome to Python console RPG mini game")
        print("=======================================")
        user_input = input("Press: "
                           "\n1 Character Selection"
                           "\n2 Exit: \n")
        if user_input == "1":
            hero = hero_selection()
            print(f"You have selected {hero.name}, class: {hero.classtype}")
            hero_menu(hero)
        elif user_input == "2":
            print("Have a nice day and don't forget to come back!")
            break

def hero_menu(hero):
    is_running = True
    while is_running:
        print("=================")
        print("Hero Menu")
        print("=================")
        print("1. Get hero data"
              "\n2. Fight in the Arena"
              "\n3. Return to main menu\n")
        user_input = input()

        if user_input == "1":
            get_hero_data(hero)
        elif user_input == "2":
            hero_activity("1",hero)
        elif user_input == "3":
            is_running = False
