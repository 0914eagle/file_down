
import sys

def max_segments_in_union(t, test_cases):
    results = []
    for i in range(t):
        n = test_cases[i][0]
        segments = sorted(test_cases[i][1:], key=lambda x: (x[0], -x[1]))
        prefix_max = [0] * n
        suffix_min = [10**9] * n
        
        for j in range(1, n):
            prefix_max[j] = max(prefix_max[j-1], segments[j-1][1])
        
        for j in range(n-2, -1, -1):
            suffix_min[j] = min(suffix_min[j+1], segments[j+1][0])
        
        max_segments = 1
        for j in range(n):
            if suffix_min[j] >= prefix_max[j]:
                max_segments = max(max_segments, j+1, n-j-1)
        
        results.append(max_segments)
    
    return results

# Read input
input_lines = sys.stdin.readlines()
t = int(input_lines[0])
test_cases = []
current_line = 1

for _ in range(t):
    n = int(input_lines[current_line])
    segments = []
    for _ in range(n):
        l, r = map(int, input_lines[current_line+1].split())
        segments.append((l, r))
        current_line += 1
    test_cases.append([n] + segments)

# Find and print the results
results = max_segments_in_union(t, test_cases)
for result in results:
    print(result)
```
