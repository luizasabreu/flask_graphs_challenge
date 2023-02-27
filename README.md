# Celus Python Challenge
![python 3.8 ][python_version]
![MongoDB][mongo_version]

[python_version]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=white
[mongo_version]: https://img.shields.io/badge/MongoDB-%234ea94b.svg?style=for-the-badge&logo=mongodb&logoColor=white

## Introduction
The main goal of this project was to extend a basic API that is part of a platform responsible to minimize travel time, based on destinations and distances between different places, so the penguins could spend more time at their final destination.  
As a backend developer, the main responsibility was to add two routes: 
1. A route: `/calculate` that find all places that must be visited in order to have a minimum travel time for a given input 
2. A route `/business-trips` to get all consulted business trip information that can be used to think of new strategies. 


## How to install
A base API with a MongoDB connection already exists at `docker-compose.yml`. 
To run it, execute the following command:
```sh
docker-compose rm -f; docker-compose -f docker-compose.yml up --build --force-recreate
```

Using a virtual environment with [Python 3.8](https://www.python.org/downloads/release/python-380/), install dependencies using:
```sh
python3 -m venv env; source env/bin/activate
```

All the created tests can be run using:
```sh
pytest test/
```

The example test given in the instructions can be run using:
```sh
pythton example.py
```
---
## Project structure, routes created and other technology choices
In the following session will be presented the project structure, and routes that were created focused on the algorithm strategies and technology choices that were made. 

## Project Structure
The project follows this path structure: 
```
.
├── app.py
├── dev-requirements.txt 
├── docker-compose.yml
├── Dockerfile
├── example.py
├── Instructions.md
├── README.md
├── requirements.txt
├── src
    ├─── database.py
    ├─── models                
    │   └─── example.py
    │   └─── penguin_travel.py
    ├─── routes
    │   ├─── add_routes.py
    │   ├─── business_trips.py
    │   ├─── calculate.py
    │   ├─── example_routes
    │   │   └─── count_calls.py
    │   │   └─── list_routes.py
    ├─── services
    │   ├─── path_optimization.py 
    │   ├───  penguin_travel_access.py
    │   ├───  travel_statistics.py
├── test
    ├─── routes_tests
    │   └─── conftest.py
    │   └─── test_route_business_trips.py
    │   └─── test_route_calculate.py
    │   └─── test_route_count_calls.py
    ├─── services_tests
    │   └─── conftest.py
    │   └─── test_path_optimization.py
    │   └─── test_penguin_access.py
    │   └─── test_travel_statistics.py
```

## Route: /calculate
* Path: `src\routes\calculate.py`

The `calculate` route is responsible to find all places that must be visited to have a minimum travel time for a given input. The input has information about the destinations and distances between cities related to the time taken to travel between them. It returns a dict with all places to visit in a certain order that guarantees minimal time on the road. 
This route has a dependency on the get_optimal_path and save_penguin_travel services. 

### Service: path_optimization
* Path: `src\services\path_optimization.py`

Inside this service is the main function `get_optimal_path` that is used by the `/calculate` route. 
Was used the library [NetworkX](https://networkx.org/) to create a graph and to use the Dijkstra method to find the [shortest path](https://networkx.org/documentation/stable/reference/algorithms/shortest_paths.html) between two nodes. 

A graph is a structure that can illustrate the problem where the nodes are the cities on the map and the edges are the roads with a certain weight (the time taken to travel between the cities). Considering this given input:
```
"distances": ["Munich - Munich: 0",
              "Munich - Kinganru: 3",
              "Munich - Facenianorth: 7",
              "Munich - SantaTiesrie: 4",
              "Munich - Mitling: 1",
              "Kinganru - Facenianorth: 2",
              "Kinganru - SantaTiesrie: 1",
              "Kinganru - Mitling: 1",
              "Facenianorth - SantaTiesrie: 5",
              "Facenianorth - Mitling:  3",
              "SantaTiesrie - Mitling: 2"]

"destinations": ["Kinganru", "Facenianorth", "SantaTiesrie"]
```
A graph that can illustrate it: 
![graph](images\graph.png)










## Penguin travel model
...

## Route: /business-trips
...

## Tests 
...