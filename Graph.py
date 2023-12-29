import heapq
from queue import PriorityQueue


class Graph:
    def __init__(self, n):
        self.N = n
        self.adj = [[] for _ in range(n)]

    def addEdge(self, u, v, w):
        self.adj[u].append((v, w))
        self.adj[v].append((u, w))

    def Dijkstra(self, src):
        pq = PriorityQueue()
        prev = [[]] * self.N
        pq.put((0, src))
        dist = [float("inf")] * self.N  # Make the value of all priorities infinite (lowest possible priority)
        dist[src] = 0  # Make the priority of the start node 0 (highest possible priority in a valid case)
        path = [[]] * self.N
        for i in range(self.N):

            d, u = pq.get()  # Pop the node with the least value (highest priority)

            for v, weight in self.adj[u]:  # Check all adjacent nodes for the current node in the adjacency matrix
                if dist[v] > dist[u] + weight:  # Ignore paths bigger than current path
                    dist[v] = dist[u] + weight  # Update path with smaller value
                    prev[v] = u
                    pq.put((dist[v], v))  # add node to queue (basic operation)

        for i in range(self.N):
            pointer = i
            print(f"the path to node {pointer} is ")
            while True:
                print(f"path:{pointer}")
                pointer = prev[pointer]
                if pointer == []:
                    print("-------------")
                    break
        for i in range(self.N):
            print(f"{i} \t\t {dist[i]}")
