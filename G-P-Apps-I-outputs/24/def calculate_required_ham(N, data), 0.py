
def calculate_required_ham(N, data):
    total_meat = sum(meat for meat, _ in data)
    total_ham = 0
    for _, ratio in sorted(data, key=lambda x: x[1], reverse=True):
        total_ham += total_meat * ratio / (N - ratio)
    return total_ham

# Input
N = int(input())
data = [tuple(map(int, input().split())) for _ in range(N)]

# Calculate and output result
result = calculate_required_ham(N, data)
if result != result:  # Check for NaN
    print(-1)
else:
    print("{:.12f}".format(result))

# Example Usage:
# Sample Input 1:
# 3
# 7 1
# 3 2
# 10 0
# Sample Output 1:
# 10.5

# Sample Input 2:
# 3
# 2 1
# 4 0
# 0 3
# Sample Output 2:
# -1
```
