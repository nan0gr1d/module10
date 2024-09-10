#  module_10_3

from threading import Thread, Lock
from random import randint
from time import sleep

class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = Lock()

    def deposit(self):
        for i in range(100):
            deposit_ = randint(50, 500)
            with self.lock:
                self.balance += deposit_
                print(f"Пополнение: {deposit_}. Баланс: {self.balance} ", flush=True)
                sleep(0.001)

            if self.balance >= 500 and self.lock.locked():
                self.lock.release()

    def take(self):
        for i in range(100):
            take_ = randint(50, 500)
            with self.lock:
                print(f"Запрос на {take_} ", flush=True)

                if self.balance >= take_:
                    self.balance -= take_
                    print(f"Снятие: {take_}. Баланс: {self.balance} ", flush=True)
                    sleep(0.001)
                    continue

            self.lock.acquire()
            print("Запрос отклонён, недостаточно средств. ", flush=True)
            sleep(0.001)
            if self.lock.locked():
                self.lock.release()


bk = Bank()

th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
