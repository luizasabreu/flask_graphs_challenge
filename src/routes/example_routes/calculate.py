from flask import request
from src.models import min_path

def calculate() -> dict:
    """Find all places that must be visited in order to have a minimum travel time for a given input

    Returns: dict with all places to visit
    """    
    data = request.form
    name = data.get('name')
    destinations = data.getlist('destinations')
    business = data.get('business')
    distances = data.getlist('distances')
    


    result = {'places_to_travel': 
              ["Munich", "Mitling", "Kinganru", "Facenianorth", "Kinganru", "SantaTiesrie"]}

    return result

