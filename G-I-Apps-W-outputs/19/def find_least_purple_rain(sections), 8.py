
def find_least_purple_rain(sections):
    n = len(sections)
    
    count_R = [0] * (n + 1)
    count_B = [0] * (n + 1)
    
    for i in range(n):
        count_R[i + 1] = count_R[i] + (sections[i] == 'R')
        count_B[i + 1] = count_B[i] + (sections[i] == 'B')
    
    max_diff = 0
    start_index = 0
    end_index = 0
    
    for i in range(n + 1):
        for j in range(i + 1, n + 1):
            diff = count_R[j] - count_R[i] - (count_B[j] - count_B[i])
            if diff > max_diff or (diff == max_diff and (i < start_index or (i == start_index and j > end_index))):
                max_diff = diff
                start_index = i
                end_index = j
    
    return start_index + 1, end_index

# Input
raindrop_colors = "BBRRBRRBRB"

# Output
start, end = find_least_purple_rain(raindrop_colors)
print(start, end)
```
