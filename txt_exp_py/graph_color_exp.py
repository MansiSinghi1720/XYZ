def is_graph_colorable(graph, node, visited, color, c):
    visited[node] = 1
    color[node] = c
    for child in graph[node]:
        if not visited[child]:
            if not is_graph_colorable(graph, child, visited, color, c ^ 1):
                return False
        elif color[node] == color[child]:
            return False
    return True

# canot be colored 
#edges = [[1, 2], [2, 4], [4, 3], [3, 1], [2, 5], [4, 5]]
#n = 5

# can be colored 
edges = [[1, 2], [2, 3], [3, 6], [6, 5], [5, 4], [1, 4]]
n = 6

graph = {}
visited = {}
color = {}

for u, v in edges:
    graph.setdefault(u, []).append(v)
    graph.setdefault(v, []).append(u)
    visited[u] = 0
    visited[v] = 0
    color[u] = None
    color[v] = None

temp = is_graph_colorable(graph, 1, visited, color, 0)
if temp:
    print("The graph is colorable.")
else:
    print("The graph is not colorable.")

'''This code defines a function `is_graph_colorable` to determine if a graph is colorable using two colors (binary coloring). Here's how it works:

1. **`is_graph_colorable` Function:**
   - This function takes the graph, starting node, visited nodes, color assignment, and a color (0 or 1) as parameters.
   - It starts by marking the current node as visited and assigns the given color to it.
   - Then, it iterates over each neighbor of the current node. If a neighbor is not visited, it recursively calls itself with the neighbor as the new current node and toggles the color (`c ^ 1`).
   - If a neighbor is already visited and has the same color as the current node, it returns `False`, indicating that the graph cannot be colored with two colors.
   - If all neighbors are visited and there are no conflicts in color assignment, it returns `True`, indicating that the graph can be colored with two colors.
   
2. **Graph Representation:**
   - The graph is represented using an adjacency list (`graph`) where each key represents a node, and the corresponding value is a list of its neighbors.
   - The `visited` dictionary is used to keep track of visited nodes, initialized with all nodes set to `0`.
   - The `color` dictionary is used to store the color assigned to each node, initialized with `None`.

3. **Input Graph:**
   - The input graph is specified using a list of edges (`edges`), where each edge is represented by a tuple `(u, v)` indicating a connection between nodes `u` and `v`.
   - The variable `n` represents the total number of nodes in the graph.

4. **Function Invocation:**
   - The function `is_graph_colorable` is invoked with the graph, starting node (`1`), visited nodes, color assignment, and initial color (`0`).
   - It checks if the graph is colorable using two colors and prints the result accordingly.

This code efficiently determines if a graph can be colored with two colors (binary coloring) using a depth-first search approach. If the graph can be colored, it prints "The graph is colorable"; otherwise, it prints "The graph is not colorable."
