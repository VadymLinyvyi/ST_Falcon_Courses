"""
    Для даного числа рахує суму цифр і їх кількість
    Вхідні дані очікуються з аргумент стрічки (1 ціле число).
    При відсутності аргументів - використовуються значення за замовчуванням
"""
import sys
import argparse


def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('digit', nargs='?', default="25")
    return parser


if __name__ == '__main__':
    namespace = createParser().parse_args(sys.argv[1:])
    prefix = ""
    if namespace.digit[0] == "-":
        namespace.digit = namespace.digit[1:]
        prefix = "-"

    assert namespace.digit.isdigit()

    digit = int(namespace.digit)
    sum = 0
    count = 0
    print("Число: " + prefix + str(digit))
    if digit == 0:
        count = 1
    while digit:
        sum += digit % 10
        count += 1
        digit //= 10
    print("Сума цифр: " + str(sum))
    print("Кількість: " + str(count))
