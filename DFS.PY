# Define a class to represent a graph
class Graph:
    def __init__(self):
        self.graph = {}

    # Function to add an edge to the graph
    def add_edge(self, vertex, neighbor):
        if vertex in self.graph:
            self.graph[vertex].append(neighbor)
        else:
            self.graph[vertex] = [neighbor]

    # Depth-First Search algorithm
    def dfs(self, start_vertex, visited=set()):
        if start_vertex not in visited:
            print(start_vertex, end=' ')
            visited.add(start_vertex)
            if start_vertex in self.graph:
                for neighbor in self.graph[start_vertex]:
                    self.dfs(neighbor, visited)

# Create a graph
g = Graph()

# Add edges to the graph
g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'D')
g.add_edge('B', 'E')
g.add_edge('C', 'F')

# Perform DFS starting from vertex 'A'
print("Depth-First Search starting from vertex 'A':")
g.dfs('A')