"""
    Генерує одномірний масив, заповнюючи його випадковими цілими числами. В комірках з непарним індексом - від'ємні цілі
    числа.
    Вхідні дані очікуються з аргумент стрічки - 2 числа.
    При відсутності аргументів - використовуються значення за замовчуванням
"""
import sys
import argparse
from random import random

# чудова ідея винести парсер в окрему функцію
# також коректне найменування
def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('f_number', nargs='?', default="25")
    return parser


if __name__ == '__main__':
    namespace = createParser().parse_args(sys.argv[1:])
    # дякую за перевірку з userfriendly попередженням
    assert namespace.f_number.isdigit, "Очікується ціле число"

    # що означає f в f_number?
    # не можу зрозуміти контекст
    f_number = int(namespace.f_number)

    data = [int(random() * 100) if x % 2 else int(-1 * random() * 100) for x in range(20)]
    print(data)

    count_f_numbers = 0
    for x in data:
        if x == f_number:
            count_f_numbers += 1
    print("Число {} повторюється в масиві {} разів".format(f_number, count_f_numbers))
