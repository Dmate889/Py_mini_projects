class Character:
    def __init__(self, name, health, dmg,special):
        self.name = name
        self.health = health
        self.dmg = dmg
        self.special = special

class Warrior(Character):
    def __init__(self,name,health,dmg,special,classtype="Warrior"):
        super().__init__(name,health,dmg,special)
        self.classtype = classtype

class Mage(Character):
    def __init__(self,name,health,dmg,special,classtype="Mage"):
        super().__init__(name,health,dmg, special)
        self.classtype = classtype

class DeathKnight(Character):
    def __init__(self,name,health,dmg,special,classtype="Death Knight"):
        super().__init__(name,health,dmg,special)
        self.classtype = classtype




