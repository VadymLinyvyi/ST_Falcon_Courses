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
        assert 0, "Coudn't find transport " + type


class AircraftFactory(TransportInterface):
    @staticmethod
    def getTransport(type):
        if type == "plane":
            return Plane()
        if type == "helicopter":
            return Helicopter()
        assert 0, "Coudn't find transport " + type