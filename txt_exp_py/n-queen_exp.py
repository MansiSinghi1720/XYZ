def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col or board[i] - i == col - row or board[i] + i == col + row:
            return False
    return True

def solve_n_queens(n):
    def branch_and_bound(board, row, remaining_rows):
        if row == n:
            result.append(board[:])
            return

        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                conflicts = sum(board[i] == board[row] or board[i] - i == board[row] - row or board[i] + i == board[row] + row for i in range(row))
                if conflicts < remaining_rows:
                    branch_and_bound(board, row + 1, remaining_rows - 1)

    result = []
    board = [-1] * n
    branch_and_bound(board, 0, n)
    return result

n = 4  # Number of queens
solutions = solve_n_queens(n)
for placement in solutions:
    for row in placement:
        for col in range(len(placement)):
            print('Q ' if row == col else '. ', end='')
        print()
    print()


'''This code implements the N-Queens problem using a branch-and-bound algorithm. Here's how it works:

1. **`is_safe(board, row, col)` Function:**
   - This function checks if it's safe to place a queen at the given row and column on the board.
   - It iterates through the rows above the current row and checks if there are any conflicts with existing queens in the same column or diagonals.

2. **`solve_n_queens(n)` Function:**
   - This function implements the branch-and-bound algorithm to find all possible solutions to the N-Queens problem.
   - It initializes an empty list `result` to store the solutions and a list `board` to represent the current state of the board.
   - The `branch_and_bound` function is a recursive helper function that explores all possible placements of queens on the board.
   - It starts with the first row (row 0) and recursively explores all possible placements of queens in subsequent rows while keeping track of the remaining rows (`remaining_rows`) that can still be explored.
   - If a safe placement is found for a queen in a row, the function recursively calls itself with the next row and decrements the `remaining_rows` count.
   - The function terminates when all rows have been explored (i.e., `row == n`), and it appends the current board configuration to the `result` list.

3. **Printing Solutions:**
   - After calling `solve_n_queens(n)`, the code iterates through the list of solutions (`solutions`) and prints each solution.
   - It prints a grid representing the placement of queens on the board, where 'Q' represents a queen and '.' represents an empty cell.

4. **Example Usage:**
   - In this example, `n` is set to 4, indicating a 4x4 chessboard.
   - The code finds and prints all possible placements of 4 queens on the board without threatening each other.

This implementation efficiently solves the N-Queens problem by using the branch-and-bound technique to explore only promising branches of the solution space, significantly reducing the search space compared to brute-force approaches.
This function `is_safe(board, row, col)` checks if it's safe to place a queen at the given position `(row, col)` on the chessboard represented by the `board`. Here's what each part of the function does:

- **Parameters**:
  - `board`: Represents the current state of the chessboard, where each element `board[i]` indicates the column position of the queen in row `i`.
  - `row`: The row where we want to place the queen.
  - `col`: The column where we want to place the queen.

- **Loop**:
  - It iterates over each row `i` from `0` to `row - 1` (exclusive). This loop checks all the rows above the current `row`.

- **Conditions**:
  - **1st Condition**: `board[i] == col`
    - Checks if there is a queen in the same column (`col`) as the current position. If found, it means placing a queen at `(row, col)` would conflict with the queen in row `i`.
  
  - **2nd Condition**: `board[i] - i == col - row`
    - Checks if there is a queen on the same diagonal (from top-left to bottom-right) as the current position `(row, col)`. 
    - The expression `board[i] - i` gives the column position of the queen in row `i` if we extend its diagonal to the current row. Similarly, `col - row` represents the diagonal of the current position.
  
  - **3rd Condition**: `board[i] + i == col + row`
    - Checks if there is a queen on the same diagonal (from bottom-left to top-right) as the current position `(row, col)`.
    - The expression `board[i] + i` gives the column position of the queen in row `i` if we extend its diagonal to the current row. Similarly, `col + row` represents the diagonal of the current position.

- **Return Value**:
  - If any of the conditions are met (indicating a conflict), the function returns `False`, meaning it's not safe to place a queen at `(row, col)`.
  - If none of the conditions are met (indicating no conflicts), the function returns `True`, indicating it's safe to place a queen at `(row, col)`.

This function is a crucial part of solving the N-Queens problem, as it helps in determining valid queen placements on the chessboard without threatening each other.

This function `solve_n_queens(n)` is an implementation of the N-Queens problem using the branch and bound algorithm. Here's what each part of the function does:

- **Parameters**:
  - `n`: Represents the size of the chessboard, i.e., the number of rows and columns, and also the number of queens to be placed.

- **Nested Function `branch_and_bound`**:
  - This is a recursive helper function responsible for solving the N-Queens problem.
  
  - **Parameters**:
    - `board`: Represents the current state of the chessboard, where each element `board[i]` indicates the column position of the queen in row `i`.
    - `row`: Represents the current row being considered for queen placement.
    - `remaining_rows`: Represents the number of rows left to place queens on.

  - **Base Case**:
    - If `row == n`, it means queens have been successfully placed on all rows, so a valid solution has been found. In this case, the current state of the board `board` is added to the `result`.

  - **Queen Placement**:
    - It iterates over each column (`col`) in the current row (`row`) and checks if it's safe to place a queen at `(row, col)` using the `is_safe` function.
    
    - If it's safe to place a queen, the column position `col` is assigned to `board[row]`, and the function is recursively called for the next row (`row + 1`). 
    
    - Before making the recursive call, it calculates the number of conflicts (`conflicts`) with queens already placed on the board. If this number is less than `remaining_rows`, it proceeds with the recursive call; otherwise, it backtracks.

- **Initialization**:
  - `result = []`: Initializes an empty list to store the solutions.
  - `board = [-1] * n`: Initializes the chessboard with `-1` values, indicating no queens have been placed yet.

This function acts as the entry point for solving the N-Queens problem using the branch and bound algorithm. By calling `solve_n_queens(n)`, you can find all valid solutions for placing `n` queens on an `n x n` chessboard without threatening each other.'''