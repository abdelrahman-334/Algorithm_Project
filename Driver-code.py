from queue import PriorityQueue
from Graph import *
import heapq


g = Graph(5)
g.addEdge(0, 1, 3)
g.addEdge(0, 3, 7)
g.addEdge(1, 3, 2)
g.addEdge(1, 2, 4)
g.addEdge(2, 4, 6)
g.addEdge(3, 2, 5)
g.addEdge(3, 4, 4)
g.Dijkstra(src=0)