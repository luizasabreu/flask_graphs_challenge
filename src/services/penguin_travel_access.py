from typing import List
from src.models.penguin_travel import PenguinTravel


def save_penguin_travel(name: str, business: bool, destinations: List[str]) -> None:
    """Creates a PenguinTravel object and save name, is_business_trip and destination inside the database.
    """
    penguin_travel = PenguinTravel(name=name, 
                                   is_business_trip=business, 
                                   destinations=destinations)
    penguin_travel.save()

def get_penguin_travels():
    """Get all PneguinTravel objects
    """
    return PenguinTravel.objects()

