
def min_vertical_moves(n, m, shopping_malls):
    # Create a dictionary to store the locations of each item being sold
    item_locations = {i: [] for i in range(1, m+1)}
    
    for x, y, t in shopping_malls:
        item_locations[t].append((x, y))

    # Sort the item locations based on the x-coordinate
    for item, locations in item_locations.items():
        item_locations[item] = sorted(locations, key=lambda loc: loc[0])

    # Initialize the vertical moves counter
    vertical_moves = 0

    for locations in item_locations.values():
        # Check if the locations are all in the same direction (up or down) from the origin
        is_up = all(y >= 0 for x, y in locations)
        is_down = all(y <= 0 for x, y in locations)

        if not is_up and not is_down:
            vertical_moves += 1

    return vertical_moves

# Sample Input
n = 3
m = 2
shopping_malls = [(1, 1, 2), (1, 2, 1), (-1, 1, 2)]

# Output the minimum number of vertical moves
print(min_vertical_moves(n, m, shopping_malls))
```
