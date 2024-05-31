
def solve_contest(n, m, s, bugs, abilities, passes):
    sorted_bugs = sorted(enumerate(bugs, start=1), key=lambda x: x[1])
    sorted_abilities = sorted(enumerate(abilities, start=1), key=lambda x: x[1], reverse=True)
    
    bug_assignments = [0] * m
    total_passes = 0
    
    for bug_idx, bug_complexity in sorted_bugs:
        found_fixer = False
        for student_idx, student_ability in sorted_abilities:
            if student_ability >= bug_complexity and passes[student_idx-1] > 0:
                bug_assignments[bug_idx-1] = student_idx
                total_passes += student_ability
                passes[student_idx-1] -= 1
                found_fixer = True
                break

        if not found_fixer:
            print("NO")
            return

    if total_passes <= s:
        print("YES")
        print(" ".join(map(str, bug_assignments)))
    else:
        print("NO")

# Input parsing
n, m, s = map(int, input().split())
bugs = list(map(int, input().split()))
abilities = list(map(int, input().split()))
passes = list(map(int, input().split()))

# Call the function
solve_contest(n, m, s, bugs, abilities, passes)
