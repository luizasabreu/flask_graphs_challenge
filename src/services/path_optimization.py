from typing import List
import networkx as nx
import itertools

def get_optimal_path(destinations: List[str], distances: List[str]) -> List[str]:
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
    graph = nx.Graph()   
    for register in distances:
        origin = register.split("-")[0].strip()
        destination = register.split("-")[1].split(":")[0].strip()
        hours = int(register.split("-")[1].split(":")[1].strip())
        graph.add_node(origin)
        graph.add_node(destination)
        graph.add_edge(origin, destination, weight=hours)
    return graph   