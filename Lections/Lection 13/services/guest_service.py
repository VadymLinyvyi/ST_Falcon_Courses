from colorama import Fore
from models.guests import Guest
from helpers.input_helper import get_string, get_age
from helpers.output_helper import pretty_print


class Guest_service():
    def search_guest(self):
        name = get_string("Please, enter guest name: ")

        guest = Guest.objects().filter(name__icontains=name)

        columns = ('Name', 'Age', 'Is_card')
        pretty_print(guest, columns)
        return guest

    def guest_list(self):
        print("Guest List")
        guests = Guest.objects()
        columns = ('Name', 'Age', 'Is_card')

        pretty_print(guests, columns)

    def add_guest(self):
        min_age = Guest.age.min_value

        name = get_string("Please, enter you name: ")

        age = get_age("Please, enter you age: ", min_age=min_age)

        guest = Guest(name=name, age=age)
        guest.save()
        
        print(Fore.GREEN, "Guest added", Fore.RESET)
        return guest
