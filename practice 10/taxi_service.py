from colorama import Fore
from json_parser import parse
from random import randint
from math import ceil
from time import sleep


def get_command():
    service = input(Fore.YELLOW + ">" + Fore.RESET)
    return service.strip().lower()


def get_services():
    with open("prices.json", "r") as file:
        services = parse(file)
    return services["prices"]


def show_services(services):
    count_services = 0
    print("Select a taxi service")
    print("\tName\t\tEstimate")
    for service in services:
        count_services += 1
        print("[{}]\t{:12}{}".format(count_services, service["display_name"], service["estimate"]))
    print("[0] Exit")


def get_estimate(selected_service):
    return randint(selected_service.get("low_estimate"), selected_service.get("high_estimate"))


def print_selected_service_info(selected_service, distance, estimate):
    if selected_service.get("high_estimate") is None or selected_service.get("low_estimate") is None:
        print(Fore.RED + "We are sorry! This service is currently unavailable" + Fore.RESET)
        return False
    else:
        price = distance * estimate
        print("You selected " + Fore.BLUE + selected_service.get("display_name") + Fore.RESET)
        print("Distance - " + Fore.LIGHTRED_EX + str(distance) + Fore.RESET)
        print("Price - " + Fore.GREEN + str(price) + Fore.RESET + " " + selected_service.get("currency_code"))
        return True


def main():
    print(Fore.CYAN, "Taxi service\n", Fore.RESET)
    services = get_services()

    while True:
        show_services(services)
        command = get_command()

        if command == "0":
            return
        elif command.isdigit() and int(command) <= len(services):
            selected_service = services[int(command)-1]
            print("Specify the distance to your destination")
            distance = ceil(float(input(Fore.YELLOW + ">" + Fore.RESET)))
            estimate = get_estimate(selected_service)
            if print_selected_service_info(selected_service, distance, estimate):
                input("Start")
                start_trip(selected_service, distance, estimate)
                return
        else:
            print(Fore.RED + "Unknown command!" + Fore.RESET)


def start_trip(selected_service, distance, estimate):
    print("Starting the trip...")
    for i in range(1, distance + 1):
        print("{} km's, {} {}".format(i, i*estimate, selected_service.get("currency_code")))
        sleep(0.25)
    print("You trip is finished! The price is {} {}. Have a nice day!".format(distance*estimate, selected_service.get("currency_code")))


if __name__ == '__main__':
    main()
