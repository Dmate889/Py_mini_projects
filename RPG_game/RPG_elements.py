import random
import classes
import time
import fantasy_names

death_knight = classes.DeathKnight(fantasy_names.randomize(),150,50,"Death Blade")
warrior = classes.Warrior(fantasy_names.randomize(),150,50,"Brutal Cut")
mage = classes.Mage(fantasy_names.randomize(),100,100,"Fireball")

hero_list = [death_knight,warrior,mage]

def hero_selection():
    selection = input("Choose your Hero: "
          "\n1. Warrior"
          "\n2. Mage"
          "\n3. Death Knight\n")
    hero_name = input("Hero name: ")
    match selection:
        case "1":
            return classes.Warrior(hero_name,150,50,"Brutal Cut")
        case "2":
            return classes.Mage(hero_name,100,100,"Fireball")
        case "3":
            return classes.DeathKnight(hero_name,150,50,"Death Blade")
        case _:
            return print("Invalid input!")


def hero_activity(command,hero):
    if command == "1":
        if hero.health <= 0:
            print("Your hero died in the last fight, please select another hero")
        else:
            enemy_hero = random.choice(hero_list)
            print(f"Your hero will face {enemy_hero.name} ({enemy_hero.classtype}) in the Arena")
            hero.fight(enemy_hero)
    elif command == "2":
        hero_rest(hero)
    elif command == "3":
        get_hero_data(hero)
    else:
        print("Invalid input!")

def get_hero_data(hero):
    user_input = input("\n1. Your hero"
                      "\n2. Enemy heroes\n")
    if user_input == "1":
        if user_input == "1":
            if hero.health > 0:
                special_line = f"Special ability: {hero.special2}\n" if not hero.special_used else f"Special ability: {hero.special2} --- USED\n"

                print(f"Hero: {hero.name}\n"
                      f"Class: {hero.classtype}\n"
                      f"Health: {hero.health}\n"
                      f"Basic attack: {hero.special}\n"
                      f"{special_line}"
                      f"Health Potions: {hero.potions}")
        elif hero.health <= 0:
            print("Your hero died in the last fight, please select another hero")
        else:
            print("You don't have a hero selected yet.")
    else:
        for hero in hero_list:
            special_line = f"Special ability: {hero.special2}\n" if hero.special_used == False else f"Special ability: {hero.special2} --- USED\n"
            print(f"\nHero: {hero.name}\n"
                  f"Class: {hero.classtype}\n"
                  f"Health: {hero.health}\n"
                  f"Basic attack: {hero.special}\n"
                  f"{special_line}"
                  f"Health Potions: {hero.potions}")

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
              "\n3. Return to main menu (you will lose your hero)\n")
        user_input = input()

        if user_input == "1":
            get_hero_data(hero)
        elif user_input == "2":
            hero_activity("1",hero)
        elif user_input == "3":
            is_running = False


def hero_rest(hero):
    hero.health = hero.health
    hero.potions = hero.potions
    hero.special_used = False
    print(f"Your hero will take some rest.. Health: {hero.health}, Health Potions: {hero.potions} and special ability no longer on cooldown")