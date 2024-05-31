s_until_new_year(M):
    hours_until_midnight = 24 - M
    hours_until_new_year = hours_until_midnight + 24
    return hours_until_new_year

# Taking input for M
M = int(input().strip())

# Calculating the hours until New Year
result = hours_until_new_year(M)

print(result)
[/PYTHON