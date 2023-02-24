from typing import List
from dijkstar import Graph, find_path

def disktra_calc(self, destinations: List[str], distances: List[str]) -> List[str]:
    destinations.insert(0,'Munich')
    graph = create_graph(distances)
      


        
    import pdb; pdb.set_trace()
    
    return ["result"]

def create_graph(distances: List[str]) -> Graph:
    graph = Graph()    
    for register in distances:
        origin = register.split("-")[0]
        destination = register.split("-")[1].split(":")[0]
        hours = register.split("-")[1].split(":")[1]
        graph.add_edge(origin.strip(), destination.strip(), int(hours.strip()))
    return graph