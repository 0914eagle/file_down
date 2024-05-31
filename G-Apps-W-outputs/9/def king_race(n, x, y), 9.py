
def king_race(n, x, y):
    total_moves = x + y - 2  # Total moves to reach cell (x, y) diagonally
    white_moves = (1 + 1) - 2  # Initial move of white king
    black_moves = (n + n) - total_moves  # Initial move of black king

    if white_moves <= black_moves:
        if total_moves % 2 == 0:
            return "White"
        else:
            return "Black"
    else:
        if total_moves % 2 == 0:
            return "Black"
        else:
            return "White"

# Input
n = int(input())
x, y = map(int, input().split())

# Output
print(king_race(n, x, y))
