
def solve(n, m, s, bugs, abilities, passes):
    bugs_sorted = sorted(enumerate(bugs, start=1), key=lambda x: x[1])
    abilities_sorted = sorted(enumerate(abilities, start=1), key=lambda x: x[1], reverse=True)
    passes_sum = 0
    result = [0] * m
    
    for bug_idx, bug_complexity in bugs_sorted:
        student_idx = 0
        while student_idx < n and abilities_sorted[student_idx][1] >= bug_complexity:
            student_idx += 1
        
        if student_idx == 0:
            return "NO"
        
        student_idx -= 1
        passes_sum += passes[student_idx]
        if passes_sum > s:
            return "NO"
        
        result[bug_idx - 1] = abilities_sorted[student_idx][0]
    
    return "YES\n" + " ".join(str(x) for x in result)

# Input parsing
n, m, s = map(int, input().split())
bugs = list(map(int, input().split()))
abilities = list(map(int, input().split()))
passes = list(map(int, input().split())

# Output
print(solve(n, m, s, bugs, abilities, passes))
