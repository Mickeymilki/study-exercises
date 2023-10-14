import threading 
class Pet:
    def __init__(self, name, hunger, Timer=10, hp=True):
        self.name = name
        self._hunger = hunger
        self.hunger_level = 0
        self.timer = Timer
        self.hp = hp

    def hunger(self):
         if self.hunger_level < self._hunger:
            self.hunger_level += 1
            self.hp = True
            print(f"{self.name} хочет есть! Уровень голода: {self.hunger_level}")
            self.timer = threading.Timer(10.0, self.hunger)
            self.timer.start()
         else:
            print(f"{self.name} умирает от голода!")
            self.hp = False
            self.timer.cancel()

    def feed(self):
        self.hunger_level = 0
        print(f"{self.name} накормлен)")
        
    def stop(self):
        self.timer.cancel()

Cat = Pet("Кот", 5)
 
gameover = False
while not gameover:
    c = input()
    match c:
        case 'z':
            Cat.hunger()
        case 'x':
            Cat.feed()
        case 'v':
            gameover = True
            Cat.stop()