
def get_max_points(N, E, S_X, S_Y, C, cans):
    # Initialize a grid to keep track of oil cans
    grid = [['.' for _ in range(N)] for _ in range(N)]
    points = 0
    
    # Set the starting position of Johnny5
    x, y = S_X, S_Y
    
    # Update grid with oil can locations
    for can in cans:
        X, Y, CT = can
        grid[X][Y] = (CT, False)  # (time, collected)
    
    # Helper function to get adjacent cells
    def get_adjacent_cells(x, y):
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        adjacent = []
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N:
                adjacent.append((nx, ny))
        return adjacent
    
    # Helper function to check for collected cans in adjacent cells
    def check_collected(x, y):
        adjacent_cells = get_adjacent_cells(x, y)
        for nx, ny in adjacent_cells:
            if grid[nx][ny][1]:
                grid[nx][ny] = ('.', False)
                E += 1
    
    for t in range(1, 101):  # Run loop for maximum of 100 seconds
        # Check if there is an oil can at current location
        if grid[x][y][0] == t:
            if not grid[x][y][1]:  # Check if the can is not collected
                points += 1
                grid[x][y] = ('.', True)
                E -= 1
                # Check for collected cans in adjacent cells and gain energy
                check_collected(x, y)
        
        # Check if there are adjacent cans to pick up spilled oil
        check_collected(x, y)
        
        # If out of energy, stop moving
        if E <= 0:
            break
        
        if t < 100:  # Move only if less than 100 seconds have passed
            # Get the direction with the most cans nearby
            max_cans = 0
            best_move = None
            for nx, ny in get_adjacent_cells(x, y):
                if grid[nx][ny][0] > t:
                    count = sum(1 for ax, ay in get_adjacent_cells(nx, ny) if grid[ax][ay][0] > t)
                    if count > max_cans:
                        max_cans = count
                        best_move = (nx, ny)
            
            if best_move:
                x, y = best_move
    
    return points

# Read input
N, E, S_X, S_Y, C = map(int, input().split())
cans = [tuple(map(int, input().split())) for _ in range(C)]

# Call the function and print the output
print(get_max_points(N, E, S_X, S_Y, C, cans))
