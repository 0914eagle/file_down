
def max_total_score(n, m, student_answers, points):
    total_score = 0
    
    for i in range(m):
        answer_count = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0}
        
        for answer in student_answers:
            answer_count[answer[i]] += 1
        
        max_points = max(points[i] * answer_count[ans] for ans in answer_count)
        total_score += max_points
    
    return total_score

# Input
n, m = map(int, input().split())
student_answers = [input() for _ in range(n)]
points = list(map(int, input().split()))

# Output
print(max_total_score(n, m, student_answers, points))
