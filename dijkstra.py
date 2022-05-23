import sys

INF = sys.maxsize

class Graph:
    def __init__(self, size):
        self.graph = [[0 for i in range(size)] for j in range(size)]
        self.row = self.col = size
        self.length = size
    
    def initGraph(self, matrix):
        self.graph = matrix

    def addEdge(self, v1, v2, w):
        if v1 == v2:
            raise ValueError(f"Same vertex {v1} and {v2}")
        self.graph[v1][v2] = self.graph[v2][v1] = w
    
    def removeEdge(self, v1, v2):
        if self.graph[v1][v2] == 0:
            raise ValueError(f"No Egge between {v1} and {v2}")
        self.graph[v1][v2] = self.graph[v2][v1] = 0
    
    def printMatrix(self):
        for row in self.graph:
            row = [str(i) for i in row]
            print(" ".join(row))
        print()

    def minDistance(self, dist, Q):
        minimum = INF
        min_index = -1

        for i in range(len(dist)):
            if dist[i] < minimum and i in Q:
                minimum = dist[i]
                min_index = i
        return min_index
    
    def dijkstra(self, src):
        Q = [i for i in range(self.row)]
        distances = [INF for _ in range(self.row)]
        prev_paths = [-1 for _ in range(self.row)]

        distances[src] = 0

        while Q:
            u = self.minDistance(distances, Q)
            Q.remove(u)

            for i in range(self.col):
                if self.graph[u][i] and i in Q:
                    if distances[u] +  self.graph[u][i] < distances[i]:
                        distances[i] = distances[u] +  self.graph[u][i]
                        prev_paths[i] = u
        
        return distances, prev_paths
    
    def getRoute(self, prev, i, route):
        if i >= 0:
            self.getRoute(prev, prev[i], route)
            route.append(str(i))
        return route

    def shortPath(self, src, dst):
        dist , prev_paths = self.dijkstra(src)
        route = []
        self.getRoute(prev_paths, dst, route)
        route = " -> ".join(route)
        print(f"Shortest path between {src} and {dst}:")
        print(f"\tDistance : {dist[dst]}")
        print(f"\tRoute : {route}")
    
    def allShortPaths(self, src):
        print(f"{'Path':<8} {'Distance':<15} {'Route':<30}")
        print(f"{'-'*8} {'-'*15} {'-'*30}")
        for i in range(self.length):
            dist , prev_paths = self.dijkstra(src)
            route = []
            self.getRoute(prev_paths, i, route)
            route = "->".join(route)
            print(f"{f'{src}->{i}':<8} {dist[i]:<15} {route:<30}")
        print()