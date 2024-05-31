
def king_race(n, x, y):
    white_distance = abs(x - 1) + abs(y - 1)  # Manhattan distance of white king to coin
    black_distance = abs(x - n) + abs(y - n)  # Manhattan distance of black king to coin

    if white_distance <= black_distance:
        return "White"
    else:
        return "Black"

# Read input
n = int(input())
x, y = map(int, input().split())

# Call the function and print the output
print(king_race(n, x, y))
