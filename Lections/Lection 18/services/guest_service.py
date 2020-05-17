from colorama import Fore
from models.guests import Guest
from helpers.input_helper import (get_string, get_price, get_age)
from helpers.output_helper import (pretty_print)


class Guest_service():
    def search_guest(self, name, last_name, age):
        guest = Guest.objects().filter(name__icontains=name, last_name__icontains=last_name, age__icontains=int(age))

        columns = ('Name', 'Last_name', 'Age', 'Is_card')
        pretty_print(guest, columns)
        return guest

    def guest_list(self):
        print("Guest List")
        guests = Guest.objects()
        columns = ('Name', 'Last_name', 'Age', 'Is_card')
        
        pretty_print(guests, columns)
        return guests

    def get_guests(self):
        guests = Guest.objects().order_by('name')
       
        rows = []
        for guest in guests:
            rows.append("{} {}, {}".format(guest['name'], guest['last_name'], guest['age']))
        return rows

    def add_guest(self):
        min_age = Guest.age.min_value
        age_retrieve_message = "Please, enter you age: {}".format(min_age)

        name = get_string("Please, enter you name: ")
        last_name = get_string("Please, enter you last name: ")
        age = get_age(age_retrieve_message, min_age = min_age)

        guest = Guest(name = name, last_name = last_name, age = age)

        guest.save()
        
        print(Fore.GREEN, "Guest added", Fore.RESET)

    def update_data(self, data):
        guest = Guest.objects(name=data['name']).first()

        if not guest:
            guest = Guest()

        guest.name = data['name']
        guest.last_name = data['last_name']
        guest.age = int(data['age'])
        guest.is_card = bool(data['is_card'])
        guest.save()