
def find_least_purple_rain(sections):
    max_diff = 0
    start = 1
    end = 1
    curr_diff = 0
    min_prefix_sum = {}
    
    prefix_sum = 0
    min_prefix_sum[0] = 0
    
    for i in range(len(sections)):
        if sections[i] == 'R':
            prefix_sum += 1
        else:
            prefix_sum -= 1
        
        if prefix_sum not in min_prefix_sum:
            min_prefix_sum[prefix_sum] = i + 1
        
        if prefix_sum - 1 in min_prefix_sum:
            curr_diff = i + 1 - min_prefix_sum[prefix_sum - 1]
            if curr_diff > max_diff or (curr_diff == max_diff and (min_prefix_sum[prefix_sum - 1] < start or (min_prefix_sum[prefix_sum - 1] == start and i + 1 < end))):
                max_diff = curr_diff
                start = min_prefix_sum[prefix_sum - 1] + 1
                end = i + 1
                
    return start, end

# Example usage
sections = "BBRRBRRBRB"
start, end = find_least_purple_rain(sections)
print(start, end)
```
