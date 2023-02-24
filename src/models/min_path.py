from typing import List
from dijkstar import Graph, find_path

def create_graph(distances: List[str]) -> Graph:
    graph = Graph()    
    for register in distances:
        origin = register.split("-")[0].strip()
        destination = register.split("-")[1].split(":")[0].strip()
        hours = int(register.split("-")[1].split(":")[1].strip())
        edge = (hours, destination)

        graph.add_edge(origin.strip(), destination.strip(), hours)
    return graph

def cost_func(u, v, edge, prev_edge):
     length, name = edge
     if prev_edge:
         prev_name = prev_edge[1]
     else:
         prev_name = None
     cost = length
     if name != prev_name:
         cost += 10
     return cost

def min_path_calc(self, destinations: List[str], distances: List[str]) -> List[str]:
    destinations.insert(0,'Munich')
    graph = create_graph(distances)
    places = []
    # for i in range(len(destinations)-1):
    path = find_path(graph, destinations[2], destinations[3])# , cost_func=cost_func)
    places.append(path.nodes)

    
    import pdb; pdb.set_trace()
    
    return ["result"]

