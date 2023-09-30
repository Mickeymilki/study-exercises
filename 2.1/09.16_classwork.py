import time
import threading 
class Pet:
    def __init__(self, name, hunger):
        self.name = name
        self._hunger = hunger
        self.hunger_level = 0

    def hunger(self):
        while self.hunger_level < self._hunger:
            self.hunger_level += 1
            print(f"{self.name} хочет есть! Уровень голода: {self.hunger_level}")
            Timer = threading.Timer(10.0, self.hunger)
            Timer.start()

        print(f"{self.name} умирает от голода!")

    def feed(self):
        self.hunger_level = 0
        print(f"{self.name} накормлен)")
    def exit(self):
        threading.Timer.cancel()
Pet = Pet("Кот", 5)
Pet.hunger()

 