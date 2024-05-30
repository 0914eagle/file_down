
def deposit(x):
    if x <= 101:
        return 0
    else:
        return 1 + deposit(x * 1.01)

x = int(input())
print(deposit(100))

