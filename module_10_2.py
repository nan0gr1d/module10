"""
module_10_2
"""
from threading import Thread
from time import sleep

class Knight(Thread):
    number_enemies = 100

    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.rest_enemies = Knight.number_enemies

    def run(self):
        print(f"{self.name}, на нас напали!")
        # rest_enemies = Knight.number_enemies
        day_count = 0
        while self.rest_enemies > 0:
            sleep(1)
            day_count += 1
            self.rest_enemies -= self.power
            print(f"{self.name} сражается {day_count} дня(дней)..., осталось {self.rest_enemies} воинов.")
        print(f"{self.name} одержал победу спустя {day_count} дней(дня)!")


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
print("Все битвы закончились!")
