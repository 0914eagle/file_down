
def max_messiness(n, k):
    if n == 1:
        return 0
    else:
        max_mess = n * (n - 1) // 2
        max_swaps = min(k, n // 2)
        return max_mess * max_swaps

# Input
n, k = map(int, input().split())

# Output
print(max_messiness(n, k))
