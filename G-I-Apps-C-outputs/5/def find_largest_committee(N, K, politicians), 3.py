
def find_largest_committee(N, K, politicians):
    def can_form_committee(committee_size):
        for i in range(N):
            count_disagreements = sum(1 for j in range(N) if j != i and politicians[i].intersection(politicians[j]) < K)
            if count_disagreements < committee_size:
                return False
        return True
    
    left, right = 0, N
    while left < right:
        mid = (left + right + 1) // 2
        if can_form_committee(mid):
            left = mid
        else:
            right = mid - 1
    
    return left

# Input processing and sample usage
N, K = map(int, input().split())
politicians = []
for _ in range(N):
    line = list(map(int, input().split()))
    politicians.append(set(line[1:]))
    
result = find_largest_committee(N, K, politicians)
print(result)
```
