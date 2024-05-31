
def fix_bugs(n, m, s, bugs, abilities, passes):
    bugs_with_index = [(bugs[i], i) for i in range(m)]
    bugs_with_index.sort()
    
    students_with_index = [(abilities[i], i) for i in range(n)]
    students_with_index.sort()
    
    total_passes = 0
    fixes = [0] * m
    
    for bug_complexity, bug_index in bugs_with_index:
        student_found = False
        for student_ability, student_index in students_with_index:
            if student_ability >= bug_complexity and passes[student_index] > 0:
                fixes[bug_index] = student_index + 1
                passes[student_index] -= 1
                total_passes += 1
                student_found = True
                break
        if not student_found:
            print("NO")
            return
    
    if total_passes <= s:
        print("YES")
        print(*fixes)
    else:
        print("NO")

# Input
n, m, s = map(int, input().split())
bugs = list(map(int, input().split()))
abilities = list(map(int, input().split()))
passes = list(map(int, input().split()))

# Solve the problem
fix_bugs(n, m, s, bugs, abilities, passes)
