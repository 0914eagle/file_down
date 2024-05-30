
def max_total_score(n, m, answers, points):
    max_score = 0
    for i in range(m):
        count = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0}
        for j in range(n):
            count[answers[j][i]] += 1
        max_score += max(count.values()) * points[i]
    return max_score

# Input
n, m = map(int, input().split())
answers = [input() for _ in range(n)]
points = list(map(int, input().split()))

# Output
print(max_total_score(n, m, answers, points))
```
