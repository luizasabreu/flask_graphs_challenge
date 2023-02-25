from typing import List
from flask import request
from src.models.penguin_travel import PenguinTravel
from src.services import get_optimal_path
import mongoengine as me

def calculate() -> List[str]:
    """Find all places that must be visited in order to have a minimum travel time for a given input

    Returns: dict with all places to visit
    """    
    data = request.get_json()
    destinations = data['destinations']
    distances = data['distances']
    
    places_to_travel = get_optimal_path(destinations, distances)
    
    __save_penguin_travel(name=data['name'], business=data['business'], places_to_travel=places_to_travel)

    return places_to_travel

def __save_penguin_travel(name: str, business: bool, places_to_travel: List[str]):
    penguin_travel = PenguinTravel(name=name, 
                                   is_business_trip=business, 
                                   places_to_travel=places_to_travel)
    penguin_travel.save()