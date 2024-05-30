
def max_segments_union(t, test_cases):
    results = []
    
    for i in range(t):
        n = test_cases[i][0]
        segments = test_cases[i][1:]
        
        max_segments = 0
        for j in range(n):
            other_segments = segments[:j] + segments[j+1:]
            union = set()
            for segment in other_segments:
                union.add((segment[0], 'start'))
                union.add((segment[1], 'end'))
            union = sorted(list(union))
            count = 0
            max_count = 0
            for point in union:
                if point[1] == 'start':
                    count += 1
                else:
                    count -= 1
                max_count = max(max_count, count)
            max_segments = max(max_segments, max_count)
        
        results.append(max_segments)
    
    return results

# Input parsing
t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    segments = []
    for _ in range(n):
        segment = tuple(map(int, input().split()))
        segments.append(segment)
    test_cases.append([n] + segments)

# Call the function and print the results
results = max_segments_union(t, test_cases)
for result in results:
    print(result)
```
