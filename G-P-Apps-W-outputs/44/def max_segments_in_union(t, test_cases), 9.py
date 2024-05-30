
def max_segments_in_union(t, test_cases):
    results = []
    
    for i in range(t):
        n = test_cases[i][0]
        segments = test_cases[i][1:]
        
        left = [0] * n
        right = [0] * n
        
        for j in range(n):
            left[j] = segments[j][0]
            right[j] = segments[j][1]
        
        left.sort()
        right.sort()
        
        max_segments = 1
        for j in range(n):
            if j == 0:
                max_segments = max(max_segments, n-1)
            elif j == n-1:
                max_segments = max(max_segments, n-1)
            else:
                max_segments = max(max_segments, j + (n-j-1))
        
        results.append(max_segments)
    
    return results

# Input
t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    segments = []
    for _ in range(n):
        l, r = map(int, input().split())
        segments.append((l, r))
    test_cases.append([n] + segments)

# Output
results = max_segments_in_union(t, test_cases)
for res in results:
    print(res)
```
