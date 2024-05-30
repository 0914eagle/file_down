
def max_total_score(n, m, student_answers, points):
    max_score = 0
    for i in range(m):
        answer_counts = {chr(ord('A') + j): 0 for j in range(5)}
        for ans in student_answers:
            answer_counts[ans[i]] += 1

        max_score += max(answer_counts.values()) * points[i]

    return max_score


# Input
n, m = map(int, input().split())
student_answers = [input().strip() for _ in range(n)]
points = list(map(int, input().split()))

# Output
print(max_total_score(n, m, student_answers, points))
```
