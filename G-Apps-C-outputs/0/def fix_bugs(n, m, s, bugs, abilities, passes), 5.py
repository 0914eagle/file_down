
def fix_bugs(n, m, s, bugs, abilities, passes):
    bugs_sorted = sorted(enumerate(bugs), key=lambda x: x[1])
    abilities_sorted = sorted(enumerate(abilities), key=lambda x: x[1], reverse=True)
    
    total_passes = 0
    bug_assignments = [-1] * m
    
    for bug_idx, bug_complexity in bugs_sorted:
        assigned = False
        for student_idx, student_ability in abilities_sorted:
            if student_ability >= bug_complexity and passes[student_idx] > 0:
                passes[student_idx] -= 1
                total_passes += 1
                bug_assignments[bug_idx] = student_idx + 1
                assigned = True
                break
        if not assigned:
            print("NO")
            return
    
    if total_passes > s:
        print("NO")
    else:
        print("YES")
        print(" ".join(map(str, bug_assignments)))

# Input parsing
n, m, s = map(int, input().split())
bugs = list(map(int, input().split()))
abilities = list(map(int, input().split()))
passes = list(map(int, input().split()))

fix_bugs(n, m, s, bugs, abilities, passes)
