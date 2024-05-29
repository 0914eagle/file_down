
def largest_committee_size(N, K, politicians):
    adj_list = [[] for _ in range(N)]
    for i, dislikes in enumerate(politicians):
        for j in dislikes[1:]:
            adj_list[i].append(j)

    def can_form_committee(size):
        for i in range(N):
            if len(adj_list[i]) < size:
                return False
            count = 0
            for j in adj_list[i]:
                if len(adj_list[j]) >= size:
                    count += 1
            if count < size:
                return False
        return True

    left, right = 0, K
    while left + 1 < right:
        mid = left + (right - left) // 2
        if can_form_committee(mid):
            left = mid
        else:
            right = mid

    return left

# Input parsing
N, K = map(int, input().split())
politicians = []
for _ in range(N):
    data = list(map(int, input().split()))
    politicians.append(data)

# Output
print(largest_committee_size(N, K, politicians))
```
