
def calculate_ham_distribution(N, competitors):
    total_meat_eaten = sum(meat for meat, _ in competitors)
    remaining_people = N
    remaining_ham = 0
    for i in range(N):
        meat, ratio = competitors[i]
        remaining_ham += (total_meat_eaten / meat) * ratio
        remaining_people -= 1
        total_meat_eaten -= meat
    
    if remaining_people == 0:
        return round(remaining_ham, 12)
    else:
        return -1

# Input processing
N = int(input())
competitors = []
for _ in range(N):
    A, B = map(int, input().split())
    competitors.append((A, B))

# Output
print(calculate_ham_distribution(N, competitors))
```
