"""
module_10_5
"""

from datetime import datetime
import multiprocessing

def read_info(name):
    all_data = []
    with open(name) as file:
        line = " "
        while len(line) > 0:
            line = file.readline()
            all_data.append(line)


filenames = [f'./file {number}.txt' for number in range(1, 5)]

#  Линейный вызов
#  0:00:06.366020
"""
start = datetime.now()
for name in filenames:
    read_info(name)
end = datetime.now()
print(end - start)
"""

#  Многопроцессный
#  0:00:02.550970
if __name__ == '__main__':
    start = datetime.now()
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, filenames)
    end = datetime.now()
    print(end - start)
