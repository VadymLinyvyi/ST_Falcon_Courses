import mongoengine


def global_init():
    mongoengine.register_connection("hotel", name="hotel_one")