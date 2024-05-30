
def days_to_find_troll(b, k, g):
    # Calculate the minimum number of groups needed to cover all bridges
    groups = (b + g - 1) // g
    # Calculate the number of days needed
    days = (groups + k - 1) // k
    return days

# Read input
b, k, g = map(int, input().split())

# Output result
print(days_to_find_troll(b, k, g))
```
