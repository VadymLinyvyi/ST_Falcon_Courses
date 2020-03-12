"""
    Для даного імені виводить ім'я  та по-батькові
    Вхідні дані очікуються з аргумент стрічки (1 строковий параметр).
    При відсутності імені в базі, виводить відповідне повідомлення
"""
import sys
import argparse


def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('name', nargs='?', default=" ")
    return parser


if __name__ == '__main__':
    namespace = createParser().parse_args(sys.argv[1:])
    dictionary = {"Олександр": "Вікторович", "Вадим": "Олександрович", "Ольга": "Петрівна",
                  "Василь": "Миколайович", "Віктор": "Федорович"}
    if namespace.name in dictionary.keys():
        print("Привіт, {} {}".format(namespace.name, dictionary[namespace.name]))
    else:
        print("Я з Вами не знайома")
