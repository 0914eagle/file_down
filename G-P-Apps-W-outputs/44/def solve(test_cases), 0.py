
def solve(test_cases):
    results = []
    for segments in test_cases:
        segments.sort(key=lambda x: x[0])
        total = len(segments)
        max_segments = 0
        for i in range(total):
            if i == 0:
                max_segments = max(max_segments, count_segments(segments[1:]))
            elif i == total - 1:
                max_segments = max(max_segments, count_segments(segments[:-1]))
            else:
                max_segments = max(max_segments, count_segments(segments[:i] + segments[i + 1:]))
        results.append(max_segments)
    return results

def count_segments(segments):
    if not segments:
        return 0
    max_right = segments[0][1]
    count = 1
    for start, end in segments[1:]:
        if start > max_right:
            count += 1
            max_right = end
        else:
            max_right = max(max_right, end)
    return count

t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    segments = []
    for _ in range(n):
        l, r = map(int, input().split())
        segments.append((l, r))
    test_cases.append(segments)

results = solve(test_cases)
for result in results:
    print(result)
```
