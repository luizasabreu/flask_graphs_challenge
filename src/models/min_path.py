from typing import List
import networkx as nx
import itertools

def create_graph(distances: List[str]):
    graph = nx.Graph()   
    for register in distances:
        origin = register.split("-")[0].strip()
        destination = register.split("-")[1].split(":")[0].strip()
        hours = int(register.split("-")[1].split(":")[1].strip())
        graph.add_node(origin)
        graph.add_node(destination)
        graph.add_edge(origin, destination, weight=hours)
    return graph               


def min_path_calc(self, destinations: List[str], distances: List[str]) -> List[str]:
    graph = create_graph(distances)
    destinations.insert(0, "Munich")
    path = [["Munich"]]
    for i in range(len(destinations)-1):
        cities = nx.shortest_path(graph, destinations[i], destinations[i+1], weight="weight")
        path.append(cities[1:])
    path = (list(itertools.chain(*path)))   
    
    return path

