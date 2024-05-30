
def max_total_score(n, m, student_answers, points):
    max_score = 0
    for q in range(m):
        answer_count = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0}
        for ans in student_answers:
            answer_count[ans[q]] += 1
        max_score += max(answer_count.values()) * points[q]
    return max_score

# Input reading
n, m = map(int, input().split())
student_answers = [input() for _ in range(n)]
points = list(map(int, input().split()))

# Calculate and print maximum total score
print(max_total_score(n, m, student_answers, points))
```
