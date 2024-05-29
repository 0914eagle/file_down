
import sys

# Read input from Standard Input
input_lines = sys.stdin.readlines()
N = int(input_lines[0])
health_values = list(map(int, input_lines[1].split()))

# Find the minimum possible final health of the last monster alive
min_health = min(health_values)

print(min_health)
```
