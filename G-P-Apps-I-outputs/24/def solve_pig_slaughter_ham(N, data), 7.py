
import sys

def solve_pig_slaughter_ham(N, data):
    total_meat_eaten = sum([A for A, _ in data])
    sorted_data = sorted(data, key=lambda x: x[0], reverse=True)
    
    min_ham = 0
    max_ham = 10**7
    
    for _ in range(1000):
        mid_ham = (min_ham + max_ham) / 2
        ham_ratio_sum = 0
        
        for i in range(N):
            ham_ratio_sum += mid_ham * sorted_data[i][1]
            if ham_ratio_sum > total_meat_eaten:
                break
        
        if ham_ratio_sum <= total_meat_eaten:
            return mid_ham
        elif ham_ratio_sum > total_meat_eaten:
            max_ham = mid_ham
        else:
            min_ham = mid_ham
    
    return -1

# Read input
N = int(input())
data = []
for _ in range(N):
    A, B = map(int, input().split())
    data.append((A, B))

# Solve and output
result = solve_pig_slaughter_ham(N, data)
print(result)
```
