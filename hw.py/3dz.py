from abc import ABC, abstractmethod

class Hero(ABC):
    def __init__(self, name, level, health, strength):
        self.name = name
        self.level = level
        self.__health = health
        self.strength = strength

    def greet(self):
        print(f'Привет, я {self.name}, мой уровень {self.level}')
    
    def rest(self):
        print(f'{self.name} отдыхает')
        self.__health += 1
    @abstractmethod
    def attack(self):
        pass

class Warrior(Hero):
    def attack(self):
        print(f'Воин атакует мечом')
class Mage(Hero):
    def attack(self):
        print(f'Маг использует магию')
class Assassin(Hero):
     def attack(self):
        print(f'Ассасин атакует из-под тишка')


Ichigo = Warrior("Ichigo", 25, 100, 10)
Ruckiya = Mage("Ruckiya", 25, 100, 10)
Uryu = Assassin("Uryu", 25, 100, 10)


Ichigo.greet()
Ichigo.attack()
Ichigo.rest()
Ruckiya.greet()
Ruckiya.attack()
Ruckiya.rest()
Uryu.greet()
Uryu.attack()
Uryu.rest()

