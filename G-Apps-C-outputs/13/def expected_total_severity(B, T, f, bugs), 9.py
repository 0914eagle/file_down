
def expected_total_severity(B, T, f, bugs):
    def expected_severity(prob, severity, hours_left, fix_factor):
        if hours_left == 0:
            return 0
        fix = prob * severity + (1 - prob) * expected_severity(prob * fix_factor, severity, hours_left - 1, fix_factor)
        not_fix = expected_severity(prob, severity, hours_left - 1, fix_factor)
        return max(fix, not_fix)
    
    total_severity = 0
    for prob, severity in bugs:
        total_severity += expected_severity(prob, severity, T, f)
    
    return round(total_severity, 6)

# Read input
B, T, f = map(float, input().split())
B = int(B)
T = int(T)
bugs = []
for _ in range(B):
    p, s = map(float, input().split())
    bugs.append((p, s))

# Calculate and output the expected total severity of bugs fixed
print(expected_total_severity(B, T, f, bugs))
