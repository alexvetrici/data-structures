class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjMatrix = [[0] * vertices for _ in range(vertices)]

    def add_edge(self, source, destination):
        if 0 <= source < self.vertices and 0 <= destination < self.vertices:
            self.adjMatrix[source][destination] = 1
            self.adjMatrix[destination][source] = 1
        else:
            raise ValueError("Invalid vertex!")

    def remove_edge(self, source, destination):
        if 0 <= source < self.vertices and 0 <= destination < self.vertices:
            self.adjMatrix[source][destination] = 0
            self.adjMatrix[destination][source] = 0
        else:
            raise ValueError("Invalid vertex!")

    def display(self):
        for row in self.adjMatrix:
            print(" ".join(map(str, row)))