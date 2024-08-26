"""
module_10_4
"""
from threading import Thread
from queue import Queue
from time import sleep
from random import randint

class Table:
    """
    Класс Table:
    Объекты этого класса должны создаваться следующим способом - Table(1)
    Обладать атрибутами number - номер стола и guest - гость, который сидит за этим столом (по умолчанию None)
    """
    def __init__(self, number, guest=None):
        self.number = number
        self.guest = guest

class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name  # имя гостя.

    def run(self):
        sleep(randint(3, 10))

class Cafe:
    def __init__(self, *tables):
        self.tables = []
        self.busy_tables = 0
        for table in tables:
            self.tables.append(table)
        self.queue = Queue()

    def guest_arrival (self, *guests):
        """
        Должен принимать неограниченное кол-во гостей (объектов класса Guest).
        Далее, если есть свободный стол, то садить гостя за стол (назначать столу guest),
        запускать поток гостя и выводить на экран строку "<имя гостя> сел(-а) за стол номер <номер стола>".
        Если же свободных столов для посадки не осталось, то помещать гостя в очередь queue
        и выводить сообщение "<имя гостя> в очереди".
        """
        for guest in guests:
            for table in self.tables:
                if table.guest is None:
                    table.guest = guest
                    guest.start()
                    print(f"{guest.name} сел(-а) за стол номер {table.number}")
                    self.busy_tables += 1
                    break
            else:
                self.queue.put(guest)
                print(f"{guest.name} в очереди")

    def discuss_guests(self):

        while (not self.queue.empty()) or self.busy_tables > 0:
            for table in self.tables:
                if table.guest is None:
                    if not self.queue.empty():
                        table.guest = self.queue.get()
                        self.busy_tables += 1
                        print(f"{table.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}")
                        table.guest.start()
                else:
                    if table.guest.is_alive():
                        #table.guest.join()
                        print(f"{table.guest.name} покушал(-а) и ушёл(ушла)")
                        print(f"Стол номер {table.number} свободен")
                        table.guest = None
                        self.busy_tables -= 1


# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
    ]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()
