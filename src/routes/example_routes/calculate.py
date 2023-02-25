from typing import List
from flask import request
from src.models.penguin_travel import PenguinTravel
from src.services import min_path_calc
import mongoengine as me

def saveData(name: str, business: bool, visited_places: List[str]):
    penguin_travel = PenguinTravel(name=name, 
                                   is_business_trip=business, 
                                   visited_places=visited_places)
    penguin_travel.save()
    

def calculate():
    """Find all places that must be visited in order to have a minimum travel time for a given input

    Returns: dict with all places to visit
    """    
    data = request.get_json()
    destinations = data['destinations']
    distances = data['distances']
    places_to_travel = min_path_calc(destinations, distances)
    
    saveData(data['name'], data['business'], places_to_travel)

    return places_to_travel

