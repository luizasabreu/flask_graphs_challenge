from typing import List
from flask import request
from src.models.penguin_travel import PenguinTravel
from src.services import get_optimal_path
import mongoengine as me

def __saveData(name: str, business: bool, visited_places: List[str]):
    penguin_travel = PenguinTravel(name=name, 
                                   is_business_trip=business, 
                                   visited_places=visited_places)
    penguin_travel.save()
    

def calculate() -> List[str]:
    """Find all places that must be visited in order to have a minimum travel time for a given input

    Returns: dict with all places to visit
    """    
    data = request.get_json()
    destinations = data['destinations']
    distances = data['distances']
    
    places_to_travel = get_optimal_path(destinations, distances)
    
    __saveData(data['name'], data['business'], places_to_travel)

    return places_to_travel

