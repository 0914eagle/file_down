
n = int(input())
a = list(map(int, input().split()))
a.sort()

if a == a:
    print(0)
else:
    print(len(a))
    for i in range(len(a)-1, 0, -1):
        print(i, i+1)

