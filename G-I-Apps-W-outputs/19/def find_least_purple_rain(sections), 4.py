
def find_least_purple_rain(sections):
    n = len(sections)
    count_r = 0
    count_b = 0
    min_diff = n
    start_idx = -1
    end_idx = -1
    
    diff_map = {0: -1}
    
    for i, section in enumerate(sections):
        if section == 'R':
            count_r += 1
        else:
            count_b += 1
        
        diff = count_r - count_b
        
        if diff not in diff_map:
            diff_map[diff] = i
        
        if i - diff_map[diff] > min_diff:
            min_diff = i - diff_map[diff]
            start_idx = diff_map[diff]
            end_idx = i
    
    return start_idx + 2, end_idx + 1

sections = "BBRRBRRBRB"
start, end = find_least_purple_rain(sections)
print(start, end)
```
