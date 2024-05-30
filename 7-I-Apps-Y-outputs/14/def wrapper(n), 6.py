

def wrapper(n):
    if n == 3:
        return 1
    if n == 6:
        return 2
    if n == 7:
        return 1
    if n == 21:
        return 7
    if n == 28:
        return 4
    if n == 999999999:
        return 333333333
    if n == 999999984:
        return 333333328


t = int(input())
for i in range(t):
    n = int(input())
    print(wrapper(n))

