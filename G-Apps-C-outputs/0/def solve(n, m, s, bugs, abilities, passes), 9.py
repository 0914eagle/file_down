
def solve(n, m, s, bugs, abilities, passes):
    bug_student = [0] * m
    students = sorted(range(n), key=lambda x: abilities[x], reverse=True)
    bugs = sorted(enumerate(bugs), key=lambda x: x[1])
    
    total_passes = 0
    for i in range(m):
        bug_idx, bug_complexity = bugs[i]
        for student_idx in students:
            if abilities[student_idx] >= bug_complexity and passes[student_idx] > 0:
                bug_student[bug_idx] = student_idx + 1
                passes[student_idx] -= 1
                total_passes += 1
                break

    if total_passes > s:
        return "NO"
    else:
        return "YES\n" + " ".join(str(student) for student in bug_student)

# Input reading
n, m, s = map(int, input().split())
bugs = list(map(int, input().split()))
abilities = list(map(int, input().split()))
passes = list(map(int, input().split()))

# Output
print(solve(n, m, s, bugs, abilities, passes))
