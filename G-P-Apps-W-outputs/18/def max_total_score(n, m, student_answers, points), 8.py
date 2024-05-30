
def max_total_score(n, m, student_answers, points):
    total_score = 0
    
    for question in range(m):
        answer_count = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0}
        for student in student_answers:
            answer_count[student[question]] += 1
        
        max_points = max(answer_count.values())
        total_score += max_points * points[question]
    
    return total_score

# Read input
n, m = map(int, input().split())
student_answers = [input().strip() for _ in range(n)]
points = list(map(int, input().split()))

# Call the function and print the result
print(max_total_score(n, m, student_answers, points))
```
