from models.apartments import Apartment
from helpers.input_helper import get_string, get_price
from helpers.output_helper import pretty_print


class Apartment_service():
    def apartments_list(self):
        print("Apartments List")

        apartments = Apartment.objects()
        columns = ('Name', 'Description', 'Price')
        
        pretty_print(apartments, columns)

    def add_apartment(self):
        print("Add Apartment")

        apartment = Apartment()
        apartment.name = get_string("Please, enter apt name: ")
        apartment.description = get_string("Please, enter apt description: ")
        apartment.price = get_price("Please, enter apt price: ")

        print(Apartment.price.min_value)

        apartment.save()

        print("Apartment saved")

    def search_apartment(self):
        name = get_string("Please, enter apt name: ")

        apartment = Apartment.objects().filter(name__icontains=name)

        columns = ('Name', 'Description', 'Price')
        pretty_print(apartment, columns)
        return apartment
