def kruskal(vertices, edges):
    parent = list(range(vertices))
    rank = [0] * vertices
    result = []
    edges.sort(key=lambda x: x[2])

    def find(i):
        return i if parent[i] == i else find(parent[i])

    def union(x, y):
        root_x, root_y = find(x), find(y)
        if rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        elif rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        else:
            parent[root_x] = root_y
            rank[root_y] += 1

    for u, v, w in edges:
        if len(result) < vertices - 1 and find(u) != find(v):
            result.append([u, v, w])
            union(u, v)

    return result


# Example usage:
num_vertices = 4
graph_edges = [[0, 1, 10], [0, 2, 6], [0, 3, 5], [1, 3, 15], [2, 3, 4]]

mst = kruskal(num_vertices, graph_edges)
print("Edges in the Minimum Spanning Tree:")
for u, v, weight in mst:
    print(f"{u} -- {v} : {weight}")

'''This code implements Kruskal's algorithm for finding the Minimum Spanning Tree (MST) of a graph. Here's a breakdown of the implementation:

1. **Function Definition:**
    - The `kruskal` function takes two arguments: `vertices`, representing the number of vertices in the graph, and `edges`, representing a list of edges in the graph.
    - It returns a list of edges representing the Minimum Spanning Tree (MST).

2. **Initialization:**
    - The `parent` list is initialized to store the parent of each vertex in the disjoint-set data structure. Initially, each vertex is its own parent.
    - The `rank` list is initialized to store the rank (or depth) of each vertex's subtree in the disjoint-set data structure. Initially, all ranks are set to 0.
    - The `result` list is initialized to store the edges of the MST.
    - The `edges` list is sorted in non-decreasing order of weight using the `sort` method and a lambda function as the sorting key.

3. **Disjoint-Set Operations:**
    - The `find` function recursively finds the parent (representative) of a vertex in the disjoint-set data structure using path compression.
    - The `union` function performs a union operation between two sets represented by their root vertices. It merges two sets based on their ranks to optimize the union operation and maintain balance in the disjoint-set data structure.

4. **Main Loop:**
    - The algorithm iterates over the sorted edges in the `edges` list.
    - For each edge `(u, v, w)`, if adding the edge `(u, v)` to the MST does not create a cycle and the MST has not yet included all vertices, the edge is added to the MST (`result`), and the sets containing vertices `u` and `v` are merged using the `union` operation.

5. **Return:**
    - Once the MST contains `vertices - 1` edges (which is the maximum number of edges in a spanning tree), the algorithm terminates, and the MST represented by the `result` list is returned.

6. **Example Usage:**
    - The code demonstrates the usage of the `kruskal` function with an example graph represented by its edges.
    - The MST edges are printed in the format `u -- v : weight`.

Overall, this implementation efficiently constructs the MST of a graph using Kruskal's algorithm and the disjoint-set data structure, ensuring that the resulting tree spans all vertices with minimum total edge weight.
This `union` function is a critical part of the implementation of Kruskal's algorithm, used to merge two disjoint sets represented by their root vertices `x` and `y`. Let's break down this function:

1. **Find Root Vertices:**
   - `root_x` and `root_y` are assigned the root vertices of the sets containing vertices `x` and `y`, respectively. This is achieved by calling the `find` function, which performs path compression to find the representative (root) of each set.

2. **Merge Sets Based on Rank:**
   - If the rank of the set containing `root_x` is less than the rank of the set containing `root_y` (`rank[root_x] < rank[root_y]`), it implies that the subtree rooted at `root_x` is smaller. In this case, the parent of `root_x` is set to `root_y`, effectively merging the set containing `x` into the set containing `y`.
   - If the rank of the set containing `root_x` is greater than the rank of the set containing `root_y` (`rank[root_x] > rank[root_y]`), a similar merge operation is performed, but this time the parent of `root_y` is set to `root_x`.
   - If the ranks are equal (`rank[root_x] == rank[root_y]`), it means both sets have the same rank. In this case, one set is arbitrarily chosen to be merged into the other, and the rank of the resulting set is incremented by one to maintain balance in the disjoint-set data structure.

3. **Rank Update:**
   - After the merge operation, if the rank of the resulting set was incremented, it indicates that the height of the resulting subtree has increased. Therefore, the rank of the root vertex of the resulting set (`root_y` in the first case and `root_x` in the second case) is incremented to reflect this change.

Overall, the `union` function efficiently merges two sets represented by their root vertices while ensuring that the resulting disjoint-set data structure remains balanced to optimize future union operations and maintain efficient performance of Kruskal's algorithm.'''S