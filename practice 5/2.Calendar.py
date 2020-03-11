"""
    Отримує дату. Виводить кількість днів в заданому місяці та чи є даний день вихідним
    Вхідні дані очікуються з аргумент стрічки (1 стрічка формату dd-mm-yyyy).
    При відсутності аргументів - використовуються значення за замовчуванням
"""
import sys
import argparse
# Знаю, що є модуль calendar, але хотів написати сам

# чудове рішення з assert

def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('date', nargs='?', default="02-07-2019")
    return parser

# дуже класно робити аннотацію функцій
# ось приблизний приклад
# """ Should call summ of deposit

#     Args:
#         SumDeposit (int): Summ of the deposit.
#         Dividends (int): Persent rate.
#         Duration (int): Duration of the deposit in years.
#         Type (int): 1 - simple / 2 - сomplex

#     Returns:
#         float: calculated rate
#     """

def leapYear(y: int):
    # немає сенсу писати if (true): true, else: false
    # можна просто повертати результат порівняння
    # return ((y % 4 != 0) or (y % 100 == 0 and y % 400 != 0))
    # як варіант
    if (y % 4 != 0) or (y % 100 == 0 and y % 400 != 0):
        return False
    else:
        return True


def centeryShift(y):
    # найменування змінних бажано здійснювати згідно контексту
    x = int(str(y)[:2])
    x2 = x + 1
    while x2 % 4:
        x2 += 1
    return (x2-1-x)*2


def monthShift(m):
    shift = [0, 3, 3, 6, 1, 4, 6, 2, 5, 0, 3, 5]
    return shift[m - 1]

def yearShift(y,m):
    # цю команду бажано розбити чи спростити
    # тернарний оператор це класна штука, але не слід його 
    # використовувати, коли необхідно виконати таку кількість команд
    # ліпше використати простий if else і можливо розбити умови на під умови

    # також важливо описувати логіку роботи подібних умов
    return ((int(str(y)[-2:]) + int(str(y)[-2:])//4) % 7)-1 if leapYear(y) and (m == 1 or m == 2) else ((int(str(y)[-2:]) + int(str(y)[-2:])//4) % 7)


def dayOfWeek (y: int, m: int, d: int):
    # dnames -> day_names або просто days
    dnames = ["неділя", "понеділок", "вівторок", "середа", "четвер", "п'ятниця", "субота"]
    cs = centeryShift(y)
    ms = monthShift(m)
    ys = yearShift(y, m)
    ds = d % 7
    return dnames[(cs+ys+ms+ds) % 7]


if __name__ == '__main__':
    namespace = createParser().parse_args(sys.argv[1:])
    assert (namespace.date[:2].isdigit and namespace.date[2] == "-" and namespace.date[3:5].isdigit and
            namespace.date[5] == "-" and namespace.date[6:].isdigit), "очікується дата в форматі dd-mm-yyyy"

    day = int(namespace.date[:2])
    month = int(namespace.date[3:5])
    year = int(namespace.date[6:])

    assert 0 < day < 32, "Число має бути цілим числом в проміжку [1:31]"
    assert 0 < month < 13, "номер місяця має бути в проміжку [1:12]"

    # якщо ми не збираємося змінювати дані в подальшому, можна використати кортеж
    months = ["січні", "лютому", "березні", "квітні", "травні", "червні",
              "липні", "серпні", "вересні", "жовтні", "листопаді", "грудні"]

    mdays = [31, 29 if leapYear(year) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    daysInMonth = mdays[month-1]
    print("У {} {} року - {} {}".format(months[month - 1], year, daysInMonth, "день" if daysInMonth == 31 else "днів"))
    print("{} - {}".format(namespace.date, dayOfWeek(year, month, day)))

