# Graph implementation using Adjascency List

class Graph:
    def __init__(self):
        self.adjList = {}

    def add_vertex(self, vertex):
        self.adjList[vertex] = []

    def add_edge(self, source, destination):
        if source not in self.adjList:
            self.add_vertex(source)

        if destination not in self.adjList:
            self.add_vertex(destination)

        self.adjList[source].append(destination)
        self.adjList[destination].append(source)

    def print_graph(self):
        for vertex, neighbors in self.adjList.items():
            print(f"Vertex {vertex}: ", end="")
            print(", ".join(map(str, neighbors)))