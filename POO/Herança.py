class Enemy: # Classe base/super/mãe
    def __init__(self,name,hp,goldDrop,armor):
        self.name = name
        self.hp = hp
        self.goldDrop = goldDrop
        self.armor = armor

    def attack(self):
        print("Inimigo atacando...")

class Boss(Enemy):
    def __init__(self, name, hp,goldDrop,armor,mana):
        super().__init__(name, hp,goldDrop,armor)
        self.mana = mana

    def attack(self):
        super().attack()
        print("CHEGOU A SUA HORA!")

enemy_1 = Enemy("Goblin", 50, 10.5, 0)
print(f"{enemy_1.name} possui {enemy_1.hp} de vida")
enemy_1.attack()

boss_1 = Boss("Cavaleiro Negro", 1000, 500, 200,300)
boss_1.attack()
