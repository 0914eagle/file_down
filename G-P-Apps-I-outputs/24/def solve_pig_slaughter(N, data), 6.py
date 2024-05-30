
def solve_pig_slaughter(N, data):
    total_meat = sum([a for a, _ in data])
    remaining_ham = 0
    order = sorted(range(N), key=lambda x: data[x][0], reverse=True)
    
    for i in range(N):
        person_index = order[i]
        ham_ratio = data[person_index][1] / total_meat
        if ham_ratio * (i+1) > remaining_ham:
            remaining_ham = ham_ratio * (i+1)
    
    if remaining_ham <= total_meat:
        return total_meat
    else:
        return remaining_ham

# Input processing
N = int(input())
data = []
for _ in range(N):
    a, b = map(int, input().split())
    data.append((a, b))

output = solve_pig_slaughter(N, data)
if output == total_meat:
    print(output)
else:
    print(-1)
```
