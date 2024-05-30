
def find_ham_amount(N, competitors):
    total_meat = sum(meat for meat, _ in competitors)
    total_ham = 0
    for _, ratio in competitors:
        total_ham += total_meat / ratio
    
    for i, (_, ratio) in enumerate(competitors):
        if total_meat / ratio <= competitors[i-1][0]:
            return -1
    
    return total_ham

# Input parsing
N = int(input())
competitors = []
for _ in range(N):
    meat, ratio = map(int, input().split())
    competitors.append((meat, ratio))

# Call the function and output the result
result = find_ham_amount(N, competitors)
print(result)
```
