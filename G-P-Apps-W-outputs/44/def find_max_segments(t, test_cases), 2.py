
def find_max_segments(t, test_cases):
    results = []
    
    for i in range(t):
        n = test_cases[i][0]
        segments = test_cases[i][1:]
        
        union = []
        for j in range(n):
            tmp = segments[:j] + segments[j+1:]
            leftmost = min(tmp, key=lambda x: x[0])[0]
            rightmost = max(tmp, key=lambda x: x[1])[1]
            union.append((leftmost, rightmost))
        
        max_segments = 0
        for j in range(n):
            tmp = union[:j] + union[j+1:]
            leftmost = min(tmp, key=lambda x: x[0])[0]
            rightmost = max(tmp, key=lambda x: x[1])[1]
            count = sum(1 for x in tmp if x[0] <= rightmost and x[1] >= leftmost)
            max_segments = max(max_segments, count)
        
        results.append(max_segments)
    
    return results

# Input processing
t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    segments = []
    for _ in range(n):
        l, r = map(int, input().split())
        segments.append((l, r))
    test_cases.append([n] + segments)

# Find and output results
results = find_max_segments(t, test_cases)
for result in results:
    print(result)
```
