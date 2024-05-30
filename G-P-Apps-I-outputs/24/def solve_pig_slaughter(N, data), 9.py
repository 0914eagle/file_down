
def solve_pig_slaughter(N, data):
    total_kilos = sum(data[k][0] for k in range(N))
    sorted_data = sorted(data, key=lambda x: x[0], reverse=True)
    
    required_ham = [0] * N
    for i in range(N):
        required_ham[i] = (sorted_data[i][0] + sum(required_ham[:i])) / sorted_data[i][1]
    
    if any(ham < 0 for ham in required_ham):
        return -1
    return round(sum(required_ham), 12)

# Input parsing
N = int(input())
data = []
for _ in range(N):
    A, B = map(int, input().split())
    data.append((A, B))

# Call the function
output = solve_pig_slaughter(N, data)
print(output)
```
