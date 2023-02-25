from typing import List
from src.models.penguin_travel import PenguinTravel


def save_penguin_travel(name: str, business: bool, places_to_travel: List[str]):
    penguin_travel = PenguinTravel(name=name, 
                                   is_business_trip=business, 
                                   places_to_travel=places_to_travel)
    penguin_travel.save()

def get_penguin_travels():
    return PenguinTravel.objects()