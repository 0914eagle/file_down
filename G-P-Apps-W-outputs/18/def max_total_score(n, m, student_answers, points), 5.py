
def max_total_score(n, m, student_answers, points):
    max_score = 0
    
    for q in range(m):
        answer_counts = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0}
        
        for student in student_answers:
            answer_counts[student[q]] += 1
        
        max_count = max(answer_counts.values())
        max_score += max_count * points[q]
    
    return max_score

# Input parsing
n, m = map(int, input().split())
student_answers = []
for _ in range(n):
    student_answers.append(input().strip())
points = list(map(int, input().split()))

# Call the function and print the result
print(max_total_score(n, m, student_answers, points))
