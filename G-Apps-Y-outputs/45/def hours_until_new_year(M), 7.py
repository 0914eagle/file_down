
def hours_until_new_year(M):
    total_hours = 24  # Hours left in the current day
    remaining_days = 2  # 31st and 1st
    remaining_hours = 24 - M  # Hours left from the given hour until midnight
    hours_until_new_year = (remaining_days * 24) + total_hours + remaining_hours
    return hours_until_new_year

# Read input
M = int(input())

# Calculate and output the result
print(hours_until_new_year(M))
