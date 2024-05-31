
def king_race(n, x, y):
    # Calculate the Manhattan distance between the coin and the starting cells of white and black kings
    white_distance = abs(1 - x) + abs(1 - y)
    black_distance = abs(n - x) + abs(n - y)
    
    # Determine the winner based on the distance
    if white_distance <= black_distance:
        return "White"
    else:
        return "Black"

# Read input
n = int(input())
x, y = map(int, input().split())

# Call the king_race function and print the result
print(king_race(n, x, y))
