
def calculate_ham(N, competitors):
    total_meat = sum(meat for meat, _ in competitors)
    total_ham = 0
    for i in range(N):
        total_ham += total_meat * competitors[i][1] / competitors[i][0]
    
    for i in range(N-1):
        if competitors[i][0] * total_ham < competitors[i+1][0] * total_meat:
            return -1
    
    return total_ham

# Input
N = int(input())
competitors = []
for _ in range(N):
    meat, ratio = map(int, input().split())
    competitors.append((meat, ratio))

# Output
result = calculate_ham(N, competitors)
print(result)
```
