import datetime

from colorama import Fore


def get_string(message):
    styled_message = "{}{}{}".format(Fore.BLUE, message, Fore.RESET)
    while True:
        str = input(styled_message)
        str = str.strip()
        if len(str) >= 1:
            return str


def get_price(message):
    styled_message = "{}{}{}".format(Fore.BLUE, message, Fore.RESET)
    while True:
        str_number = input(styled_message)

        try:
            number = float(str_number)
            return number
        except:
            print(Fore.YELLOW + "Please, enter number value" + Fore.RESET)


def get_age(message, min_age):
    styled_message = "{}{}{}".format(Fore.BLUE, message, Fore.RESET)
    while True:
        str_number = input(styled_message)
        
        try:
            number = int(str_number)

            assert number >= min_age, "Please, enter age greater {}".format(min_age)
            return number
        except Exception as ex:
            print(Fore.YELLOW + "Please, enter number value" + Fore.RESET)
            print("Please, enter age greater {}".format(min_age))


def get_int(message, min_val, max_val):
    styled_message = "{}{}{}".format(Fore.BLUE, message, Fore.RESET)
    error_message = "{}Please, enter value between {} and {}{}".format(Fore.RED, min_val, max_val, Fore.RESET)
    if min_val == max_val:
        return min_val

    while True:
        str_number = input(styled_message)

        try:
            number = int(str_number)

            assert min_val <= number <= max_val, error_message
            return number
        except ValueError:
            print(Fore.YELLOW + "Please, enter number value" + Fore.RESET)
        except Exception:
            print(error_message)


def get_date(message):
    styled_message = "{}{} (YYYY-MM-DD) {}".format(Fore.BLUE, message, Fore.RESET)

    while True:
        str_date = input(styled_message)
        try:
            year, month, day = map(int, str_date.split('-'))
            new_date = datetime.date(year, month, day)
            return new_date
        except:
            print("Please, enter date (YYY-MM-DD)")
