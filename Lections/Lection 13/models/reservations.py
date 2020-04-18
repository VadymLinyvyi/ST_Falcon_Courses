import mongoengine


class Reservation(mongoengine.EmbeddedDocument):
    guest_id = mongoengine.ObjectIdField()
    booked_date = mongoengine.DateTimeField()
    check_in_date = mongoengine.DateTimeField(required=True)
    check_out_date = mongoengine.DateTimeField(required=True)

    @property
    def duration(self):
        tmp = self.check_out_date - self.check_in_date
        return tmp.days