
def find_least_purple_rain_section(locations):
    max_diff = 0
    diff_position = {0: -1}
    current_diff = 0
    start_position = 0

    for i, color in enumerate(locations):
        current_diff += 1 if color == 'R' else -1

        if current_diff not in diff_position:
            diff_position[current_diff] = i
        
        if i - diff_position[current_diff] > max_diff:
            max_diff = i - diff_position[current_diff]
            start_position = diff_position[current_diff] + 1

    return start_position, start_position + max_diff

# Input
locations = input().strip()
# Call the function
start, end = find_least_purple_rain_section(locations)
# Output
print(start, end)
```
