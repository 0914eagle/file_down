
def find_troll_days(b, k, g):
    # Calculate the minimum number of groups needed to cover all bridges
    groups = (b + g - 1) // g
    
    # Calculate the number of days it would take to search all bridges
    days = (groups + k - 1) // k
    
    return days

# Read input
b, k, g = map(int, input().split())

# Call the function and print the output
print(find_troll_days(b, k, g))
```
