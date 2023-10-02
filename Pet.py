import time

class Animal:
    def __init__(self, name, hunger_threshold):
        self.name = name
        self.hunger_threshold = hunger_threshold
        self.hunger_level = 0

    def increase_hunger(self):
        while self.hunger_level < self.hunger_threshold:
            self.hunger_level += 1
            print(f"{self.name} is getting hungry... Hunger level: {self.hunger_level}")
            time.sleep(1)

        print(f"{self.name} is starving! Game over.")

    def feed(self):
        self.hunger_level = 0
        print(f"{self.name} has been fed. Hunger level reset to 0.")
