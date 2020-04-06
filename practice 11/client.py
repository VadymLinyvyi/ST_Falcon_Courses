import os
import sys

from colorama import Fore
from switchlang import switch

from actions.book_actions import *
from actions.writer_actions import *

import models.book as book
import models.writer as writer

from services.data_service import (create_db)

sys.path.append(os.getcwd())


def main():
    print(Fore.GREEN, "Books world", Fore.WHITE)
    show_commands()

    while True:
        action = get_action()

        with switch(action) as s:
            s.case("b", books_list)
            s.case("i", get_book_info)
            s.case("r", add_book)
            s.case("l", view_writers)
            s.case("w", add_writer)
            s.case("?", show_commands)
            s.case("e", exit)
            s.default(lambda: print("Sorry, this is unknown command"))


def show_commands():
    print("What action would you like to do:")
    print("[B]ooks list")
    print("Book [i]nfo")
    print("[R]egister book")
    print("Writer [l]ist")
    print("Register a [w]riter")
    print("[?] Help (this info)")
    print("[E]xit")


def get_action():
    action = input(Fore.YELLOW + ">" + Fore.RESET)
    return action.strip().lower()


if __name__ == "__main__":
    create_db(writer.TABLE, book.TABLE)
    main()
