
def calculate_rounds_won(n, a, b):
    min_wins = max(0, a[0] - b[1]) + max(0, a[1] - b[2]) + max(0, a[2] - b[0])
    max_wins = min(a[0], b[2]) + min(a[1], b[0]) + min(a[2], b[1])
    
    return min_wins, max_wins

# Input
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Calculate and output results
min_wins, max_wins = calculate_rounds_won(n, a, b)
print(min_wins, max_wins)
