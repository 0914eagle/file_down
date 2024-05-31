
def chess_race(n, x, y):
    # Check if the coin is in the starting cell of the black king
    if (x, y) == (n, n):
        return "Black"
    
    # Check if the distance from the white king to the coin is less than or equal to the distance from the black king to the coin
    if x + y <= min(n + 1, x + n - y, n - x + y):
        return "White"
    else:
        return "Black"

# Read input
n = int(input())
x, y = map(int, input().split())

# Output the result
print(chess_race(n, x, y))
