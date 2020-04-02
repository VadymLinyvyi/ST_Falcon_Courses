class TransportInterface:
    def drive(self):
        pass


class Car(TransportInterface):
    def drive(self):
        print("Give ride by car")


class Ship(TransportInterface):
    def drive(self):
        print("Give ride by ship")


class TransportFactory:
    @staticmethod
    def getTransport(type):
        if type == "car":
            return Car()
        if type == "ship":
            return Ship()
        assert 0, "Coudn't find transport " + type


#car = TransportFactoty.getTransport("car")
#car.drive()

#ship = TransportFactoty.getTransport("ship")
#ship.drive()


class AircraftInterface:
    def getType(self):
        pass


class Plane(AircraftInterface):
    def getType(self):
        print("Plane")


class Helicopter(AircraftInterface):
    def getType(self):
        print("Helicopter")


class VehileInterface:
    def getType(self):
        pass


class Car(VehileInterface):
    def getType(self):
        print("Car")


class Truck(VehileInterface):
    def getType(self):
        print("Truck")


class TransportInterface:
    def getTransport(self, type):
        pass


class VehicleFactory(TransportInterface):
    @staticmethod
    def getTransport(type):
        if type == "car":
            return Car()
        if type == "truck":
            return Truck()
        assert 0, "Couldn't find transport " + type


class AircraftFactory(TransportInterface):
    @staticmethod
    def getTransport(type):
        if type == "plane":
            return Plane()
        if type == "helicopter":
            return Helicopter()
        assert 0, "Couldn't find transport " + type


class CarrierFactory:
    @staticmethod
    def getCarrier(type):
        if type == "vehicle":
            return VehicleFactory()
        if type == "aircraft":
            return AircraftFactory()
        assert 0, "Couldn't find transport " + type


aircraft = CarrierFactory.getCarrier("aircraft")
plane = aircraft.getTransport("plane")
plane.getType()

vehicle = CarrierFactory.getCarrier("vehicle")
car = vehicle.getTransport("car")
car.getType()