
def compare(a, b):
    if a + b < b + a:
        return a + b
    else:
        return b + a


a, b = map(int, input().split())
print(compare(str(a), str(b)))

