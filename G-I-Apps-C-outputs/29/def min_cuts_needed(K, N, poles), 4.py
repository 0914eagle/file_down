
def min_cuts_needed(K, N, poles):
    poles.sort()
    diffs = [poles[i+1] - poles[i] for i in range(K-1)]
    cuts = 0
    while len(diffs) > 0:
        max_diff_index = diffs.index(max(diffs))
        cuts += 1
        diff_value = diffs[max_diff_index]
        diffs.pop(max_diff_index)
        if diff_value % 2 == 0:
            new_diffs = [diff_value // 2] * 2
        else:
            new_diffs = [diff_value // 2, diff_value // 2 + 1]
        if max_diff_index > 0:
            new_diffs[0] += poles[max_diff_index]
        if max_diff_index < len(poles) - 1:
            new_diffs[1] += poles[max_diff_index + 1]
        poles.pop(max_diff_index)
        poles.pop(max_diff_index)
        poles = poles[:max_diff_index] + new_diffs + poles[max_diff_index:]
    return cuts

# Input processing
K, N = map(int, input().split())
poles = list(map(int, input().split()))

# Output
print(min_cuts_needed(K, N, poles))
```
