
def find_troll_days(b, k, g):
    if k % g == 0:
        return b // (k // g)
    else:
        return b // (k // g) + 1

# Read input
b, k, g = map(int, input().split())

# Calculate and print the number of days
print(find_troll_days(b, k, g))
