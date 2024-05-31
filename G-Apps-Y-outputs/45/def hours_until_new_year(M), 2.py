
def hours_until_new_year(M):
    hours_until_midnight = 24 - M
    hours_until_new_year = 24 + hours_until_midnight + 24
    return hours_until_new_year

# Read input from Standard Input
M = int(input().strip())

# Calculate and print the output
print(hours_until_new_year(M))
