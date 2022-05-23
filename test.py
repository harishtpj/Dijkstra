from dijkstra import Graph

adjgraph = Graph(3)

adjgraph.addEdge(0, 1, 3)
adjgraph.addEdge(0, 2, 5)
adjgraph.addEdge(1, 2, 1)

adjgraph.printMatrix()
adjgraph.allShortPaths(0)

################################################

adjgraph2 = Graph(9)
adjgraph2.initGraph(
    [[0, 4, 0, 0, 0, 0, 0, 8, 0],
        [4, 0, 8, 0, 0, 0, 0, 11, 0],
        [0, 8, 0, 7, 0, 4, 0, 0, 2],
        [0, 0, 7, 0, 9, 14, 0, 0, 0],
        [0, 0, 0, 9, 0, 10, 0, 0, 0],
        [0, 0, 4, 14, 10, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 1, 6],
        [8, 11, 0, 0, 0, 0, 1, 0, 7],
        [0, 0, 2, 0, 0, 0, 6, 7, 0]
        ]
)

adjgraph2.shortPath(0, 4)