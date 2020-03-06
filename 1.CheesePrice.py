"""
    Розрахунок вартості вагового товару у діапазоні ваги від 50 до 1000 грам з кроком 50 грам
    Вхідні дані очікуються з аргумент стрічки (1 число - вартість кілограма товару).
    При відсутності аргументів - використовуються значення за замовчуванням
"""
import sys
import argparse


def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('price', nargs='?', default="500")
    return parser


def toFixed(numObj, digits=2):
    return f"{numObj:.{digits}f}"


if __name__ == '__main__':
    namespace = createParser().parse_args(sys.argv[1:])
    assert namespace.price.isdigit() and int(namespace.price) >= 0
    price = int(namespace.price)

    print("1кг сиру - {}грн".format(price))
    print("Вага\t\tЦіна")
    for i in range(50, 1050, 50):
        #print("{}\t\t\t{}".format(i, toFixed(price/1000*i, 0)))
        print("%4d%12d" % (i, price/1000*i))
