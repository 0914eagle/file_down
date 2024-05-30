
def find_troll_days(b, k, g):
    if k % g == 0:
        return b * (k // g)
    else:
        return b * ((k // g) + 1)

# Input parsing
input_values = input().split()
b = int(input_values[0])
k = int(input_values[1])
g = int(input_values[2])

# Call the function and output the result
print(find_troll_days(b, k, g))
```
