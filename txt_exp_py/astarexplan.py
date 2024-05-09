from collections import deque
#This line imports the deque class from the collections module. A deque is a double-ended queue that supports adding and removing elements from both ends efficiently.


class Graph:
    def __init__(self, adjacency_list):
        self.adjacency_list = adjacency_list
#This defines a class called Graph to represent the graph structure. The constructor initializes the graph with an adjacency list.


    def get_neighbors(self, v):
        return self.adjacency_list[v]
#This method returns the neighbors of a given node v by accessing the adjacency list dictionary.

    def h(self, n):
        H = {'A': 1, 'B': 1, 'C': 1, 'D': 1}
        return H[n]
#This method defines a heuristic function h(n) which returns the heuristic value for a given node n. In this case, it's a simple heuristic function that returns a constant value for each node.

    def a_star_algorithm(self, start_node, stop_node):
        open_list = {start_node}
        closed_list = set()
        g = {start_node: 0}
        parents = {start_node: start_node}

        while open_list:
            n = min(open_list, key=lambda v: g[v] + self.h(v), default=None)

            if n is None:
                print('Path does not exist!')
                return None

            if n == stop_node:
                reconst_path = deque()
                while parents[n] != n:
                    reconst_path.appendleft(n)
                    n = parents[n]
                reconst_path.appendleft(start_node)
                print('Path found: {}'.format(list(reconst_path)))
                return list(reconst_path)

            for m, weight in self.get_neighbors(n):
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight
                elif g[m] > g[n] + weight:
                    g[m] = g[n] + weight
                    parents[m] = n
                    if m in closed_list:
                        closed_list.remove(m)
                        open_list.add(m)





            open_list.remove(n)
            closed_list.add(n)

        print('Path does not exist!')
        return None

adjacency_list = {
    'A': [('B', 1), ('C', 3), ('D', 7)],
    'B': [('D', 5)],
    'C': [('D', 12)]
}
graph1 = Graph(adjacency_list)
graph1.a_star_algorithm('A', 'D')

#The A* algorithm finds the shortest path by iteratively exploring nodes with the lowest combined cost of the path from the start node and the heuristic value to the goal node, until the goal node is reached or no more nodes are left to explore. The algorithm terminates either when the goal node is reached, in which case it prints and returns the shortest path, or when there is no path from the start node to the goal node, in which case it prints a message indicating that the path does not exist.

'''min(open_list, key=lambda v: g[v] + self.h(v), default=None): This part finds the node n with the minimum total cost (g[v] + self.h(v)) from the start node to the current node v. Here:
g[v] represents the cost of the shortest path found so far from the start node to node v.
self.h(v) represents the heuristic value of node v.
The lambda function lambda v: g[v] + self.h(v) calculates the total cost of reaching node v from the start node.
The min() function finds the minimum value of this total cost among all nodes in the open_list.
If there are multiple nodes with the same minimum total cost, min() selects the node with the lowest lexicographic order (i.e., the node with the lowest name).
n = ...: This assigns the selected node n to the variable n for further processing.
In summary, this line of code selects the node with the minimum total cost (g[v] + self.h(v)) from the open_list for expansion in the A* algorithm. This node is chosen because it is expected to lead to the most promising path towards the goal node.'''

'''if n == stop_node:: This condition checks if the current node n is the same as the stop node stop_node. If they are equal, it means that the A* algorithm has found a path from the start node to the stop node.
reconst_path = deque(): This line creates a deque (double-ended queue) called reconst_path, which will store the reconstructed path from the start node to the stop node. Deque is used here because it supports efficient appending and popping operations from both ends.
while parents[n] != n:: This while loop iterates until the parent of the current node n is equal to n. This loop effectively traverses back through the parents of each node, starting from the stop node and ending at the start node.
reconst_path.appendleft(n): Inside the while loop, each node n is added to the left end of the deque reconst_path. This effectively reverses the order of nodes, ensuring that the start node is at the beginning of the reconstructed path.
n = parents[n]: This line updates the current node n to its parent node, moving backward along the path towards the start node.
reconst_path.appendleft(start_node): After the while loop finishes, the start node start_node is added to the left end of the deque reconst_path. This ensures that the start node is included in the reconstructed path.
print('Path found: {}'.format(list(reconst_path))): This line prints the reconstructed path as a list using the format() method to insert the path into the string.
return list(reconst_path): Finally, the reconstructed path is returned as a list.
In summary, this block of code constructs the path from the start node to the stop node by tracing back through the parent pointers stored in the parents dictionary. It then prints and returns the reconstructed path.'''

'''for m, weight in self.get_neighbors(n):: This loop iterates over each neighbor m of the current node n, along with the weight of the edge connecting n and m. It obtains this information from the get_neighbors method of the graph, which returns a list of neighbors and their associated weights.
if m not in open_list and m not in closed_list:: This condition checks if the neighbor m is neither in the open_list nor in the closed_list. If this is the case, it means that m has not been encountered before in the A* algorithm traversal, and it is a candidate for expansion.
open_list.add(m): If m is not in the open_list, it is added to the open_list, indicating that it will be considered for expansion in the future.
parents[m] = n: The parent of m is set to n, indicating that the shortest path to m is through n.
g[m] = g[n] + weight: The cost g associated with reaching m from the start node is updated. The new cost is the sum of the cost of reaching n and the weight of the edge from n to m.
elif g[m] > g[n] + weight:: If m is already in the open_list or closed_list and the new cost of reaching m through n is less than the previously recorded cost, then the cost and parent of m are updated.
if m in closed_list:: If m is in the closed_list, indicating that it has been encountered before, it is removed from the closed_list and added back to the open_list. This is done to revisit m and consider its updated cost and parent node.
In summary, this block of code expands the current node n by considering its neighbors, updating their costs and parent nodes if necessary, and adding them to the open_list for further exploration. It ensures that the A* algorithm progresses towards finding the shortest path from the start node to the stop node.'''









