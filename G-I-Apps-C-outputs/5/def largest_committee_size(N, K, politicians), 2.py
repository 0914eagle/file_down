
def largest_committee_size(N, K, politicians):
    disagreements = [[] for _ in range(N)]
    for i, disagreement_list in enumerate(politicians):
        for j in disagreement_list[1:]:
            disagreements[i].append(j)

    def can_form_committee(committee):
        for p in committee:
            count_disagreements = sum(1 for other in committee if other in disagreements[p])
            if count_disagreements >= K:
                return False
        return True

    largest_committee = 0
    for size in range(1, N + 1):
        for committee in combinations(range(N), size):
            if can_form_committee(committee):
                largest_committee = size

    return largest_committee

# Read input
N, K = map(int, input().split())
politicians = []
for _ in range(N):
    politician_data = list(map(int, input().split()))
    politicians.append(politician_data)

# Get the largest committee size
largest_size = largest_committee_size(N, K, politicians)
print(largest_size)
```
