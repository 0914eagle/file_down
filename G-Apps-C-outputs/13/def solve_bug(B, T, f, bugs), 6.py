
import math

def solve_bug(B, T, f, bugs):
    # Sort bugs based on severity in descending order
    bugs.sort(key=lambda x: x[1], reverse=True)
    
    # Initialize expected total severity of fixed bugs
    total_severity = 0
    
    for _ in range(T):
        max_expected_severity = 0
        
        for i in range(B):
            p, s = bugs[i]
            expected_severity = p * s
            
            for j in range(B):
                if j != i:
                    expected_severity += (1 - p) * bugs[j][0] * bugs[j][1]
            
            max_expected_severity = max(max_expected_severity, expected_severity)
        
        total_severity += max_expected_severity
        
        for i in range(B):
            p, s = bugs[i]
            p *= f
            bugs[i] = (p, s)
    
    return round(total_severity, 6)

# Read input
B, T, f = map(float, input().split())
B = int(B)
T = int(T)
f = float(f)

bugs = []
for _ in range(B):
    p, s = map(float, input().split())
    bugs.append((p, s))

# Call the function and print the output
print(solve_bug(B, T, f, bugs))
