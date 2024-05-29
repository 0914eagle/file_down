
def find_min_purple_rain(input_str):
    n = len(input_str)
    
    counts = {'R': 0, 'B': 0}
    diff = {'R': 0, 'B': 0}
    min_diff = n
    start_pos = 1
    end_pos = n
    
    for i in range(n):
        counts[input_str[i]] += 1
        diff[input_str[i]] = counts['R'] - counts['B']
        
        if diff['R'] - diff['B'] > 0:
            if diff['R'] - diff['B'] < min_diff:
                min_diff = diff['R'] - diff['B']
                start_pos = i + 2 - min_diff
                end_pos = i + 1
    
    print(start_pos, end_pos)

# Input example
input_str = "BBRRBRRBRB"
find_min_purple_rain(input_str)
```
