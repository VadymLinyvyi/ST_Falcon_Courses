"""
    Розрахунок прибутку при депозитному вкладі в банк заданної суми під заданий відсоток на визначений термін.
    Вхідні дані очікуються з аргумент стрічки в порядку Сума, Відсоток, Тривалість.
    При відсутності аргументів - використовуються значення за замовчуванням
"""
import sys
import argparse


def createParser ():
    parser = argparse.ArgumentParser()
    parser.add_argument('sum', nargs='?', default="500")
    parser.add_argument('percent', nargs='?', default="5")
    parser.add_argument('duration', nargs='?', default="10")
    return parser


def toFixed(numObj,digits=2):
    return f"{numObj:.{digits}f}"


if __name__ == '__main__':
    namespace = createParser().parse_args(sys.argv[1:])
    assert (namespace.percent.isdigit() and namespace.sum.isdigit() and namespace.duration.isdigit() and
            int(namespace.percent.isdigit()) >= 0 and int(namespace.sum.isdigit()) >= 0 and
            int(namespace.duration.isdigit()) >= 1)
    print("Вклад {}% річних".format(namespace.percent))
    print("Рік\t\t\tСума\t\t\tПрибуток")

    sum = int(namespace.sum)
    for i in range(int(namespace.duration)):
        year = i+1
        profit = sum/100*float(namespace.percent)
        print("{}\t\t\t{}\t\t\t{}".format(year, toFixed(sum), toFixed(profit)))
        sum += profit
