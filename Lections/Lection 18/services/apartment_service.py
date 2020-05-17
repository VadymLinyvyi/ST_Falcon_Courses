from models.apartments import Apartment
from helpers.input_helper import (get_string, get_price)
from helpers.output_helper import (pretty_print)


class Apartment_service():
    def apartments_list(self):
        print("Apartments List")
        apartments = Apartment.objects()
        return apartments

    def apartments_count(self):
        return len(self.apartments_list())

    def get_apartments(self):
        apartments = Apartment.objects().order_by('name')
        rows = []
        for apartment in apartments:
            rows.append(apartment.name)
        return rows

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
        print("Apartment Search")

        name = get_string("Please, enter apt name: ")

        apartment = Apartment.objects().filter(name = name)

        columns = ('Name', 'Description', 'Price')
        pretty_print(apartment, columns)

        return apartment

    def search_apartment(self, name):
        print("Apartment Search")

        apartment = Apartment.objects().filter(name = name)

        columns = ('Name', 'Description', 'Price')
        pretty_print(apartment, columns)

        return apartment

    def update_data(self, data):
        apartment = Apartment.objects(name=data['name']).first()

        if not apartment:
            apartment = Apartment()
        
        apartment.name = data['name']
        apartment.description = data['description']
        apartment.price = float(data['price'])
        apartment.save()

    def remove_apartment(self, name):
        print("removed")
        apartments = Apartment.objects(name=name)
        apartments.delete()
