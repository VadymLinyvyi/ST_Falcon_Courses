from colorama import Fore
from switchlang import switch
from services import Apartment_service, Guest_service, Reservation_service
import services.mongo_setup as db_setup


def main():
    db_setup.global_init()

    print(Fore.BLUE, "Hotel service", Fore.RESET)
    commands()

    apartments = Apartment_service()
    guests = Guest_service()
    reservations = Reservation_service()

    while True:
        action = get_action()
        with switch(action) as s:
            s.case('l', apartments.apartments_list)
            s.case('a', apartments.add_apartment)
            s.case('s', apartments.search_apartment)
            s.case('v', guests.guest_list)
            s.case('g', guests.add_guest)
            s.case('b', reservations.reservation_list)
            s.case('m', reservations.add_reservation)
            s.case('?', commands)
            s.case('e', exit)
            s.default(lambda: print("Sorry, this is unknown command"))


def commands():
    print("What action would you like to do?")
   
    print("Apartments [L]ist")
    print("[A]dd apartment")
    print("[S]earch apartment")
    print("[V]iew guest")
    print("Add [g]uest")
    print("[B]ooking info")
    print("[M]ake reservation")
    print("[?] Help (this info)")
    print("[e] Exit")


def get_action():
    print(Fore.YELLOW + '>' + Fore.RESET, end='')
    action = input()
    return action.strip().lower()


if __name__ == '__main__':
    main()
