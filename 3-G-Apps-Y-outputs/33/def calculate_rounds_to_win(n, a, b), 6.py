
def calculate_rounds_to_win(n, a, b):
    min_wins = max(0, a[0] - b[2]) + max(0, a[1] - b[0]) + max(0, a[2] - b[1])
    max_wins = min(a[0], b[1]) + min(a[1], b[2]) + min(a[2], b[0])
    return min_wins, max_wins

# Read input
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Calculate and print the results
min_wins, max_wins = calculate_rounds_to_win(n, a, b)
print(min_wins, max_wins)
