"""
module_10_1
"""
from threading import Thread
from time import sleep
from datetime import datetime

def write_words(word_count, file_name):  # Объявление функции write_words
    with open(file_name, "w", encoding='UTF-8') as file:
        for i in range(word_count):
            file.write(f"Какое-то слово № {i}\n")
            sleep(0.1)
    print(f"Завершилась запись в файл {file_name}")


start_time = datetime.now()  # Взятие текущего времени
write_words(10, "example1.txt")  # Запуск функций с аргументами из задачи
write_words(30, "example2.txt")
write_words(200, "example3.txt")
write_words(100, "example4.txt")

functions_time = datetime.now() # Взятие текущего времени
print(f"Работа функций {functions_time - start_time}")  # Вывод разницы начала и конца работы функций

thread1 = Thread(target=write_words, args=(10, "example5.txt"))  # Создание и запуск потоков с аргументами из задачи
thread2 = Thread(target=write_words, args=(30, "example6.txt"))
thread3 = Thread(target=write_words, args=(200, "example7.txt"))
thread4 = Thread(target=write_words, args=(100, "example8.txt"))

thread1.start()
thread2.start()
thread3.start()
thread4.start()

thread1.join()
thread2.join()
thread3.join()
thread4.join()

threads_time = datetime.now() # Взятие текущего времени
print(f"Работа потоков {threads_time - functions_time}")  # Вывод разницы начала и конца работы потоков
