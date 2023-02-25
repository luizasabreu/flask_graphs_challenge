import mongoengine as me  

class PenguinTravel(me.Document):
    name = me.StringField(max_length=200, required=True)
    is_business_trip = me.BooleanField(required=True)
    places_to_travel = me.ListField(required=True)
