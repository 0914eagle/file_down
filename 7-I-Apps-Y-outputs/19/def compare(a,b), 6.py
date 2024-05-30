
def compare(a,b):
    return str(a)[::-1] if a > b else str(b)[::-1]

a,b = map(int, input().split())
print(compare(a,b))

