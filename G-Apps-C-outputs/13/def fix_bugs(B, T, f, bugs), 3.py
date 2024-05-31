
def fix_bugs(B, T, f, bugs):
    bugs.sort(key=lambda x: x[1], reverse=True)  # Sort bugs in descending order of severity

    total_severity = 0
    for _ in range(T):
        max_expected_severity = 0
        chosen_bug = None

        for i, bug in enumerate(bugs):
            p, s = bug
            fix_probability = p * (f ** i)  # Adjusted fix probability based on previous failures
            expected_severity = fix_probability * s

            if expected_severity > max_expected_severity:
                max_expected_severity = expected_severity
                chosen_bug = i

        if chosen_bug is not None:
            p, s = bugs.pop(chosen_bug)
            total_severity += p * s

    return total_severity

# Input parsing
B, T, f = map(float, input().split())
B = int(B)
T = int(T)
f = float(f)

bugs = []
for _ in range(B):
    p, s = map(float, input().split())
    bugs.append((p, s))

print('{:.6f}'.format(fix_bugs(B, T, f, bugs)))
