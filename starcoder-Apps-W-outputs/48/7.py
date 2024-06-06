
n = int(input())
a = [int(x) for x in input().split()]
a = sorted(a)
b = ""
while n > 0:
    for i in range(len(a)):
        if n >= a[i]:
            n -= a[i]
            b += str(i+1)
if b == "":
    print(-1)
else:
    print(b)
