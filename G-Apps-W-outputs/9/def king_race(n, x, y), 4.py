
def king_race(n, x, y):
    # Calculate the manhattan distance from white king to coin
    white_dist = abs(x - 1) + abs(y - 1)
    
    # Calculate the manhattan distance from black king to coin
    black_dist = abs(x - n) + abs(y - n)
    
    # Check which king will reach the coin first
    if white_dist <= black_dist:
        return "White"
    else:
        return "Black"

# Input
n = int(input())
x, y = map(int, input().split())

# Output
print(king_race(n, x, y))
