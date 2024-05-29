
def clean_ice_rink(r, c, i, j, n):
    ice = [['.' for _ in range(c)] for _ in range(r)]  # Initialize ice rink with white cells
    
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
    current_direction = 3  # Initially facing up
    colors = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'  # Colors A-Z
    
    step_size = 1
    color_index = 0
    
    for step in range(n):
        for _ in range(step_size):
            # Update ice color
            ice[i-1][j-1] = colors[color_index]
            
            # Move the zamboni
            i += directions[current_direction][0]
            j += directions[current_direction][1]
            
            # Wrap around if out of bounds
            i = i % r
            j = j % c
            
        # Rotate direction 90 degrees clockwise
        current_direction = (current_direction + 1) % 4
        
        # Switch to the next color
        color_index = (color_index + 1) % 26
        
        step_size += 1
    
    ice[i-1][j-1] = '@'  # Mark final location of the zamboni
    
    return '\n'.join([''.join(row) for row in ice])

# Sample input test case
print(clean_ice_rink(5, 5, 3, 3, 4))
```

