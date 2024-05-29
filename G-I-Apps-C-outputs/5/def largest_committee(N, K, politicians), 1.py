
def largest_committee(N, K, politicians):
    def disagree(i, j):
        return j not in politicians[i][1:]

    def find_committee_size(member):
        queue = [member]
        visited = set()
        while queue:
            current = queue.pop()
            visited.add(current)
            for i in range(N):
                if i not in visited and disagree(current, i):
                    queue.append(i)
        return len(visited)

    max_committee_size = 0
    for i in range(N):
        committee_size = find_committee_size(i)
        if committee_size > max_committee_size and committee_size <= K:
            max_committee_size = committee_size

    return max_committee_size

# Reading input
N, K = map(int, input().split())
politicians = []
for _ in range(N):
    data = list(map(int, input().split()))
    politicians.append(data)

result = largest_committee(N, K, politicians)
print(result)
```
