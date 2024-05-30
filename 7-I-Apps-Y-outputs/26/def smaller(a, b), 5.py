
def smaller(a, b):
    if a == b:
        return a
    elif a > b:
        return b
    else:
        return a


a, b = map(int, input().split())
print(smaller(a, b))

