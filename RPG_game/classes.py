import random
import time
import RPG_elements as Rpg

class Character:
    def __init__(self, name, health, dmg, special, special2, potions,level):
        self.name = name
        self.health = health
        self.dmg = dmg
        self.special = special
        self.special2 = special2
        self.potions = potions
        self.special_used = False
        self.xp = 0
        self.level = level

    def health_potion(self):
        if self.potions > 0:
            hp_amount = random.randint(0,50)
            time.sleep(1)
            print(f"{self.name} uncorks a healing potion and drinks it in one swift motion.")
            self.health += hp_amount
            time.sleep(3)
            print(f"{self.name} healed for {hp_amount}. {self.name} HP: {self.health}")
            self.potions -= 1
        else:
            print("You don't have more potions left - You lost your round!")

    def fight(self, enemy_hero):
        turns = 2

        for turn in range(turns):
            print(f"\n--- Round {turn + 1} ---")
            time.sleep(3)
            self.attack_phase(enemy_hero)
            if enemy_hero.health <= 0:
                time.sleep(2)
                print(f"{enemy_hero.name}'s journey ends here. Their name fades from the Arena.")
                time.sleep(3)
                print("You gained 30 XP!")
                self.xp += 30
                time.sleep(2)
                self.level_up()
                Rpg.fallen_hero(enemy_hero)
                return


            enemy_hero.attack_phase(self)
            if self.health <= 0:
                time.sleep(2)
                print(f"{self.name}'s journey ends here. Their name fades from the Arena.")
                return

        while self.health > 0 and enemy_hero.health > 0:
            print("\n--- Action Phase ---")
            time.sleep(2)
            print("Choose your action:")
            print("1. Regular attack")
            print(f"2. Use special ability ({self.special2}) --USED" if self.special_used == True else f"2. Use special ability ({self.special2})")
            print(f"3. Use health potion. {self.potions} remains")

            choice = input("Your choice: ")

            if choice == "1":
                self.attack_phase(enemy_hero)
            elif choice == "2":
                self.special_attack(enemy_hero)
            elif choice == "3":
                self.health_potion()
            else:
                print("Invalid input, you lose your turn!")

            if enemy_hero.health <= 0:
                time.sleep(2)
                print(f"{enemy_hero.name}'s journey ends here. Their name fades from the Arena.")
                time.sleep(2)
                print("You gained 30 XP!")
                self.xp += 30
                time.sleep(2)
                self.level_up()
                Rpg.fallen_hero(enemy_hero)
                break

            print(f"\n{enemy_hero.name} strikes back!")
            enemy_choices = [1]  # 1 = attack

            if not enemy_hero.special_used:
                enemy_choices.append(3)  # 3 = special attack

            if enemy_hero.potions > 0:
                enemy_choices.append(2)  # 2 = potion

            enemy_ai = random.choice(enemy_choices)
            if enemy_ai == 1:
                enemy_hero.attack_phase(self)
                if self.health <= 0:
                    print(f"{self.name}'s journey ends here. Their name fades from the Arena.")
                    break
            elif enemy_ai == 2:
                enemy_hero.health_potion()
            elif enemy_ai == 3:
                enemy_hero.special_attack(self)
                if self.health <= 0:
                    print(f"{self.name}'s journey ends here. Their name fades from the Arena.")
                    break

    def attack_phase(self, enemy_hero):
        print(f"{self.name} attacks {enemy_hero.name} with {self.special}")
        time.sleep(3)
        damage = random.randint(10, self.dmg)
        print(f"CRITICAL DAMAGE: {damage}" if damage == self.dmg else f"The damage was {damage}")
        enemy_hero.health -= damage
        time.sleep(3)
        if enemy_hero.health > 0:
            print(f"{enemy_hero.name} HP: {enemy_hero.health}")
        else:
            print(f"{enemy_hero.name} died")

    def special_attack(self, enemy_hero):
        raise NotImplementedError("This class must implement its own special_attack() method.")

    def level_up(self):
        if self.xp >= 90:
            self.level += 1
            print(f"==== LEVEL UP! ====\n"
                  f"You are level {self.level} now! You gained: "
                  f"\n + 50 health"
                  f"\n + 50 damage")
            self.xp = 0
            self.dmg += 50
            self.health += 50
            time.sleep(3)
        else:
            print(f"You need {90 - self.xp} XP to reach the next level")
            time.sleep(2)

class Warrior(Character):
    def __init__(self,name,health,dmg,special,level,special2="Execution", potions= 2, classtype="Warrior"):
        super().__init__(name,health,dmg,special,special2, potions,level)
        self.classtype = classtype


    def special_attack(self,enemy_hero):
        if not self.special_used:
            execution_damage = random.randint(30,50)
            print(f"Sensing weakness, {self.name} charges forward with unrelenting fury... EXECUTION incoming!")
            time.sleep(3)
            print(f"CRITICAL EXECUTION: {execution_damage}" if execution_damage == 50 else f"The damage was: {execution_damage}")
            time.sleep(3)
            print(f"{enemy_hero.name} HP: {enemy_hero.health}")
            time.sleep(3)
            enemy_hero.health -= execution_damage
            self.special_used = True
        else:
            print("Special ability has been already used! Take some rest to use it again!")


class Mage(Character):
    def __init__(self,name,health,dmg,special,level, special2="Lava Shield", potions= 2, classtype="Mage"):
        super().__init__(name,health,dmg, special,special2, potions,level)
        self.classtype = classtype

    def special_attack(self, enemy_hero):
        if not self.special_used:
            shield_protection = random.randint(50,100)
            self.health += shield_protection
            print(f"Molten fire swirls around {self.name}, forming a blazing shield of lava!")
            time.sleep(3)
            print(f"SUPER SHIELD! {shield_protection}" if shield_protection == 100 else f"{self.name} is empowered by the elemental force and gains {shield_protection} health!")
            time.sleep(3)
            print(f"{self.name} HP: {self.health}")
            time.sleep(3)
            self.special_used = True
        else:
            print("Special ability has been already used! Take some rest to use it again!")

class DeathKnight(Character):
    def __init__(self,name,health,dmg,special,level, special2="Corpse Explosion", potions= 2, classtype="Death Knight"):
        super().__init__(name,health,dmg,special,special2, potions,level)
        self.classtype = classtype

    def special_attack(self, enemy_hero):
        if not self.special_used:
            execution_damage = random.randint(20,40)
            self.health += int(execution_damage * 0.5)
            print(f"Rotten flesh ignites with necrotic energy as {self.name} triggers a Corpse Explosion!")
            time.sleep(3)
            print(f"CRITICAL EXPLOSION! {execution_damage}"if execution_damage == 30 else f"{enemy_hero.name} is engulfed by the blast and takes {execution_damage} damage.")
            time.sleep(3)
            print(f"{self.name} siphons strength from the explosion and heals for {int(execution_damage * 0.5)}.")
            time.sleep(3)
            print(f"{enemy_hero.name} HP: {enemy_hero.health}")
            print(f"{self.name} HP: {self.health}")
            time.sleep(3)
            self.special_used = True
        else:
            print("Special ability is on cooldown, take some rest to use it again!")



