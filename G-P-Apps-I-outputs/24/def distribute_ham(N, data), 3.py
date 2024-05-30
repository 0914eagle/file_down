
def distribute_ham(N, data):
    total_meat = sum(meat for meat, _ in data)
    total_ham = 0
    for _, ratio in data:
        total_ham += ratio / sum(ratio for _, ratio in data) * (total_meat + total_ham)
    return total_ham if abs(total_ham - round(total_ham, 12)) < 1e-12 else -1

# Reading input
N = int(input())
data = []
for _ in range(N):
    meat, ratio = map(int, input().split())
    data.append((meat, ratio))

# Calculate and print output
result = distribute_ham(N, data)
print(result)
```
