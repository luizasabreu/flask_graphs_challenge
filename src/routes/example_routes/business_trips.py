import itertools
from src.models.penguin_travel import PenguinTravel

def business_trips() -> dict:
    """Get all consulted business trips information

    Returns: dict with information about business trips
    """
    penguin_travels = PenguinTravel.objects()
    names = {}
    count_business = 0
    visited_places_list = []
    for travel in penguin_travels:
        if travel.name in names.keys():
            names[travel.name] += 1
        else:
            names[travel.name] = 1

        if travel.is_business_trip:
            count_business+=1

        visited_places_list.append(travel.visited_places)

    visited_places_list = (list(itertools.chain(*visited_places_list)))  
    visited_places = {}
    for place in visited_places_list:
        if place in visited_places.keys():
            visited_places[place] += 1
        else:
            visited_places[place] = 1


    max_names_count = max(names.values())    
    penguins_with_most_trips = list(map(lambda x: x[0], filter(lambda x: x[1] == max_names_count, names.items())))

    max_visited_places_count = max(visited_places.values())
    most_visited_place = list(map(lambda x: x[0], filter(lambda x: x[1] == max_visited_places_count, visited_places.items())))

    total_business_trips = count_business

    result = {'penguins_with_most_trips': penguins_with_most_trips,
              'most_visited_place': most_visited_place,
              'total_business_trips': total_business_trips}
    
    return result

