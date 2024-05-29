
def solve_grid(A, B):
    # Calculate the dimensions of the grid
    h = A + 1  # Number of rows
    w = B + 1  # Number of columns

    # Create the grid with white squares (.) and black squares (#)
    grid = [['#' if (r < A and c < B) else '.' for c in range(w)] for r in range(h)]

    # Print the grid in the specified format
    print(f"{h} {w}")
    for row in grid:
        print(''.join(row))

# Read input
A, B = map(int, input().split())

# Call the function with the given inputs
solve_grid(A, B)
``` 
