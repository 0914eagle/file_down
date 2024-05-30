
def f(s):
    n = len(s)
    a = s.count('a')
    b = s.count('b')
    if a == b:
        return 0, s
    else:
        if a > b:
            return (a-b)//2, s.replace('a', 'b', (a-b)//2)
        else:
            return (b-a)//2, s.replace('b', 'a', (b-a)//2)


n = int(input())
s = input()

print(f(s)[0])
print(f(s)[1])

