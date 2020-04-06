from colorama import Fore
from prettytable import PrettyTable


def pretty_print(table):
    if not table or len(table) == 0:
        print(Fore.RED, "No results", Fore.RESET)
    else:
        print(Fore.GREEN, "Results", Fore.RESET)

        output_table = PrettyTable(table[0].keys())
        for row in table:
            output_table.add_row(list(row.values()))

        print(output_table)