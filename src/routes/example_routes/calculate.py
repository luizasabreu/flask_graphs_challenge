from flask import request
from src.models import min_path_calc

def calculate() -> dict:
    """Find all places that must be visited in order to have a minimum travel time for a given input

    Returns: dict with all places to visit
    """    
    data = request.form
    destinations = data.getlist('destinations')
    distances = data.getlist('distances')
    places_to_travel = min_path_calc(destinations, distances)
    

    result = {'places_to_travel': places_to_travel}

    return result

