"""
    Отримує число в цифровому вигляді. Виводить його прописом
    Вхідні дані очікуються з аргумент стрічки (1 ціле число).
    При відсутності аргументів - використовуються значення за замовчуванням
"""
import sys
import argparse


def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('digit', nargs='?', default="25")
    return parser


# Знаю, що занадто довгі стрічки, але залишив для кращого розуміння структури матриці
words = [[None],
         ["", "один", "два", "три", "чотири", "п'ять", "шість", "сім", "всім", "дев'ять", "десять",
          "одинадцять", "дванадцять", "тринадцять", "чотирнадцять", "п'ятнадцять", "шіснадцять", "сімнадцять", "вісімнадцять", "дев'ятнадцять"],
         ["", "", "двадцять", "тридцять", "сорок", "п'ятдесят", "шістдесят", "сімдесят", "вісімдесят", "дев'яносто"],
         ["", "сто", "двісті", "триста", "чотириста", "п'ятсот", "шістсот", "сімсот", "вісімсот", "дев'ятсот"],
         ["", "тисяча", "дві тисячі", "три тисячі", "чотири тисячі", "п'ять тисяч", "шість тисяч", "сім тисяч", "вісім тисяч", "дев'ять тисяч"]]

# Гарна ідея використати рекурсію
def numToWord (number: int):
    # цікавий підхід з числами від 1 до 19
    if number < 20:
        print(words[1][number])
    else:
        # гадаю ліпше винести операції з number на за межі print, бо код є перевантажений логікою
        #strNumber = str(number)
        # i = len(strNumber)
        # j = int(strNumber[0])
        #print(worlds[i][j], end=" ")
        #numToWorld(int(strNumber[1:]))
        print(words[len(str(number))][int(str(number)[0])], end=" ")
        numToWord(int(str(number)[1:]))


if __name__ == '__main__':
    namespace = createParser().parse_args(sys.argv[1:])
    assert namespace.digit.isdigit() and 0 <= int(namespace.digit) < 10_000, "Очікується натуральне менше 10 000"
    if int(namespace.digit) == 0:
        print("нуль")
    else:
        numToWord(int(namespace.digit))
