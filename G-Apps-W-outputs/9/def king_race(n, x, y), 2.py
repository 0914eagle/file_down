
def king_race(n, x, y):
    # Calculate the Manhattan distance from each king to the coin
    white_distance = abs(x - 1) + abs(y - 1)
    black_distance = abs(x - n) + abs(y - n)
    
    # Determine which king will reach the coin first based on the distances
    if white_distance <= black_distance:
        return "White"
    else:
        return "Black"

# Input reading
n = int(input())
x, y = map(int, input().split())

# Call the function and print the output
print(king_race(n, x, y))
