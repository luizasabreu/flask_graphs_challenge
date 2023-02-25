from src.services.penguin_travel_access import get_penguin_travels
from src.services.travel_statistics import get_most_visited_places, get_penguins_with_most_trips, get_total_business_trips

def business_trips() -> dict:
    """Get all consulted business trips information

    Returns: dict with information about business trips
    """
    penguin_travels = get_penguin_travels()
    return {'penguins_with_most_trips': get_penguins_with_most_trips(penguin_travels),
            'most_visited_place': get_most_visited_places(penguin_travels),
            'total_business_trips': get_total_business_trips(penguin_travels)}
    

