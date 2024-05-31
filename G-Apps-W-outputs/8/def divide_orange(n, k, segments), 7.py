
def divide_orange(n, k, segments):
    result = []
    for i in range(k):
        start = (segments[i] - 1) // n
        row = list(range(start * n + 1, (start + 1) * n + 1))
        result.extend(row)

    return result

# Input parsing
n, k = map(int, input().split())
segments = list(map(int, input().split()))

# Output
result = divide_orange(n, k, segments)
print(*result)
