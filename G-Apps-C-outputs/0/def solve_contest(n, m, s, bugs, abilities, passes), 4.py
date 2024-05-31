
def solve_contest(n, m, s, bugs, abilities, passes):
    bugs_sorted = sorted(enumerate(bugs, 1), key=lambda x: x[1])
    abilities_sorted = sorted(enumerate(abilities, 1), key=lambda x: x[1], reverse=True)
    
    total_passes = 0
    result = [0] * m
    
    for bug_index, bug_complexity in bugs_sorted:
        student_found = False
        for student_index, student_ability in abilities_sorted:
            if student_ability >= bug_complexity and passes[student_index - 1] > 0:
                result[bug_index - 1] = student_index
                total_passes += student_index
                passes[student_index - 1] -= 1
                student_found = True
                break
        if not student_found:
            print("NO")
            return
    
    if total_passes <= s:
        print("YES")
        print(" ".join(map(str, result)))
    else:
        print("NO")

# Input parsing
n, m, s = map(int, input().split())
bugs = list(map(int, input().split()))
abilities = list(map(int, input().split()))
passes = list(map(int, input().split()))

solve_contest(n, m, s, bugs, abilities, passes)
