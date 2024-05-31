
def hours_until_new_year(M):
    hours_until_midnight = 24 - M
    return hours_until_midnight + 24 + 24

# Read input
M = int(input())

# Calculate and print the result
print(hours_until_new_year(M))
