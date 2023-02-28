import itertools
from typing import List
from src.models.penguin_travel import PenguinTravel


def get_penguins_with_most_trips(penguin_travels: PenguinTravel) -> List[str]:
    """Creates a dictionary where
        * keys = penguin's names   
        * values = number of times that they are mentioned in the database    

    Returns: list of the most popular names
    """
    names_list = [travel.name for travel in penguin_travels]
    names_dict = __create_count_dict(names_list)

    return __get_keys_with_the_greatest_value(names_dict)

def get_most_visited_places(penguin_travels: PenguinTravel) -> List[str]: 
    """Creates a dictionary where
        * keys = destinations   
        * values = number of times that they are mentioned in the database    

    Returns: list of the most popular destinations
    """
    visited_places = [travel.destinations for travel in penguin_travels]
    visited_places_list = (list(itertools.chain(*visited_places)))
    visited_places_dict = __create_count_dict(visited_places_list)
    
    return __get_keys_with_the_greatest_value(visited_places_dict)


def get_total_business_trips(penguin_travels: PenguinTravel) -> int:
    """Counts how many business trip registers are in the database.

    Returns: int with the number of business trip registers
    """
    count_business = 0    
    for travel in penguin_travels:
        if travel.is_business_trip:
            count_business+=1

    return count_business  

def __create_count_dict(items_list: List[str]) -> dict:
    new_dict = {}
    for item in items_list:
        if item in new_dict.keys():
            new_dict[item] += 1
        else:
            new_dict[item] = 1

    return new_dict

def __get_keys_with_the_greatest_value(dictionary: dict) -> List[str]:
    max_value = max(dictionary.values())

    return list(map(__get_keys(), __filter_dict_by_max_value(dictionary, max_value)))

def __filter_dict_by_max_value(dictionary: dict, max_value: int) -> List[str]:
    return filter(__get_values_equals_to(max_value), dictionary.items())

def __get_values_equals_to(max_value: int) -> List[str]:
    return lambda x: x[1] == max_value 

def __get_keys() -> List[str]:
    return lambda x: x[0]