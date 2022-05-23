from dijkstra import Graph

home = 0
nearby_shop = 1
school = 2
bus_stand = 3
bakery = 4
office = 5

map_graph = Graph(6)

map_graph.add_edge(home, nearby_shop, 7)
map_graph.add_edge(home, school, 9)
map_graph.add_edge(home, office, 14)
map_graph.add_edge(nearby_shop, bus_stand, 15)
map_graph.add_edge(nearby_shop, school, 10)
map_graph.add_edge(school, office, 2)
map_graph.add_edge(school, bus_stand, 11)
map_graph.add_edge(bakery, office, 9)
map_graph.add_edge(bakery, bus_stand, 6)

#map_graph.printMatrix()
map_graph.all_short_paths(school)