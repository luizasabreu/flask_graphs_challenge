from typing import List, Tuple
import networkx as nx
import itertools

def get_optimal_path(destinations: List[str], distances: List[str]) -> List[str]:
    """Get an optimal path based on penguin~s destinations and distances between cities

    Returns: a minimal path calculated using Dijkstra algorithm
    """
    graph = __create_graph(distances)
    destinations.insert(0, "Munich")
    path = [["Munich"]]

    for city in range(len(destinations)-1):
        cities = nx.shortest_path(graph, destinations[city], destinations[city+1], weight="weight")
        path.append(cities[1:])

    new_path = (list(itertools.chain(*path)))  
    destinations.remove("Munich")
    
    return new_path

def __create_graph(distances: List[str]) -> nx.Graph:
    assert distances != [''], AssertionError("Distances are a necessary data!")
    graph = nx.Graph()  
    for register in distances:
        origin, destination, hours = __parse_register(register)

        assert hours >= 0, AssertionError("Distances must be positive numbers!")

        graph.add_node(origin)
        graph.add_node(destination)
        graph.add_edge(origin, destination, weight=hours)        
    return graph

def __parse_register(register: str) -> Tuple[str, str, int]:
    origin, part_2 = register.split(" - ")
    destination, hours = part_2.split(":")
    return (origin.strip(), destination.strip(), int(hours.strip()))
