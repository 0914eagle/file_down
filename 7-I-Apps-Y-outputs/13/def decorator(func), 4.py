
def decorator(func):
    def wrapper(n):
        for i in range(n):
            if n[i][0] == '0':
                n[i] = '+91' + n[i][1:]
            elif n[i][0] == '9' or n[i][0] == '8' or n[i][0] == '7':
                n[i] = '+91' + n[i][1:]
        return func(n)
    return wrapper

@decorator
def sort_mobile(n):
    n.sort()
    for i in n:
        print(i)

n = int(input())
l = []
for i in range(n):
    l.append(input())
sort_mobile(l)

