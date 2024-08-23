"""
module_10_3
"""
from threading import Thread, Lock
from random import randint
from time import sleep


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = Lock()

    def deposit(self):
        for _ in range(100):
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            deposit_ = randint(50, 500)
            self.balance += deposit_
            print(f"Пополнение: {deposit_}. Баланс: {self.balance} ", flush=True)
            sleep(0.001)

    def take(self):
        for _ in range(100):
            take_ = randint(50, 500)
            print(f"Запрос на {take_} ", flush=True)
            if self.balance >= take_:
                self.balance -= take_
                print(f"Снятие: {take_}. Баланс: {self.balance} ", flush=True)
            else:
                self.lock.acquire()
                print("Запрос отклонён, недостаточно средств. ", flush=True)
            sleep(0.001)


bk = Bank()

th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
