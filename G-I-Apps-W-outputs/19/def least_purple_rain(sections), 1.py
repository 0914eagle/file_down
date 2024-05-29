
def least_purple_rain(sections):
    n = len(sections)
    count = 0
    max_diff = -1
    max_diff_index = -1
    prefix_sums = [0]
    for color in sections:
        if color == 'R':
            count += 1
        else:
            count -= 1
        prefix_sums.append(count)
    
    min_prefix = min(prefix_sums)
    for i, prefix_sum in enumerate(prefix_sums):
        if prefix_sum == min_prefix:
            start_index = i
            if max_diff < i - max_diff_index:
                max_diff = i - max_diff_index
                result = (max_diff_index + 1, i)
            max_diff_index = i

    return result

# Example usage
sections = "BBRRBRRBRB"
start, end = least_purple_rain(sections)
print(start, end)
```
