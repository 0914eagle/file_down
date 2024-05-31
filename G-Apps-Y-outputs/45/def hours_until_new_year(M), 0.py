
def hours_until_new_year(M):
    hours_until_midnight = 24 - M
    hours_until_new_year = hours_until_midnight + 24*2
    return hours_until_new_year

M = int(input().strip())
print(hours_until_new_year(M))
