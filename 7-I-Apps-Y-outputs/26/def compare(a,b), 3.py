
def compare(a,b):
    if a+a < b+b:
        return a+a
    else:
        return b+b

a,b = input().split()
print(compare(a,b))

