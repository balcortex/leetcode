# Python Program to detect cycle in an undirected graph
from collections import defaultdict

# This class represents a undirected
# graph using adjacency list representation


class Graph:

    def __init__(self, vertices):

        # No. of vertices
        self.V = vertices  # No. of vertices

        # Default dictionary to store graph
        self.graph = defaultdict(list)

    # Function to add an edge to graph
    def addEdge(self, v, w):

        # Add w to v_s list
        self.graph[v].append(w)

        # Add v to w_s list
        self.graph[w].append(v)

    def isCyclic(self):

        def visit(node, parent):
            visited.add(node)

            for neigh in self.graph[node]:
                if neigh != parent:
                    if neigh in visited:
                        return True
                    visit(neigh, node)

            return False

        visited = set()

        for i in range(self.V):
            return visit(i, -1)

        return False


# Create a graph given in the above diagram
g = Graph(3)
g.addEdge(0, 1)
g.addEdge(1, 2)
g.addEdge(2, 3)

print(g.isCyclic())


# Create a graph given in the above diagram
g = Graph(4)
g.addEdge(0, 1)
g.addEdge(1, 2)
g.addEdge(2, 3)
g.addEdge(3, 0)

print(g.isCyclic())

# if g.isCyclic():
# 	print("Graph contains cycle")
# else:
# 	print("Graph doesn't contain cycle ")
# g1 = Graph(3)
# g1.addEdge(0, 1)
# g1.addEdge(1, 2)


# if g1.isCyclic():
# 	print("Graph contains cycle")
# else:
# 	print("Graph doesn't contain cycle ")
