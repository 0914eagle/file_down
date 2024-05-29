
def find_least_purple_rain(sections):
    count = 0
    max_diff = 0
    start = 0
    end = 0
    curr_start = 0
    
    for i, color in enumerate(sections):
        if color == 'R':
            count += 1
        else:
            count -= 1
        
        if count > max_diff:
            max_diff = count
            start = curr_start
            end = i
        elif count == max_diff:
            if i - curr_start < end - start:
                start = curr_start
                end = i
        
        if count < 0:
            count = 0
            curr_start = i + 1
    
    return start + 1, end + 1

# Input
raindrops = input().strip()

# Output
start, end = find_least_purple_rain(raindrops)
print(start, end)
```
