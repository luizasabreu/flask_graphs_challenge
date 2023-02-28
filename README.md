# Celus Python Challenge
![python 3.8 ][python_version]
![MongoDB][mongo_version]

[python_version]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=white
[mongo_version]: https://img.shields.io/badge/MongoDB-%234ea94b.svg?style=for-the-badge&logo=mongodb&logoColor=white

## 1. Introduction
The main goal of this project was to extend a basic API that is part of a platform responsible to minimize travel time, based on destinations and distances between different places, so the penguins could spend more time at their final destination.  
For the backend development the main task was to add two routes: 
1. A route: `/calculate` that find all places that must be visited to have a minimum travel time for a given input 
2. A route `/business-trips` to get all consulted business trip information that can be used to think of new strategies. 

For that the project will have three layers:
* __an API layer__ arranging the routes and calls to the service layer;
* __a Service layer__ performing calculations, manipulations and calling the model layer;
* __a Model layer__ performing basic operations on MongoDB.

---

## 2. Algorithm strategy choices

In the following section, it will be presented some concepts of graph theory and a quick summary of the Dijkstra algorithm, chosen to deal with the minimal path problem. After that, it will be presented the project structure, routes, and models that were created. 


### 2.1 Graph theory
A graph is a structure that can represent the problem where the nodes are the cities on the map and the edges are the roads with a certain weight which is the time taken to travel between the cities. In this case, we will use an undirected graph, which means that the weight from nodes A to B is the same as from B to A. 

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
A graph can be drawn as:

![graph](images\graph.png)

### 2.2 Dijkstra algorithm

