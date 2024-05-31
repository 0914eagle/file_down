
def king_race(n, x, y):
    # Calculate Manhattan distance from white king to coin
    white_distance = abs(1-x) + abs(1-y)
    
    # Calculate Manhattan distance from black king to coin
    black_distance = abs(n-x) + abs(n-y)
    
    # Determine the winner based on the distances
    if white_distance <= black_distance:
        return "White"
    else:
        return "Black"

# Read input
n = int(input())
x, y = map(int, input().split())

# Call the function and print the result
result = king_race(n, x, y)
print(result)
