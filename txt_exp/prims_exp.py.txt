from heapq import heappop, heappush, heapify

def prim(graph):
    start_vertex = list(graph.keys())[0]
    mst = []
    visited = set([start_vertex])
    edges = [(weight, start_vertex, neighbor) for neighbor, weight in graph[start_vertex]]
    heapify(edges)

    while edges:
        weight, u, v = heappop(edges)
        if v not in visited:
            visited.add(v)
            mst.append((u, v, weight))

            for neighbor, weight in graph[v]:
                if neighbor not in visited:
                    heappush(edges, (weight, v, neighbor))

    return mst

graph = {
    'A': [('B', 5), ('C', 1)],
    'B': [('A', 5), ('C', 2), ('D', 1)],
    'C': [('A', 1), ('B', 2), ('D', 4)],
    'D': [('B', 1), ('C', 4)]
}

minimum_spanning_tree = prim(graph)
for edge in minimum_spanning_tree:
    u, v, weight = edge
    print(f'{u} -- {v}: {weight}')


'''A heap is a specialized tree-based data structure that satisfies the heap property. In a min-heap, for every node `i` other than the root, the value of the parent node is less than or equal to the value of node `i`. Similarly, in a max-heap, for every node `i` other than the root, the value of the parent node is greater than or equal to the value of node `i`.

Heapify is an operation that transforms a given array into a heap. It essentially arranges the elements of the array in such a way that the heap property is satisfied. This operation is crucial for maintaining the efficiency of heap-based algorithms, such as priority queues and heap sort.

In Python, the `heapq` module provides functions for heap operations. Here's how heapify is used:

1. **Heapify Operation**:
   - The `heapify` function in Python rearranges the elements of a list to satisfy the heap property.
   - It operates in-place, meaning it modifies the original list rather than returning a new one.
   - The time complexity of the `heapify` operation is O(n), where n is the number of elements in the list.

In the context of algorithms like Prim's algorithm for finding the Minimum Spanning Tree (MST) or Dijkstra's algorithm for finding shortest paths, heapify can be used to efficiently maintain a priority queue of vertices or edges. This priority queue ensures that the algorithm always selects the next vertex or edge with the minimum weight, leading to optimal solutions.'''
'''If the destination vertex v of the popped edge has not been visited yet, it means that the edge leads to a new vertex in the MST. In this case, the algorithm marks v as visited, adds the edge (u, v, weight) to the MST (mst), and proceeds to explore its neighbors.

The algorithm iterates over the neighbors of vertex v in the original graph (graph). For each neighbor that has not been visited yet, the algorithm adds the corresponding edge to the priority queue (edges) using the heappush function. This ensures that the algorithm continues to explore vertices connected to the MST and adds the minimum-weight edges to the priority queue for consideration in subsequent iterations.

Overall, this part of the code efficiently constructs the MST by iteratively adding the minimum-weight edges to the MST and exploring new vertices connected to the MST. The use of a priority queue ensures that the algorithm always selects the next edge with the minimum weight, leading to the construction of a minimum spanning tree.



'''