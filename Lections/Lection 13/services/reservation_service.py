from colorama import Fore
from helpers.output_helper import pretty_print
from models.apartments import Apartment
from models.reservations import Reservation
from helpers.input_helper import get_int, get_date
import datetime
from services import Apartment_service, Guest_service



class Reservation_service():
    def reservation_list_filter_select(self):
        print("Filter by [a]partment")
        print("Filter by [g]uest")
        command = input(Fore.YELLOW+">"+Fore.RESET)
        if command.strip().lower() == 'a':
            self.reservation_list()
        elif command.strip().lower() == 'g':
            self.reservation_list_filtered_by_guest()
        else:
            print("Unknown command")

    def reservation_list_filtered_by_guest(self):
        Guests = Guest_service()
        guests = Guests.search_guest()
        if guests is None or len(guests) == 0:
            print(Fore.YELLOW, "Guests not found", Fore.RESET)
            return
        rowIdx = get_int("Please, select guest name: ", 1, len(guests))-1
        result = []

        guest = guests[rowIdx]
        columns = ('Check_in_date', 'Check_out_date', 'Booked_date')
        reservations = Apartment.objects(reservations__guest=guest).all()
        for apts in reservations:
            data = {}
            data['apartment'] = apts.name
            for cell in columns:
                data[cell.lower()] = apts.reservations[0][cell.lower()]
            result.append(data)
        columns = ('Apartment', 'Check_in_date', 'Check_out_date', 'Booked_date')
        pretty_print(result, columns)



    def reservation_list(self):
        Apartments = Apartment_service()
        apartments = Apartments.search_apartment()

        if apartments is None or len(apartments) == 0:
            print(Fore.YELLOW, "Apartments not found", Fore.RESET)
            return

        rowIdx = get_int("Please, select apt number: ", 1, len(apartments))-1

        apartment = apartments[rowIdx]
        reservations = apartment.reservations
        columns = ('Check_in_date', 'Check_out_date', 'Booked_date')
        pretty_print(reservations, columns)



    def add_reservation(self):
        print("Add Reservation")

        Apartments = Apartment_service()
        apartments = Apartments.search_apartment()

        if apartments is None or len(apartments) == 0:
            print(Fore.YELLOW, "Apartments not found", Fore.RESET)
            return

        rowIdx = get_int("Please, select apt number: ", 1, len(apartments))-1

        apartment = apartments[rowIdx]

        Guests = Guest_service()
        guests = Guests.search_guest()

        if guests is None or len(guests) == 0:
            guest = Guests.add_guest()
        else:
            rowId = get_int("Please, select guest number: ", 1, len(guests))-1
            guest = guests[rowId]

        reservation = Reservation()

        reservation.guest = guest
        reservation.booked_date = datetime.datetime.now()
        reservation.check_in_date = get_date("Please, enter check in date: ")
        reservation.check_out_date = get_date("Please, enter check out date: ")

        if reservation.check_in_date > reservation.check_out_date:
            print("Check out date must be later than the check in date")
            return

        apartment.reservations.append(reservation)

        apartment.save()

        columns = ('Check_in_date', 'Check_out_date', 'Booked_date')
        pretty_print([reservation], columns)
        print("{} Booking duration is {} day(s).{}".format(Fore.BLUE, reservation.duration, Fore.RESET))

        print(Fore.GREEN, "Reservation made successfully", Fore.RESET)
