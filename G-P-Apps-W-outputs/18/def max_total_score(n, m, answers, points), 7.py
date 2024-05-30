
def max_total_score(n, m, answers, points):
    max_score = 0
    for question in range(m):
        answer_counts = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0}
        for student in answers:
            answer_counts[student[question]] += 1
        max_score += max(answer_counts.values()) * points[question]
    return max_score

# Read input
n, m = map(int, input().split())
answers = [input() for _ in range(n)]
points = list(map(int, input().split()))

# Calculate and print the maximum total score
print(max_total_score(n, m, answers, points))
```
