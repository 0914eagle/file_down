
def fix_bugs(n, m, s, bugs, abilities, passes):
    bugs_sorted = sorted(enumerate(bugs, 1), key=lambda x: x[1])
    students_sorted = sorted(enumerate(abilities, 1), key=lambda x: x[1])
    
    total_passes = 0
    student_index = 0
    result = [0] * m
    
    for bug_index, complexity in bugs_sorted:
        while student_index < n and students_sorted[student_index][1] < complexity:
            student_index += 1
        
        if student_index >= n:
            print("NO")
            return
        
        student, level = students_sorted[student_index]
        result[bug_index-1] = student
        total_passes += passes[student-1]
        
        if total_passes > s:
            print("NO")
            return
    
    print("YES")
    print(*result)

# Input parsing
n, m, s = map(int, input().split())
bugs = list(map(int, input().split()))
abilities = list(map(int, input().split()))
passes = list(map(int, input().split()))

# Call the function with parsed input
fix_bugs(n, m, s, bugs, abilities, passes)
