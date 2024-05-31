
def solve_contest(n, m, s, bugs, abilities, passes):
    bugs_sorted = sorted(enumerate(bugs, start=1), key=lambda x: x[1])
    abilities_sorted = sorted(enumerate(abilities, start=1), key=lambda x: x[1], reverse=True)
    
    total_passes = 0
    bug_to_student = [0] * (m+1)
    
    for bug_idx, bug_complexity in bugs_sorted:
        assigned = False
        for student_idx, student_ability in abilities_sorted:
            if student_ability >= bug_complexity and passes[student_idx-1] > 0:
                bug_to_student[bug_idx] = student_idx
                total_passes += 1
                passes[student_idx-1] -= 1
                assigned = True
                break
        
        if not assigned:
            print("NO")
            return
    
    if total_passes > s:
        print("NO")
    else:
        print("YES")
        print(" ".join(str(student_idx) for student_idx in bug_to_student[1:]))

# Input parsing
n, m, s = map(int, input().split())
bugs = list(map(int, input().split()))
abilities = list(map(int, input().split()))
passes = list(map(int, input().split()))

solve_contest(n, m, s, bugs, abilities, passes)
