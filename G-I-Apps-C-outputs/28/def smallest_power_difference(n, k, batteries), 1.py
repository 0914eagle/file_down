
def smallest_power_difference(n, k, batteries):
    batteries.sort()
    
    # Calculate the possible power differences between chips of each machine
    power_diffs = []
    for i in range(0, len(batteries), 2*k):
        chip1 = batteries[i:i+k]  # Power outputs of chips in first section
        chip2 = batteries[i+k:i+2*k]  # Power outputs of chips in second section
        chip_diffs = [abs(a - b) for a in chip1 for b in chip2]  # Calculate all differences
        power_diffs.extend(chip_diffs)
    
    # Determine the smallest possible power difference
    min_diff = max(power_diffs)
    for diff in range(1, max(power_diffs)+1):
        valid = all(d <= diff for d in power_diffs)
        if valid:
            min_diff = diff
            break
    
    return min_diff

# Read input
n, k = map(int, input().split())
batteries = list(map(int, input().split()))

# Calculate and print the smallest power difference
print(smallest_power_difference(n, k, batteries))
```
