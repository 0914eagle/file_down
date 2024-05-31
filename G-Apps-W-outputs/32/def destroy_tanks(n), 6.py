
def destroy_tanks(n):
    positions = [1, n]  # Start with the first and last cells
    for i in range(2, n):
        if i % 2 == 0:
            positions.insert(1, i)  # Insert even positions at index 1
        else:
            positions.append(i)  # Append odd positions

    bombs = len(positions)
    
    print(bombs)
    print(" ".join(map(str, positions)))

# Example usage
n = 3
destroy_tanks(n)
