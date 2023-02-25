from flask import request
from src.models import min_path_calc

def calculate():
    """Find all places that must be visited in order to have a minimum travel time for a given input

    Returns: dict with all places to visit
    """    
    data = request.get_json()
    destinations = data['destinations']
    distances = data['distances']
    places_to_travel = min_path_calc(destinations, distances)
    
    return places_to_travel

