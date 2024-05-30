
def max_total_score(n, m, answers, points):
    max_score = 0
    for i in range(m):
        answer_count = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0}
        for j in range(n):
            answer_count[answers[j][i]] += 1
        max_count = max(answer_count.values())
        max_score += max_count * points[i]
    return max_score

# Input parsing
n, m = map(int, input().split())
answers = [input() for _ in range(n)]
points = list(map(int, input().split()))

# Calculate and output the maximum total score
print(max_total_score(n, m, answers, points))
```
