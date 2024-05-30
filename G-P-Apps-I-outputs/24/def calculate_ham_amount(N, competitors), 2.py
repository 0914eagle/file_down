
def calculate_ham_amount(N, competitors):
    total_meat = sum(competitor[0] for competitor in competitors)
    target_rank = sorted(range(N), key=lambda i: competitors[i][0], reverse=True)
    
    remaining_ham = total_meat
    ham_distribution = [0] * N
    for i in target_rank:
        ham_distribution[i] = remaining_ham / competitors[i][1]
        remaining_ham -= ham_distribution[i] * competitors[i][1]
    
    if not all(0 <= ham <= 1e7 for ham in ham_distribution):
        return -1
    return sum(ham_distribution)

# Input parsing
N = int(input())
competitors = [tuple(map(int, input().split())) for _ in range(N)]

# Output
print("{:.12f}".format(calculate_ham_amount(N, competitors)))
```
