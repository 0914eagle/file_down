
def days_to_find_troll(b, k, g):
    if k % g == 0:
        days = k // g
    else:
        days = k // g + 1
    return days

# Read input
b, k, g = map(int, input().split())

# Calculate and print the number of days
print(days_to_find_troll(b, k, g))
