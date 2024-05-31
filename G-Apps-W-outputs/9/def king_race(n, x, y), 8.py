
def king_race(n, x, y):
    # Calculate the Manhattan distance between starting positions and the coin
    white_distance = abs(x - 1) + abs(y - 1)
    black_distance = abs(x - n) + abs(y - n)
    
    # Check which king will reach the coin first based on the distances
    if white_distance <= black_distance:
        return "White"
    else:
        return "Black"

# Read input values
n = int(input())
x, y = map(int, input().split())

# Call the function and print the result
print(king_race(n, x, y))
