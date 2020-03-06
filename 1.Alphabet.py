"""
    Для даної літери англійського алфавіту, виводить сусідні літери
    Вхідні дані очікуються з аргумент стрічки (1 символ англійського алфавіта).
    При відсутності аргументів - використовуються значення за замовчуванням
"""
import sys
import argparse


def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('char', nargs='?', default="b")
    return parser


if __name__ == '__main__':
    namespace = createParser().parse_args(sys.argv[1:])
    assert ord("A") <= ord(namespace.char) <= ord("Z") or ord("a") <= ord(namespace.char) <= ord("z")

    previous = "None"
    next = "None"

    if ord(namespace.char) > ord("a") or ord(namespace.char) > ord("A"):
        previous = chr(ord(namespace.char)-1)
    if ord(namespace.char) < ord("z") or ord(namespace.char) < ord("Z"):
        next = chr(ord(namespace.char)+1)
    print("Введений символ: " + namespace.char)
    print("Попередній: " + previous)
    print("Наступний: " + next)