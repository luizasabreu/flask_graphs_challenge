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
  
    penguins_with_most_trips = __get_keys_with_the_greatest_value(names)
    most_visited_place = __get_keys_with_the_greatest_value(visited_places)

    total_business_trips = count_business

    result = {'penguins_with_most_trips': penguins_with_most_trips,
              'most_visited_place': most_visited_place,
              'total_business_trips': total_business_trips}
    
    return result

def __get_keys_with_the_greatest_value(dictionary):
    max_value = max(dictionary.values())
    return list(map(__get_keys(), __filter_dict_by_max_value(dictionary, max_value)))

def __filter_dict_by_max_value(dictionary, max_value):
    return filter(__get_values_equals_to(max_value), dictionary.items())

def __get_values_equals_to(max_value):
    return lambda x: x[1] == max_value 

def __get_keys():
    return lambda x: x[0]