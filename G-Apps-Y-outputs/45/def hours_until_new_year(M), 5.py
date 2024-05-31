
def hours_until_new_year(M):
    hours_left = 24 - M + 24
    return hours_left

M = int(input())
result = hours_until_new_year(M)
print(result)
