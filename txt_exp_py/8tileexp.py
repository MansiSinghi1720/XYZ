from queue import PriorityQueue

goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def calculate_manhattan_distance(state):
    return sum(abs(i // 3 - (value - 1) // 3) + abs(i % 3 - (value - 1) % 3)
               for i, row in enumerate(state) for value in row if value != 0)

def solve_puzzle(start_state):
    visited = set()
    queue = PriorityQueue()
    queue.put((0, start_state))
    
    while not queue.empty():
        _, current_state = queue.get()
        
        if current_state == goal_state:
            return current_state
        
        visited.add(tuple(map(tuple, current_state)))
        empty_row, empty_col = next((i, j) for i in range(3) for j in range(3) if current_state[i][j] == 0)
        
        for move in moves:
            new_row, new_col = empty_row + move[0], empty_col + move[1]
            
            if 0 <= new_row < 3 and 0 <= new_col < 3:
                new_state = [list(row) for row in current_state]
                new_state[empty_row][empty_col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[empty_row][empty_col]
                
                if tuple(map(tuple, new_state)) not in visited:
                    priority = calculate_manhattan_distance(new_state)
                    queue.put((priority, new_state))
                    visited.add(tuple(map(tuple, new_state)))
    
    return None

start_state = [[1, 2, 3], [4, 0, 6], [7, 5, 8]]
solution = solve_puzzle(start_state)

if solution:
    print("Solution found:")
    for row in solution:
        print(row)
else:
    print("No solution found.")


'''for i, row in enumerate(state): This iterates over each row of the puzzle state state, where i represents the index of the row.
for value in row if value != 0: This iterates over each non-zero value (tile) in the current row row. The condition if value != 0 ensures that only non-zero values (tiles) are considered because the Manhattan distance for the empty tile (0) is always 0.
abs(i // 3 - (value - 1) // 3) + abs(i % 3 - (value - 1) % 3): This calculates the Manhattan distance for each non-zero value (tile) in the puzzle state. Let's break it down further:
(value - 1): Subtracting 1 from value adjusts the tile values to be zero-based (0-indexed), as the puzzle starts with 1.
value - 1) // 3: This calculates the row index of the goal position for the current tile value by integer-dividing the adjusted value by 3.
i // 3: This calculates the row index of the current position of the tile by integer-dividing the row index (i) by 3.
abs(i // 3 - (value - 1) // 3): This calculates the vertical Manhattan distance between the current position and the goal position of the tile.
(value - 1) % 3: This calculates the column index of the goal position for the current tile value by taking the remainder of the adjusted value divided by 3.
i % 3: This calculates the column index of the current position of the tile by taking the remainder of the row index (i) divided by 3.
abs(i % 3 - (value - 1) % 3): This calculates the horizontal Manhattan distance between the current position and the goal position of the tile.
sum(...): This sums up the Manhattan distances calculated for all non-zero values (tiles) in the puzzle state, providing the total Manhattan distance heuristic for the state.
In summary, this function efficiently calculates the Manhattan distance heuristic for the given puzzle state, which is used as a heuristic estimate of the number of moves required to reach the goal state from the current state in the A* algorithm.'''

'''start_state: This parameter represents the initial state of the puzzle provided as a 2D list.
visited = set(): This line initializes an empty set visited to keep track of visited states. This set will store states in a hashed format to quickly check if a state has been visited before.
queue = PriorityQueue(): This line creates an instance of the PriorityQueue class, which is used to store states (along with their heuristic values) in priority order. States with lower heuristic values (indicating closer proximity to the goal state) are given higher priority in the queue.
queue.put((0, start_state)): This line adds the initial state start_state to the priority queue with a priority of 0. The priority queue is initialized with tuples where the first element is the priority (heuristic value) and the second element is the state itself.
In summary, this function initializes the search process for solving the 8-puzzle problem using the A* algorithm. It sets up the priority queue and adds the initial state to it with a priority of 0. The search process will continue from this initial state, exploring possible moves and prioritizing states based on their heuristic values.'''

'''while not queue.empty():: This loop continues as long as the priority queue queue is not empty. It iterates over the states in the priority queue, processing each state one by one.
_, current_state = queue.get(): This line retrieves the state with the lowest priority (heuristic value) from the priority queue. The get() method returns a tuple containing the priority and the state itself. Here, we're using the _ to discard the priority value, as it is not needed for further processing. current_state holds the current state of the puzzle being explored.'''

'''if current_state == goal_state:: This condition checks if the current state current_state is equal to the goal state goal_state. If they are equal, it means that the goal state has been reached, and the function returns the goal state, indicating that the puzzle has been solved.'''
'''visited.add(tuple(map(tuple, current_state))): This line adds the current state to the set of visited states visited. Since visited is a set of tuples, current_state (which is a list of lists) is converted to a tuple of tuples using map(tuple, current_state), and then added to the visited set.empty_row, empty_col = next((i, j) for i in range(3) for j in range(3) if current_state[i][j] == 0)
This line finds the row and column indices of the empty tile (0) in the current state. It uses a generator expression with next() to iterate over all indices (i, j) in the puzzle grid (3x3) and find the indices where the value is equal to 0.
The subsequent code block inside the loop iterates over possible moves (moves) of the empty tile, generates new states by applying these moves, calculates their Manhattan distance heuristics, and adds them to the priority queue if they have not been visited before.

This loop continues until the goal state is found or until all possible states have been explored without finding the goal state.'''