The Dijkstra algorithm is a strategy to find minimal paths between two nodes in a graph. It used a [greedy approach](https://www.programiz.com/dsa/greedy-algorithm#:~:text=A%20greedy%20algorithm%20is%20an,if%20the%20choice%20is%20wrong.) so it won’t work correctly with negative weights but, for the case analyzed, it's not a problem considering that a path will never have a negative time between two cities. 

In a summarized way, the algorithm:

> 1. Starts at the node that we give as a parameter and it will return the shortest path between this node and all the other nodes (or vertexes) in the graph.
> 2. It calculates the shortest distance from each node to the source and saves this value if it finds a shorter path that the path that it had saved before. It calculates the distance between a node and the origin node, if this distance is less than it has been saved before, the new minimum distance will be the new distance.
> 3. Once Dijkstra’s algorithm has found the shortest path between the origin node and another node, it marks the node as visited (if it didn’t do it the algorithm could enter into an infinite loop).
> 4. Steps 2 and 3 are repeated until all the nodes are visited. This way, we have visited all the nodes and we’ve saved the shortest path possible to reach each node.
> 
> <cite>https://medium.com/codex/how-does-dijkstras-algorithm-work-easy-explanation-in-less-than-5-minutes-e27f46795c18</cite>

Comparing it with other algorithms for the same objective, like the Floyd-Warshall algorithm, the Dijkstra has a time complexity of O(n^2) in the worst case, while its counterpart has a time complexity of O(n^3).

---

## 3. Routes

### 3.1 `POST /calculate`
* `src\routes\calculate.py`

This route is responsible to find all places that must be visited to have a minimum travel time for a given sequence of destinations. 

**Input**: json with the name of the penguin, the desired sequence of destinations, if it is a business trip and distances between cities related to the time taken to travel between them. 

**Output**: a JSON with all places to visit so that guarantees minimal travel time. 

```json
{
    "places_to_travel": ["Munich", "Mitling", "Kinganru", "Facenianorth", "Kinganru", "SantaTiesrie"]
}
```

This route has a dependency on the following services: 
- `get_optimal_path`
- `save_penguin_travel` 

### 3.2 `GET /business-trips`
* `src\routes\business_trips.py`

This route is responsible to get information about all business trips. 

**Output**: a JSON with the following schema:

* `penguins_with_most_trips` -> `List[str]`
    * Penguins with most business trips. If more than one penguin has the same number of trips, all must be on the list.
* `most_visited_places` -> `List[str]`
    * Places that most appear as destinations (places between destinations don't count!). If more than one place appears on the list, all of them must be returned.
* `total_business_trips` -> `int`
    * The total number of business trips.

The first action on this route is to call `get_penguin_travels` which is a function inside the `penguin_travel_access` service that returns the `PenguinTravel` model. 

After that, are called the following functions:
- `get_penguins_with_most_trips`
- `get_most_visited_places`
- `get_total_business_trips` 

All of them are inside `travel_statistics.py` service.  

---

## 4. Services

### 4.1 `path_optimization`
* `src\services\path_optimization.py`

This service exposes the `get_optimal_path` method that is used by the `/calculate` route.
To model and process the date the [NetworkX](https://networkx.org/) will be used since it's possible to [create a graph](https://networkx.org/documentation/stable/tutorial.html) and use the Dijkstra algorithm by calling the [shortest_path](https://networkx.org/documentation/stable/reference/algorithms/shortest_paths.html) method.


From each city in the `destinations` input, the `shortest_path` method is called to find the minimal path between the actual city and the next destination.

The service then returns the optimal path that was found after all destinations analysis were made and the order of the cities that the penguin is going to be in.

Let's make an example using the following sequence of destinations:
```
["Kinganru", "Facenianorth", "SantaTiesrie"]
```
For the first destination, the penguin will start from Munich and wants to reach Kinganru using the minimal weight route. Using Dijkstra the result is going to be `Munich - Mitling - Kinganru`, which is optimal.

![path1](images\path1.png)

Now, from Kinganru to Facenianorth, the optimal path then will be `Kinganru - Facenianorth`.

 ![path2](images\path2.png)

Finally, from Facenianorth to Santa Tiesrie, the optimal path will be `Facenianorth - Kinganru - SantaTiesrie`.

 ![path3](images\path3.png)

So the final result will be the sequence 
```
"Munich" - "Mitling" - "Kinganru" - "Facenianorth" - "Kinganru" - "SantaTiesrie".
```

### 4.2 `penguin_travel_access`
* `src\services\penguin_travel_access.py`

After getting the optimal travel path, the function `save_penguin_travels` is called inside the `/calculate` route. This method creates a `PenguinTravel`` model instance and saves it inside the database. 

The `get_penguin_travels` function collects the `PenguinTravel` models saved in the database.

### 4.3 `travel_statistics`
* `src\services\travel_statistics.py`

After getting the `PenguinTravel` information, `penguins_with_most_trips` are calculated using `get_penguins_with_most_trips` function. This function creates a dictionary where the keys are the penguin's names and the values are the number of times that they are mentioned inside the database 'name' field. The return of this function is a list of the most popular names. 

The function `get_most_visited_places` works in a similar way creating a dictionary where the keys are the destination places and the values are the number of times that they are mentioned inside the database 'destinations' field. The return of this function is a list of the most popular destinations. 

The last function `get_total_business_trips` counts how many business trip registers are in the database. 

For example, having on the bank these three registers: 
```json
{"name": "Alanto",
"destinations": ["Kinganru", "Facenianorth", "SantaTiesrie"],
"business": True}

{"name": "Alanto",
"destinations": ["Kinganru", "Facenianorth", "SantaTiesrie"],
"business": True}

{"name": "Alanto",
"destinations": ["Kinganru", "Facenianorth", "SantaTiesrie"],
"business": True}

```
The output from each function will be:
```json
get_penguins_with_most_trips : ["Alanto"]

get_most_visited_places: ["Kinganru", "Facenianorth", "SantaTiesrie"]

get_total_business_trips: 3

```


---

## 5. Models

### 5.1 PenguinTravel
A `PenguinTravel` class was created to represent the travel that a penguin is doing. The model has three fields that are: 
- `name` - string type - the Penguin's name
- `is_business_trip` - boolean type - True if it's a business trip or False if it's not
- `destinations` - list type - a list of strings with the destinations.

The distances between cities and the minimal path are not saved inside the model because they are not being used by any other route and were chosen to implement the simplest solution. 

If more routes were implemented and the API was dealing with more strategies using more complex data, the information could be saved in separate models. Could exist a specific penguin model that would have all the information about the person like name, age, and address, for example, and another model related to the business with the data about destinations, distances, and if it's a business trip.

---

## 6. Tests 
Some tests were created to guarantee code integrity, they were split between route_tests and services_tests. 

### 6.1 Services tests:
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


### 6.2 Route tests:
Were created a test file for each route: 
* `test_route_business_trips`
    * `test_route_business_trips`
* `test_route_calculate`
    * `test_route_calculate`
    * `test_route_calculate_from_example`
* `test_route_count_calls`

---
## 7. How to install
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

## 8. Project Structure
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