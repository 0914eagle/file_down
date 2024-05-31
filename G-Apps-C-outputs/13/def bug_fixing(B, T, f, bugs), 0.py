
def bug_fixing(B, T, f, bugs):
    bugs.sort(key=lambda x: (x[1], x[0]), reverse=True)  # Sort bugs by severity in descending order

    expected_severity = 0
    for _ in range(T):
        max_expected_severity_increase = 0
        best_bug_index = -1

        for i, bug in enumerate(bugs):
            p, s = bug
            p_fix = p
            p_factor = 1
            for j in range(i):
                p_factor *= f
            p_fix *= p_factor

            expected_severity_increase = p_fix * s
            if expected_severity_increase > max_expected_severity_increase:
                max_expected_severity_increase = expected_severity_increase
                best_bug_index = i

        if best_bug_index != -1:
            p_fix = bugs[best_bug_index][0]
            p_factor = 1
            for j in range(best_bug_index):
                p_factor *= f
            p_fix *= p_factor

            expected_severity += p_fix * bugs[best_bug_index][1]
            bugs.pop(best_bug_index)

    return expected_severity

# Input parsing
B, T, f = map(float, input().split())
B = int(B)
T = int(T)
f = float(f)

bugs = []
for _ in range(B):
    p, s = map(float, input().split())
    bugs.append((p, s))

print("{:.6f}".format(bug_fixing(B, T, f, bugs)))
