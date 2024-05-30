
def days_to_find_troll(b, k, g):
    groups_needed = k // g
    days = b // groups_needed
    if b % groups_needed != 0:
        days += 1
    return days

# Input processing
input_data = input().split()
b = int(input_data[0])
k = int(input_data[1])
g = int(input_data[2])

# Call the function and print the result
print(days_to_find_troll(b, k, g))
```
