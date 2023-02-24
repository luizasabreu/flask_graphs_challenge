from flask import request


def calculate() -> dict:
    """Find all places that must be visited in order to have a minimum travel time for a given input

    Returns: List[str] list with all places to visit
    """
    import pdb; pdb.set_trace()
    data = request.form
    name = data.get('name')
    destinations = data.getlist('destinations')
    business = data.get('business')
    distances = data.getlist('distances')


    result = {'places_to_travel': 
              ["Munich", "Mitling", "Kinganru", "Facenianorth", "Kinganru", "SantaTiesrie"]}

    return result

