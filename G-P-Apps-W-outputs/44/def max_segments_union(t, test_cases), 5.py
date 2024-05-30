
def max_segments_union(t, test_cases):
    results = []
    
    for case in test_cases:
        n = case[0]
        segments = case[1:]
        
        max_segments = 0
        for i in range(n):
            temp_segments = segments[:i] + segments[i+1:]
            temp_segments.sort(key=lambda x: x[0])
            
            union_count = 1
            rightmost = temp_segments[0][1]
            
            for j in range(1, len(temp_segments)):
                if temp_segments[j][0] > rightmost:
                    union_count += 1
                    rightmost = temp_segments[j][1]
                else:
                    rightmost = max(rightmost, temp_segments[j][1])
                
            max_segments = max(max_segments, union_count)
            
        results.append(max_segments)
    
    return results

# Input
t = 3
test_cases = [
    (4, (1, 4), (2, 3), (3, 6), (5, 7)),
    (3, (5, 5), (5, 5), (5, 5)),
    (6, (3, 3), (1, 1), (5, 5), (1, 5), (2, 2), (4, 4))
]

# Output
output = max_segments_union(t, test_cases)
for res in output:
    print(res)
```
