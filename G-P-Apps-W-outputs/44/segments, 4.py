segments_in_union(t, test_cases):
    results = []
    
    for case in test_cases:
        n = case[0]
        segments = case[1:]
        max_segments = 0
        
        for i in range(n):
            remaining_segments = segments[:i] + segments[i+1:]
            union = []
            
            for seg in remaining_segments:
                if not union:
                    union.append(seg)
                else:
                    last_seg = union[-1]
                    if seg[0] <= last_seg[1]:
                        union[-1] = [last_seg[0], max(last_seg[1], seg[1])]
                    else:
                        union.append(seg)
                        
            max_segments = max(max_segments, len(union))
        
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
output = max_segments_in_union(t, test_cases)
for res in output:
    print(res)  
