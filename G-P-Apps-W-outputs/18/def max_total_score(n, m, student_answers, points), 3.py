
def max_total_score(n, m, student_answers, points):
    total_score = 0
    for j in range(m):
        answer_count = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0}
        for i in range(n):
            answer_count[student_answers[i][j]] += 1
        max_count = max(answer_count.values())
        total_score += max_count * points[j]
    return total_score

# Read input
n, m = map(int, input().split())
student_answers = [input() for _ in range(n)]
points = list(map(int, input().split()))

# Calculate and print max total score
print(max_total_score(n, m, student_answers, points))
```
