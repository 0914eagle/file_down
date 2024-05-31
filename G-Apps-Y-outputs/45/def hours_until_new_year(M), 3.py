
def hours_until_new_year(M):
    # Hours in a day
    hours_in_day = 24
    
    # Hours until New Year
    hours_until_new_year = (24 - M) + hours_in_day
    
    return hours_until_new_year

# Read input
M = int(input().strip())

# Calculate and print the result
result = hours_until_new_year(M)
print(result)
