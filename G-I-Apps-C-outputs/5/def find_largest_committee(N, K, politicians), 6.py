
def find_largest_committee(N, K, politicians):
    def can_form_committee(committee_size):
        for i in range(N):
            if len(politicians[i].intersection(committee)) < K:
                return False
        return True

    max_committee_size = 0
    for i in range(1, N+1):
        committee = set(range(i))
        if can_form_committee(committee):
            max_committee_size = max(max_committee_size, i)
    
    return max_committee_size

# Input
N, K = map(int, input().split())
politicians = []
for _ in range(N):
    politician = set(map(int, input().split()[1:]))
    politicians.append(politician)

# Output
print(find_largest_committee(N, K, politicians))
```
