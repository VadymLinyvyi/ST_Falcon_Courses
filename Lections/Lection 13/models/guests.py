import mongoengine


class Guest(mongoengine.Document):
    name = mongoengine.StringField(required=True)
    age = mongoengine.IntField(min_value=16, required=True)
    is_card = mongoengine.BooleanField(default=True)

    meta = {
        'db_alias': 'hotel',
        'collection': 'guests'
    }