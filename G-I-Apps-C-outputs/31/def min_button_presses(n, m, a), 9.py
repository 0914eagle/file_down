
def min_button_presses(n, m, a):
    total_presses = 0

    for i in range(n - 1):
        diff = abs(a[i] - a[i + 1])
        total_presses += min(diff, m - diff)

    return total_presses

# Read input
n, m = map(int, input().split())
a = list(map(int, input().split()))

# Find the minimum number of times to press the buttons
result = min_button_presses(n, m, a)
print(result)
