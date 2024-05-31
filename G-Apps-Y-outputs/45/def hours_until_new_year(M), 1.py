
def hours_until_new_year(M):
    if M == 23:
        return 1
    else:
        return 24 - M + 1

M = int(input())
print(hours_until_new_year(M))
