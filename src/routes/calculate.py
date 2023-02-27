from typing import List
from flask import request
from src.services import get_optimal_path

from src.services.penguin_travel_access import save_penguin_travel

def calculate() -> List[str]:
    """Find all places that must be visited to have a minimum travel time for a given input

    Returns: dict with all places to visit
    """    
    data = request.get_json()
    destinations = data['destinations']
    distances = data['distances']
    
    places_to_travel = get_optimal_path(destinations, distances)
    
    save_penguin_travel(name=data['name'], business=data['business'], destinations=destinations)

    return places_to_travel

