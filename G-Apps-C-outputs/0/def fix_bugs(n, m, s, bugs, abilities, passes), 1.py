
def fix_bugs(n, m, s, bugs, abilities, passes):
    bugs_sorted = sorted(enumerate(bugs), key=lambda x: x[1])
    abilities_sorted = sorted(enumerate(abilities), key=lambda x: x[1], reverse=True)

    total_days = 0
    students_used = []
    bug_fixers = [-1] * m
    passes_used = 0

    for bug_idx, bug_complexity in bugs_sorted:
        student_found = False
        for student_idx, ability in abilities_sorted:
            if ability >= bug_complexity and passes[student_idx] > 0:
                total_days += 1
                students_used.append(student_idx + 1)
                bug_fixers[bug_idx] = student_idx + 1
                passes_used += passes[student_idx]
                passes[student_idx] -= 1
                student_found = True
                break

        if not student_found:
            print("NO")
            return

    if passes_used <= s:
        print("YES")
        print(" ".join(map(str, bug_fixers)))
    else:
        print("NO")

# Input parsing
n, m, s = map(int, input().split())
bugs = list(map(int, input().split()))
abilities = list(map(int, input().split()))
passes = list(map(int, input().split()))

# Call the function with the input values
fix_bugs(n, m, s, bugs, abilities, passes)
