
def calculate_rounds_to_win(n, a, b):
    min_win = max(0, a[0] - b[1]) + max(0, a[1] - b[2]) + max(0, a[2] - b[0])
    max_win = min(a[0], b[2]) + min(a[1], b[0]) + min(a[2], b[1])
    return min_win, max_win

# Input
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Calculate and output
min_win, max_win = calculate_rounds_to_win(n, a, b)
print(min_win, max_win)
