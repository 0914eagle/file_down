
def max_total_score(n, m, answers, points):
    total_score = 0

    for i in range(m):
        answer_counts = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0}
        for j in range(n):
            answer_counts[answers[j][i]] += 1

        max_count = max(answer_counts.values())
        total_score += max_count * points[i]

    return total_score

# Input
n, m = map(int, input().split())
answers = [input() for _ in range(n)]
points = list(map(int, input().split()))

# Output
print(max_total_score(n, m, answers, points))
```
