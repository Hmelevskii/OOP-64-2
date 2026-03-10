import random

class Hero: 
    def __init__(self, name, lvl=25, hp=100, stren=89):
        self.name = name
        self.lvl = lvl
        self.hp = hp
        self.stren = stren
    
    def greet(self):
        print(f"Привет, я {self.name}, Мой уровень {self.lvl}")

    def attack(self):
        print(f"{self.name} наносит удар!")
        self.stren -= 1 
        print(f'Сила уменьшилась: {self.stren}')

    def rest(self):
        print(f'Герой отдыхает')
        self.hp += 1
        print(f'Герой отдохнул. Здоровье восстановилось на: {self.hp} hp')

class Warrior(Hero):
    def __init__(self, name, lvl, hp, stamina):
        super().__init__(name, lvl, hp)
        self.stamina = stamina 
    def attack(self):
        print(f"Воин атакует мечом!")

class Mage(Hero):
    def __init__(self, name, lvl, hp, mp):
        super().__init__(name, lvl, hp)
        self.mana = mp
    def attack(self):
        print(f"Маг кастует заклинание!")

class Assassin(Hero):
    def __init__(self, name, lvl, hp, steal):
        super().__init__(name, lvl, hp)
        self.stealth = steal  
    def attack(self):
        print(f"Ассасин атакует из-под тишка!")


warrior = Warrior("Dwarf", 25, 100, 100)
mage = Mage("Priestess", 25, 100, 100)
assassin = Assassin("High_Elf_Archer", 25, 100, 10)

heroes = {"warrior": warrior, "mage": mage, "assassin": assassin}

hero_choice = input("Выберите героя: Warrior / Mage / Assassin: ").lower()

player = heroes.get(hero_choice)
if not player:
    print("Выберите правильного героя!")
    exit()


opponent = [i for name, i in heroes.items() if i != player]
opponent = random.choice(opponent)

win = {"Warrior": "Assassin", "Assassin": "Mage", "Mage": "Warrior"}

player_class = player.__class__.__name__
opponen_class = opponent.__class__.__name__
print(f" Вы выбрали: {player_class}")
print(f" Противник: {opponen_class}")

if player_class == opponen_class:
    print("Ничья")
elif win[player_class] == opponen_class:
    print(f'{player_class} победил!')
else:
    print(f'{opponen_class} победил!')