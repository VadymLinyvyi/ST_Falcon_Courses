from colorama import Fore
from prettytable import PrettyTable

def pretty_print(table, columns):
    if not table or len(table) == 0:
        print(Fore.YELLOW, "No results found", Fore.RESET)
        return

    print(Fore.GREEN, "Results:", Fore.RESET)

    output_table = PrettyTable(columns)
    for row in table:
        rowData = []
        for cell in columns:
            rowData.append(row[cell.lower()])
        output_table.add_row(rowData)

    print(output_table)