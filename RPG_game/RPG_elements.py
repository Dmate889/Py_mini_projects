import random
import classes
import time
import hero_factory as hf

hero_list = []
waves = 1
hf.hero_creation(hero_list, 1,50,150)

def hero_selection():
    while True:
        selection = input("Choose your Hero: "
                          "\n1. Warrior"
                          "\n2. Mage"
                          "\n3. Death Knight\n")
        hero_name = input("Hero name: ")

        match selection:
            case "1":
                return classes.Warrior(hero_name, 150, 50, "Brutal Cut",1)
            case "2":
                return classes.Mage(hero_name, 100, 50, "Fireball",1)
            case "3":
                return classes.DeathKnight(hero_name, 150, 50, "Death Blade",1)
            case _:
                print("Invalid input! Please try again.\n")

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
    user_input = input("1. Your hero"
                      "\n2. Enemy heroes\n")
    if user_input == "1":
            if hero.health > 0:
                special_line = f"Special ability: {hero.special2}\n" if not hero.special_used else f"Special ability: {hero.special2} --- USED\n"

                print(f"Hero: {hero.name}\n"
                      f"Level: {hero.level}\n"
                      f"Class: {hero.classtype}\n"
                      f"Health: {hero.health}\n"
                      f"Basic attack: {hero.special}\n"
                      f"{special_line}"
                      f"Health Potions: {hero.potions}\n")
            elif hero.health <= 0:
               print("Your hero died in the last fight, please select another hero")
    elif user_input == "2":
        for hero in hero_list:
            special_line = f"Special ability: {hero.special2}\n" if hero.special_used == False else f"Special ability: {hero.special2} --- USED\n"
            print(f"\nHero: {hero.name}\n"
                  f"Level: {hero.level}\n"
                  f"Class: {hero.classtype}\n"
                  f"Health: {hero.health}\n"
                  f"Basic attack: {hero.special}"
                  f"{special_line}"
                  f"Health Potions: {hero.potions}\n")
    else:
        print("Invalid input!")

def main_menu():
    is_running = True
    while is_running:
        print("=======================================")
        print("Welcome to the Arena of Endless Carnage")
        print("=======================================")
        user_input = input("Press: "
                           "\n1 Character Selection"
                           "\n2 Exit: \n")
        if user_input == "1":
            hero = hero_selection()
            print(f"You have selected {hero.name}, class: {hero.classtype}")
            hero_menu(hero)
        elif user_input == "2":
            print("Farewell traveller!")
            time.sleep(2)
            break

def hero_menu(hero):
    is_running = True
    while is_running:
        print("=================")
        print("Hero Menu")
        print("=================")
        print("1. Get hero data"
              "\n2. Fight in the Arena"
              "\n3. Get some rest"
              "\n4. Return to main menu (you will lose your hero)\n")
        user_input = input()

        if user_input == "1":
            get_hero_data(hero)
        elif user_input == "2":
            hero_activity("1",hero)
            new_heroes(hero_list)
        elif user_input == "3":
            hero_activity("2",hero)
        elif user_input == "4":
            is_running = False
        else:
            print("Invalid input")


def hero_rest(hero):
    hero.health = 100 if hero.classtype == "Mage" else 150
    hero.potions = 2
    hero.special_used = False
    print(f"Your hero took some rest.. Health: {hero.health}, Health Potions: {hero.potions} and special ability no longer on cooldown")

def fallen_hero(hero):
    hero_list.remove(hero)

def new_heroes(hero_list):
    global waves
    base_health = 100
    base_dmg = 50

    if len(hero_list) == 0:
        waves += 1
        health = base_health + (waves - 1) * 50
        dmg = base_dmg + (waves - 1) * 50
        print(f"\nWave {waves}: New champions have entered the Arena, stronger than ever!")
        hf.hero_creation(hero_list, waves, health, dmg)
    else:
        print(f"{len(hero_list)} remain to fight another day in the Arena.")
        time.sleep(2)
