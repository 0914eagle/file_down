
def king_race(n, x, y):
    # Calculate the minimum number of moves required for white king to reach (x, y)
    white_moves = max(x, y) - 1
    
    # Calculate the minimum number of moves required for black king to reach (x, y)
    black_moves = max(n - x, n - y)
    
    # Determine the winner based on the total moves required
    if white_moves <= black_moves:
        return "White"
    else:
        return "Black"

# Read input values
n = int(input())
x, y = map(int, input().split())

# Call the function and print the result
print(king_race(n, x, y))
