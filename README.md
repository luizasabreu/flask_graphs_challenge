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

---

## Project structure and algorithm strategy choices
In the following session will be presented some graph theory and the explanation of the Dijkstra algorithm chosen to deal with the minimal path problem. After that, will be presented the project structure, routes, and models that were created. 

---

## Graph theory and Dijkstra algorithm
A graph is a structure that can illustrate the problem where the nodes are the cities on the map and the edges are the roads with a certain weight which is the time taken to travel between the cities. 

Considering this given input:
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
```
A graph that can illustrate it can be draw as:

![graph](images\graph.png)

Dijkstra algorithm is a strategy to find minimal paths between two nodes in a graph. It used a [greedy approach](https://www.programiz.com/dsa/greedy-algorithm#:~:text=A%20greedy%20algorithm%20is%20an,if%20the%20choice%20is%20wrong.) so it won’t work correctly with negative weights but, for the case analyzed, it's not a problem considering that a path will never have a negative time between two cities. 

In a summarized way, the algorithm:

> 1. Starts at the node that we give as a parameter and it will return the shortest path between this node and all the other nodes (or vertexes) in the graph.
> 2. It calculates the shortest distance from each node to the source and saves this value if it finds a shorter path that the path that it had saved before. It calculates the distance between a node and the origin node, if this distance is less than it has been saved before, the new minimum distance will be the new distance.
> 3. Once Dijkstra’s algorithm has found the shortest path between the origin node and another node, it marks the node as visited (if it didn’t do it the algorithm could enter into an infinite loop).
> 4. Steps 2 and 3 are repeated until all the nodes are visited. This way, we have visited all the nodes and we’ve saved the shortest path possible to reach each node.

> <cite>https://medium.com/codex/how-does-dijkstras-algorithm-work-easy-explanation-in-less-than-5-minutes-e27f46795c18</cite>

---



## Route: /calculate
* Path: `src\routes\calculate.py`

The `calculate` route only allows POST and is responsible to find all places that must be visited to have a minimum travel time for a given input. 

- The input has information about the destinations and distances between cities related to the time taken to travel between them. 

- The output returns a dictionary with all places to visit in a certain order that guarantees minimal time on the road. 

This route has a dependency on the following services: 
- `get_optimal_path`
-  `save_penguin_travel` 


## Service: path_optimization
* Path: `src\services\path_optimization.py`

Inside this service is the main function `get_optimal_path` that is used by the `/calculate` route. Using [NetworkX](https://networkx.org/) it's possible to automatize how to [create a graph](https://networkx.org/documentation/stable/tutorial.html) and how to use the Dijkstra algorithm calling the function [shortest_path](https://networkx.org/documentation/stable/reference/algorithms/shortest_paths.html).

Getting the following destinations: 
```
"destinations": ["Kinganru", "Facenianorth", "SantaTiesrie"]
```
Can be understood that the penguin is going out from the start point which is Munich and want to be on Kinganru using the route with minimal weight. Using Dijkstra the result was going to be `Munich - Mitling - Kinganru`.

![path1](images\path1.png)

From Kinganru, the penguin wants to go to Facenianorth, the following path is going to be `Kinganru - Facenianorth`

 ![path2](images\path2.png)

From Facenianorth, the penguin wants to go to SantaTiesrie, the following path is going to be `Facenianorth - Kinganru - SantaTiesrie`

 ![path3](images\path3.png)

That's the behavior that `path_otimization` service tries to reproduce. From each city in `destinations` input, the Dijkstra algorithm function is called to try to find the minimal path between the actual city and the next destination.

The service returns the optimal path that was found after all destinations analysis and the order of the cities that the penguin is going to be.



## Service: penguin_travel_access
* Path: `src\services\penguin_travel_access.py`

After getting the optimal travel path, the function `save_penguin_travels` is called inside the `/calculate` route. This function is inside the penguin_travel_access file and was created to create a `PenguinTravel` model and save it inside the database. 

To collect the data that are saved inside the database, the function `get_penguin_travels` were created.

## Model: PenguinTravel
A `PenguinTravel` class was created to represent the travel that a penguin is doing. The model has three fields that are: 
- `name` - string type - the Penguin's name
- `is_business_trip` - boolean type - True if it's a business trip or False if it's not
- `destinations` - list type - a list of strings with the destinations.

The distances between cities and the minimal path are not saved inside the model because they are not being used by any other route and were chosen to implement the simplest solution. 

If more routes were implemented and the API was dealing with more strategies using more complex data, the information could be saved in separate models. Could exist a specific penguin model that would have all the information about the person like name, age, and address, for example, and another model related to the business with the data about destinations, distances, and if it's a business trip.

## Route: /business-trips
* Path: `src\routes\business_trips.py`

The `business-trips` route is responsible to get information about all business trips. Only allows GET and expected a JSON with the following results: 
   * `penguins_with_most_trips`: List[str]. Penguins with most business trips. If more than one penguin has the same number of trips, all must be on the list.
   * `most_visited_places`: List[str]. Places that most appear as destinations (places between destinations don't count!). If more than one place appears on the list, all of them must be returned.
   * `total_business_trips`: int. The number of business trips.

The first action on this route is to call `get_penguin_travels` which is a function inside the `penguin_travel_access` service that returns the `PenguinTravel` model. 

After that, are called the following functions:
-  `get_penguins_with_most_trips`
- `get_most_visited_places`
- `get_total_business_trips` 

All of them are inside `travel_statistics` service:  

## Service: travel_statistics
* Path: `src\services\travel_statistics.py`

After getting `PenguinTravel` information, `penguins_with_most_trips` are calculated using `get_penguins_with_most_trips` function. This function creates a dictionary where the keys are the penguin's names and the values are the number of times that they are mentioned inside the database 'name' field. The return of this function is a list of the most popular names. 

The function `get_most_visited_places` works in a similar way creating a dictionary where the keys are the destination places and the values are the number of times that they are mentioned inside the database 'destinations' field. The return of this function is a list of the most popular destinations. 

The last function `get_total_business_trips` counts how many business trip registers are in the database. 

---

## Tests 
Some tests were created to guarantee code integrity, they were split between route_tests and services_tests. 

### Services tests:
Were created a test file for each service: 
* `test_path_optimization` 
    * `test_get_optimal_path`
    * `test_get_optimal_path_without_destinations`
    * `test_get_optimal_path_with_negative_distance`
    * `test_get_optimal_path_without_distances`


* `test_penguin_access`
    * `test_save_penguin_travel`

* `test_travel_statistics`
    * `test_get_penguins_with_most_trips`
    * `test_get_most_visited_places`
    * `test_get_total_business_trips`


### Route tests:
Were created a test file for each route: 
* `test_route_business_trips`
    * `test_route_business_trips`

* `test_route_calculate`
    * `test_route_calculate`
    * `test_route_calculate_from_example`

* `test_route_count_calls`







---
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

The example test given in the instructions can be running using:
```sh
pythton example.py
```
---

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