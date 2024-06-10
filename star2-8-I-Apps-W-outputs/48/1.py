
n = int(input())
a = 0
while n > 0:
    a += 1
    s = sum(map(int, str(a)))
    if s == 10:
        n -= 1
print(a)

