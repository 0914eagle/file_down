
def find_least_purple_rain(sections):
    n = len(sections)
    num_red = 0
    num_blue = 0
    count_diff = {}
    min_diff = float('inf')
    start_idx = 1
    min_start = 1
    for i in range(n):
        if sections[i] == 'R':
            num_red += 1
        else:
            num_blue += 1
        
        diff = num_red - num_blue

        if diff in count_diff:
            if i - count_diff[diff] < min_diff or (i - count_diff[diff] == min_diff and count_diff[diff] < min_start):
                min_diff = i - count_diff[diff]
                min_start = count_diff[diff] + 2
                start_idx = count_diff[diff] + 1
        else:
            count_diff[diff] = i

    return start_idx, start_idx + min_diff

# Input
sections = "BBRRBRRBRB"
# Output
start, end = find_least_purple_rain(sections)
print(start, end)
```
