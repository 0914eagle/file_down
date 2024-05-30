
def max_segments_union(t, test_cases):
    def merge_segments(segments):
        segments.sort()
        merged = []
        for segment in segments:
            if not merged or segment[0] > merged[-1][1]:
                merged.append(segment)
            else:
                merged[-1] = (merged[-1][0], max(merged[-1][1], segment[1]))
        return merged

    def count_segments_in_union(segments):
        union_segments = merge_segments(segments)
        return len(union_segments)

    results = []
    for i in range(t):
        n = test_cases[i][0]
        segments = test_cases[i][1]
        max_segments = -1
        for j in range(n):
            segments_copy = segments.copy()
            segments_copy.pop(j)
            max_segments = max(max_segments, count_segments_in_union(segments_copy))
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

# Get results
results = max_segments_union(t, test_cases)

# Output results
for res in results:
    print(res)
```
