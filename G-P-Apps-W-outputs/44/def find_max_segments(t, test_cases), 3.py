
def find_max_segments(t, test_cases):
    results = []
    
    for i in range(t):
        n = test_cases[i][0]
        segments = test_cases[i][1:]
        
        # Calculate the total coverage span
        total_span = 0
        for segment in segments:
            total_span += segment[1] - segment[0] + 1
        
        max_segments = 0
        
        for j in range(n):
            # Calculate the span covered by segments excluding the j-th segment
            span_excluding_j = total_span - (segments[j][1] - segments[j][0] + 1)
            
            # Check if the span excluding j-th segment results in more segments in union
            if span_excluding_j % 2 == 0:
                max_segments = max(max_segments, n - 1)
            else:
                for k in range(n):
                    if k != j:
                        new_span_excluding_j_k = span_excluding_j - (segments[k][1] - segments[k][0] + 1)
                        if new_span_excluding_j_k % 2 == 0:
                            max_segments = max(max_segments, n - 1)
                            break
        
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
    test_cases.append((n, *segments))

# Find and print the results
results = find_max_segments(t, test_cases)
for result in results:
    print(result)
```
