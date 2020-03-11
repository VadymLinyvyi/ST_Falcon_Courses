"""
    Сортує числа на парні та непарні на заданому проміжку
    Вхідні дані очікуються з аргумент стрічки (2 числа - ліва та права межа сортованого проміжку).
    При відсутності аргументів - використовуються значення за замовчуванням
"""
import sys
import argparse


def createParser ():
    parser = argparse.ArgumentParser()
    parser.add_argument('start', nargs='?', default="5")
    parser.add_argument('stop', nargs='?', default="15")
    return parser


if __name__ == '__main__':
    namespace = createParser().parse_args(sys.argv[1:])
    assert namespace.start.isdigit() and namespace.stop.isdigit() and int(namespace.start) <= int(namespace.stop)
    start = int(namespace.start)
    stop = int(namespace.stop)
    even = []
    odd = []
    for i in range(start, stop+1):
        if i % 2 :
            odd.append(str(i))
        else:
            even.append(str(i))
    print("Проміжок {} - {}".format(start, stop))
    print("Парні: " + " ".join(even))
    print("Непарні: " + " ".join(odd))
