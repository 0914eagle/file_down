
def generate_grid(A, B):
    total_areas = A + B
    grid = [["." for _ in range(total_areas)] for _ in range(total_areas)]
    
    # Fill A white areas
    for i in range(A):
        grid[i][0] = "#"
    
    # Fill B black areas
    for i in range(A, total_areas):
        grid[i][1] = "#"
    
    # Print the grid
    print(total_areas, total_areas)
    for row in grid:
        print("".join(row))

# Input
A, B = map(int, input().split())

# Generate and print the grid
generate_grid(A, B)
```
