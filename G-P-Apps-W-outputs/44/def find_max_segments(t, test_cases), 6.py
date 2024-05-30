
def find_max_segments(t, test_cases):
    results = []
    
    for _ in range(t):
        n = test_cases[_][0]
        segments = test_cases[_][1]
        
        max_segments = 0
        for i in range(n):
            temp_segments = segments[:i] + segments[i+1:]
            temp_segments.sort()
            
            max_end = float('-inf')
            count = 0
            for seg in temp_segments:
                if seg[0] > max_end:
                    count += 1
                    max_end = seg[1]
                else:
                    max_end = max(max_end, seg[1])
            
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
    test_cases.append((n, segments))

# Find and print the maximum number of segments in the union of n-1 segments
results = find_max_segments(t, test_cases)
for res in results:
    print(res)
```
