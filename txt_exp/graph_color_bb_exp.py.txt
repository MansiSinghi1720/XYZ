def graph_coloring(graph, m):
    vertices = len(graph)
    color_assignment = [-1] * vertices
    color_assignment[0] = 0

    def is_safe(vertex, color):
        for v in range(vertices):
            if graph[vertex][v] and color_assignment[v] == color:
                return False
        return True

    def bound(vertex):
        max_color = max(color_assignment[:vertex]) + 1
        return max_color

    def backtrack(vertex):
        if vertex == vertices:
            return True

        for color in range(m):
            if is_safe(vertex, color):
                color_assignment[vertex] = color
                if bound(vertex) < m:
                    if backtrack(vertex + 1):
                        return True
                color_assignment[vertex] = -1

        return False

    if backtrack(1):
        return color_assignment
    else:
        return None


# canot be colored 
edges = [[1, 2], [2, 4], [4, 3], [3, 1], [2, 5], [4, 5]]
n = 5

# can be colored 
# edges = [[1, 2], [2, 3], [3, 6], [6, 5], [5, 4], [1, 4]]
# n = 6

graph = [[0] * n for _ in range(n)]
for u, v in edges:
    graph[u-1][v-1] = 1
    graph[v-1][u-1] = 1

m = 3  # Number of colors
color_assignment = graph_coloring(graph, m)

if color_assignment:
    print("Graph coloring possible with at most", m, "colors.")
    print("Color assignment:", color_assignment)
else:
    print("Graph coloring not possible with", m, "colors.")

'''This code block is part of the `graph_coloring` function and contains three key helper functions:

1. **`is_safe(vertex, color)` Function:**
   - This function checks if it is safe to assign a particular color to the given vertex. It iterates over all vertices in the graph, and if there exists an edge between the given vertex and another vertex (`graph[vertex][v] == 1`), it checks if the color of the other vertex (`color_assignment[v]`) is the same as the proposed color. If any adjacent vertex already has the proposed color, it returns `False`, indicating that the assignment is not safe. Otherwise, it returns `True`.

2. **`bound(vertex)` Function:**
   - This function determines the upper bound for the number of colors that can be used at a given vertex. It takes into account the colors already assigned to the preceding vertices up to the current vertex (`vertex`). It finds the maximum color index assigned so far and increments it by 1 to provide a bound on the number of colors available for the current vertex.

3. **`backtrack(vertex)` Function:**
   - This function recursively assigns colors to vertices using backtracking. It starts from the given `vertex` and tries all possible colors (`m`) one by one. For each color, it checks if it is safe to assign that color to the current vertex using the `is_safe` function. If it is safe, it assigns the color to the vertex, updates the color assignment, and recursively moves to the next vertex (`vertex + 1`). If the upper bound (`bound`) for the number of colors at the current vertex is less than the total number of colors (`m`), it explores further. If the backtrack process succeeds in coloring all vertices, it returns `True`, indicating that graph coloring is possible with the given number of colors. Otherwise, it returns `False`.

The `graph_coloring` function utilizes these helper functions to perform graph coloring with backtracking. If the `backtrack` function succeeds, it returns the color assignment; otherwise, it returns `None`, indicating that graph coloring is not possible with the given number of colors.'''