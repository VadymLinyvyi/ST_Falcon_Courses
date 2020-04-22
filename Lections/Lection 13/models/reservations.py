import mongoengine

from models.guests import Guest


class Reservation(mongoengine.EmbeddedDocument):
    guest = mongoengine.ReferenceField(Guest)
    booked_date = mongoengine.DateTimeField()
    check_in_date = mongoengine.DateTimeField(required=True)
    check_out_date = mongoengine.DateTimeField(required=True)

    @property
    def duration(self):
        tmp = self.check_out_date - self.check_in_date
        return tmp.days
