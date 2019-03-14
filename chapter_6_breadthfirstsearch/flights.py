from collections import defaultdict
from pprint import pprint


class FlightNetwork:

    def __init__(self):
        self.neighbours = defaultdict(list)
        self.cost = defaultdict(list)
        
    def add_flight(self, source, destination, price):
        self.neighbours[source].append(destination)
        self.cost[source].append(price)

    def show_flights(self):
        pprint(dict(self.neighbours))
        print()
        pprint(dict(self.cost))

    def bfs(self, start_node):
        visited = [start_node]
        queue = [start_node]

        while queue:
            current_node = queue.pop(0)
           
            for neighbour in self.neighbours[current_node]: 
                if not neighbour in visited:
                    queue.append(neighbour)
                    visited.append(neighbour)
                    
        return visited

    def get_route(self, destination, source, parent):
        if destination[0] == source:
            return [source]
        
        routes = []
        for p in parent[destination]:
            routes.extend([r + "-->" + destination[0] for r in self.get_route(p, source, parent)])

        return routes

    def level_order_traversal(self, source, destination, stops_range):
        least_stops, max_stops = stops_range
        queue = [(source, 0, -1)]
        parent = defaultdict(list)

        while queue:
            location, cost_till_now, stops_since_source = queue.pop(0)
            
            if location in self.neighbours:
                for neighbour, cost in zip(self.neighbours[location], self.cost[location]):
                    parent[(neighbour, stops_since_source+1)].append((location, stops_since_source))
                    if stops_since_source < max_stops:
                        queue.append((neighbour, cost + cost_till_now, stops_since_source+1))

        return parent


f = FlightNetwork()
""" f.add_flight('Los Angeles', 'New Delhi', 200)
f.add_flight('Los Angeles', 'Japan', 87)
f.add_flight('Germany', 'New Delhi', 125)
f.add_flight('Italy', 'Los Angeles', 150)
f.add_flight('New Delhi', 'France', 100)
f.add_flight('Los Angeles', 'France', 200)
f.add_flight('Italy', 'New Delhi', 300)
f.add_flight('France', 'Norway', 175)
f.add_flight('Ireland', 'Chicago', 100)
f.add_flight('Chicago', 'Italy', 135)
f.add_flight('Los Angeles', 'Ireland', 100)
f.add_flight('Ireland', 'New Delhi', 200)
print(f.bfs("Los Angeles"))"""



f.add_flight('A', 'C', 10)
f.add_flight('A', 'B', 20)
f.add_flight('A', 'F', 14)
f.add_flight('B', 'D', 20)
f.add_flight('C', 'B', 120)
f.add_flight('C', 'M', 200)
f.add_flight('D', 'C', 75)
f.add_flight('C', 'E', 145)
f.add_flight('C', 'F', 50)
f.add_flight('D', 'E', 45)
f.add_flight('D', 'F', 60)
f.add_flight('M', 'F', 45)
f.add_flight('E', 'F', 60)

f.show_flights()
print()

parent = f.level_order_traversal('A', 'F', (2, 5))

for r in range(2, 6):
    print("\nFlights with {} stops in between are as follows:".format(r))
    routes = f.get_route(('F', r), 'A', parent)
    for r in routes:
        print(r)

