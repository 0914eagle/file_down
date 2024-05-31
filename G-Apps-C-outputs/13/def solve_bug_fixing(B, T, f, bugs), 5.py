
def solve_bug_fixing(B, T, f, bugs):
    bugs.sort(key=lambda x: (-(x[1] * x[0]), x[0]))  # Sort bugs by severity * fix probability (descending) and then fix probability (ascending)

    total_severity = 0
    for _ in range(T):
        best_bug = None
        max_value = 0
        
        for bug in bugs:
            value = bug[0] * bug[1] * (f ** min(_, T))
            if value > max_value:
                max_value = value
                best_bug = bug
                
        if best_bug is not None:
            total_severity += best_bug[1]
            best_bug[0] *= f  # Update fix probability after a failure

    return total_severity

# Reading input
B, T, f = map(float, input().split())
B = int(B)
T = int(T)
f = float(f)

bugs = []
for _ in range(B):
    p, s = map(float, input().split())
    bugs.append((p, s))

# Call the function and print the result
result = solve_bug_fixing(B, T, f, bugs)
print("{:.6f}".format(result))
