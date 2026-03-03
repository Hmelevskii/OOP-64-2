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



Luffi = Hero("Luffi")
Luffi.greet()
Luffi.attack()
Luffi.rest()
Zoro = Hero('Zoro')
Zoro.greet()
Zoro.attack()
Zoro.rest()

