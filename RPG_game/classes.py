import random
import time

class Character:
    def __init__(self, name, health, dmg,special, special2):
        self.name = name
        self.health = health
        self.dmg = dmg
        self.special = special
        self.special2 = special2

    def health_potion(self):
        hp_amount = random.randint(0,25)
        print(f"{self.name} uncorks a healing potion and drinks it in one swift motion.")
        self.health += hp_amount
        print(f"{self.name} healed for {hp_amount}")

    def fight(self, enemy_hero):
        turns = 3

        for turn in range(turns):
            print(f"\n--- Round {turn + 1} ---")
            self.attack_phase(enemy_hero)
            if enemy_hero.health <= 0:
                print(f"{enemy_hero.name} has fallen!")
                return

            enemy_hero.attack_phase(self)
            if self.health <= 0:
                print(f"{self.name} has fallen!")
                return

        while self.health > 0 and enemy_hero.health > 0:
            print("\n--- Action Phase ---")
            print("Choose your action:")
            print("1. Regular attack")
            print(f"2. Use special ability ({self.special2})")
            print("3. Use health potion")

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
                print(f"{enemy_hero.name} has fallen!")
                break

            print(f"\n{enemy_hero.name} strikes back!")
            enemy_hero.attack_phase(self)
            if self.health <= 0:
                print(f"{self.name} has fallen!")
                break

    def attack_phase(self, enemy_hero):
        print(f"{self.name} attacks {enemy_hero.name} with {self.special}")
        time.sleep(2)
        damage = random.randint(0, self.dmg)
        print(f"CRITICAL DAMAGE: {damage}" if damage == self.dmg else f"The damage was {damage}")
        enemy_hero.health -= damage
        time.sleep(2)
        if enemy_hero.health > 0:
            print(f"{enemy_hero.name} HP: {enemy_hero.health}")
        else:
            print(f"{enemy_hero.name} died")

    def special_attack(self, enemy_hero):
        raise NotImplementedError("This class must implement its own special_attack() method.")

class Warrior(Character):
    def __init__(self,name,health,dmg,special,special2="Execution",classtype="Warrior"):
        super().__init__(name,health,dmg,special,special2)
        self.classtype = classtype

    def special_attack(self,enemy_hero):
        execution_damage = random.randint(10,50)
        print(f"Sensing weakness, {self.name} charges forward with unrelenting fury... EXECUTION incoming!")
        print(f"CRITICAL EXECUTION: {execution_damage}" if execution_damage == 50 else f"The damage was: {execution_damage}")
        enemy_hero.health -= execution_damage

class Mage(Character):
    def __init__(self,name,health,dmg,special, special2="Lava Blast", classtype="Mage"):
        super().__init__(name,health,dmg, special,special2)
        self.classtype = classtype

    def special_attack(self, enemy_hero):
        execution_damage = random.randint(10,50)
        print(f"Molten fire surges through the cracks of reality as {self.name} releases a devastating Lava Blast!")
        print(f"CRITICAL EXECUTION: {execution_damage}" if execution_damage == 50 else f"The damage was: {execution_damage}")
        enemy_hero.health -= execution_damage

class DeathKnight(Character):
    def __init__(self,name,health,dmg,special, special2="Corpse Explosion", classtype="Death Knight"):
        super().__init__(name,health,dmg,special,special2)
        self.classtype = classtype

    def special_attack(self, enemy_hero):
        execution_damage = random.randint(10,50)
        print(f"Rotten flesh ignites with necrotic energy as {self.name} triggers a Corpse Explosion!")
        print(f"CRITICAL EXECUTION: {execution_damage}" if execution_damage == 50 else f"The damage was: {execution_damage}")
        enemy_hero.health -= execution_damage




