import RPG_elements as Rpg

def main():
    is_running = True
    while is_running:
        print("=======================================")
        print("Welcome to Python console RPG mini game")
        print("Main Menu: ")
        print("=======================================")
        user_input = input("Press: "
              "\n1 for character selection"
              "\n2 for exit: \n")
        if user_input == "1":
            hero = Rpg.hero_selection()
            print(f"You have selected {hero.name}, class: {hero.classtype}")
            Rpg.hero_menu(hero)
        elif user_input == "2":
            print("Have a nice day and don't forget to come back!")
            is_running = False


if __name__ == "__main__":
    main()