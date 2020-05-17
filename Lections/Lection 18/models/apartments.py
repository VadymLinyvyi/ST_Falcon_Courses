import mongoengine
from models.reservations import Reservation

class Apartment(mongoengine.Document):
    name = mongoengine.StringField(required=True, unique=True)
    price = mongoengine.FloatField(required=True, min_value=15)
    description = mongoengine.StringField()
    smoke_allowed = mongoengine.BooleanField(default=False)

    reservations = mongoengine.EmbeddedDocumentListField(Reservation)
    
    meta = {
        'db_alias': 'hotel',
        'collection': 'apartments'
    }