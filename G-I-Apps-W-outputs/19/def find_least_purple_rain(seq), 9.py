
def find_least_purple_rain(seq):
    n = len(seq)
    counts = {'R': 0, 'B': 0}
    prefix_sums = [(0, -1)]
    for i, char in enumerate(seq):
        counts[char] += 1
        prefix_sums.append((counts['R'] - counts['B'], i))

    min_dist = n
    result = (0, n)
    max_seen = {}
    
    for i, (diff, pos) in enumerate(prefix_sums):
        if diff in max_seen:
            dist = i - max_seen[diff] - 1
            if dist < min_dist or (dist == min_dist and max_seen[diff] < result[0]):
                min_dist = dist
                result = (max_seen[diff], i - 1)
        else:
            max_seen[diff] = i

    print(result[0] + 1, result[1])

# Sample Input
seq = "BBRRBRRBRB"
find_least_purple_rain(seq)
```
