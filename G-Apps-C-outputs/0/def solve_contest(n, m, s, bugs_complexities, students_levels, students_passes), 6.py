
def solve_contest(n, m, s, bugs_complexities, students_levels, students_passes):
    bugs = [(bugs_complexities[i], i) for i in range(m)]
    bugs.sort()
    
    students = [(students_levels[i], i) for i in range(n)]
    students.sort(reverse=True)
    
    result = [-1] * m
    total_passes = 0
    days = 0
    
    for bug_complexity, bug_index in bugs:
        student_index = 0
        while student_index < n and students[student_index][0] >= bug_complexity:
            student_index += 1
        
        if student_index == 0:
            print("NO")
            return
        
        student_index -= 1
        if total_passes + students_passes[students[student_index][1]] > s:
            print("NO")
            return
        
        result[bug_index] = students[student_index][1] + 1
        total_passes += students_passes[students[student_index][1]]
        days = max(days, students[student_index][0])
    
    print("YES")
    print(" ".join(map(str, result)))

# Input
n, m, s = map(int, input().split())
bugs_complexities = list(map(int, input().split()))
students_levels = list(map(int, input().split()))
students_passes = list(map(int, input().split()))

# Call the function
solve_contest(n, m, s, bugs_complexities, students_levels, students_passes)
