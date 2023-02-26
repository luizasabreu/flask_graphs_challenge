import mongoengine as me  

class PenguinTravel(me.Document):
    name = me.StringField(max_length=200, required=True)
    is_business_trip = me.BooleanField(required=True)
    destinations = me.ListField(required=True)
