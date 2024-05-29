
def find_least_purple_rain(s):
    n = len(s)
    
    diff = 0
    max_diff = 0
    start = 1
    end = 0
    min_start = 1
    min_end = 0
    
    for i in range(n):
        if s[i] == 'R':
            diff += 1
        else:
            diff -= 1
        
        if diff > max_diff:
            max_diff = diff
            start = i + 2
            end = i + 2
        
        if diff < 0:
            diff = 0
            min_start = i + 2
            min_end = i + 2
    
    print(min_start, min_end)

# Input
raindrops = "BBRRBRRBRB"
find_least_purple_rain(raindrops)
```
