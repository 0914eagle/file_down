
def days_to_find_troll(b, k, g):
    if k % g == 0:
        return b * (k // g)
    else:
        return b * (k // g + 1)

# Read input
input_str = input().strip()
b, k, g = map(int, input_str.split())

# Calculate and print result
result = days_to_find_troll(b, k, g)
print(result)
```
